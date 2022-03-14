#Zad1. Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

def circular_field(radius):
    pi = 3.14
    return pi * (radius**2)

area = circular_field(3)

print(f'Pole wynosi {area}')