import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import AddToBasket
import time


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


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = AddToBasket(browser, link)
#     page.open_page()
#     # page.should_not_be_success_message()
#     page.should_be_basket_add()
#     page.solve_quiz_and_get_code()
#     page.check_text_added_book()
#     page.check_price_added_book()


@pytest.mark.success_message
class TestSuccesMessage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        self.page = AddToBasket(browser, TestSuccesMessage.link)
        self.page.open_page()
        self.page.should_be_basket_add()
        self.page.should_not_be_success_message()


    def test_guest_cant_see_success_message(self, browser):
        self.page = AddToBasket(browser, TestSuccesMessage.link)
        self.page.open_page()
        self.page.should_not_be_success_message()


    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        self.page = AddToBasket(browser, TestSuccesMessage.link)
        self.page.open_page()
        self.page.should_be_basket_add()
        self.page.should_disappear_success_message()


# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = AddToBasket(browser, link)
#     page.open_page()
#     page.should_be_login_link()
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = AddToBasket(browser, link)
#     page.open_page()
#     page.go_to_login_page()
#     page.should_be_login_link()

@pytest.mark.product_in_basket
class TestSeeProductInOpenedForm:

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        self.page = AddToBasket(browser, link)
        self.page.open_page()
        self.page.click_basket_button()
        self.page.check_basket_empty()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = AddToBasket(browser, link)
        self.page.open_page()
        self.page.should_be_basket_add()
        self.page.click_basket_button()
        self.page.check_basket_empty()
