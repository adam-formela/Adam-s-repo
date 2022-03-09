# Zadanie 5. W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

text = '''Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce'''

text = text.lower()
text = text.replace(',','')

text = text.replace('\n',' ')
text = text.split(' ')
print(text)
print(type(text))
print('-------------------')

counting_dict = {}

for word in text:
  if word in counting_dict:
    counting_dict[word] += 1
  else: #jeszcze słowa nie ma w słowniku
    counting_dict[word] = 1 # dodaj klucz do słownika po raz pierwszy - wartość 1

for k, v in counting_dict.items():
  print(k, '---->', v)