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
# Search an Element
# ============================================================

key = 30

current = head
found = False

while True:

    if current.item == key:
        found = True
        break

    current = current.next

    if current == head:
        break


print("search")

if found:
    print(key, "found in the list")
else:
    print(key, "not found in the list")

print("_________________________________________________")


# ============================================================
# Count Nodes
# ============================================================

count = 0

current = head

while True:
    count += 1
    current = current.next

    if current == head:
        break


print("count_nodes")
print("Number of nodes:", count)
print("_________________________________________________")


# ============================================================
# Find Last Node
# ============================================================

last = head

while last.next != head:
    last = last.next


print("find_last_node")
print("Last node:", last.item)
print("_________________________________________________")
