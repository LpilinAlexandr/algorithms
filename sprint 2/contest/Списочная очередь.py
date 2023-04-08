

class LinkedList:

    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


class Queue:
    """Очередь через связный список"""

    def __init__(self):
        self.__size = 0
        # Используем 2 указателя: на голову и на хвост.
        # На хвост, чтобы добавлять в конец и на голову, чтобы доставать из начала.
        self.head = self.tail = None

    def get(self):
        if self.head:
            item = self.head.val
            self.head = self.head.nxt
            self.__size -= 1
        else:
            item = 'error'

        return print(item)

    def put(self, x):
        if not self.head:
            self.tail = self.head = LinkedList(x)
        else:
            self.tail.nxt = LinkedList(x)
            self.tail = self.tail.nxt

        self.__size += 1

    def size(self):
        return print(self.__size)


q = Queue()
while True:
    command = input().split()

    if len(command) == 1:
        getattr(q, command[0])()
    else:

        getattr(q, command[0])(int(command[1]))
