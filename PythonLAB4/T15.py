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


class Editor:
    def __init__(self):
        self.text = ""
        self.undo_s = Stack()
        self.redo_s = Stack()

    def write(self, t):
        self.undo_s.push(t)
        self.redo_s = Stack()
        self.text += t

    def undo(self):
        if not self.undo_s.isEmpty():
            t = self.undo_s.pop()
            self.redo_s.push(t)
            self.text = self.text[:-len(t)]

    def redo(self):
        if not self.redo_s.isEmpty():
            t = self.redo_s.pop()
            self.undo_s.push(t)
            self.text += t

    def showText(self):
        print(repr(self.text))

e = Editor()
e.write("Hello")
e.write(" World")
e.showText()
e.undo()
e.showText()
e.redo()
e.showText()