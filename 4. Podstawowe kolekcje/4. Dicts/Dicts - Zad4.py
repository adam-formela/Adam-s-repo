# Zadanie 4. Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.



list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

list1 = list[0]
list2 = list[1]

for i in list1:
    for j in list2:
        print(i*j, end='\t')
    print()