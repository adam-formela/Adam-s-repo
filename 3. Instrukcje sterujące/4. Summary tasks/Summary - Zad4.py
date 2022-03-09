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