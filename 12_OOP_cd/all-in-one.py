from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def poop(self):
        pass

class Horse(Animal):
    def __init__(self):
        self.__emoji = '💩'

    def poop(self):
        return self.__emoji

class Unicorn(Animal):
    def __init__(self):
        self.__emoji = '🌈'

    def floof(self):
        return "I'm flying"

    def poop(self):
        return self.__emoji


#----
def vet(animal: Animal): #type hints
    print('robie badanie -->', animal.poop())

def main():
    print('Chodźmy do weterynarza')
    konik = Horse()
    jednorozec = Unicorn()

    vet(konik)
    vet(jednorozec)

if __name__ == '__main__':
    main()


