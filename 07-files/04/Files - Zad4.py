# Wyświetl 3 losowe cytaty

import random


# funkcja do pobrania tekstu, zwraca liste
def get_quotes():
  with open('text.txt') as fopen:
    quotes = fopen.readlines()

  return quotes


# funkcja wyświetlająca
def show(content):
  for i in range(3):
    quote = random.choice(content).strip()
    quote = quote.split(' - ')
    width = len(quote[0]) * 2

    print(f'\nQuote of the day {i+1}: \n')
    print(width * '*')
    print(quote[0].center(width))
    print(quote[1].rjust(width))
    print(width * '*')


# main code

quotes_list = get_quotes()
show(quotes_list)