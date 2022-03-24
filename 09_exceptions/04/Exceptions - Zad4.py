# Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinen być odporny na błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
import os


arithmetic_sum = 0

while True:
    try:
        numbers_list = input('Enter several of numbers separated by comma: ').split(',')
        print('Provided numbers :', numbers_list)
        if len(numbers_list) < 2:
            print('Enter several numbers')
            continue
        for e in numbers_list:
            arithmetic_sum = arithmetic_sum + int(e)
        break
    except ValueError as err:
        with open('log.txt', 'a+') as f:
            f.write(f'Error: {err}')
        print('Provide correct numbers')

arithmetic_mean = arithmetic_sum / len(numbers_list)

print(f'Arithmetic mean from of the provided numbers is: {arithmetic_mean}')

if os.path.isfile('log.txt'):
    print('Error log created')