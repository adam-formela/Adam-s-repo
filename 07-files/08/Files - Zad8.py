# Zad8. Utwórz generator dowolnego typu np. generator zdań, tweetów czy konferencji.
# Dane wejściowe pobierz z pliku csv (plik csv możesz traktować jako plik txt ze znanym znakiem podziału), który będzie przechowywał dane potrzebne do generowania.

import random

with open('generator.csv', encoding='utf-8') as f:
  content = f.readlines()

first = []
second = []
third = []

# for -> uzupełnie kolumny
for line in content:
  splitted_line = line.strip().split(';')
  first.append(splitted_line[0])
  second.append(splitted_line[1])
  third.append(splitted_line[2])

begining = random.choice(first)
mid = random.choice(second)
ending = random.choice(third)

print('Genereator tytułu konfernecji naukowej')
print('----------------------------------')
print(f'{begining} {mid} {ending}')