from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키보드 입력
from selenium.webdriver.common.by import By # 태그 조회 방식
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get('http://naver.com')
time.sleep(1)

search_box = driver.find_element(By.ID, 'query')
search_box.send_keys('chatgpt')
search_box.send_keys(Keys.RETURN)
time.sleep(1)

news_btn = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[8]/a')
news_btn.click()
time.sleep(1)

news_contents_btn = driver.find_element(By.XPATH, '//*[@id="sp_nws1"]/div[1]/div/div[2]/a[2]')
response = news_contents_btn.click()
time.sleep(1)

