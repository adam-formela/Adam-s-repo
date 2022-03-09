# Zadanie3. Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.

tuple = (1,2,3,4,5,6)

number = int(input('Podaj dowolna liczbe: '))

if number in tuple:
    index = tuple.index(number)
    print(f'Indeks liczby {number} to {index}')
else:
    print(f'Podana liczba {number} nie znajduje sie w krotce')

