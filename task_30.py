
# 6.6 Операция: Следопыт чётных печенек (!)

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(cookie)
        print(f'x = {int(5700+27000+45500+20482+117150+61105+1545300+92872+46992)}')





