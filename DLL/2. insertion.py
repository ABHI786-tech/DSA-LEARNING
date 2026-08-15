
class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None

# Existing list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


# --------------------------------------------
# insert_at_beginning
# --------------------------------------------
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


head = node1


# New node
new_node = Node(5)

new_node.next = head
head.prev = new_node

head = new_node


# Traversal
current = head

while current is not None:
    print(current.item, end=" <-> ")
    current = current.next

print("None")


# --------------------------------------------
# insert_at_end
# --------------------------------------------
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


head = node1


# Find last node
current = head

while current.next is not None:
    current = current.next


# Insert new node
new_node = Node(50)

new_node.prev = current
current.next = new_node


# Traversal
current = head

while current is not None:
    print(current.item, end=" <-> ")
    current = current.next

print("None")




# --------------------------------------------
# insert_at_middle
# --------------------------------------------
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


head = node1


# Insert 30 at position 3
position = 3
new_node = Node(80)

current = head

# Go to position 2
for _ in range(position - 2):
    current = current.next


# Connect new node
new_node.next = current.next
new_node.prev = current

current.next.prev = new_node
current.next = new_node


# Traversal
current = head

while current is not None:
    print(current.item, end=" <-> ")
    current = current.next

print("None")



