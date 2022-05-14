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

import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/ru/'

browser = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'), options=webdriver.ChromeOptions())
browser.get(link)
login_url = browser.find_element(By.CSS_SELECTOR, '#login_link').click()
new_window = browser.current_url
print(new_window)




