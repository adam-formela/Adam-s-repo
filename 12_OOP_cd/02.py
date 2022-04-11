# Do klasy człowiek dodaj metodę super() tak, aby móc wyświetlić opis dostępny gdziekolwiek w klasie ssaki.

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
    def show_desc(self):
        super().show_desc()


human1 = Human()
human1.show_desc()

