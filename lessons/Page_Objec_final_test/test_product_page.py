import pytest

from pages.product_page import AddToBasket


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = AddToBasket(browser, link)
    page.open_page()
    page.should_be_basket_add()
    page.solve_quiz_and_get_code()
    page.check_text_added_book()
    page.check_price_added_book()
