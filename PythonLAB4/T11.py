class Stack:
    def __init__(self):
        self.a = []
    def push(self, x):
        self.a.append(x)
    def pop(self):
        return self.a.pop() if self.a else None
    def peek(self):
        return self.a[-1] if self.a else None
    def isEmpty(self):
        return not self.a
    def size(self):
        return len(self.a)

class Queue:
    def __init__(self):
        self.a = []
    def enqueue(self, x):
        self.a.append(x)
    def dequeue(self):
        return self.a.pop(0) if self.a else None
    def front(self):
        return self.a[0] if self.a else None
    def isEmpty(self):
        return not self.a
    def size(self):
        return len(self.a)

class Q2S:
    def __init__(self):
        self.in_s = Stack()
        self.out_s = Stack()

    def move(self):
        if self.out_s.isEmpty():
            while not self.in_s.isEmpty(): self.out_s.push(self.in_s.pop())

    def enqueue(self, x):
        self.in_s.push(x)

    def dequeue(self):
        self.move()
        return self.out_s.pop()

    def peek(self):
        self.move()
        return self.out_s.peek()

    def isEmpty(self):
        return self.in_s.isEmpty() and self.out_s.isEmpty()

q = Q2S()
for i in [1, 2, 3]: q.enqueue(i)
print(q.dequeue(), q.peek(), q.dequeue(), q.dequeue(), q.isEmpty())