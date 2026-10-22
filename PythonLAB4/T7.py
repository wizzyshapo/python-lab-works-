class Stack:
    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)

    def pop(self):
        if self.st:
            return self.st.pop()
        return None

    def peek(self):
        if self.st:
            return self.st[-1]
        return None

    def isEmpty(self):
        return len(self.st) == 0

    def size(self):
        return len(self.st)


class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if self.q:
            return self.q.pop(0)
        return None

    def front(self):
        if self.q:
            return self.q[0]
        return None

    def isEmpty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)


q = Queue()
for i in [10, 20, 30, 40, 50]:
    q.enqueue(i)

s = Stack()
while not q.isEmpty():
    s.push(q.dequeue())
while not s.isEmpty():
    q.enqueue(s.pop())

print(q.q)