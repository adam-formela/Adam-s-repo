# Zadanie 5. Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#     Dorota, Wellman, dziennikarka
#     Adam, Małysz, sportowiec
#     Robert, Lewandowski, piłkarz
#     Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika

list = [
['Dorota', 'Wellman', 'dziennikarka'],
['Adam', 'Małysz', 'sportowiec'],
['Robert', 'Lewandowski', 'piłkarz'],
['Krystyna', 'Janda', 'aktorka']
]

for row in list:
    print('******')
    for item in row:
        print(item, end=' ')
    print()