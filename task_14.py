
#4.5  Миссия "Загадочный След"

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

browser = webdriver.Chrome()
x=((12434107696 * 3) * 2) + 1
print(f'Значение:x=',x)
browser.get('https://parsinger.ru/selenium/6/6.html')
element1=browser.find_element(By.XPATH,'//*[@id="selectId"]/option[60]').text
element2=browser.find_element(By.XPATH,'//*[@id="selectId"]')
element2.send_keys(element1)
element3=browser.find_element(By.XPATH,'//*[@id="sendbutton"]').click()
element4=browser.find_element(By.XPATH,'//*[@id="result"]').text
print(f'Ключ:',element4)

sleep(5)
browser.quit()