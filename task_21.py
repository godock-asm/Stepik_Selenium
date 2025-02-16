
#5.3 Перенос профиля с основного браузера Chrome в браузер под управлением Selenium (НЕ РАБОТАЕТ)

import time
from selenium import webdriver

# Задаем опции для Chrome
options_chrome = webdriver.ChromeOptions()
# Указываем путь к профилю пользователя
options_chrome.add_argument('user-data-dir=C:\\Users\Admin\AppData\Local\Google\Chrome')

# Инициализируем драйвер с указанными опциями
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)  # Открываем страницу
    time.sleep(10)  # Даем время на загрузку страницы