from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class BasketButtonLocators:
    BUTTON_LINK_ADD_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form>.btn')
    CHECK_TEXT_ADDED_BOOK = (By.CSS_SELECTOR, '.alertinner>strong')
    CHECK_TEXT_ORDERED_BOOK = (By.CSS_SELECTOR, '.product_main>h1')
    CHECK_PRICE_ADDED_BOOK = (By.CSS_SELECTOR, '.alertinner>p>strong')
    CHECK_PRICE_ORDERED_BOOK = (By.CSS_SELECTOR, '.product_main>.price_color')
    CHECK_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    CLICK_BUTTON_BASKET = (By.CSS_SELECTOR, '.basket-mini>.btn-group>.btn')
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p>a")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    USER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    USER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    USER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "[name='registration_submit']")



