# Zadanie 1. Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#     C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

# WHILE:

fahrenheit = 0

while fahrenheit > -1:
    celsius = round(5/9 * (fahrenheit - 32),2)
    print(f'{fahrenheit} stopni F to {celsius} stopni C')
    if fahrenheit >= 200:
        break
    fahrenheit += 20

# FOR:

fahrenheit = 0

for i in range(0, 201, 20):
    print(fahrenheit, 'F to ', round(5 / 9 * (fahrenheit - 32),2), 'C')
    fahrenheit += 20


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

