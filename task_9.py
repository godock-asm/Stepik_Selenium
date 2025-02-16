
#4.3 Объект WebElement. Учимся получать значение атрибута.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://parsinger.ru/selenium/3/3.2.4/index.html")
btn = browser.find_element(By.ID, "secret-key-button")
btn.click()
key=btn.get_attribute("data")
print(key)
time.sleep(2)
browser.quit()