import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    find_el = browser.find_element(By.ID, 'input_value').text
    answer = str(math.log(abs(12 * math.sin(int(find_el)))))
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()