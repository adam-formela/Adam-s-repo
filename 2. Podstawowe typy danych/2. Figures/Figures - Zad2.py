# Zadanie2. Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym. Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).

bin_num = 1001111
print(int(bin_num))
print((1*2**6) + (1*2**3) + (1*2**2) + (1*2**1) + (1*2**0))

bin_num = '1001111'
dec = int(bin_num, 2)
print(dec)