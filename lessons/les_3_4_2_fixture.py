import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'


class TestMainPage1():

    @classmethod
    def setup_class(cls):
        print("start browser for test suite..")
        cls.browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'),
                                        options=webdriver.ChromeOptions())


    def test_guest_should_see_login_link(self):
        print("login_link1")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("login_basket1")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @classmethod
    def teardown_class(cls):
        print("quit browser for test suite..")
        cls.browser.quit()

class TestMainPage2():

    def setup_method(self):
        print("start browser for test2..")
        self.browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'),
                                        options=webdriver.ChromeOptions())

    def test_guest_should_see_login_link(self):
        print("login_link2")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("login_basket2")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    def teardown_method(self):
        print("quit browser for test2..")
        self.browser.quit()