class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self._size = 0

    def size(self):
        return print(self._size)

    def peek(self):
        return print(self.queue[self.head])

    def push(self, item):
        if self._size == self.max_size:
            return print("error")

        self.queue[self.tail] = item
        self._size += 1

        self.tail = (self.tail + 1) % self.max_size

    def pop(self):
        item = self.queue[self.head]
        print(item)
        if item is None:
            return
        self.queue[self.head] = None
        self._size -= 1
        self.head = (self.head + 1) % self.max_size
