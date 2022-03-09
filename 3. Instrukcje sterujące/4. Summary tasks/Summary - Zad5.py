# Zadanie 5.  Stwórz grę ciepło zimno.
#         Komputer losuje liczbę z zakresu od 1 do 100.
#         Użytkownik podaje swój traf.
#         Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#         Jeśli użytkownik zgadnie wygrywa gracz.
#         Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

number = random.randint(1,100)

for i in range(6):
    user_number = int(input('Podaj swoj traf: '))
    if user_number == number:
        break
    elif user_number <= number + 5 and user_number >= number - 5:
        print('Cieplo')
        continue
    else:
        print('Zimno')
        continue
if user_number == number:
    print('Trafiles')
else:
    print('Niestety nie udalo Ci sie trafic')