
class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


head = node1


# Reverse
current = head

while current is not None:

    # Swap prev and next
    current.prev, current.next = current.next, current.prev

    # Move to original next
    current = current.prev


# New head
head = node4


# Traversal
current = head

while current is not None:
    print(current.item, end=" <-> ")
    current = current.next

print("None")
