# Класс Mammal представляет род млекопитающих.

class Mammal:
    # Метод __init__ принимает аргумент для
    # вида млекопитающего.

    def __init__(self, species):
        self.__species = species

    # Метод show_species выводит сообщение
    # о виде млекопитающего.

    def show_species(self):
        print('Я - ', self.__species)

    # Метод make_sound издаёт характерный
    # для всех млекопитающих звук.

    def make_sound(self):
        print('Грррррр...')
