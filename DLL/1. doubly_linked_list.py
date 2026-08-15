
# --------------------------------------------
#  Traversal
# --------------------------------------------
# Question: Create a doubly linked list and print it from left to right and right to left.



class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None



# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


# Connect nodes
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


# Forward Traversal
print("Forward Traversal:")

current = node1

while current is not None:
    print(current.item, end=" <-> ")
    current = current.next

print("None")


# Backward Traversal
print("\nBackward Traversal:")

current = node4

while current is not None:
    print(current.item, end=" <-> ")
    current = current.prev

print("None")