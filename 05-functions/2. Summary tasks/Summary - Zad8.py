# Zadanie 8. Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
'''
    Program zacznie ze stworzonym słownikiem o trzech kluczach:
            marka (str)
            model (str)
            rocznik (int)
    Wypisze ten słownik na ekran (bez żadnego formatowania)
    Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
        “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
    Jeśli nie spełnia powyższego warunku, wypisze komunikat:
        “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
    Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.
'''

car_dict = {
    'brand' : 'Volkswagen',
    'model' : 'Golf',
    'year' : 2006
}

brand = car_dict.get('brand')

print(car_dict)
if car_dict.get('year') <= 1997:
    print(f'Congratulations! Your car {brand} may be registered as an antique.')
else:
    print(f'You car {brand} is still too modern.')