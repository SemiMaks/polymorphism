# Эта программа демонстрирует полиморфизм.

from animals import Mammal
from cat import Cat
from dog import Dog

sept = '-' * 25


def main():
    # Создать объект Mammal, объект Dog
    # и объект Cat.
    mammal = Mammal('Обычное животное.')
    dog = Dog()
    cat = Cat()

    # Показать информацию о каждом животном.
    print('Вот несколько животных и звуки, которык они издают.')
    print(sept)
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info('Я - последовательность символов, а не ссылка на объект.')


# Функция show_mammal_info принимает объект в качестве
# аргумента и вызывает свои методы show_species и make_sound.

def show_mammal_info(creature):
    if isinstance(creature, Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('Это не млекопитающее!')


# Вызываем главную функцию.
main()
