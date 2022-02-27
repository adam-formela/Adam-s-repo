# 1. ZMIENNE

# Zadanie1. Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.


dystans = 120
spalanie = 6.4 / 100
cena = 5.04
print(type(cena))

koszt_wyprawy = dystans * spalanie * cena
koszt_wyprawy = round(koszt_wyprawy,2)

print(f'Laczny koszt wyprawy wyniosl {koszt_wyprawy} zl')


# Zadanie2. Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.


dystans = int(input('Wprowadz przebyty dystans [w km]: '))

spalanie = float(input('Wprowadz wartosc spalania samochodu [na 100 km]: '))
spalanie = spalanie / 100

cena = float(input('Wprowadz cene benzyny [za 1 litr]: '))

koszt_wyprawy = dystans * spalanie * cena
koszt_wyprawy = round(koszt_wyprawy,2)

print(f'Laczny koszt wyprawy wyniosl {koszt_wyprawy} zl')
