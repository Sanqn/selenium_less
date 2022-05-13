import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(service=Service('C:\geckodriver\geckodriver.exe'), options=webdriver.FirefoxOptions())
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