# Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc. Poproś użytkownika o podanie kategorii przed rozpoczęciemy gry.
# Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy. Rozgrywka powinna być maksymalnie intuicyjna.

import sys, json


def find_in_list(keyword, guess):
    output = []
    if guess not in keyword:
        return output
    for index, j in enumerate(keyword):
        if guess == j:
            output.append(index)
    return output


def is_letter(guess):
    if guess == '':
        return False
    elif len(guess) != 1:
        return False
    elif not guess.isalpha():
        return False
    else:
        return True


def check_guess(text):
    password = input('Enter your guess: ').upper()
    if password.upper() == keyword_str:
        print('***Congratulations! You guessed the keyword!***')
        return 1
    else:
        print('***You did not guess***')
        return 2


category = input('Provide category[fruits, animals]: ').lower()
if category != 'fruits' and category != 'animals':
    print('No proper category selected')
    sys.exit()
if category == 'fruits':
    keywords = json.load(open('Fruits.JSON'))
else:
    keywords = json.load(open('Animals.JSON'))
for nr in keywords:
    keyword = nr
    keyword_str = ''
    for word in keyword:
        keyword_str = keyword_str + word
    masked_keyword = []
    for word2 in keyword:
        masked_keyword.append('_')
    len_keyword = len(keyword)
    print(f'Keyword has {len_keyword} letters.')

    for i in range(1,10):
        if masked_keyword == keyword:
            print('***Congratulations! You guessed the keyword!***')
            print(f'Keyword: {keyword_str}')
            break
        print(f'Current state: {masked_keyword}')
        print('--------------------------------------------------')
        print(f'Round {i}')
        guess = str(input("Enter a letter or word 'GUESS' to guess the word: ").upper())
        if guess == 'GUESS':
            if check_guess(guess) == 1:
                masked_keyword = keyword
                break

        while True:
            if not is_letter(guess):
                guess = input("Try again. Enter a letter: ").upper()
                continue
            else:
                output = find_in_list(keyword,guess)
                for k, j in enumerate(output):
                    masked_keyword[j] = guess
                try:
                    print(f"Letter {guess} occurred {k+1} times.\n--------")
                except:
                    print(f'Letter {guess} is not in list.\n--------')
                k = ''
                j = ''
                break

    if '_' in masked_keyword:
        print('Game over! You are hanged!')
    answer = input('Type [yes] if you want to play another round: ')
    print('--------------------------------------------------')
    if answer != 'yes':
        sys.exit()

print('Sorry! No more keywords in the database!')
sys.exit()