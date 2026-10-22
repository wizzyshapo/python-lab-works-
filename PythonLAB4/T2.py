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


def rev(t):
    s = Stack()
    for c in t:
        s.push(c)
    result = ""
    while not s.isEmpty():
        result = result + s.pop()
    return result


print(rev("HELLO"))