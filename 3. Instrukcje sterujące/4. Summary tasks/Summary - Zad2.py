# Zadanie 2. Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

text = 'abrakadabra'
len_text = int(len(text))

for letter in range(1,len_text,2):
    print(text[letter])

text = 'abrakadabra'
len_text = int(len(text))

print(text[1::2])