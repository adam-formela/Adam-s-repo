# Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

elements = [13, 'text', 2.45, 0, ('1', '2'), [], {1,2}, {'key':123}, range(10)]

try:
    new_index = int(input('Podaj index, ktory podmienic: '))
    matched_element = elements[new_index]
    result = 1 / matched_element
    print(result)
except (TypeError, ZeroDivisionError, IndexError, NameError) as err:
    print('Error: ', err)
except ValueError:
    print('List index out of range')