
#6.4 Добавление cookie

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

cookie_dict = {
    'name': 'any_name_cookie',    # Любое имя для cookie
    'value': 'any_value_cookie',  # Любое значение для cookie
    'expiry': 2_000_000_000,      # Время жизни cookie в секундах
    'path': '/',                  # Директория на сервере дял которой будут доступны cookie
    'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
    'secure': True,  # or False # Сигнал браузера о том что передать cookie только по защищённому HTTPS
    'httpOnly': True,  # or False # Ограничивает доступ к cookie по средствам API
    'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
}

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/4/index.html')
    browser.add_cookie(cookie_dict)
    print(browser.get_cookies())
    time.sleep(5)

#6.4 Добавьте cookie на сайт.

from selenium.webdriver.common.by import By
import time
from selenium import webdriver

cookie_dict = {
    'name': 'secretKey',    # Любое имя для cookie
    'value': 'selenium123',  # Любое значение для cookie
}

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
    browser.add_cookie(cookie_dict)
    print(browser.get_cookies())
    browser.refresh()
    password = browser.find_element(By.ID, "password")
    print(password.text)
    time.sleep(40)