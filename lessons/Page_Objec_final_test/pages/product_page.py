from .base_page import BasePage
from .locators import BacketButtonLocators


class AddToBasket(BasePage):

    def should_be_basket_add(self):
        print('should_be_basket_add')
        botton = self.browser.find_element(*BacketButtonLocators.BUTTON_LINK_ADD_BASKET)
        botton.click()

    def check_text_added_book(self):
        print('check_text_added_book')
        text_added_book = self.browser.find_element(*BacketButtonLocators.CHECK_TEXT_ADDED_BOOK).text
        text_ordered_book = self.browser.find_element(*BacketButtonLocators.CHECK_TEXT_ORDERED_BOOK).text
        assert text_added_book == text_ordered_book, 'The Book orderd not right'

    def check_price_added_book(self):
        print('check_price_added_book')
        text_added_book_price = self.browser.find_element(*BacketButtonLocators.CHECK_PRICE_ADDED_BOOK).text
        text_ordered_book_price = self.browser.find_element(*BacketButtonLocators.CHECK_PRICE_ORDERED_BOOK).text
        assert text_added_book_price == text_ordered_book_price, 'The Book price right'

