# Zadanie 9. 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach. Wyświetl najpopularniejszy przedmiot.
# (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)

user1 = ['polski', 'Matematyka', 'ANGIELSKI', 'historia']
user2 = ['biologia', 'Matematyka', 'ANGIELSKI', 'historia']
user3 = ['w-f', 'PLASTYKA', 'Sztuka', 'PO']
user4 = ['polski', 'Matematyka', 'ANGIELSKI', 'historia']
user5 = ['polski', 'PO', 'ANGIELSKI', 'Informatyka']

list = user1 + user2 + user3 + user4 + user5

list_lower = []

for i in list:
    list_lower.append(i.lower())

print(f'Lista (male litery): {list_lower}')

counting_dict = {}

for word in list_lower:
  if word in counting_dict:
    counting_dict[word] += 1
  else:
    counting_dict[word] = 1

counting_dict_sorted = sorted(counting_dict.items(), key=lambda item: item[1], reverse=True)

print(f'Najpopolarniejszym przedmiotem jest: {counting_dict_sorted[0][0]}. Przedmiot ten zostal podany {counting_dict_sorted[0][1]} razy.')