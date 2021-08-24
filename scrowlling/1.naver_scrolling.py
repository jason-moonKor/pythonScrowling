import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


plusUrl = urllib.parse.quote_plus(input('검색어를 입력하세요 : '))

pageNum = 1
count = 1

i = input('몇페이지 크롤링 할까요? : ')

lastPage = int(i) * 10 - 9

while pageNum < lastPage + 1:

    url = f'https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query={plusUrl}&c_id=&c_name=&sm=tab_pge&kin_start={pageNum}&kin_age=0'

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')


    title = soup.find_all(class_='sh_blog_title')

    print(f'--------{count}페이지 결과입니다-------')
    for i in title:
        print(i.attrs['title'])
        print(i.attrs['href'])
    print()
    
    pageNum += 10
    count += 1