
# 6.6 Операция: Чистый Лист

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/selenium/5.5/1/1.html')
    tasks = webdriver.find_elements(By.TAG_NAME, 'input')

    for task in tasks:
        task.clear()
    button = webdriver.find_element(By.XPATH, '// *[ @ id = "checkButton"]').click()
    # Секретный Код: копируем число, которое появится во всплывающем alert-окне, с помощью Selenium.
    alert = webdriver.switch_to.alert
    # Выводим результат
    print(f'Секретный Код:{alert.text}')
    time.sleep(5)