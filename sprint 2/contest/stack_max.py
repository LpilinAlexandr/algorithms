
class DoubleLinkedList:

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'DLL: {self.value}'


class StackMax:

    """
    Стек, который может возвращать максимальное и минимальное значения за O(1)
    А также pop, push за O(1)
    """

    def __init__(self):
        self.items = []
        self.head = self.tail = None

    def push(self, element):
        self.items.append(element)

        if not self.head:
            self.head = self.tail = DoubleLinkedList(value=element)
            return

        if element >= self.head.value:
            new = DoubleLinkedList(value=element, prev=self.head)
            self.head.next = new
            self.head = new
        else:
            new = DoubleLinkedList(value=element, next=self.tail)
            self.tail.prev = new
            self.tail = new

    def pop(self):
        if not self.items:
            return print('error')

        element = self.items.pop()

        if not self.items:
            self.head = self.tail = None

        elif element == self.head.value:
            self.head = self.head.prev
            if self.head:
                self.head.next = None
        else:
            self.tail = self.tail.next
            if self.tail:
                self.tail.prev = None

        return element

    def get_max(self):
        if self.head:
            return print(self.head.value)

        return print('None')

    def size(self):
        return len(self.items)
