
#4.5 Поход за сокровищами в Цифровом Лабиринте(!)

from selenium import webdriver
from selenium.webdriver.common.by import By

# URL веб-страницы для парсинга
url = 'http://parsinger.ru/selenium/3/3.html'

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get(url)

    # Используем метод .find_elements() для поиска всех элементов, соответствующих нашему XPath
    p_element = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")

    amount_list = [int(element.text) for element in p_element]

    print(f"Ключ к Загадке:{sum(amount_list)}")
