# Zadanie 8. Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 6 krajach.

UK = ['Lily','Amelia','Sophia','Olivia','Emily','Isla','Rosie','Aria','Freya','Ella']
US = ['Emily','Mia','Isabella','Ivy','Hannah','Layla','Grace','Sophie','Evelyn','Evie']
Scotland = ['Isabelle','Elsie','Luna','Poppy','Willow','Emily','Zara','Daisy','Sienna','Eva']
Canada = ['Emily','Mia','Isabella','Ivy','Hannah','Layla','Grace','Sophie','Evelyn','Evie']
Poland = ['Zuzanna','Zofia', 'Hanna', 'Julia', 'Maja', 'Laura', 'Oliwia', 'Alicja', 'Lena', 'Pola']
Wales = ['Emily','Mia','Isabella','Ivy','Hannah','Layla','Grace','Sophie','Evelyn','Evie']
Portugal = ['Emily','Mia','Isabella','Ivy','Hannah','Layla','Grace','Sophie','Evelyn','Evie']
Spain = ['Emily','Mia','Isabella','Ivy','Hannah','Layla','Grace','Sophie','Evelyn','Evie']
France = ['Emily','Mia','Isabella','Ivy','Hannah','Layla','Grace','Sophie','Evelyn','Evie']
Germany = ['Emily','Mia','Isabella','Ivy','Hannah','Layla','Grace','Sophie','Evelyn','Evie']

combined_list = UK + US + Scotland + Canada + Poland + Wales + Portugal + Spain + France + Germany

counting_dict = {}

for name in combined_list:
  if name in counting_dict.keys():
    counting_dict[name] += 1
  else:
    counting_dict[name] = 1

popular_names_dict = {}

for i,j in counting_dict.items():
    if j > 6:
        popular_names_dict[i] = j

popular_names = list(popular_names_dict.keys())

print(f'Imiona, ktore wystapily conajmniej w 6 krajach to: {popular_names}')