
#4.3 Объект WebElement. Учимся кликать по кнопке.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/3/3.2.1/index.html")
    time.sleep(5)
    browser.quit()
# или
browser = webdriver.Chrome()
browser.get("https://parsinger.ru/selenium/3/3.2.1/index.html")
btn = browser.find_element(By.ID, "clickButton")
btn.click()
time.sleep(5)
browser.quit()
# или task_6

