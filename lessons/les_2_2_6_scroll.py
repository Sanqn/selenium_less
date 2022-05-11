from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service

link = 'http://suninjuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    browser.get(link)
    find_x = browser.find_element(By.ID, 'input_value').text
    answer = str(math.log(abs(12 * math.sin(int(find_x)))))
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.execute_script("window.scrollBy(0, 200)")
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()