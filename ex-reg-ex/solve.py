import requests
from bs4 import BeautifulSoup
import re

# dr\w{5,7}e\d+am@[a-z]{3,7}\.\w+
# dr                              t
#     the literal text dr (case sensitive)
# \w{5,7}
#     any word character, repeated between 5 and 7 times
# e
#     the literal e (10110 / 1458 / 6516) (case sensitive)
# \d+
#     a digit, repeated at least once
# am@
#     the literal text am@ (case sensitive)
# Character Class
#     [a-z]{3,7}
#     {3,7}
#         matches between 3 and 7 characters from the set below:
# a-z
#     one character from a (9710) to z (12210) (case sensitive)
# \.
#     the literal . (4610 / 568 / 2E16) 
# \w+
#     any word character, repeated at least once

if __name__ == "__main__":
    url = "http://host3.dreamhack.games:24232"
    input_val = "dreeeeeeee2am@abcdefg.1"
    res = requests.post(url + '/', {'input_val': input_val})

    content = BeautifulSoup(res.content, 'html.parser').get_text()
    m = re.search(r'Flag:\s*(\S+)', content)

    if m:
        print(m.group(1))
    else:
        print(content)
