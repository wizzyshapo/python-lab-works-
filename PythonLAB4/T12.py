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


class S2Q:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    def push(self, x):
        self.q2.enqueue(x)
        while not self.q1.isEmpty(): self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self): return self.q1.dequeue()
    def peek(self): return self.q1.front()
    def isEmpty(self): return self.q1.isEmpty()


s = S2Q()
for i in [1, 2, 3]: s.push(i)
print(s.peek(), s.pop(), s.pop(), s.pop(), s.isEmpty())
