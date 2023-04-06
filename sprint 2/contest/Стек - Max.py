class StackMax:

    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.size():
            return self.items.pop()
        print('error')

    def get_max(self):
        print(max(self.items) if self.size() else 'None')

    def size(self):
        return len(self.items)