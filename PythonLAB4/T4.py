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


def remove_dup(t):
    s = Stack()
    for c in t:
        if s.peek() == c:
            s.pop()
        else:
            s.push(c)
    res = ""
    for x in s.st:
        res += x
    return res


print(remove_dup("abbaca"))