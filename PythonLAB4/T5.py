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


def binary(n):
    s = Stack()
    while n > 0:
        ost = n % 2
        s.push(ost)
        n = n // 2
    res = ""
    while not s.isEmpty():
        res += str(s.pop())
    return res


print(binary(25))