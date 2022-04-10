# Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta, dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).
# Utwórz kilka obiektów klasy Queue z różnymi parametrami.

class Queue():
    def __init__(self, fifo):
        self.fifo = fifo

    def show(self):
        print(self.fifo)

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self, element):
        self.fifo.append(element)

    def get(self):
        element = self.fifo.pop(0)
        return element


example_queue = Queue([5, 8, 3, 8, 20, 59, 3, 1, 2357])
example_queue.show()
print(example_queue.is_empty())
example_queue.put(6)
example_queue.put(1)
example_queue.put(61)
example_queue.show()
print('====get ====')
print(example_queue.get())
example_queue.show()