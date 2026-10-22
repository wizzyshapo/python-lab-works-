class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0


def is_balanced(s):
    st = Stack()
    for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
            st.push(ch)
        elif ch == ")" or ch == "]" or ch == "}":
            if st.is_empty():
                return False
            top = st.pop()
            if ch == ")" and top != "(":
                return False
            if ch == "]" and top != "[":
                return False
            if ch == "}" and top != "{":
                return False
    return st.is_empty()


print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))