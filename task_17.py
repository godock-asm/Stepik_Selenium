
#Кодекс Охотников за Цифрами
import time

from pycparser.ply.yacc import resultlimit
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    url = 'http://parsinger.ru/selenium/3/3.html'
    browser.get(url)

    element_1 = browser.find_elements(By.XPATH, "//div[@class='text']/p[1]")
    amount_list1 = [int(element.text) for element in element_1]

    element_2 = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    amount_list2 = [int(element.text) for element in element_2]

    element_3 = browser.find_elements(By.XPATH, "//div[@class='text']/p[3]")
    amount_list3 = [int(element.text) for element in element_3]

    print(f":{sum(amount_list1)}")
    print(f":{sum(amount_list2)}")
    print(f":{sum(amount_list3)}")
    print(f'Отчет о Сокровищах: {150825263400+149494128600+150064802300}')


