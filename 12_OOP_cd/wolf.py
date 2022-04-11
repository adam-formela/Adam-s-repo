class Animal:
    def __init__(self):
        print("I'm animal !!!")

    def give_sound(self):
        print('ROAR!!!')

class Wolf(Animal):
    paw = 4

    def __init__(self):
        print("I'm WOLF!!!")

    def show_desc(self):
        print('''Species of this genus are distinguished
                   by their moderate to large size, their massive,
                   well-developed skulls and dentition,
                   long legs, and comparatively short ears and tails''')


class Dog(Wolf):
    def __init__(self,name,color,race,size):
        self.name = name
        self.color = color
        self.bread = race
        self.size = size

    def show_desc(self):
        super().show_desc()
        print('''Dog s a member of the genus Canis (canines),
            which forms part of the wolf-like canids.''')

# wolf_obj = Wolf()
# print(wolf_obj.paw)

nazar = Dog('Nazar','white','husky','big')
nazar.show_desc()
nazar.give_sound()