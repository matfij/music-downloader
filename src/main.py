import re
import json
from selenium import webdriver
from bs4 import BeautifulSoup


with open('config.json', 'r') as config_file:
    config = json.load(config_file)

url = config['baseUrl']


driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)
driver.find_element_by_css_selector('#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.qqtRac > form > div.lssxud > div > button').click()
driver.implicitly_wait(5)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html)
tags = soup.find_all("a", {"id": "thumbnail"}, href=True)

links = []
for tag in tags:
    link = tag['href'].replace('/watch?v=', '')
    links.append(link)
