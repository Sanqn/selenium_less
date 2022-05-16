import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage



@pytest.mark.login_guest
class TestLoginFromMainPage:
    link = "http://selenium1py.pythonanywhere.com"

    def test_guest_can_go_to_login_page(self, browser):
        self.page = MainPage(browser, TestLoginFromMainPage.link)
        self.page.open_page()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        self.page = MainPage(browser, TestLoginFromMainPage.link)
        self.page.open_page()
        self.page.should_be_login_link()


