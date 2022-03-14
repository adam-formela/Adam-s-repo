# Zadanie 2. Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

list = ['maslo', 'ser', 'pomidor', 'sol', 'pieprz']

print('Na chleb naloz po kolei: ')
for ingrediens in list:
    print('-', ingrediens)
print('Gotowe!')