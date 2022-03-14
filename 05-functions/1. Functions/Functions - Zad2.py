# Zad2. Napisać funkcję, która sprawdza czy liczba jest parzysta.

def even_number(number):
    if number % 2 == 0:
        print(f'Liczba {number} jest parzysta')
    else:
        print(f'Liczba {number} NIE jest parzysta')

even_number(32)