import time

from conftest import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
    browser.get(link)
    #time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "На странице нет кнопки добавления товара в корзину"



