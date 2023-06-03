

# Stack implementation in python


"""
A stack is a linear data structure that follows the principle of Last In First Out (LIFO). 
This means the last element inserted inside the stack is removed first.
"""


# Create a stack
def create_stack():
    stack = []
    return stack


# Create an empty stack
def check_empty(stack):
    return len(stack) == 0


# Add items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Remove an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()


if __name__ == '__main__':
    stack = create_stack()
    push(stack, str(1))
    push(stack, str(2))
    push(stack, str(3))
    push(stack, str(4))
    print("popped item: " + pop(stack))
    print("stack after popping an element: " + str(stack))


# Output:

"""
pushed item: 1
pushed item: 2
pushed item: 3
pushed item: 4
popped item: 4
stack after popping an element: ['1', '2', '3']
"""