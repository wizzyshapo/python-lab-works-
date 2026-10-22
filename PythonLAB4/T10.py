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

def prec(o):
    if o == "+" or o == "-":
        return 1
    return 2

def to_postfix(e):
    for c in "+-*/()":
        e = e.replace(c, " " + c + " ")
    s = Stack()
    out = []
    for t in e.split():
        if t == "(":
            s.push(t)
        elif t == ")":
            while s.peek() != "(":
                out.append(s.pop())
            s.pop()
        elif t == "+" or t == "-" or t == "*" or t == "/":
            while not s.isEmpty() and s.peek() != "(" and prec(s.peek()) >= prec(t):
                out.append(s.pop())
            s.push(t)
        else:
            out.append(t)
    while not s.isEmpty():
        out.append(s.pop())
    return " ".join(out)

print(to_postfix("A + B * C"), "|", to_postfix("(A + B) * C"))

