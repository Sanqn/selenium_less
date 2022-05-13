from conftest import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form>.btn-add-to-basket")



