# Zadanie 7. Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
#BMI = (masa (kg)) / (wzrost (m))²

masa = int(input('Podaj wage w kg: '))
wzrost = float(input('Podaj wzrost w metrach np [1.77]: '))

BMI = round(masa / (wzrost ** 2),2)

print(BMI)

if BMI < 18.5:
    print('Niedowaga')
elif BMI >= 25 and BMI <= 29.9:
    print('Nadwaga')
elif BMI >= 30:
    print("Otylosc")
else:
    print('Waga normalna')