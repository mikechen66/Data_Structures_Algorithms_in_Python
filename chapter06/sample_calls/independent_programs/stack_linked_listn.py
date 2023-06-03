

# stack_singly_linked_list.py

"""
Implementation using a singly linked list
Singly-linked lists are the most efficient and effective way of implementing dynamic stacks. 
We use the class and object approach of Python OOP to create linked lists in Python. We have 
certain functions at our disposal in Python that are useful in stack implementation, such as
 getSize(), isEmpty(), push(n), and pop(). Let’s take a look at how each of these functions 
 helps in implementing a stack.
"""


# Node creation
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Stack creation
class Stack:
    # Stack with dummy node
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    #  For string representation of the stack
    def __str__(self):
        val = self.head.next
        show = ""
        while val:
            show += str(val.value) + " , "
            val = val.next
        return show[:-3]
    # Retrieve the size of the stack
    def get_size(self):
        return self.size
    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0
    # Retrieve the top item of the stack
    def peek(self):
        # Check for empty stack.
        if self.isEmpty():
            raise Exception("This is an empty stack")
        return self.head.next.value
    # Push operation
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    # Pop Operation
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


if __name__ == "__main__":
    stack = Stack()
    n = 20
    for i in range(1, 11):
        stack.push(n)
        n += 5
    print(f"Stack:{stack}")
    for i in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")


# Output:

"""
Stack:65 , 60 , 55 , 50 , 45 , 40 , 35 , 30 , 25 , 20
Pop: 65
Pop: 60
Pop: 55
Pop: 50
Pop: 45
Stack: 40 , 35 , 30 , 25 , 20

"""