import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup

import constants as C
from config import Quality


# load user configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

BASE_URL = config['baseUrl']
QUALITY = config['quality']
DOWNLOAD_DEPTH = config['downloadDepth']
DOWNLOAD_LIMIT = config['downloadLimit']
DOWNLOAD_DELAY = config['downloadDelay']
MAX_WAIT_TIME = config['maxWaitTime']

driver = webdriver.Chrome()

# visit target channel html
driver.get(BASE_URL)
continue_btn = WebDriverWait(driver, MAX_WAIT_TIME).until(
    expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, C.YT_BTN_CONTINUE_SELECTOR)
    )
)
continue_btn.click()

driver.execute_script(f'window.scrollTo(0, {DOWNLOAD_DEPTH})') 

page_html = driver.page_source

# extract video ids from channel html
soup = BeautifulSoup(page_html, 'html.parser')
video_tags = soup.find_all('a', {'id': C.YT_VIDEO_ID_ATTRIBUTE}, href=True)

video_links = []
for tag in video_tags:
    link = tag['href'].replace(C.YT_VIDEO_ID_PREFIX, '')
    video_links.append(link)
print(len(video_links))
# download videos
download_btn_selector = C.DOWNLOAD_BTN_HQ_SELECTOR if QUALITY == Quality.HIGH else C.DOWNLOAD_BTN_LQ_SELECTOR

for link in video_links:
    driver.get(C.DOWNLOAD_API_URL + link)

    download_btn = WebDriverWait(driver, MAX_WAIT_TIME).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, download_btn_selector)
        )
    )
    driver.implicitly_wait(DOWNLOAD_DELAY)
    download_btn.click()
 