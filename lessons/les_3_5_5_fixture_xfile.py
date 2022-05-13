import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='function')
def browser(request):
    print('Start browser')
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    def finish_browser():
        browser.quit()
    print('finish request')
    request.addfinalizer(finish_browser)
    return browser

class TestPageLink:

    @pytest.mark.skip
    def test_link_should_be_see(self, browser):
        print('Start link login')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
        print('Finish link login')


    def test_basket_should_see(self, browser):
        print('Start link basket')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini>.btn-group>a.btn')
        print('Finish link basket')

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        print('button Xfile')
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")

#pytest -rx -v  les_3_5_5_fixture_xfile.py (-rv to see reason="fixing this bug right now" in xfile)
