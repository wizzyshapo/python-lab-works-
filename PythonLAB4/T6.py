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
for i in [1, 2, 3]:
    q.enqueue(i)

print(q.front(), q.dequeue(), q.dequeue(), q.size(), q.isEmpty())