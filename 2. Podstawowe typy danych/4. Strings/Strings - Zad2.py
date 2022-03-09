# Zadanie 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = 'Kacper'
s2 = 'Adrianna'

len_s1 = (len(s1)) // 2 #3
print(len_s1)

s3 = s1[:len_s1] + s2 + s1[len_s1:]
print(s3)