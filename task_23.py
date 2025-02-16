
#6.1 Переход назад.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.2/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)

    time.sleep(2)
    page_1 = browser.find_element(By.XPATH, '/html/body/div/a').click()
    time.sleep(2)
    page_2 = browser.find_element(By.XPATH, '/html/body/p/a').click()
    time.sleep(2)
    browser.back()
    time.sleep(2)
    browser.back()
    button = browser.find_element(By.XPATH, '//*[@id="getPasswordBtn"]').click()

    time.sleep(10)
