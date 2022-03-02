# Zadanie 1. Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = int(input('Podaj liczbe 1-100: '))

if number % 3 == 0:
    print(f'Liczba {number} jest podzielna przez 3')
else:
    print(f'Liczba {number} NIE jest podzielna przez 3')

# Zadanie 2. Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

number1 = int(input('Podaj pierwsza liczbe: '))
number2 = int(input('Podaj druga liczbe: '))

if (number1 + number2) > 100:
    print(number1 + number2)
else:
    print('Koniec')

# Zadanie 3. Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

score1 = int(input('Wprowadz swoja opinie o ksiazce [1-10]: '))
score2 = int(input('Wprowadz swoja opinie o ksiazce [1-10]: '))
score3 = int(input('Wprowadz swoja opinie o ksiazce [1-10]: '))

print('Srednia opinia o ksiazce wynosi: ' + str(((score1 + score2 + score3)/3)))

if (score1 + score2 + score3)/3 > 7:
    print('bardzo dobra')
elif (score1 + score2 + score3)/3 > 5:
    print('warta uwagi')
else:
    print('nie warta uwagi')


# Zadanie 4. Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

text = 'aaaaaaa'

if len(text) > 5:
    print('Tekst jest dluzszy niz 5 znakow')
if not text.__contains__('a'):
    print('Tekst nie zawiera litery a')
else:
    print('Tekst zawiera litere a')
    print(text.replace('a','z'))


# Zadanie 5. Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input('Podaj haslo: ')

if password.__contains__('!' or '&' or '^' or '%' or '$' or '#'):
    print('Haslo zawiera znak specjalny')
    if len(password) < 8:
        print('Haslo musi zawirac co najmniej 8 znakow')
    elif password.islower():
        print('Haslo musi zawierac co najmniej 1 wielka lietre')
    elif password.isalpha():
        print('Haslo musi zawierac co najmniej 1 cyfre')
    else:
        print('Haslo poprawne')
else:
    print('Haslo nie zawiera znaku spcjalnego')

# Zadanie 6. Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

hidden_number = 67
number = int(input('Podaj numer [1-100]: '))

if number == hidden_number:
    print('Gratulacje!')
else:
    print('Pudlo')

# Zadanie 7. Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
#BMI = (masa (kg)) / (wzrost (m))²

masa = int(input('Podaj wage w kg: '))
wzrost = float(input('Podaj wzrost w metrach np [1.77]: '))

BMI = round(masa / (wzrost ** 2),2)

print(BMI)

if BMI < 18.5:
    print('Niedowaga')
elif BMI >= 25 and BMI <= 29.9:
    print('Nadwaga')
elif BMI >= 30:
    print("Otylosc")
else:
    print('Waga normalna')

# Zadanie 8. Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

number1 = int(input('Wprowadz liczbe calkowita numer 1: '))
number2 = int(input('Wprowadz liczbe calkowita numer 2: '))
number3 = int(input('Wprowadz liczbe calkowita numer 3: '))

list = [number1, number2, number3]

print(f'Wprowadzone liczby to: {list}')
print()

list.sort(reverse=True)

print(f'Najwieksza wprowadzona liczba to: {list[0]}')
print()

print(f'Posortowane liczby od najwiekszej do najmniejszej: {list}')

