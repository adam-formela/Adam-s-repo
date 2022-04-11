from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r
        self.pi = 3.14

    def area(self):
        return self.pi * self.r**2

    def __repr__(self):
        return f'Circle area = {self.area()}'


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

    def __repr__(self):
        return f'Square area = {self.area()}'

c = Circle(10)
print(c)

s = Square(10)
print(s)

print(s.area() + c.area())