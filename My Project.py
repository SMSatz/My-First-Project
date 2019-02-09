from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

url = input()
wd = input()
gt = requests.get(url)

if gt.status_code==200:
    soup=BeautifulSoup(gt.text,'html.parser')
    cn = soup.getText().lower()
    print(cn)
    tn = cn.split()
    print(tn.count(wd))

else:
    print("Invalid URL")
