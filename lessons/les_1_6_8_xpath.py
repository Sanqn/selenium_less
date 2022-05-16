from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/find_xpath_form'

browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
browser.get(link)
elements = browser.find_elements(By.XPATH, "//input[@type='text']")
for element in elements:
    element.send_keys('root')

browser.find_element(By.XPATH, "//button[@type='submit']").send_keys()
