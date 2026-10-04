import requests
from bs4 import BeautifulSoup


url = 'http://host3.dreamhack.games:24316'

if __name__ == "__main__":
    step1 = requests.get(url+'/step1', {'param': 'getget', 'param2':'rerequest'})
    soup1 = BeautifulSoup(step1.content, 'html.parser')
    check = soup1.find("input", {"name": "check"}).get("value")
    print(check)
    flag = requests.post(url+'/flag', {'param': 'pooost', 'param2': 'requeeest', 'check': check})
    print(BeautifulSoup(flag.content, 'html.parser').find('pre'))