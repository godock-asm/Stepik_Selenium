

#5.2 Запуск браузера в скрытом режиме

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected
import time
options_chrome = webdriver.ChromeOptions()
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://parsinger.ru/selenium/3/3.3.3/index.html'
    browser.get(url)
    time.sleep(5)




