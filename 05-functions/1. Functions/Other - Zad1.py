# Zad1. Napisz funkcje, ktora pyta usera o pary ksiazka + ocena i zapisuje je w programie.

def save_book():
    book_title = input('Podaj tytul ksiazki: ')
    book_rate = int(input('Podaj ocene ksiazki 1-10: '))
    books[book_title] = book_rate

books = {}

for i in range(3):
    save_book()
    print('-------')

print(books)