#2. SYSTEMY LICZBOWE

# Zadanie1. Na kartce papieru oblicz jak twój wiek będzie reprezentowany binarnie. Sprawdź czy to samo zwróci Python.

dec = int(input('Wprowadz twoj wiek: '))
print('Twoj wiek w systemie binarnym to: '+ str(bin(dec)))

# Zadanie2. Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym. Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).


bin_num = 1001111
print(int(bin_num))
print((1*2**6) + (1*2**3) + (1*2**2) + (1*2**1) + (1*2**0))

bin_num = '1001111'
dec = int(bin_num, 2)
print(dec)


# Zadanie3. Dla liczb hex_num = 1DB i oct_num = 2063 zwróć wartość w systemie dziesiętynym.


hex_num = '1DB'
dec1 = int(hex_num, 16)
print(dec1)

oct_num = '2063'
dec2 = int(oct_num, 8)
print(dec2)
