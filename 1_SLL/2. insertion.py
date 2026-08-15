class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


# --------------------------------------------
# insert at beginning
# --------------------------------------------
node1.next = node2
node2.next = node3
node3.next = node4


# Insert 5 at beginning
new_node = Node(5)

new_node.next = node1
node1 = new_node


# Traversal
current = node1

while current is not None:
    print(current.item)
    current = current.next



# --------------------------------------------
# insert at end
# --------------------------------------------

# Insert 60 at end
new_node = Node(60)

current = node1

while current.next is not None:
    current = current.next

current.next = new_node


# Traversal
current = node1

while current is not None:
    print(current.item)
    current = current.next


# --------------------------------------------
# insert at specific position 
# --------------------------------------------



node1.next = node2
node2.next = node3
node3.next = node4


# Insert 90 at position 3
new_node = Node(90)

current = node1

# Move to position 2
for i in range(1, 2):
    current = current.next

new_node.next = current.next
current.next = new_node


# Traversal
current = node1

while current is not None:
    print(current.item)
    current = current.next
