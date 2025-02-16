
#4.3 Объект WebElement. Учимся получать текст из элемента.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://parsinger.ru/selenium/3/3.2.3/index.html")
start_btn = browser.find_element(By.ID, "showTextBtn")
start_btn.click() # метод для симуляции клика мышью

password = browser.find_element(By.ID, "text1").text #  метод для получения видимого текста элемента

field = browser.find_element(By.ID, "userInput")
field.send_keys("M1SS10N-P0SS1BL3") #  метод для ввода текста (полезно для текстовых полей)
check_btn = browser.find_element(By.ID, "checkBtn")
check_btn.click() # метод для симуляции клика мышью
time.sleep(5)

key = browser.find_element(By.ID, "text2").text #  метод для получения видимого текста элемента
print(key)
browser.quit()