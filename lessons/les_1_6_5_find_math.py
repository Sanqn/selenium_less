# By.ID – поиск по уникальному атрибуту id элемента;
# By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
# By.XPATH – поиск элементов с помощью языка запросов XPath;
# By.NAME – поиск по атрибуту name элемента;
# By.TAG_NAME – поиск по названию тега;
# By.CLASS_NAME – поиск по атрибуту class элемента;
# By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
# By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math

link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    browser.get(link)
    find_text = browser.find_element(By.LINK_TEXT, text)
    find_text.click()
    textarea_first_name = browser.find_element(By.NAME, "first_name")
    textarea_first_name.send_keys("Sanqn")
    textarea_last_name = browser.find_element(By.NAME, "last_name")
    textarea_last_name.send_keys("Davinci")
    textarea_city = browser.find_element(By.CLASS_NAME, "city")
    textarea_city.send_keys("NY")
    textarea_country = browser.find_element(By.ID, 'country')
    textarea_country.send_keys('USA')
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    time.sleep(20)


finally:
    browser.quit()


