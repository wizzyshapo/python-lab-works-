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

q = Queue()
for t in [(1, "Aidar", 5), (2, "Dana", 2), (3, "Timur", 8)]: q.enqueue(t)
total = 0
while not q.isEmpty():
    i, name, pages = q.dequeue()
    print("task", i, name, pages)
    total += pages
print("total pages:", total)
