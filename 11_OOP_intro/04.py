class Mammals(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} eats food.')

    def wave_tail(self):
        return 'machu-machu'


wolf = Mammals('Wolf')
horse = Mammals('Horse')
dog = Mammals('Dog')

wolf.eat()
horse.eat()
dog.eat()