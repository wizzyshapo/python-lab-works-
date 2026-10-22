class Queue():
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)
    def dequeue(self):
        return self.data.pop(0)
    def is_empty(self):
        return len(self.data) == 0

def b_muns(n):
    q = Queue()
    q.enqueue("1")
    r = []
    for i in range(n):
        cur = q.dequeue()
        r.append(cur)
        q.enqueue(cur + "0")
        q.enqueue(cur + "1")
    return r

n = 5
print(b_muns(n))