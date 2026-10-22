class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

t = Tree(10)
t.left = Tree(5)
t.right = Tree(15)
t.left.left = Tree(3)

print(height(t))
