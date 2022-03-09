#Zadanie2. Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

list = []

for i in range (1,11):
    print(f'Podaj liczbe nr {i}: ')
    list.append(int(input()))
    for j in list:
        if j % 2 != 0:
            continue
        else:
            list.remove(j)

print(f'Nieparzyste liczby to: {list}')