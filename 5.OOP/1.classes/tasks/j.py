class Stack:

    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.s.__len__() != 0:
            return self.s.pop()
    
    def is_empty(self):
        return self.s.__len__() == 0