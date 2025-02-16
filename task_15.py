
# Мастер заполнения форм

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')

    input_form1 = browser.find_element(By.XPATH, '/html/body/div/div/div[3]/input').send_keys('Сергей')
    print('Сергей')
    input_form2 = browser.find_element(By.XPATH, '/html/body/div/div/div[4]/input').send_keys('Аззамасцев')
    print('Арзамасцев')
    input_form3 = browser.find_element(By.XPATH, '/html/body/div/div/div[5]/input').send_keys('Михайлович')
    print('Михайлович')
    input_form4 = browser.find_element(By.XPATH, '/html/body/div/div/div[6]/input').send_keys('64')
    print('64')
    input_form5 = browser.find_element(By.XPATH, '//html/body/div/div/div[7]/input').send_keys('Санкт-Петербург')
    print('Санкт-Петербург')
    input_form6 = browser.find_element(By.XPATH, '//html/body/div/div/div[8]/input').send_keys('godock@mail.ru')
    print('godock@mail.ru')

    button = browser.find_element(By.XPATH, '//*[@id="btn"]').click()

    key = browser.find_element(By.XPATH, '// *[ @ id = "result"]').text
    print(key)

    time.sleep(2)
