import pytest
from pages.product_page import AddToBasket


@pytest.mark.parametrize('link_promo', [1, 2, 3, 4, 5, 6,
                                        pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link_promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_promo}'
    promo_link = AddToBasket(browser, link)
    promo_link.open_page()
    promo_link.should_be_basket_add()
    promo_link.solve_quiz_and_get_code()
    promo_link.check_text_added_book()
    promo_link.check_price_added_book()
