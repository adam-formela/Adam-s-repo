'''
Tic Tac Toe game:

The program is a Tic Tac Toe game for two players.
Data structure used: function, dictionary, list.
For this project two modules were imported: random and time.

Program description:
 - The program first asks for your name and your fiends' name. Optionally you can play with PC.
 - PC randomly chooses the keys from the created dictionary.
 - After the game the program asks if you want to play again. The number of rounds are infinite.

Have fun!
'''

import random, time

def board(area):
    print(' '.center(3) + '1'.center(3) + ' ' + '2'.center(3) + ' ' + '3'.center(3))
    print('A'.center(3) + area['A1'].center(3) + '|' + area['A2'].center(3) + '|' + area['A3'].center(3))
    print('B'.center(3) + area['B1'].center(3) + '|' + area['B2'].center(3) + '|' + area['B3'].center(3))
    print('C'.center(3) + area['C1'].center(3) + '|' + area['C2'].center(3) + '|' + area['C3'].center(3))


answer = input("Would you like to play the 'Tic Tac Toe' game? [yes/no] ")
while answer == 'yes':
    turn = 'X'
    name1 = input('Provide player1 name: ')
    name2 = input("Provide player2 name or type 'PC' to play with the computer: ")

    board_dict = {
        'A1': '.', 'A2': '.', 'A3': '.',
        'B1': '.', 'B2': '.', 'B3': '.',
        'C1': '.', 'C2': '.', 'C3': '.'
    }

    for i in range(8):
        while i <= 8:
            board(board_dict)

            if turn == 'X':
                print('Player ' + name1 + '. Mark position (X): ')
                move = input()
            else:
                print('Player ' + name2 + '. Mark position (O): ')
                if name2 == 'PC':
                    CPU = list(board_dict.keys())
                    time.sleep(2)
                    move = random.choice(CPU)
                else:
                    move = input()

            while move not in board_dict.keys():
                print('Provide correct field name')
                move = input()
                continue

            while board_dict[move] != '.':
                if turn == 'O' and name2 == 'PC':
                    time.sleep(2)
                    move = random.choice(CPU)
                    continue
                print('This field has been used. Try again: ')
                move = input()
                continue
            else:
                board_dict[move] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

                board_list = list(board_dict.values())
                if board_list[0:3] == ['X', 'X', 'X'] or board_list[3:6] == ['X', 'X', 'X'] or board_list[6:9] == ['X', 'X', 'X']:
                    print('The winner is: ' + name1)
                    break
                elif board_list[0:3] == ['O', 'O', 'O'] or board_list[3:6] == ['O', 'O', 'O'] or board_list[6:9] == ['O', 'O', 'O']:
                    print('The winner is: ' + name2)
                    break
                elif board_list[0] + board_list[3] + board_list[6] == 'XXX' or board_list[1] + board_list[4] + board_list[7] == 'XXX' or board_list[2] + board_list[5] + board_list[8] == 'XXX':
                    print('The winner is: ' + name1)
                    break
                elif board_list[0] + board_list[3] + board_list[6] == 'OOO' or board_list[1] + board_list[4] + board_list[7] == 'OOO' or board_list[2] + board_list[5] + board_list[8] == 'OOO':
                    print('The winner is: ' + name2)
                    break
                elif board_list[0] + board_list[4] + board_list[8] == 'XXX' or board_list[2] + board_list[4] + board_list[6] == 'XXX':
                    print('The winner is: ' + name1)
                    break
                elif board_list[0] + board_list[4] + board_list[8] == 'OOO' or board_list[2] + board_list[4] + board_list[6] == 'OOO':
                    print('The winner is: ' + name1)
                    break
                i += 1
        if i >= 8:
            print('Draw!')
            break
        else:
            break

    print()
    print('Final field: ')
    board(board_dict)

    answer = input('Would you like to play another round? [yes/no] ')
    continue


