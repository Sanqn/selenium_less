import math
import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

link = 'http://suninjuly.github.io/alert_accept.html'
try:
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    alert = browser.switch_to.alert
    alert.accept()
    find_el = browser.find_element(By.ID, 'input_value').text
    answer = str(math.log(abs(12 * math.sin(int(find_el)))))
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.TAG_NAME, 'button').click()
    alert2 = browser.switch_to.alert
    alert2_text = alert2.text
    list_aler2 = alert2_text.split()
    print(float(list_aler2[-1]))
    alert2.accept()
finally:
    time.sleep(10)
    browser.quit()