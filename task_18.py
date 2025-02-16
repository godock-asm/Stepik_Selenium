#5.1 Запуск браузера с расширениями (НЕ РАБОТАЕТ)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension ('C:\\Users\Admin\AppData\Local'
                              '\Google\Chrome\\User Data\Default\Extensions\ololmadlpnbbagpk'
                              'jhdomclggmfomhdg.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    a = browser.find_element(By.TAG_NAME, 'a')
    time.sleep(10)

    print(a.get_attribute('href'))
browser.get(url)