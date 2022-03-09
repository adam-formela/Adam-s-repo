# Zadanie1. Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

dystans = 120
spalanie = 6.4 / 100
cena = 5.04
print(type(cena))

koszt_wyprawy = dystans * spalanie * cena
koszt_wyprawy = round(koszt_wyprawy,2)

print(f'Laczny koszt wyprawy wyniosl {koszt_wyprawy} zl')