import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture
def browser(request):
    print("start browser for test suite..")
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    def close_browser():
        browser.quit()
    request.addfinalizer(close_browser)
    print('Start request')
    return browser

class TestPage:
    def test_guest_should_see_login_link(self, browser):
        print("login_link1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("login_basket1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


