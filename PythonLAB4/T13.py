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


class Browser:
    def __init__(self):
        self.back_s = Stack()
        self.fwd_s = Stack()
        self.cur = None
    def visit(self, p):
        if self.cur:
            self.back_s.push(self.cur)
        self.cur = p
        self.fwd_s = Stack()
    def back(self):
        if not self.back_s.isEmpty():
            self.fwd_s.push(self.cur)
            self.cur = self.back_s.pop()
        return self.cur
    def forward(self):
        if not self.fwd_s.isEmpty():
            self.back_s.push(self.cur)
            self.cur = self.fwd_s.pop()
        return self.cur
    def currentPage(self):
        return self.cur

b = Browser()
for p in ["Google", "YouTube", "GitHub"]:
    b.visit(p)

print(b.back(), b.back(), b.forward())