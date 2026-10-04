# string so với string: nếu cả hai đều là chuỗi số thì so theo số, ngược lại so theo ký tự (ASCII).
# string so với int: chuỗi bị ép về số.


from bs4 import BeautifulSoup
import requests


if __name__ == "__main__":
    url = "http://host3.dreamhack.games:11550"
    lst = []
    for i in range(ord("9") + 1, ord("A")):
        lst.append(chr(i))

    res = requests.post(url+'/check.php', {'input1':'7.'+lst[0], 'input2':'7f'})
    print(BeautifulSoup(res.content, 'html.parser').pre)