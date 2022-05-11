import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
browser.find_element(By.ID, 'book').click()
find_el = browser.find_element(By.ID, 'input_value').text
answer = str(math.log(abs(12 * math.sin(int(find_el)))))
browser.find_element(By.ID, 'answer').send_keys(answer)
browser.find_element(By.ID, 'solve').click()
asert_text = browser.switch_to.alert.text.split()
print(float(asert_text[-1]))

