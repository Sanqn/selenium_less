from .base_page import BasePage
from .locators import BasketButtonLocators


class AddToBasket(BasePage):

    def should_be_basket_add(self):
        print('should_be_basket_add')
        button = self.browser.find_element(*BasketButtonLocators.BUTTON_LINK_ADD_BASKET)
        button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketButtonLocators.CHECK_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*BasketButtonLocators.CHECK_MESSAGE), \
            "Success message is presented, but should not be"

    def check_text_added_book(self):
        print('check_text_added_book')
        text_added_book = self.browser.find_element(*BasketButtonLocators.CHECK_TEXT_ADDED_BOOK).text
        text_ordered_book = self.browser.find_element(*BasketButtonLocators.CHECK_TEXT_ORDERED_BOOK).text
        assert text_added_book == text_ordered_book, 'The Book ordered not right'

    def check_price_added_book(self):
        print('check_price_added_book')
        text_added_book_price = self.browser.find_element(*BasketButtonLocators.CHECK_PRICE_ADDED_BOOK).text
        text_ordered_book_price = self.browser.find_element(*BasketButtonLocators.CHECK_PRICE_ORDERED_BOOK).text
        assert text_added_book_price == text_ordered_book_price, 'The Book price right'
