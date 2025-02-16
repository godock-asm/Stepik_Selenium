

# 6.3 Извлеките значение cookie token_22 .
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html')
    cookies = browser.get_cookies()
    print('Значение token_22: ')
    print(browser.get_cookie('token_22')['value'])

# 6.3 Поиск cookie.

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3/index.html')
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(cookie)
    password = cookie['name']
    browser.find_element(By.ID, 'phraseInput').send_keys(password)
    time.sleep(5)
    browser.find_element(By.ID, 'checkButton').click()
    print('Password:')
    print(browser.find_element(By.ID, 'result').text)

# 6.3 Удаляем все cookie.

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.2/index.html')
    cookies = browser.get_cookies()
    # Получаем список существующих кук до удаления
    print("Cookies before deletion:")
    print(browser.get_cookies())
    # Удаляем все куки
    browser.delete_all_cookies()
    time.sleep(5)
    print((browser.find_element(By.XPATH, '//*[@id="password"]').text))
    # Проверяем, что куки удалены
    print("Cookies after deletion:")
    print(browser.get_cookies())