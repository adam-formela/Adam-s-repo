#Zadanie3. Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

list = []
for i in range(0,5):
    print(f'Podaj liczbe calkowita nr {i+1}: ')
    list.append(int(input()))

if list[0] == list[-1]:
    print('Pierwszy i ostatni element listy sa takie same')
else:
    print('Pierwszy i ostatni element listy NIE sa takie same')