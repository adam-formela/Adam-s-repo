# Zad1. Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.
# BMI = (masa (kg)) / (wzrost (m))²

def bmi(weight, height):
    bmi_result = round(weight / height **2,2)
    print(f'BMI = {bmi_result}')
    if bmi_result < 18.5:
        return 'Niedowaga'
    elif bmi_result >= 25 and bmi_result <= 29.9:
        return 'Nadwaga'
    elif bmi_result >= 30:
        return "Otylosc"
    else:
        return 'Waga normalna'

result = bmi(56, 1.6)
print(result)
