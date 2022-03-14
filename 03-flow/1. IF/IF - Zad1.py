# Zadanie 1. Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = int(input('Podaj liczbe 1-100: '))

if number % 3 == 0:
    print(f'Liczba {number} jest podzielna przez 3')
else:
    print(f'Liczba {number} NIE jest podzielna przez 3')