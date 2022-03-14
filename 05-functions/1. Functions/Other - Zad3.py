# Zad3. Obsluz blad uzytkownika - uzytkownik zapyta o ksiazke w bazie ktora nie itnieje.

books = {
    'LOTR':8,
    'harry':9,
    'Batman':5
    }

def show_book(title):
    print(f'Ksiazka {title} ma ocene {books[title]}')


while True:
    given_title = input('Podaj tytul: ')
    if given_title in books.keys():
        break
    print('Nie ma takiej ksiazki w bazie danych.')
    continue

show_book(given_title)