class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def reset(self):
        self.items = []