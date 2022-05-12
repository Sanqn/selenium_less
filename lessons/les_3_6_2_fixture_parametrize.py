import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture(scope='function')
def browser(request):
    print('Start browser')
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    def finish_browser():
        browser.quit()
    print('Start request')
    request.addfinalizer(finish_browser)
    return browser

@pytest.mark.parametrize('language', ['ru', 'en-gb'])
def test_find_link_login(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


