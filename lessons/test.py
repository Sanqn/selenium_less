class Toy:

    color = 'Red' #атрибут класса

    def __init__(self, name, age):
        self.age = age #атрибут экземпляра класса
        self.name = name

    @classmethod
    def game_dol(cls):
        return cls('Fist', 25)

    @staticmethod
    def adult(age):
        if age > 18:
            return True
        else:
            return False

toy = Toy.game_dol() #создаем объект класса
print(toy.age)
print(toy.name)
print(Toy.adult(19))

def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world():
    print('Hello world!')

hello_world()

