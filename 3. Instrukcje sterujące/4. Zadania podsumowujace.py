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

# Zadanie 2. Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

text = 'abrakadabra'
len_text = int(len(text))

for letter in range(1,len_text,2):
    print(text[letter])

text = 'abrakadabra'
len_text = int(len(text))

print(text[1::2])

# Zadanie 3. W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

text = 'abra123!ABC'

counter = 0
for i in text:
    if i.islower():
        counter += 1
print(f'Ilosc malych liter w tekscie to: {counter}')

counter = 0
for i in text:
    if i.isupper():
        counter += 1
print(f'Ilosc duzych liter w tekscie to: {counter}')

counter = 0
for i in text:
    if i.isdigit():
        counter += 1
print(f'Ilosc duzych liter w tekscie to: {counter}')

counter = 0
for i in text:
    if not i.isdigit() and not i.isupper() and not i.islower():
        counter += 1
print(f'Ilosc znakow specjalnych w tekscie to: {counter}')

# Zadanie 4. Napisz grę - kamień (k) / papier (p) / nożyce (n).
        # Użytkownik podaje jedną z 3 figur.
        # Komputer losuje jedną z 3 figur.
        # Sprawdź kto wygrał tę rundę.
        # Zmień kod tak, by użytkownik mógł podac liczbę rund.
        # Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
        # Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

options =['k','p','n']

rounds = int(input('Podaj liczbe rund: '))

CPU_wins = 0
user_wins = 0

for i in range(1,rounds+1):
    print("Wybierz figure: kamień (k) / papier (p) / nożyce (n). Jesli chcesz zakonczyc gre wpisz 'koniec'")
    user = input()
    if user == 'koniec':
        exit()
    if user !='k' and user !='p' and user !='n':
        print('Miales wybrac k, p lub n')
        exit()
    CPU = random.choice(options)
    print(f'Wybrales: {user}')
    print(f'CPU wybral: {CPU}')

    if user == 'k' and CPU == 'k':
        print('draw')
    elif user == 'p' and CPU == 'p':
        print('draw')
    elif user == 'n' and CPU == 'n':
        print('draw')

    if user == 'k' and CPU == 'p':
        print('you loose')
        CPU_wins += 1
    elif user == 'k' and CPU == 'n':
        print('you win')
        user_wins += 1

    if user == 'p' and CPU == 'k':
        print('you win')
        user_wins += 1
    elif user == 'p' and CPU == 'n':
        print('you loose')
        CPU_wins += 1

    if user == 'n' and CPU == 'k':
        print('you loose')
        CPU_wins += 1
    elif user == 'n' and CPU == 'p':
        print('you win')
        user_wins += 1

print(f'Wygrales {user_wins} rund(y). CPU wygral {CPU_wins} rund(y)')
if user_wins > CPU_wins:
    print('Wygrales z komputerem')
elif user_wins < CPU_wins:
    print('Przegrales z komputerem')
else:
    print('Remis')


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

