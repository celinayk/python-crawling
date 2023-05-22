

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
###셀레니움으로 무엇인가 입력하기 위한 import
import time ### 페이지 로딩기다리는데 사용할 time모듈
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

from naver_news import extract_naver_news
import csv
import ssl

keyword = input("검색할 키워드를 입력해주세요: ")    
naver=extract_naver_news(keyword)
print(naver)

file = open(f"{keyword}.csv","w",encoding='utf-8-sig')
file.write("date,title,link\n")

for article in naver:
  file.write(f"{article['date']},{article['title']},{article['link']}\n")

file.close()

