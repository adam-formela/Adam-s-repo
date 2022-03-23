# Stwórz moduł, który przechowuje wzór na deltę. Skorzystaj z wbudowanego modułu math. W nowym pliku wykorzystaj moduł.
# delta = b**2 - 4ac

import delta

def delta_result(result):
    print(f'Delta wynosi: {result}')
    if result > 0:
        print('Delta dodania. Funkcja kwadratowa ma 2 miejsca zerowe.')
    elif result < 0:
        print('Delta ujemna. Funkcja kwadratowa nie ma miejsc zerowych.')
    else:
        print('Delta ma 1 miejsce zerowe.')

def main():
    a = float(input('Podaj wartosc wspolczynnika A: '))
    b = float(input('Podaj wartosc wspolczynnika B: '))
    c = float(input('Podaj wartosc wspolczynnika C: '))
    result = delta.calculate_delta(a, b, c)
    delta_result(result)


if __name__ == '__main__':
    main()
