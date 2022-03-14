# Zadanie 2. Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}. Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?
# append() - dodaje element na koniec listy -
# extend() - rozszerza listę o inną listę -
# insert() - wstawia element do listy pod danym indeksie -
# remove() - wyszukuje dany element na liście i usuwa pierwszy pasujący element (sets only)
# index() - przeszukuje element na liście i zwraca jego indeks (tuple only)
# count() - zwraca liczbę wystąpień elementu na liście (tuple only)
# pop() - usuwa element z listy pod podanym indeksem, zwraca również usunięty element (sets only)
# reverse() - odwraca kolejność elementów na liście -

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

method_list = ['append()','extend()','insert()','remove()','index()','count()','pop()','reverse()']

tuple_nonworking_metods = []
set_nonworking_metods = []

for i in method_list:
    if i == method_list[0]:
        try:
            T_test.append()
        except AttributeError:
            tuple_nonworking_metods.append(i)
    if i == method_list[1]:
        try:
            T_test.extend()
        except AttributeError:
            tuple_nonworking_metods.append(i)
    if i == method_list[2]:
        try:
            T_test.insert()
        except AttributeError:
            tuple_nonworking_metods.append(i)
    if i == method_list[3]:
        try:
            T_test.remove(1)
        except AttributeError:
            tuple_nonworking_metods.append(i)
    if i == method_list[4]:
        try:
            T_test.index(1)
        except AttributeError:
            tuple_nonworking_metods.append(i)
    if i == method_list[5]:
        try:
            T_test.count(2)
        except AttributeError:
            tuple_nonworking_metods.append(i)
    if i == method_list[6]:
        try:
            T_test.pop(1)
        except AttributeError:
            tuple_nonworking_metods.append(i)
    if i == method_list[7]:
        try:
            T_test.reverse()
        except AttributeError:
            tuple_nonworking_metods.append(i)

for i in method_list:
    if i == method_list[0]:
        try:
            S_test.append()
        except AttributeError:
            set_nonworking_metods.append(i)
    if i == method_list[1]:
        try:
            S_test.extend()
        except AttributeError:
            set_nonworking_metods.append(i)
    if i == method_list[2]:
        try:
            S_test.insert()
        except AttributeError:
            set_nonworking_metods.append(i)
    if i == method_list[3]:
        try:
            S_test.remove(1)
        except AttributeError:
            set_nonworking_metods.append(i)
    if i == method_list[4]:
        try:
            S_test.index(1)
        except AttributeError:
            set_nonworking_metods.append(i)
    if i == method_list[5]:
        try:
            S_test.count(2)
        except AttributeError:
            set_nonworking_metods.append(i)
    if i == method_list[6]:
        try:
            S_test.pop()
        except AttributeError:
            set_nonworking_metods.append(i)
    if i == method_list[7]:
        try:
            S_test.reverse()
        except AttributeError:
            set_nonworking_metods.append(i)

print(f'Dla tuple nie beda dzialac metody {tuple_nonworking_metods}')
print(f'Dla setow nie beda dzialac metody {set_nonworking_metods}')