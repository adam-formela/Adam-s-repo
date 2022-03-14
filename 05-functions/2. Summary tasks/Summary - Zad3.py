# Zadanie 3. Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def max_function(number1, number2, number3):
    number_list = [number1, number2, number3]
    number_list_sorted = sorted(number_list, reverse=True)
    print(f'Najmniejsza podana liczba to: {number_list_sorted[0]}')

max_function(543,643,222)
