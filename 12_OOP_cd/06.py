# Utworz klasę Kraj, która zawiera informację o powierzchni. ludności, jaki język jest urzędowy, jakie miasto jest stolicą.
# Utwórz klika obiektów klasy Kraj, stwórz listę obiektów klasy kraj, wyświetl elementy na liście krajów.

class Country():
    objects_list = []

    def __init__(self, name, area, population, language, capital):
        self.name = name
        self.area = area
        self.population = population
        self.language = language
        self.capital = capital
        Country.objects_list.append(self.name)


pl = Country('Poland', '50000', '40000000', 'polish', 'Warsaw')
ger = Country('Germany', '70000', '50000000', 'german', 'Berlin')
esp = Country('Spain', '60000', '45000000', 'spanish', 'Madrid')

print(Country.objects_list)