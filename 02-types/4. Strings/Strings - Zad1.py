# Zadanie 1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

a = 'banananan'

len_txt = (len(a)) // 2
print(len_txt)
print(a[len_txt-1:len_txt+2])