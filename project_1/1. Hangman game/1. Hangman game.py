'''
### Hangman game:

The program is a Hangman game.
Data structure used: function, list.
For this project one module was imported: sys, json.

Program description:
 - The program gets the keyword from JSON file.
 - Before the game, the program displays the length of the keyword and the encrypted keyword.
 - In each round the program asks for a letter, or optionally you can try to guess the keyword.
 - Each time the letter appears in the keyword the letter(s) are reveled with their index.
 - If the entered letter is not in list the program will display an appropriate message.
 - You have 9 rounds to guess the keyword.
 - If you do not guess the keyword within 9 rounds you will be hanged ;)

Good luck and Have fun!
'''
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


keywords = json.load(open('../../08_modules/04/Hangman.JSON'))
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