# Zadanie 2. Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def min_function(number1, number2, number3):
    number_list = [number1, number2, number3]
    number_list_sorted = sorted(number_list)
    print(f'Najmniejsza podana liczba to: {number_list_sorted[0]}')

min_function(543,643,222)