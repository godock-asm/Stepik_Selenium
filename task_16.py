

# Охотник за Сокровищами

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')

    input_form1 = browser.find_element(By.LINK_TEXT, '16243162441624').text
    print(input_form1 )

    time.sleep(1)
