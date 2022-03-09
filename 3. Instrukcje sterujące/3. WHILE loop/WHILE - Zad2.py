# Zadanie 2. Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5

while True:
    number = int(input('Zgadnij liczbe od 0 do 20: '))
    if number == secret_num:
        print('Zgadles')
        break
    if number < secret_num:
        print('Podana liczba jest za mala. Sprobuj jeszcze raz')
    else:
        print('Podana liczba jest za duza. Sprobuj jeszcze raz')