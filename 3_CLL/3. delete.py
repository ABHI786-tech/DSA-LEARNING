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
# Delete from Beginning
# ============================================================

# Find last node
last = head

while last.next != head:
    last = last.next

# Delete first node
head = head.next
last.next = head


# Traversal
current = head

print("delete_from_beginning")

while True:
    print(current.item, end=" -> ")
    current = current.next

    if current == head:
        break

print("(back to head)")
print("_________________________________________________")


# ============================================================
# Delete from End
# ============================================================

# Find second-last node
current = head

while current.next.next != head:
    current = current.next

# Delete last node
current.next = head


# Traversal
current = head

print("delete_from_end")

while True:
    print(current.item, end=" -> ")
    current = current.next

    if current == head:
        break

print("(back to head)")
print("_________________________________________________")


# ============================================================
# Delete from Mid / Position
# ============================================================

# Position
position = 2

# Find node before the position
current = head

for i in range(1, position - 1):
    current = current.next

# Delete node
current.next = current.next.next


# Traversal
current = head

print("delete_from_mid")

while True:
    print(current.item, end=" -> ")
    current = current.next

    if current == head:
        break

print("(back to head)")
print("_________________________________________________")