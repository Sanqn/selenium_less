from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class BacketButtonLocators:
    BUTTON_LINK_ADD_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form>.btn')
    CHECK_TEXT_ADDED_BOOK = (By.CSS_SELECTOR, '.alertinner>strong')
    CHECK_TEXT_ORDERED_BOOK = (By.CSS_SELECTOR, '.product_main>h1')
    CHECK_PRICE_ADDED_BOOK = (By.CSS_SELECTOR, '.alertinner>p>strong')
    CHECK_PRICE_ORDERED_BOOK = (By.CSS_SELECTOR, '.product_main>.price_color')
