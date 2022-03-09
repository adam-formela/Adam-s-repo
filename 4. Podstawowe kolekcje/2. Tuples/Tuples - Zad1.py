# Zad1. Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.

dog = ('pies','mieszaniec','Dyzio')
zwierze, rasa, imie = dog

print(f'Moj {zwierze}, rasy {rasa} wabi sie {imie}')