# Zadanie5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

sentence = input('Wprowadz potencjalne zdanie ktore moze byc palindromem: ')

sentence = sentence.replace(" ","")
sentence = sentence.lower()

if sentence == sentence[::-1]:
    print('To zdanie jest polindromem')
else:
    print('To zdanie nie jest polindromem')
    