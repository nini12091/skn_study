import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlretrieve
import os
os.makedirs('images', exist_ok=True)

# 스크랩한 뉴스 정보를 담을 NewsEntry class
class NewsEntry:
    def __init__(self, title, href, img_path):
        self.title =title
        self.href = href
        self.img_path = img_path

    def __repr__(self):
        return f'NewsEntry<title={self.title}, href={self.href}, img_path={self.img_path}'

# 1. request -> url 요청
keyword = input('뉴스 검색 키워드 입력: ')
url = f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}"
response = requests.get(url)

# 2. html 응답
html = response.text

# 3. BeautifulSoup 객체 생성
bs = BeautifulSoup(html, 'html.parser')

# 4. li.bx 반복순회 > .newscontent > 두 번째 a 태그
news_contents = bs.select('div.news_contents')
# print(len(news_contents))

# 5. href 속성 : 링크, text : 뉴스 제목

news_list = []
for i, news_content in enumerate(news_contents):
    a_tag =news_content.select_one('a.news_tit')
    title = a_tag.text
    href = a_tag['href']

    img_tag = news_content.select_one('img.thumb')
    print(img_tag)
    if img_tag:
        img_lazysrc = img_tag['data-lazysrc']
        if img_lazysrc.startswith("http"):
            img_dir ="images"
            today = datetime.now().strftime('%y%m%d')
            filename = f'{img_dir}/{today}_{i}.jpg'
            urlretrieve(img_lazysrc, filename)
    else:
        filename = 'empty'
        
    news_entry =NewsEntry(title, href, filename)
    news_list.append(news_entry)

for news in news_list:
    print(news)

