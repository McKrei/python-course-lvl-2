import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from p import paswd
s = Service(executable_path='path_to_driver')
driver = webdriver.Chrome(service=s)

try:
    driver.maximize_window()
    driver.get('https://vk.com')
    time.sleep(2)

    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys('mckrei5@ya.ru')
    email_input.send_keys(Keys.ENTER)
    time.sleep(2)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(paswd)
    password_input.send_keys(Keys.ENTER)
    time.sleep(3)

    my_page = driver.find_element(By.PARTIAL_LINK_TEXT, 'Новости').click()
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    like = driver.find_element(By.CLASS_NAME, 'PostBottomAction__icon').click()

    time.sleep(5)
    # driver.find_element(By.CLASS_NAME, 'page_post_video_play_inline').click()
    # time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
