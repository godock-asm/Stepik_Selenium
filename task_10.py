
#4.4 Методы .find_element() и .find_elements(). Каскадный поиск.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://parsinger.ru/selenium/3/3.3.1/index.html")

parent_element = browser.find_element(By.ID, 'parent_id') # Ищем родительский элемент
child_element = parent_element.find_element(By.CLASS_NAME, 'child_class') # Ищем дочерний элемент внутри
# родительского
child_element.click()
time.sleep(2)
password=child_element.get_attribute('password') # выводим значение атрибута

print(password)
browser.quit()