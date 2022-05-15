import pytest

from pages.product_page import AddToBasket
import time


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = AddToBasket(browser, link)
#     page.open_page()
#     # page.should_not_be_success_message()
#     page.should_be_basket_add()
#     page.solve_quiz_and_get_code()
#     page.check_text_added_book()
#     page.check_price_added_book()
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#
# @pytest.mark.xfail(reason="fixing this bug right now")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = AddToBasket(browser, link)
#     page.open_page()
#     page.should_be_basket_add()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     page = AddToBasket(browser, link)
#     page.open_page()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail(reason="fixing this bug right now")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = AddToBasket(browser, link)
#     page.open_page()
#     page.should_be_basket_add()
#     page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddToBasket(browser, link)
    page.open_page()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddToBasket(browser, link)
    page.open_page()
    page.go_to_login_page()
    page.should_be_login_link()


