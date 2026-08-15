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


search_value = 30

current = node1
# found = True

while current is not None:

    if current.item == search_value:
        found = True
        break

    current = current.next


if found:
    print("Element found")
else:
    print("Element not found")



# --------------------------------------------
# count the number of nodes
# --------------------------------------------

count = 0
current = node1

while current is not None:
    count += 1
    current = current.next

print("Length:", count)




# --------------------------------------------
# Reverse linked list
# --------------------------------------------
previous = None
current = node1

while current is not None:

    next_node = current.next

    current.next = previous

    previous = current

    current = next_node


# New head
node1 = previous


# Traversal
current = node1

while current is not None:
    print(current.item)
    current = current.next
