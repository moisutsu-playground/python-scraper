import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.yahoo.co.jp/categories/it")
soup = BeautifulSoup(r.content, "html.parser")
elems = soup.select("#contentsWrap > section > div > div > div > ul > li.topicsListItem > a")
for elem in elems:
    print(elem.text)
