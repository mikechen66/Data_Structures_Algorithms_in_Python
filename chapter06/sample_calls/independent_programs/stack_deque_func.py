

# stack_dequeu_func.py


"""
We can also use the deque class of the Python collections module to 
implement a stack. Since a deque or double ended queue allow us to 
insert and delete element from both front and rear sides, it might 
be more suitable at times when we require faster append() and pop() 
operations. 
"""


from collections import deque  


# Create empty deque
def create_stack():  
    stack = deque()    
    return stack 


# Push operation using append()
def push(stack, item):
    stack.append(item)


# Pop operation
def pop(stack):
    if(stack):
        print('Element popped from stack:')
        print(stack.pop())
    else:
        print('Stack is empty')


# Display Stack
def show(stack):
    print('Stack elements are:')
    print(stack)


if __name__ == '__main__':
    new_stack = create_stack()
    push(new_stack, 25)
    push(new_stack, 56)
    push(new_stack, 32)
    show(new_stack)
    pop(new_stack)
    show(new_stack)


# Output:

"""
Stack elements are:
deque([25, 56, 32])
Element popped from stack:
32
Stack elements are:
deque([25, 56])
"""