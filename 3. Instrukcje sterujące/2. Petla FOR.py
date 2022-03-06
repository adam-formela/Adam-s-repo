# Zadanie 1. Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

items = ['latarka','kompas','noz']

for i in items:
    print('Spakowano: ', i)
print('Great, we are ready')

# Zadanie 2. Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

list = ['maslo', 'ser', 'pomidor', 'sol', 'pieprz']

print('Na chleb naloz po kolei: ')
for ingrediens in list:
    print('-', ingrediens)
print('Gotowe!')


# Zadanie 3. Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników. Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

sum_number = 0

for number in range(1,11):
    sum_number = sum_number + number
    print(sum_number)

# Zadanie 4. Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

number = int(input('Podaj liczbe naturalna nie wieksza niz 8: '))

if number <= 0:
    print('Podana liczba nie jest liczba naturalna')
    exit()
if number > 8:
    print('Podana liczba jest wieksza niz 8')
    exit()

if number == 8:
    silnia = (number * (number-1) * (number-2) * (number-3) * (number-4) * (number-5) * (number-6) * (number-7))
elif number == 7:
    silnia = (number * (number - 1) * (number - 2) * (number - 3) * (number - 4) * (number - 5) * (number - 6))
elif number == 6:
    silnia = (number * (number - 1) * (number - 2) * (number - 3) * (number - 4) * (number - 5))
elif number == 5:
    silnia = (number * (number - 1) * (number - 2) * (number - 3) * (number - 4))
elif number == 4:
    silnia = (number * (number - 1) * (number - 2) * (number - 3))
elif number == 3:
    silnia = (number * (number - 1) * (number - 2))
elif number == 2:
    silnia = (number * (number - 1))
elif number == 1:
    silnia = (number)

print(f'Silnia z {number} wynosi: {silnia}')
