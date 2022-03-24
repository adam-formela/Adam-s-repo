'''
Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.

Wejście:

    var = ‘banannnnannnnnnnnnanananananaaaana’
Wyjście

    ‘nnnnnnnnn’, 9

    Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr od 0-9. Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.

    Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.

    Zaimportuj generator bezpośrednio do programu.
'''
import generator

# text = 'banannnnannnnnnnnnanananananaaaana'
text = generator.get_number()
print(text)

list = []
longest_list = []
counter = 0
longest_counter = 0

for i in text:
    if list == []:
        list.append(i)
        counter += 1
    elif i in list:
        list.append(i)
        counter += 1
        if len(longest_list) < len(list):
            longest_list = list
        if longest_counter < counter:
            longest_counter = counter
    else:
        list = []
        counter = 0
        list.append(i)
        counter += 1
        continue

if len(longest_list) == 0:
    print('There are no at least 2 characters in the sequence')
else:
    for j in longest_list:
        print(j, end="")

    print(f" - '{j}' occured {longest_counter} times in a sequence")