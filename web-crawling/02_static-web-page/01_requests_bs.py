# 정적 페이지 웹 스크랩핑 -> requests, beautifulsoup
# 정적 페이지 : 요청한 url에서 응답받은 html을 그대로 사용한 경우 (Server Sid Rendering)

import requests
from bs4 import BeautifulSoup

def web_request(url):
    response = requests.get(url)
    print(response)
    print(response.status_code)
    print(response.text)
    return response

# url = 'https://naver.com'
# response = web_request(url)

with open('../html_sample.html', 'r', encoding='utf-8') as f:
    html = f.read()

# BeautifulSoup = html, xml을 parsing해서 데이터 추출출
bs = BeautifulSoup(html, 'html.parser')
# print(bs)
# print(type(bs))

def test_find():
    # find, find_all
    # find : html 태그 및 속성을 dict로 조회 (1개 만 조회)
    tag = bs.find('li')
    print(tag)
    print(type(tag))
    
    # find_all : html 태그 및 속성을 dict로 조회 (전부 다 조회)
    tags = bs.find_all('section', {'id': 'contact'})
    print(tags)
    print(type(tags))

# test_find()

def test_selector():
    #css 선택자로 특정 태그 찾기
    tag = bs.select_one('section#section2')
    # print(tag)
    # print(type(tag))

    tags = bs.select('.section-content')
    print(tags)
    print(type(tags))

# test_find()

def get_content():
    #id가 section2인 section 태그의 자손 li 태그들을 추출
    # 자식 요소 : section#services > li
    # 후손 요소 : section#services li
    tags = bs.select('section#services li')
    
    for tag in tags:
        print(tag.text)

# get_content()

def get_content2():
    #id가 section1인 section 태그의 자손 h2태그의 '내용', p태그의 '내용' 출력
    h2_tag = bs.select_one('section#contact > h2')
    print(f'h2 text: {h2_tag.text}')

    label_tags = bs.select('section#contact label')
    for label_tag in label_tags:
        print('label_tag :', label_tag.text)

# get_content2()

def get_content3():
    # 자식 태그 조회
    section_tag = bs.select_one('section#contact')
    h2_tag = section_tag.select_one('h2')
    print(h2_tag.text)
    label_tags = section_tag.select_one('label')
    print([label_tag.text for label_tag in label_tags])

    children = section_tag.findChildren()
    print(children)
    
get_content3()