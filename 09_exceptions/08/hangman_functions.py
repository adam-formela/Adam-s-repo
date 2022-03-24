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