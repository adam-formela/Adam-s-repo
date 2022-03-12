'''
Address book:

The program contain a list of addresses in its database.
Data structure used: function, list.
For this project one module was imported: sys.

Program description:
 - The program first asks if you want to open address book options or exit.
 - The program allows you to select from 4 different options:
    1. Allows you to print all records in the address book.
    2. Allows you to add new persons.
    3. Allows you to remove records from the database.
    4. Ends the program.

Have fun!
'''
import sys


def is_phone(text):
    if len(text) != 15:
        return False
    if text[0:3] != '+48':
        return False
    if text[3] != ' ':
        return False
    if text[7] != '-' and text[11] != '-':
        return False
    for i in range(4,6):
        if not text[i].isdecimal():
            return False
    for i in range(8,10):
        if not text[i].isdecimal():
            return False
    for i in range(12,14):
        if not text[i].isdecimal():
            return False
    return True


address_book = [
    ['Pawel', 'Kowalski', 'Warsaw', '+48 111-111-111'],
    ['Anna', 'Kopernik', 'Warsaw', '+48 222-222-222'],
    ['Krzysztof', 'Sarna', 'Gdansk', '+48 333-333-333'],
    ['Katarzyna', 'Zlodziej', 'Krakow', '+48 444-444-444']
]

text = '''Hello! You are in the address book:
    - type 1 to display all contacts
    - type 2 to create another entry
    - type 3 to delete existing contact
    - type 4 to exit
    Chosen option: '''

run_list = ['yes','no']
run = input('Do you want to open the address book? [yes/no]: ')
while run != 'yes':
    if run not in run_list:
        print('Use the proper keyword')
        run = input('Do you want to open the address book? [yes/no]: ')
        continue
    if run == 'no':
        sys.exit()

answer_list = ['1','2','3','4']
while True:
    answer = input(text)
    if answer not in answer_list:
        print('You selected the nonexistent option. Try again.')
        print('--------')
        continue
    if answer == '1':
        print()
        for row in address_book:
            print()
            for item in row:
                print(item)
            print('---------')

    elif answer == '2':
        print()
        new_record = []
        name = input('Provide name: ').title()
        while not name.isalpha():
            name = input('Provide name in correct format: ').title()
        else:
            new_record.append(name)
        surname = input('Provide surname: ').title()
        while not surname.isalpha():
            surname = input('Provide surname in correct format: ').title()
        else:
            new_record.append(surname)
        city = input('Provide city: ').title()
        while not city.isalpha():
            city = input('Provide city in correct format: ').title()
        else:
            new_record.append(city)
        phone = input("Provide telephone number in format '+48 XXX-XXX-XXX': ")
        while not is_phone(phone):
            phone = input("Provide telephone number in correct format '+48 XXX-XXX-XXX': ")
        else:
            new_record.append(phone)
        address_book.append(new_record)
        print('New record has been successfully added')
        print('--------')

    elif answer == '3':
        print()
        for index, row in enumerate(address_book):
            print(index, end=" --> ")
            for elem in row:
                print(elem, end=" ")
            print()
            print('--------------------------------------')
        len_address_book = len(address_book)-1
        while True:
            del_index = int(input('Provide index to remove: '))
            if del_index > len_address_book:
                print('Provide proper index')
                continue
            else:
                break
        address_book.remove(address_book[del_index])
        print('Record has been successfully removed from address book')
        print('--------')

    elif answer == '4':
        sys.exit()
