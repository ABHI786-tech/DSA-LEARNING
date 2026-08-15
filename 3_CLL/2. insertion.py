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



# New node
new_node = Node(5)


# Find last node
last = head

while last.next != head:
    last = last.next

# --------------------------------------------
# Insert at beginning
# --------------------------------------------
new_node.next = head
last.next = new_node
head = new_node


# Traversal
current = head
print("insert_at_beginning")
while True:
    print(current.item, end=" -> ")
    current = current.next

    if current == head:
        break

print("(back to head)")
print("_________________________________________________")




# --------------------------------------------
# Insert at end
# --------------------------------------------


# New node
new_node = Node(40)


# Find last node
last = head

while last.next != head:
    last = last.next


# Insert at end
last.next = new_node
new_node.next = head


# Traversal
current = head
print("insert_at_end")
while True:
    print(current.item, end=" -> ")
    current = current.next

    if current == head:
        break

print("(back to head)")
print("_________________________________________________")





# --------------------------------------------
# Insert at mid
# --------------------------------------------

# New node
new_node = Node(25)

# Position
position = 3


# Traverse to position - 1
current = head

for i in range(1, position - 1):
    current = current.next


# Insert node
new_node.next = current.next
current.next = new_node


# Traversal
current = head

print("insert at mid")
while True:
    print(current.item, end=" -> ")
    current = current.next

    if current == head:
        break


print("(back to head)")
print("_________________________________________________")
