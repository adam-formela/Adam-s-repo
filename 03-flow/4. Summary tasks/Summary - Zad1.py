# Zadanie 1. Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.

names = []

while True:
    print('Podaj imie: ')
    name = input()
    if name == '':
        break
    names = names + [name]
print(names)

for name in names:
    print('Hello', name)