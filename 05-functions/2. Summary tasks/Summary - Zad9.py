# Zadanie 9. Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#     Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
#     -dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
#     -ponownie wyświetl zmieniony słownik
#     Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.

def is_antique():
    if car_dict.get('year') <= 1997 and car_dict.get('genuine'):
        print(f'Congratulations! Your car {brand} may be registered as an antique.')
    elif car_dict.get('year') <= 1997:
        print(f'Your car {brand} is not genuine.')
    elif car_dict.get('genuine'):
        print(f'Your car {brand} is genuine, but it is still too modern.')
    else:
        print(f'You car {brand} is not genuine and it is too modern.')


car_dict = {
    'brand' : 'Volkswagen',
    'model' : 'Golf',
    'year' : 1996,
    'genuine' : True
}

brand = car_dict.get('brand')

print(car_dict)

is_antique()
