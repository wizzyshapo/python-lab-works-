class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items) - 1]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, x):

        self.items.append(x)
    def dequeue(self):

        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)

    def front(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[0]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

s = Stack()
for i in range(1, 11):
    s.push(i)
print(s.size(), s.peek(), s.pop(), s.size(), s.isEmpty())