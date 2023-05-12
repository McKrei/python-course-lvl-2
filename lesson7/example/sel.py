from selenium import webdriver
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Создание экземпляра драйвера
driver = webdriver.Chrome()

# Переход на страницу
url = 'https://www.ozon.ru/category/zhestkie-diski-ssd-i-setevye-nakopiteli-15710/'
driver.get(url)

# Найти поле ввода поискового запроса и ввести запрос
# search_box = driver.find_element(By.ID, 'APjFqb')
# search_box.send_keys("python selenium")
# search_box.send_keys(Keys.RETURN)

# Дождаться загрузки результатов поиска
driver.implicitly_wait(10)
time.sleep(10)
# Получить результаты поиска
# search_results = driver.find_elements(By.CLASS_NAME, 'MjjYud')

# Вывести заголовки результатов поиска
# for result in search_results:
# #     title = result.find_element(By.CLASS_NAME, 'LC20lb MBeuO DKV0Md')
#     print(result)

html = driver.page_source
with open('o1.html', 'w', encoding='utf-8') as f:
    f.write(html)
# Закрыть браузер
driver.quit()

resp = requests.get(url)
with open(f'o2.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)
