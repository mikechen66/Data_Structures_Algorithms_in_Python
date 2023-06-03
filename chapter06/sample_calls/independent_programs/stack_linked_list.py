
# Python program to demonstrate
# stack implementation using a linked list.

"""

Implementation using a singly linked list:

The linked list has two methods addHead(item) and removeHead() that run in constant time. These two methods 
are suitable to implement a stack. 

get_size()– Get the number of items in the stack.

is_empty() – Return True if the stack is empty, False otherwise.
peek() – Return the top item in the stack. If the stack is empty, raise an exception.
push(value) – Push a value into the head of the stack.
pop() – Remove and return a value in the head of the stack. If the stack is empty, raise an exception.
"""


# node class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]
    # Get the current size of the stack
    def get_size(self):
        return self.size
    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0
    # Get the top item of the stack
    def peek(self):
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    # Remove a value from the stack and return.
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")


# Output:

"""
Stack: 10->9->8->7->6->5->4->3->2->1
Pop: 10
Pop: 9
Pop: 8
Pop: 7
Pop: 6
Stack: 5->4->3->2->1
"""