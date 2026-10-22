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

def gen(n):
    q = Queue()
    q.enqueue("1")
    res = []
    for i in range(n):
        x = q.dequeue()
        res.append(x)
        q.enqueue(x + "0")
        q.enqueue(x + "1")
    return res

print(gen(5))