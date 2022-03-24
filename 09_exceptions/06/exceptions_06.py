# Wywołaj błąd związany z otwarciem pliku.
#     Spróbuj odczytać plik, który nie istnieje.
#     Spróbuj odczytać wartość z pliku otwartym w trybie w
#     Spróbuj utworzyć plik, który już istnieje w trybie x
# Obsłuż w dowolny sposób każdy z powyższych błędów.
from io import UnsupportedOperation

filename = 'text.txt'
filename2 = 'text2.txt'
try:
    with open(filename2, 'r') as f:
        f.readlines()
except FileNotFoundError:
    print(f"Error: the file '{filename2}' does not exist")

try:
    with open(filename, 'w') as f:
        f.readlines()
except UnsupportedOperation:
    print('Cannot read in write mode')

try:
    with open(filename, 'x') as f:
        f.write('Line2')
except FileExistsError:
    print(f"The file '{filename}' already exists")