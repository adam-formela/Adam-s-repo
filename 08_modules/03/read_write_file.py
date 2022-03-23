# Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty. Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.
import os


def read_file():
    try:
        with open('text.txt', 'r') as f:
            content = f.readlines()
    except:
        print('The file text.txt does not exist in this location.')
    try:
        if os.stat('text.txt').st_size != 0:
            print('Non-empty file with the same name exists in this location. To overwrite the file remove it first.')
        else:
            print('Empty file with the same name exists in this location. To overwrite the file remove it first.')
        return False
    except:
        return True

def write_file(text):
    if read_file():
        with open('text.txt', 'x') as g:
            g.write(text)
            print('The file has been created and saved')
