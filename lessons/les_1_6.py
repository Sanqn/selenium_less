from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

link = 'http://suninjuly.github.io/simple_form_find_task.html'
try:
    driver = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    driver.get(link)
    # Ищем поле для ввода текста
    textarea_first_name = driver.find_element(By.NAME, "first_name")
    # Напишем текст ответа в найденное поле
    textarea_first_name.send_keys("Sanqn")
    textarea_last_name = driver.find_element(By.NAME, "last_name")
    textarea_last_name.send_keys("Davinci")
    textarea_city = driver.find_element(By.CLASS_NAME, "city")
    textarea_city.send_keys("NY")
    textarea_country = driver.find_element(By.ID, 'country')
    textarea_country.send_keys('USA')
    button = driver.find_element(By.ID, 'submit_button')
    button.click()
    time.sleep(20)

finally:
    driver.quit()


