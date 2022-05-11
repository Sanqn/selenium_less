from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    find_scr = browser.find_element(By.ID, 'treasure')
    get_value_scr = find_scr.get_attribute('valuex')
    answer = str(math.log(abs(12 * math.sin(int(get_value_scr)))))
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()