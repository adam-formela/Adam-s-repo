# Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.

class Animals():
    is_animal = 'yes'

    def __init__(self):
        print('A new animal was created!')

    def show_desc(self):
        print('''Species of this genus are distinguished\
by their moderate to large size, their massive,\
well-developed skulls and dentition,\
long legs, and comparatively short ears and tails.''')


class Mammals(Animals):
    def show_desc(self):
        super().show_desc()


class Cat(Mammals):
    pass


class Dog(Mammals):
    pass


class Human(Mammals):
    pass


cat1 = Cat()
print(cat1.is_animal)
cat1.show_desc()