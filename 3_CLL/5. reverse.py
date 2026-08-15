class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
node3.next = node1

head = node1

# ============================================================
# Reverse Circular Linked List
# ============================================================

previous = None
current = head

while True:

    next_node = current.next
    current.next = previous

    previous = current
    current = next_node

    if current == head:
        break


# Connect old head to previous node
head.next = previous

# Change head
head = previous


# Traversal
current = head

print("reverse")

while True:
    print(current.item, end=" -> ")
    current = current.next

    if current == head:
        break

print("(back to head)")
print("_________________________________________________")