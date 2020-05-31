import requests
from bs4 import BeautifulSoup

r = requests.get("https://db.netkeiba.com/?pid=horse_hitchart")
soup = BeautifulSoup(r.content, "html.parser")
elems = soup.select("#db_hitchart > div.fc > div > table > tbody > tr > td:nth-child(2) > a")
for elem in elems:
    print(elem.text)

# 要素を指定するのは、セレクタが一番楽
# http://semooh.jp/jquery/api/selectors/
# 要素を右クリック > 検証 > Copy > Copy selector
#db_hitchart > div.fc > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > a
