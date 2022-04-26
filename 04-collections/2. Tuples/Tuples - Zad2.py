# Zad2. Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

numbers = (1,2,2,2,3,4,4,4)

counters = []
repeating_items = []

for i in numbers:
    if i not in counters:
        counters.append(i)
    else:
        if i not in repeating_items:
            repeating_items.append(i)

print(f'Powtarzajace sie elementy krotki to: {repeating_items}')
