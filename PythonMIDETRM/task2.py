class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    s = ""
    cur = head
    while cur is not None:
        s += str(cur.data)
        if cur.next is not None:
            s += "->"
        cur = cur.next
    print(s)

def delete_duplicates(head):
    cur = head
    while cur is not None:
        prev = cur
        nxt = cur.next
        while nxt is not None:
            if nxt.data == cur.data:
                prev.next == cur.next
            else:
                pver = nxt
            nxt = nxt.next
        cur = cur.next
    return head

a = Node(4)
a.next = Node(2)
a.next.next = Node(4)
a.next.next.next = Node(7)
a.next.next.next.next = Node(2)
a.next.next.next.next.next = Node(9)

print_list(a)
a = delete_duplicates(a)
print_list(a)