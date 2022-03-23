# Korzystając z Google dowiedz się więcej o kodowaniu ASCII. Utwórz plik, który tworzy prostą zaszyfrowaną wiadomość. Każdą literę tekstu zapisuje za pomocą dziesiętnych wartości kodów ASCII.
# Przykładowo literze A odpowiada numer 65. Zapoznaj się z metodami ord() oraz char(). Pamiętaj o dodaniu znaku podziału. Utwórz drugi skrypt, który rozszyfruje wiadomość.

encrypted_text = ''
unencrypted_text = ''

with open('text.txt', 'r', encoding='UTF-8') as f:
    content = f.readlines()

for line in content:
    for character in line:
        encrypted_letter = str(ord(character))
        encrypted_text = encrypted_text + encrypted_letter + ','

print(f'Encrypted text: {encrypted_text}')

encrypted_text_list = encrypted_text.split(',')

for i in encrypted_text_list:
    if i !='':
        unencrypted_letter = chr(int(i))
        unencrypted_text = unencrypted_text + unencrypted_letter

print(f'Unencrypted text:\n{unencrypted_text}')
