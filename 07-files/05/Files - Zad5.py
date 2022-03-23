# Zadanie 5. Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.

def get_text():
    with open('text.txt', encoding='UTF-8') as fopen:
        content = fopen.read()

    return content


def clean_text(text):
    extras = '.!,()'

    for symbol in extras:
        text = text.replace(symbol, '')

    return text


def find_longest_word(text):
    text = text.split()
    longest_word = ''

    for current_word in text:
        if len(current_word) > len(longest_word):
            longest_word = current_word

    return longest_word


# -- main code

txt = get_text()
txt = clean_text(txt)
search_word = find_longest_word(txt)

print(search_word, ', o długości - ', len(search_word))