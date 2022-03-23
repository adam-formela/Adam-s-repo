'''
Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py. Zaimportuj module do pliku fitmeter.py.
Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.

    Utwórz plik bmi.py zawierający metodę obliczania bmi. Metoda zwraca wartości: niedowaga, waga normalna, nadwaga, otyłość.

    Utwórz 4 pliki .txt zawierające porady.

    Utwórz plik fitmeter.py, który zaimportuje moduł bmi.

    fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.

    Na podstawie zwróconej wartości fitmeter.py wyświetli odpowiednie porady dla pacjenta.
'''

import bmi

def show_advice(state):
    filename = state + '.txt'
    with open(filename) as fopen:
        content = fopen.read()

    print('----Twoja porada:')
    print(content)


def main():
    w = float(input('Podaj swoją wagę [kg]: '))
    h = float(input('Podaj swoj wzrost [m]: '))
    result = bmi.get_bmi_value(w, h)
    show_advice(result)


if __name__ == '__main__':
    main()