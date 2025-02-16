
#6.3 Cookies на практике
import time
from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('https://ya.ru/')

# Получаем список всех Cookies
    cookies = browser.get_cookies()
    print(cookies)

# или получаем имена Cookies
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(cookie['name']) # или cookie['value'] чтобы получить их значение

# Удаляет только одну cookie по её имени.
with webdriver.Chrome() as browser:
    url = "https://parsinger.ru/methods/3/index.html"
    browser.get(url)
    # Итерируемся по всем именам куков, в которых последнее число — чётное, и удаляем их.
    for i in range(0, 17, 2):
        browser.delete_cookie(f"secret_cookie_{i}")
    time.sleep(30)

# Удаление всех кук текущей сессии браузера.
with webdriver.Chrome() as browser:
    url = "https://parsinger.ru/methods/3/index.html"
    browser.get(url)

    # Получаем список существующих кук до удаления
    print("Cookies before deletion:")
    print(browser.get_cookies())

    # Удаляем все куки
    browser.delete_all_cookies()

    # Проверяем, что куки удалены
    print("\nCookies after deletion:")
    print(browser.get_cookies())

#Если нужно удалить только одну cookie, используйте delete_cookie(name). Если нужно очистить всё — delete_all_
# cookies().
