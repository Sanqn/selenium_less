# By.ID – поиск по уникальному атрибуту id элемента;
# By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
# By.XPATH – поиск элементов с помощью языка запросов XPath;
# By.NAME – поиск по атрибуту name элемента;
# By.TAG_NAME – поиск по названию тега;
# By.CLASS_NAME – поиск по атрибуту class элемента;
# By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
# By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
link = 'http://google.com'

try:
    browser.get(link)
    # search site
    browser.find_element(By.TAG_NAME, 'input').send_keys('ozon.ru')
    time.sleep(5)
    # browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.RETURN)
    browser.find_element(By.NAME, 'btnK').click()
    browser.find_element(By.PARTIAL_LINK_TEXT, 'OZON — интернет-магазин').click()

    #find goods
    browser.find_element(By.NAME, 'text').send_keys('toy')
    browser.find_element(By.CLASS_NAME, 't2w').click()

    #input to basket 3 goods
    find_prod1 = browser.find_element(By.CSS_SELECTOR, '.pi0:nth-child(1) button[type="button"]').click()
    find_prod2 = browser.find_element(By.CSS_SELECTOR, '.pi0:nth-child(2) button[type="button"]').click()
    find_prod3 = browser.find_element(By.CSS_SELECTOR, '.pi0:nth-child(3) button[type="button"]').click()
    time.sleep(2)

    #open basket
    go_to_backet = browser.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()

    #looking for all added products
    goods = browser.find_elements(By.CSS_SELECTOR, '.p3a:last-child .an9')
    print(goods)
    print(len(goods))

    #check the number of products
    assert len(goods) == 3

finally:
    time.sleep(10)
    browser.quit()



