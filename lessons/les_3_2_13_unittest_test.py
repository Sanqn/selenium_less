from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
import unittest

class TestFild(unittest.TestCase):
    def test_link(self):
        self.link = 'http://suninjuly.github.io/registration1.html'
        self.browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
        self.browser.get(self.link)
        self.browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input").send_keys('First name')
        self.browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input").send_keys('Last name')
        self.browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input").send_keys('Email')
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        self.welcome_text_el = self.browser.find_element(By.TAG_NAME, 'h1')
        self.welcome_text = self.welcome_text_el.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, 'Not open')

    def test_link1(self):
        self.link2 = 'http://suninjuly.github.io/registration2.html'
        self.browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'),
                                        options=webdriver.ChromeOptions())
        self.browser.get(self.link2)
        self.browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input").send_keys(
            'First name')
        self.browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input").send_keys(
            'Last name')
        self.browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input").send_keys('Email')
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        self.welcome_text_el = self.browser.find_element(By.TAG_NAME, 'h1')
        self.welcome_text1 = self.welcome_text_el.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text1, 'Not open')

if __name__ == '__main--':
    unittest.main()

