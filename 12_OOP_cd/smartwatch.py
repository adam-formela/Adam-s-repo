class ElectricThings():
    def get_electric(self):
        print('ElectricThings ----')

class Electoronics:
    def get_electronic(self):
        print('Electronics ****')

class Watch(Electoronics):
    def __init__(self):
        print('Watch function is presenting the time')

    def show_time(self):
        print('18:50')


class Phone(ElectricThings):
    def __init__(self):
        print('Phone is great invent')

    def make_call(self):
        print('Calling... best friend')



class SmartWatch(Watch, Phone):
    def __init__(self):
        print('This smartwatch is great')


handband = SmartWatch()
handband.make_call()
handband.show_time()
handband.get_electronic()
handband.get_electric()