class Point:
    def __init__(self, num):
        self.__x = '0'
        self.num = num

    def get(self):
        return self.__x

    def set(self, x):
        self.__x = x


p1 = Point(10)
print('point value', p1.num)
print('point x params:', p1.get())
p1.set(1)
print('point x params:', p1.get())