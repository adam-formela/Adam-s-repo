# Zad4. Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

def even_numbers(list):
    for i in list:
        if int(i) % 2 == 0:
            print(i)

list1 = [1,2,3,4,5,6,7,8,9,10,11,12]

even_numbers(list1)

