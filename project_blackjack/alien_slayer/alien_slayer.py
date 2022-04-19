import random

class Player:
    """ Gracz w grze strzelance. """

    def blast(self, enemy):
        print('Gracz razi wroga.\n')
        if random.randint(1,10) >= 6:
            print('Gracz trafil wroga')
            enemy.die()
            return True
        else:
            print('Wrog nie zostal trafiony')
            return False

    def player_die(self):
        print('Obcy zjada gracza')



class Alien:
    """ Obcy w grze strzelance. """

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')

    def attack(self, enemy):
        print('Obcy atakuje')
        enemy.player_die()


print('************ Śmierć Obcego ************\n')
hero = Player()
invader = Alien()
if not hero.blast(invader):
    invader.attack(hero)
    print('Obcy mlaska i idzie spac')
input('\n\nAby zakończyć program, naciśnij klawisz Enter.')