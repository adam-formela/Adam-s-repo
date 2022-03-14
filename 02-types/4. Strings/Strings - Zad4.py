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