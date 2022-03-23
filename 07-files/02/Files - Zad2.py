# Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.

import os


size = os.path.getsize('text.txt')
print(f'The size of a given file: {size} bajtów')