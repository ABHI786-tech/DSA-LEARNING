

class stack:
    def __init__(self):
        self.items = []

# check the stack is empty 
    def is_empty(self):
        return len(self.items) == 0

#  add the item  in the stack 
    def push(self,item):
        self.items.append(item)

# remove the top item from the stack 
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

# return the top item value in the stack 
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

# check the length of the items
    def size(self):
        return len(self.items)



s1= stack()
s1.push(10)
s1.push(20)
s1.push(30)


# print(s1.pop())
# print(s1.peek())
# print(s1.size())
# print(s1.is_empty())
# print(s1.items)
