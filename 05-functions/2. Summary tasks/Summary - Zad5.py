# Zadanie 5. Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

def hot_cold(item_location):
    for i in range(3):
        guess = input(f'Gdzie szukasz zabawki? Proba {i+1}/3: ').lower()
        try:
            if list.index(guess) == list.index(item_location):
                print('***Znalazles/as zabawke!***')
                break
            elif abs(list.index(guess) - list.index(item_location)) == 1:
                print('Goraco')
            elif abs(list.index(guess) - list.index(item_location)) == 2:
                print('Cieplo')
            elif abs(list.index(guess) - list.index(item_location)) == 3:
                print('Zimno')
            elif abs(list.index(guess) - list.index(item_location)) >= 4:
                print('Lodowato')
        except:
            print('Nie ma takiego pomieszczenia')


list = ['sypialnia1', 'korytarz1', 'pokoj1', 'sypialnia2', 'lazienka', 'salon', 'pokoj2', 'korytarz2', 'przedpokoj', 'kuchnia', 'korytarz3', 'sypialnia3']

hot_cold('salon')
