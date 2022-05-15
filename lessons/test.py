# class Toy:
#
#     color = 'Red' #атрибут класса
#
#     def __init__(self, name, age):
#         self.age = age #атрибут экземпляра класса
#         self.name = name
#
#     @classmethod
#     def game_dol(cls):
#         return cls('Fist', 25)
#
#     @staticmethod
#     def adult(age):
#         if age > 18:
#             return True
#         else:
#             return False
#
# toy = Toy.game_dol() #создаем объект класса
# print(toy.age)
# print(toy.name)
# print(Toy.adult(19))
#
# def decorator_function(func):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         func()
#         print('Выходим из обёртки')
#     return wrapper
#
# @decorator_function
# def hello_world():
#     print('Hello world!')
#
# hello_world()
#
# import pytest
#
#
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected
import math

import pytest
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'

browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
browser.get(link)
login_url = browser.find_element(By.CSS_SELECTOR, '.price_color').text
print(login_url)
alert = browser.switch_to.alert
x = alert.text.split(" ")[2]
answer = str(math.log(abs((12 * math.sin(float(x))))))
alert.send_keys(answer)
alert.accept()
try:
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Your code: {alert_text}")
    alert.accept()
except NoAlertPresentException:
    print("No second alert presented")
print(x)




