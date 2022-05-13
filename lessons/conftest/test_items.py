import time

from conftest import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
    browser.get(link)
    #time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form>.btn-add-to-basket")
    #assert button.text == 'Ajouter au panier' #test language France
    assert button.text == 'Añadir al carrito'  # test language France



