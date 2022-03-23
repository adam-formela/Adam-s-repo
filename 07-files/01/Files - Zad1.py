# Zadanie 1. Utwórz plik na pulpicie zawierający listę ok. 20 cytatów.
# Każdy cytat powinen się znaleźć w nowej linii. Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:

# import random
#
# with open(input('Podaj swoj plik z cytatami z rozszerzeniem txt: ')) as fopen:
#   quotes = fopen.readlines()
#
# quote = random.choice(quotes).strip()
# width = len(quote) * 2
#
# print('Quote of the day: \n')
# print(width * '*')
# print(quote.center(width))
# print(width * '*')

#------------------------

import random


# funkcja do pobrania tekstu, zwraca liste
def get_quotes():
  with open('text.txt') as fopen:
    quotes = fopen.readlines()

  return quotes


# funkcja wyświetlająca
def show(content):
  quote = random.choice(content).strip()
  quote = quote.split(' - ')
  width = len(quote[0]) * 2

  print('Quote of the day: \n')
  print(width * '*')
  print(quote[0].center(width))
  print(quote[1].rjust(width))
  print(width * '*')


# main code

quotes_list = get_quotes()
show(quotes_list)