# Zad2. Napisz funkcje, ktora zapyta o numer ksiazki i wyswietli film wraz z ocena.

books = {
    'LOTR':8,
    'harry':9,
    'Batman':5
    }

def show_book(title):
    print(f'Ksiazka {title} ma ocene {books[title]}')

given_title = input('Podaj tytul: ')

show_book(given_title)