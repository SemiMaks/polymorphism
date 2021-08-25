from animals import Mammal
from dog import Dog
from cat import Cat

sept = '-' * 25

print(sept)
mammal = Mammal('Обычное млекопитающее.')
mammal.show_species()
mammal.make_sound()

print(sept)
dog = Dog()
dog.show_species()
dog.make_sound()

print(sept)
cat = Cat()
cat.show_species()
cat.make_sound()
