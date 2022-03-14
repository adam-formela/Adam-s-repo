# Zad3. Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystkich elementów na liście.

def number_sum():
    list = []
    for num in range(5):
        num2 = int(input(f'Podaj liczbe nr {num+1}: '))
        list.append(num2)
    print(sum(list))

number_sum()