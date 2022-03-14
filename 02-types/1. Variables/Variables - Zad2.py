# Zadanie2. Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

dystans = int(input('Wprowadz przebyty dystans [w km]: '))

spalanie = float(input('Wprowadz wartosc spalania samochodu [na 100 km]: '))
spalanie = spalanie / 100

cena = float(input('Wprowadz cene benzyny [za 1 litr]: '))

koszt_wyprawy = dystans * spalanie * cena
koszt_wyprawy = round(koszt_wyprawy,2)

print(f'Laczny koszt wyprawy wyniosl {koszt_wyprawy} zl')
