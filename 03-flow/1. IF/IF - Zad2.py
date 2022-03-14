# Zadanie 2. Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

number1 = int(input('Podaj pierwsza liczbe: '))
number2 = int(input('Podaj druga liczbe: '))

if (number1 + number2) > 100:
    print(number1 + number2)
else:
    print('Koniec')