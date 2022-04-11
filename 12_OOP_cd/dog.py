class Dog():
    vaccinated = True

    def __init__(self,name,color,race,size):
        self.name = name
        self.color = color
        self.bread = race
        self.size = size

    def drink_water(self, sound = 'bu!'):
        return f'pur pur pur omnomnom {sound}'


lord = Dog('Lord', 'black', 'spaniel','big beast')
nazar = Dog('Nazar','white','husky','big')
baron = Dog('Baron','brown','retriver', 'gryfin friend-small')

print(lord.__dict__)

print(lord.drink_water())
