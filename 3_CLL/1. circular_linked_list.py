class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Last node points back to first node
node4.next = node1


head = node1


# Traversal
current = head

while True:
    print(current.item, end=" -> ")
    current = current.next

    if current == head:
        break

print("(back to head)")




# ============================================================
# Update an Element
# ============================================================

old_value = 30
new_value = 35

current = head

while True:

    if current.item == old_value:
        current.item = new_value
        break

    current = current.next

    if current == head:
        break


# Traversal
current = head

print("update_element")

while True:
    print(current.item, end=" -> ")
    current = current.next

    if current == head:
        break

print("(back to head)")
print("_________________________________________________")

