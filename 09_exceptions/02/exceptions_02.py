# Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość. Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd

elements = (1,'bigdata', 3.1, 'cellphone', 23)

new_index = input('Podaj index, ktory podmienic: ')
new_value = input('Podaj nowa wartosc: ')

try:
    elements[new_index] = new_value
except TypeError as err:
    print('Error: ', err)
