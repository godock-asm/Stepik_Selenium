
#4.4 Методы .find_element() и .find_elements(). Поиск внутри списка элементов.(!)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://parsinger.ru/selenium/3/3.3.2/index.html")

blocks = browser.find_elements(By.CLASS_NAME, 'block') # Ищем блок элементов

# Проходим по каждому блоку и кликаем на кнопку внутри
for block in blocks:
    button = block.find_element(By.CLASS_NAME, 'button')
    button.click()
# Получения видимого текста элемента.
password = browser.find_element(By.TAG_NAME, 'password')

time.sleep(2)
key=password.text
print("Key:", key)

browser.quit()