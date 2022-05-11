from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# link = 'http://suninjuly.github.io/registration1.html'
link = 'http://suninjuly.github.io/registration1.html'

try:
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    browser.get(link)
    browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input").send_keys('First name')
    browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input").send_keys('Last name')
    browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input").send_keys('Email')
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(1)

    welcome_text_el = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_el.text
    print(welcome_text)

    assert "Congratulations! You have successfully registered!" == welcome_text



finally:
    time.sleep(10)
    browser.quit()