# Zadanie 3. Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

print('Podaj wymiar tablicy: ')
n = int(input())

array = [['-'] * n] * n
print(array)
print()
for row in array:
    for col in row:
        print(col, end=' ')
    print() # dodaje enter po kazdym wierszu