from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.co.kr/search?q='
plusUrl = input('무엇을 검색할까요? : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

r = soup.select('.tF2Cxc')
for i in r:
    print(i.select_one('.LC20lb.DKV0Md').text)
    #print(i.select_one('.iUh30.Zu0yb.qLRx3b.tjvcx').text)
    print(i.a.attrs['href'])
    print()

driver.close()