import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:23845"
    req = requests.get(url+'//flag.php')
    print(BeautifulSoup(req.content, 'html.parser').h3.text)