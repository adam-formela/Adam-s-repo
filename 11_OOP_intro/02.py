# Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki. Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
# Utwórz kilka storczyków z różnymi parametrami.

class Flower(object):
    plant_family = 'orchid'
    def __init__(self, color, flowering_time, type):
        self.color = color
        self.flowering_time = flowering_time
        self.type = type

    def water_flower(self, amount_of_water):
        if amount_of_water > 200:
            print(f"The flower '{self.type}' is dead. You poured too much water.")
        elif amount_of_water < 50:
            print(f"The flower '{self.type}' is dead. You poured too little water.")
        else:
            print(f"The flower '{self.type}' is hydrated.")

flower1 = Flower('yellow', 'autumn', 'new orchid')
flower2 = Flower('blue', 'summer', 'old orchid')

flower1.water_flower(210)
flower2.water_flower(100)
