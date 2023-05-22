from selenium import webdriver
from selenium.webdriver.common.keys import Keys
###셀레니움으로 무엇인가 입력하기 위한 import
import time ### 페이지 로딩기다리는데 사용할 time모듈
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
s = Service('/D/VS Code/WebCrawling/chromedriver.exe')
driver = webdriver.Chrome(service=s,options=chrome_options)
driver.implicitly_wait(5)
 

def get_page_count(keyword):
  base_url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
  driver.get(f"{base_url}{keyword}")
  soup = BeautifulSoup(driver.page_source, "html.parser")
  pasination = soup.find("div",class_="sc_page_inner")
  if pasination==None:
    return 1;
  pages = pasination.find_all("a")
  count = len(pages)
  if count >=10:
    return 10
  else:
    return count


def extract_naver_news(keyword):
  pages = get_page_count(keyword)
  print("불러옵니다", pages,"페이지")
  #searchkeyword = print("검색할 키워드를 입력해주세요: ");
  results = []

  for page in range(pages):
    base_url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
    final_url = f"{base_url}{keyword}&start={page*10+1}"
    print(final_url)
    driver.get(final_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    news_list=soup.find("ul", class_="list_news")
    real_news=news_list.find_all("li",recursive=False)
    for real_news2 in real_news:
      news_date = real_news2.select(".info_group > span")
      short_news=real_news2.select(".news_tit")
      for i in news_date:
        date = i.text
        #result.append(date)
      for i in short_news:
        title = i.text.replace(","," ")
        link=i.get("href")
        #result.append(title)
        #result.append(link)
      news_data = {
        'date' : date,
        'title' : title,
        'link' : link  
      }
      results.append(news_data)    
    return results;

