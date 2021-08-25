# Класс Dog является подклассом Mammal

from animals import Mammal


class Dog(Mammal):
    # Метод __init__ вызывает метод __init__
    # надкласса, передавая 'собаку' в качестве вида.

    def __init__(self):
        Mammal.__init__(self, 'собака')

    # Метод make_sound переопределяет
    # метод make_sound надкласса.
    def make_sound(self):
        print('Гав-гав')
