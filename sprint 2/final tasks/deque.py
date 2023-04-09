
class SpecialEmpty:
    """
    Специальный объект, который кладётся на пустое место в массиве Дека,
    чтобы туда можно было класть любой Python объект.
    """


class Deque:
    __EMPTY = SpecialEmpty()

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [self.__EMPTY] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, item):
        assert not isinstance(item, SpecialEmpty), 'SpecialEmpty нельзя положить в Deque'
        if self.size == self.max_size:
            return print('error')

        if not isinstance(self.queue[self.tail], SpecialEmpty):
            self.tail = (self.tail + 1) % len(self.queue)

        self.queue[self.tail] = item
        self.size += 1

    def pop_back(self):
        item = self.queue[self.tail]
        if isinstance(item, SpecialEmpty):
            return print('error')

        self.queue[self.tail] = self.__EMPTY
        self.size -= 1
        if self.size:
            self.tail = (self.tail - 1) % len(self.queue)

        print(item)

    def push_front(self, item):
        assert not isinstance(item, SpecialEmpty), 'SpecialEmpty нельзя положить в Deque'
        if self.size == self.max_size:
            return print('error')

        if not isinstance(self.queue[self.head], SpecialEmpty):
            self.head = (self.head - 1) % len(self.queue)

        self.queue[self.head] = item
        self.size += 1

    def pop_front(self):
        item = self.queue[self.head]
        if isinstance(item, SpecialEmpty):
            return print('error')

        self.queue[self.head] = self.__EMPTY
        self.size -= 1
        if self.size:
            self.head = (self.head + 1) % len(self.queue)

        print(item)


deque = Deque(10)

deque.push_back(1)
deque.push_front(1)
deque.pop_back()
deque.pop_back()
