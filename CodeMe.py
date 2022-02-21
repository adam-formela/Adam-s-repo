# BMI = (masa (kg)) / (wzrost (m))2

waga = input('Podaj swoja wage: ')
wzrost = input('Podaj swoj wzrost w m: ')

BMI = (float(waga) / float(wzrost)**2)
print(f'Twoje BMI wynosi: {BMI}')

