# --------------------------------------------
#  search
# --------------------------------------------

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


# Search
value = 30
current = head
found = False

while current is not None:

    if current.item == value:
        found = True
        break

    current = current.next


if found:
    print(value, "found")
else:
    print(value, "not found")



# --------------------------------------------
#  length
# --------------------------------------------
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


head = node1


# Find length
count = 0
current = head

while current is not None:
    count += 1
    current = current.next


print("Length:", count)
