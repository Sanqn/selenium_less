from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    browser.get(link)
    find_1_number = browser.find_element(By.ID, 'num1').text
    find_2_number = browser.find_element(By.ID, 'num2').text
    answer = int(find_1_number) + int(find_2_number)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(answer))
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
