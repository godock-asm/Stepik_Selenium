
#6.1 Делаем скриншот.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.2.1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)

    time.sleep(2)
    skr=browser.find_element(By.ID, "this_pic")
    skr.screenshot('this_pic.png')
    time.sleep(2)




