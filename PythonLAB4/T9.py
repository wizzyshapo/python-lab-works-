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


def postfix(e):
    s = Stack()
    for t in e.split():
        if t == "+" or t == "-" or t == "*" or t == "/":
            b = s.pop()
            a = s.pop()
            if t == "+":
                s.push(a + b)
            elif t == "-":
                s.push(a - b)
            elif t == "*":
                s.push(a * b)
            else:
                s.push(a / b)
        else:
            s.push(int(t))
    return s.pop()


print(postfix("5 3 + 2 *"))