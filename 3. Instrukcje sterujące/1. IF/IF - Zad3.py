# Zadanie 3. Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

score1 = int(input('Wprowadz swoja opinie o ksiazce [1-10]: '))
score2 = int(input('Wprowadz swoja opinie o ksiazce [1-10]: '))
score3 = int(input('Wprowadz swoja opinie o ksiazce [1-10]: '))

print('Srednia opinia o ksiazce wynosi: ' + str(((score1 + score2 + score3)/3)))

if (score1 + score2 + score3)/3 > 7:
    print('bardzo dobra')
elif (score1 + score2 + score3)/3 > 5:
    print('warta uwagi')
else:
    print('nie warta uwagi')