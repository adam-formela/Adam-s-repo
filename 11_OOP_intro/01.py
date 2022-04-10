# Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#         atrybuty: imię, kolor sierści, rasę
#         metody: szczekaj, machaj ogonem
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class Dog():
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def bark(self, number = 1):
        return 'hau ' * number

    def wave_tail(self):
        return 'machu-machu'

dyzio = Dog('Dyzio', 'black', 'posnanian terrier')
print(dyzio.__dict__)

print(dyzio.bark(10))
print(dyzio.wave_tail())

reksio = Dog('Reksio', 'white', 'Bielsko-Biała\'s dog')
print(reksio.__dict__)
