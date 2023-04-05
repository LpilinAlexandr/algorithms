
class StackMax:

    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop() if self.size() else 'error'

    def get_max(self):
        return max(self.items) if self.size() else 'None'

    def size(self):
        return len(self.items)
