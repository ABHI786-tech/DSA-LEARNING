class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# --------------------------------------------
#  Delete at beginning
# --------------------------------------------


node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


head = node1


# Delete first node
head = head.next
head.prev = None


# Traversal
current = head

while current is not None:
    print(current.item, end=" <-> ")
    current = current.next

print("None")



# --------------------------------------------
# Delete from end
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


# Remove last node
current.prev.next = None


# Traversal
current = head

while current is not None:
    print(current.item, end=" <-> ")
    current = current.next

print("None")









# --------------------------------------------
#  Delete by Value
# --------------------------------------------
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


head = node1


# Value to delete
value = 30

current = head

while current is not None:

    if current.item == value:

        # If node is not first
        if current.prev is not None:
            current.prev.next = current.next

        # If node is first
        else:
            head = current.next

        # If node is not last
        if current.next is not None:
            current.next.prev = current.prev

        break

    current = current.next


# Traversal
current = head

while current is not None:
    print(current.item, end=" <-> ")
    current = current.next

print("None")
    