# Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej typ. Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.

def is_american_express(card_number):
    card_length = len(card_number)
    return card_length == 15 and (card_number[0:2] == '34' or card_number[0:2] == '37')


def is_visa(card_number):
    card_length = len(card_number)
    return card_length in [13, 16] and card_number[0] == '4'


def is_mastercard(card_number):
    card_length = len(card_number)
    starts_with_51_55 = 51 <= int(card_number[0:2]) <= 55
    starts_with_2221_2720 = 2221 <= int(card_number[0:4]) <= 2720

    return card_length == 16 and (starts_with_51_55 or starts_with_2221_2720)


with open('card_list.txt', 'r') as f:
    for line in f:
        line = line.replace('\n','')
        print(line)
        if is_visa(line):
            print("To jest visa\n")
            with open('visa.txt', 'a+') as v:
                v.write(line + '\n')
        elif is_mastercard(line):
            print("To jest master card\n")
            with open('mastercard.txt', 'a+') as m:
                m.write(line + '\n')
        elif is_american_express(line):
            print("To jest american express\n")
            with open('american_express.txt', 'a+') as a:
                a.write(line + '\n')
        else:
            print("To może być inna karta\n")