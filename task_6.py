
#4.3 Объект WebElement. Учимся кликать по кнопке.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://parsinger.ru/selenium/3/3.2.1/index.html")
btn = browser.find_element(By.XPATH, '//*[@id="clickButton"]')
btn.click()
time.sleep(5)
browser.quit()