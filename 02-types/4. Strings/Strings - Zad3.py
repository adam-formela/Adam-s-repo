# Zadanie3. Do zmiennej quote przypisz zdanie: „Honesty is the first chapter in the book of wisdom.”, a następnie:

quote = 'Honesty is the first chapter in the book of wisdom.'

# a) Policz wszystkie znaki w napisie

print(len(quote))

# b) Nie modyfikując zmiennej wyświetl słowo wisdom

print(quote[-7:-1])

# c) Wyświetl tylko pierwszą połowę tekstu

len_quote = len(quote) // 2

print(quote[:len_quote])

# d) Wyświetl tylko kropkę

print(quote[-1:])

# e) Wyświetl od połowy tylko co trzecią literę cytatu

print(quote[len_quote::3])

# f) Wyświetl ‘Hnsyi h is hpe ntebo fwso.’

print(quote[::2])

# g) Wyświetl cały cytat odwrotnie

print(quote[::-1])

# h) Zamień wisdom na słowo friendship

print(quote.replace('wisdom','friendship'))