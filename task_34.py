
# 4.5 Операция: Выпадающие списки(!)

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    g = browser.find_elements(By.TAG_NAME, 'option')
    lst = []
    for x in range(len(g)):
        lst.append(int(g[x].text))
    browser.find_element(By.ID, 'input_result').send_keys(sum(lst))
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
    #print(sum(lst))