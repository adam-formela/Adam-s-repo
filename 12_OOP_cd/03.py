# Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple. Logiki to nie ma, więc dodaj wg uznania.

class Pen():
    def __init__(self):
        print('Pen', end='')


class Apple(Pen):
    def __init__(self):
        print('Apple', end='')
        super().__init__()


class Pinapple(Apple):
    def __init__(self):
        print('Pineapple', end='')
        super().__init__()


class Pen(Pinapple):
    def __init__(self):
        print('Pen', end='')
        super().__init__()


class PenPineapple(Pen):
    pass


desc = PenPineapple()



