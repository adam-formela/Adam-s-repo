#Zadanie 4. Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def range(a,b):
    number = int(input('Podaj liczbe: '))
    if number >= a and number <= b:
        print(f'Tak, liczba {number} znajduje się w zadanym zakresie')
    else:
        print(f'Nie, liczba {number} jest z poza zakresu')


range1 = int(input('Podaj wartosc poczatkowa zakresu: '))
range2 = int(input('Podaj wartosc koncowa zakresu: '))

range(range1, range2)