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