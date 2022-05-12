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
    print('Start rquest')
    request.addfinalizer(finish_browser)
    return browser

class TestPageLink:


    @pytest.mark.smoke
    def test_link_should_be_see(self, browser):
        print('Start link login')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
        print('Finish link login')

    @pytest.mark.regression
    def test_basket_should_see(self, browser):
        print('Start link basket')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini>.btn-group>a.btn')
        print('Finish link basket')



