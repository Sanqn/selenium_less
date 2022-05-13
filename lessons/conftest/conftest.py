import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--user_language', action='store', default=None,
                     help="Choose language: ru, en ...")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("user_language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(service=Service('C:\geckodriver\geckodriver.exe'), firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    # yield browser
    # print("\nquit browser..")
    # browser.quit()
    def close_window():
        browser.quit()
    print('finish request')
    request.addfinalizer(close_window)
    return browser