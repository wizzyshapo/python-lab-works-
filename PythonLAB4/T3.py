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


def balanced(t):
    s = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in t:
        if c == '(' or c == '[' or c == '{':
            s.push(c)
        elif c in pairs:
            top = s.pop()
            if top != pairs[c]:
                return False
    return s.isEmpty()


for expr in ["{[()]}", "{[(])}"]:
    if balanced(expr):
        print("Balanced")
    else:
        print("Not balanced")