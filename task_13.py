#Операция Кодовый Замок

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    buttons = browser.find_elements('tag name', 'input')
    for button in buttons:
        button.click()

    but = browser.find_element(By.XPATH, '/html/body/div/div[2]/input')
    but.click()
    time.sleep(10)
