class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4


# --------------------------------------------
# delete first node
# --------------------------------------------
node1 = node1.next


# Traversal
current = node1

while current is not None:
    print(current.item)
    current = current.next





# --------------------------------------------
# Delete last node
# --------------------------------------------
current = node1

while current.next.next is not None:
    current = current.next

current.next = None


# Traversal
current = node1

while current is not None:
    print(current.item)
    current = current.next


# --------------------------------------------
# Delete node containing 30
# --------------------------------------------
current = node1

while current.next is not None:

    if current.next.item == 30:
        current.next = current.next.next
        break

    current = current.next


# Traversal
current = node1

while current is not None:
    print(current.item)
    current = current.next
