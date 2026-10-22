class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def search(root, value):
    current = root
    while current is not None:
        if current.value == value:
            return True
        elif value < current.value:
            current = current.left
        else:
            current = current.right
    return False


root = None
numbers = [50, 30, 70, 20, 40, 60, 80]
for n in numbers:
    root = insert(root, n)

key = 40
if search(root, key):
    print("Found")
else:
    print("Not found")