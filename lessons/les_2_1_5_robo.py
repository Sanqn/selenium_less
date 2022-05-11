from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    browser.get(link)
    x_el = browser.find_element(By.ID, 'input_value').text
    answer = str(math.log(abs(12*math.sin(int(x_el)))))
    browser.find_element(By.ID, 'answer').send_keys(answer)
    people_radio = browser.find_element(By.ID, 'peopleRule')
    people_checked = people_radio.get_attribute('checked')
    assert people_checked is not None, "People radio is not selected by default"
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(10)
