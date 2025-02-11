from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

COUNT = 100
URL = f'https://www.saramin.co.kr/zf_user/search?cat_kewd=87&exc_keyword=국비%2C교육&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage=1&recruitSort=relation&recruitPageCount={COUNT}&mainSearch=n'

driver.get(URL)
sleep(2)

recruit_items = driver.find_elements(By.CLASS_NAME, 'item_recruit')

main_items = []

for recruit_item in recruit_items:
  job_tit = recruit_item.find_element(By.CLASS_NAME, 'job_tit')
  a = job_tit.find_element(By.TAG_NAME, 'a')
  title = a.get_attribute("title")
  url = a.get_attribute("href")

  corp_name = recruit_item.find_element(By.CLASS_NAME, 'corp_name')
  company_name = corp_name.find_element(By.TAG_NAME, 'a').text

  main_items.append({ "title": title, "url": url, "company_name": company_name })

for recruit_item in main_items:
  driver.get(recruit_item["url"])
  sleep(1)