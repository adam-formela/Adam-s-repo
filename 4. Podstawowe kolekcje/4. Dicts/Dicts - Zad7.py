# Zadanie 7. Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

list_no_duplicates = []
repeating_items = []

for i in example_list:
    if i not in list_no_duplicates:
        list_no_duplicates.append(i)
    else:
        if i not in repeating_items:
            repeating_items.append(i)

print(f'Powtarzajace sie elementy listy to: {repeating_items}')

print(f'Nieposortowana lista: {list_no_duplicates}')

new_list_sorted = sorted(list_no_duplicates)

print(f'Posortowana lista: {new_list_sorted}')

tuple = tuple(new_list_sorted)

print()
print(tuple)

print('Minimalna liczba w krotce to: ' + str(tuple[0]))

len_tuple = len(tuple)

print('Maksymalna liczba w krotce to: ' + str(tuple[len_tuple-1]))