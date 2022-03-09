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