from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_URL).click()
        new_window = self.browser.current_url
        assert new_window, 'Login url not found'

    def should_be_login_form(self):
        pass

    def should_be_register_form(self):
            register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
            assert register_form, 'Register form not found'