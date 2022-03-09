# Zadanie 4. Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

number = int(input('Podaj liczbe naturalna nie wieksza niz 8: '))

if number <= 0:
    print('Podana liczba nie jest liczba naturalna')
    exit()
if number > 8:
    print('Podana liczba jest wieksza niz 8')
    exit()

sum = 1

for number in range(1,number+1):
    sum = sum*number
print(number,'! = ',sum)