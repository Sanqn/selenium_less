import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('name')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('lastname')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('email')
    with open('file.txt', 'w') as file:
        file.write('test1')
    curr_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curr_path, 'file.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()