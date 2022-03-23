# Wyświetl tylko 5 pierwszych linii

with open('text.txt', 'r') as f:
    for i in range(5):
        for line in f:
            print(line)
            break
        continue
