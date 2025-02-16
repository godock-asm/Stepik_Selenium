

# 6.6 Операция: Минное поле

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/selenium/5.5/2/1.html')
    elements = webdriver.find_elements(By.XPATH, '//*[@data-enabled="true"]')
    for i in elements:
        i.clear()

    webdriver.find_element(By.ID, 'checkButton').click()
    print(f'Секретный код:{webdriver.switch_to.alert.text}')

    time.sleep(2)