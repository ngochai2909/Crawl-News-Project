from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
url = 'https://baomoi.com//agribank-trinh-dien-6-dich-vu-tai-su-kien-chuyen-doi-so-nganh-ngan-hang-c49053623.epi'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
# elements = driver.find_elements(By.TAG_NAME, 'p')

source = driver.page_source


soup = BeautifulSoup(source, 'html.parser')
p_tag = soup.find_all('p')
img_tags = soup.find_all('img')
print(soup.prettify())
print(img_tags)

# time.sleep(20)