from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

browser = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)
browser.get('https://qiita.com')

WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)

html = browser.page_source.encode('utf-8')
soup = BeautifulSoup(html, "html.parser")
ra_tag_names = soup.find_all(class_='ra-Tag_name pr-1')
tag_ranking_data = {}
for i, ra_tag_name in enumerate(ra_tag_names):
    tag_ranking_data[i+1] = [ra_tag_name.text,
    'https://qiita.com/tags/%s' % (ra_tag_name.text.lower())]

for key, value in tag_ranking_data.items():
    print(f"{key} {value}")

browser.close()
browser.quit()
