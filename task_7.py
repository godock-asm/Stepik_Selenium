
#4.3 Объект WebElement. Учимся вводить текст в поле.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://parsinger.ru/selenium/3/3.2.2/index.html'
browser = webdriver.Chrome()
browser.get(url)
elem = browser.find_element(By.XPATH, '//*[@id="codeInput"]')
elem.send_keys("Дрогон")
time.sleep(15)
btn = browser.find_element(By.XPATH,'//*[@id="clickButton"]')
btn.click()

print(elem)
browser.quit()