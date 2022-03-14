#Zadanie4. Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

list = []

for i in range(0,6):
    print(f'Podaj element nr {i+1}: ')
    list.append(input())

len_list = len(list)
middle_item = int(len_list/2)

if list[middle_item-1] == list[middle_item]:
    print('Dwa środkowe elementy listy są takie same.')
else:
    print('Dwa środkowe elementy listy NIE są takie same.')