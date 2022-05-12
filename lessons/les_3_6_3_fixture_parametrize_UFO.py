import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import math
import time


@pytest.fixture(scope='function')
def browser(request):
    print('Start browser')
    browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
    def finish_browser():
        browser.quit()
    print('Start request')
    request.addfinalizer(finish_browser)
    return browser

@pytest.mark.parametrize('links', ['https://stepik.org/lesson/236895/step/1',
                                'https://stepik.org/lesson/236896/step/1',
                                'https://stepik.org/lesson/236897/step/1',
                                'https://stepik.org/lesson/236898/step/1',
                                'https://stepik.org/lesson/236899/step/1',
                                'https://stepik.org/lesson/236903/step/1',
                                'https://stepik.org/lesson/236904/step/1',
                                'https://stepik.org/lesson/236905/step/1'
                                    ])
def test_find_link_login(browser, links):
    link = links
    browser.get(link)
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    correct_field = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert correct_field == "Correct!"


