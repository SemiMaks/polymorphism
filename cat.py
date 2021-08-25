# Класс Cat является подклассом классом Mammal.

from animals import Mammal


class Cat(Mammal):
    # Метод __init__ вызыввает метод __init__
    # надкласа, передаёт 'кот' в качестве вида.

    def __init__(self):
        Mammal.__init__(self, 'кот')

    def make_sound(self):
        print('Мяу-мяу')
