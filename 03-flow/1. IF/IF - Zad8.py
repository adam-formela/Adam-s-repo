# Zadanie 8. Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

number1 = int(input('Wprowadz liczbe calkowita numer 1: '))
number2 = int(input('Wprowadz liczbe calkowita numer 2: '))
number3 = int(input('Wprowadz liczbe calkowita numer 3: '))

list = [number1, number2, number3]

print(f'Wprowadzone liczby to: {list}')
print()

list.sort(reverse=True)

print(f'Najwieksza wprowadzona liczba to: {list[0]}')
print()

print(f'Posortowane liczby od najwiekszej do najmniejszej: {list}')
