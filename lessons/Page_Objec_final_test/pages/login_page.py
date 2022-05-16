from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
import time


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        assert login_url, 'Login url not found'

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, 'Login form not found'

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form, 'Register form not found'

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = 'Password1@'
        self.browser.find_element(*BasePageLocators.USER_EMAIL).send_keys(email)
        self.browser.find_element(*BasePageLocators.USER_PASSWORD1).send_keys(password)
        self.browser.find_element(*BasePageLocators.USER_PASSWORD2).send_keys(password)
        self.browser.find_element(*BasePageLocators.BUTTON_REGISTRATION).click()
