# Zadanie 6. Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

hidden_number = 67
number = int(input('Podaj numer [1-100]: '))

if number == hidden_number:
    print('Gratulacje!')
else:
    print('Pudlo')