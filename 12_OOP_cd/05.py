# Stwórz abstrakcyjną klasę Pojazdy. Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki.
# Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane. Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def desc(self):
        pass

    @abstractmethod
    def require_driving_licence(self):
        pass


class Car(Vehicle):
    def desc(self):
        return 'Car is ....'

    def require_driving_licence(self):
        return 'cat. B'

    def __repr__(self):
        return f'Car - licence {self.require_driving_licence()}'

class Bike(Vehicle):
    def desc(self):
        return 'I love my bike ....'

    def require_driving_licence(self):
        return 'bike card'

    def __repr__(self):
        return f'Bike - licence {self.require_driving_licence()}'


suzuki = Car()
print(suzuki)

mars = Bike()
print(mars)
print(mars.desc())