# Zadanie 6. Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.

import random

def winner():
    if user_wins > CPU_wins:
        print('You defeated the computer')
    elif user_wins < CPU_wins:
        print('You lost to the computer')
    else:
        print('Final result: draw')


def check_round():
    if user == 'r' and CPU == 'p':
        return 2
    elif user == 'r' and CPU == 's':
        return 1
    elif user == 'p' and CPU == 'r':
        return 1
    elif user == 'p' and CPU == 's':
        return 2
    elif user == 's' and CPU == 'r':
        return 2
    elif user == 's' and CPU == 'p':
        return 1


options = ['r','p','s']

rounds = int(input('Enter number of rounds: '))

CPU_wins = 0
user_wins = 0

for i in range(1,rounds+1):
    print("----------\nMake a selection: rock (r) / paper (p) / scissors (s). \nIf you want to quit type 'end'")
    user = input()
    if user == 'end':
        exit()
    if user not in ['r','p','s']:
        print('Wrong selection')
        continue
    CPU = random.choice(options)
    print(f'Your selection: {user}')
    print(f'CPU selection: {CPU}')
    check_round()
    if check_round() == 1:
        print('***You won this round***')
        user_wins += 1
    elif check_round() == 2:
        print('***You lost this round***')
        CPU_wins += 1
    else:
        print('draw')

print(f'----------\nFinal result:\nUser wins: {user_wins}\nCPU wins: {CPU_wins}')
winner()