# Zadanie 5. Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input('Podaj haslo: ')

if password.__contains__('!' or '&' or '^' or '%' or '$' or '#'):
    print('Haslo zawiera znak specjalny')
    if len(password) < 8:
        print('Haslo musi zawirac co najmniej 8 znakow')
    elif password.islower():
        print('Haslo musi zawierac co najmniej 1 wielka lietre')
    elif password.isalnum():
        print('Haslo musi zawierac co najmniej 1 cyfre')
    else:
        print('Haslo poprawne')
else:
    print('Haslo nie zawiera znaku spcjalnego')