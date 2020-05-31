import requests
from bs4 import BeautifulSoup

r = requests.get("http://skymotors.boy.jp/n46/discography/allmusic_001.html")
soup = BeautifulSoup(r.content, "html.parser")
# find_all: 指定したものをすべて取得してリストを返す
tables = soup.find_all("table")
for table in tables:
    # fild: 指定したものを一つだけ指定 attrsでタグの引数の値を指定できる
    title = table.find("td", attrs={"width" : "225"}).text
    print(title)
