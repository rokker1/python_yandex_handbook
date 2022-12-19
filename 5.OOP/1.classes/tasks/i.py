class Queue:

    def __init__(self):
        self.q = []

    def push(self, item):
        self.q.append(item)

    def pop(self):
        if len(self.q) != 0:
            return self.q.pop(0)

    def is_empty(self):
        return len(self.q) == 0


queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")
