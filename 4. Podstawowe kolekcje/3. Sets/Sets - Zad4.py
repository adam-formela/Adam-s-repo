# Zadanie 4. Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#
#     input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#
#     output:
#
#     [4, 3, 2, 1]
#     [14, 13, 12, 11]
#     [24, 23, 22, 21]

list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

len_list = len(list)
print(f'Dlugosc listy to {len_list}')

equal_parts = int(len_list/3)
if len_list % 3 == 0:
    print(f'Aby podzielic liste na 3 rowne czesci, kazda lista powinna skladac sie z {equal_parts} elementow')
else:
    print('Listy nie da sie podzielic na 3 rowne czesci')

list1 = []
list2 = []
list3 = []

for i in list:
    if len(list1) < equal_parts:
        list1.append(i)
        continue
    if len(list2) < equal_parts:
        list2.append(i)
        continue
    if len(list3) < equal_parts:
        list3.append(i)
        continue

print(sorted(list1, reverse=True))
print(sorted(list2, reverse=True))
print(sorted(list3, reverse=True))

