

# stack_lq_func.py

"""
The queue module of Python consists of a LIFO queue. A LIFO queue is nothing but a stack. Hence, 
we can easily and effectively implement a stack in Python using the queue module. For a LifoQueue, 
we have certain functions that are useful in stack implementation, such as qsize(), full(), 
empty(), put(n), get() as seen in the following piece of code. The max size parameter of LifoQueue 
defines the limit of items that the stack can hold.
"""


from queue import LifoQueue


# Initialize a stack
def new():
    stack = LifoQueue(maxsize=3)            # Fix the stack size
    return stack


# Push using put(n) 
def push(stack, item):
    if(stack.full()):                       # Check if the stack is full
        print("The stack is already full")
    else:
        stack.put(item)
        print("Size: ", stack.qsize())      # Determine the stack size


# Pop using get()
def pop(stack):
    if(stack.empty()):                      # Check if the stack is empty
        print("Stack is empty")
    else:
        print('Element popped from the stack is ', stack.get()) # Remove the last element
        print("Size: ", stack.qsize())


if __name__ == '__main__':
    stack = new()
    pop(stack)
    push(stack, 32)
    push(stack, 56)
    push(stack, 27)
    pop(stack)


# Output:

"""
Stack is empty
Size:  1
Size:  2
Size:  3
Element popped from the stack is  27
Size:  2
"""