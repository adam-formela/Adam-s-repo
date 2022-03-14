#Zad3. Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

numbers = (1,2,3,4,5)
numbers2 = (6,7,8,9,10)

list = []
list = numbers[::2] + numbers2[1::2]

list = set(list)
print(list)
print(type(list))
