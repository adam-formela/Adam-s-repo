# 4. STRINGI

# Zadanie 1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.


a = 'banananan'

len_txt = (len(a)) // 2
print(len_txt)
print(a[len_txt-1:len_txt+2])


# Zadanie 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.


s1 = 'Kacper'
s2 = 'Adrianna'

len_s1 = (len(s1)) // 2 #3
print(len_s1)

s3 = s1[:len_s1] + s2 + s1[len_s1:]
print(s3)


# Zadanie3. Do zmiennej quote przypisz zdanie: „Honesty is the first chapter in the book of wisdom.”, a następnie:

quote = 'Honesty is the first chapter in the book of wisdom.'

# a) Policz wszystkie znaki w napisie

print(len(quote))

# b) Nie modyfikując zmiennej wyświetl słowo wisdom

print(quote[-7:-1])

# c) Wyświetl tylko pierwszą połowę tekstu

len_quote = len(quote) // 2

print(quote[:len_quote])

# d) Wyświetl tylko kropkę

print(quote[-1:])

# e) Wyświetl od połowy tylko co trzecią literę cytatu

print(quote[len_quote::3])

# f) Wyświetl ‘Hnsyi h is hpe ntebo fwso.’

print(quote[::2])

# g) Wyświetl cały cytat odwrotnie

print(quote[::-1])

# h) Zamień wisdom na słowo friendship

print(quote.replace('wisdom','friendship'))

# Zadanie4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

book_title = input('Podaj tytul ksiazki: ')
book_author = input('Podaj autora ksiazki: ')
book_pages = input('Podaj liczbe stron ksiazki: ')


# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.


print(book_title.isalpha())
print(book_author.isalpha())
print(type(book_pages))


# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich


if book_title.istitle() == False:
    print('Podana nazwa ksiazki to: '+ book_title)
    print('Nazwa ksiazki z wielkiej litery: '+ book_title.capitalize())
else:
    print('Tytul zostal podany z wielkiej litery')

if book_author.istitle() == False:
    print('Podana nazwa autora to: '+ book_author)
    print('Nazwa autora z wielkiej litery: '+ book_author.capitalize())
else:
    print('Autor zostal podany z wielkiej litery')


# Połącz dane w jeden ciąg book za pomocą spacji


book = (book_title + " " + book_author + " " + book_pages)
print(book)


# Policz liczbę wszystkich znaków w napisie book

print(len('book'))

# Zadanie5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.


sentence = input('Wprowadz potencjalne zdanie ktore moze byc palindromem: ')

sentence = sentence.replace(" ","")
sentence = sentence.lower()

if sentence == sentence[::-1]:
    print('To zdanie jest polindromem')
else:
    print('To zdanie nie jest polindromem')


# Zadanie 6. Przekopiuj zawartość import this do zmiennej.

import this

text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

# Policz liczbę wystąpień słowa better.

print(text.count('better'))

# Usuń z tekstu symbol gwiazdki

print(text.replace('*',''))

# Zamień jedno wystąpienie explain na understand

print(text.replace('explain','understand',1))

# Usuń spacje i połącz wszystkie słowa myślnikiem

print(text.replace(' ','-'))

# Podziel tekst na osobne zdania za pomocą kropki

#  TODO Nie rozumiem co tu trzeba zrobic, zdania sa juz podzielone za pomoca kropki...

# Zadanie 7. Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową. Użyj funkcji format(), by wyświetlić zdanie zawierające te wartości.


age = 27
name = 'Adam'

print(f'Masz na imie {name} i masz {age} lat')
