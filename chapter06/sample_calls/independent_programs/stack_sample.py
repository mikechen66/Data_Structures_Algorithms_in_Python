
# stack_simple.py

"""

The script only show the output according to the pop() command, if users 
want to get the output according to push(), users can use 

def push(self, item):
    self.stack.append(item)
    return print(item)
def pop(self):
    if (self.check_empty()):
        return "stack is empty"
"""



class Stack: 
    def __init__(self):
        self.stack = []
    # Check an empty stack
    def check_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if (self.check_empty()):
            return "stack is empty"
        return self.stack.pop()


if __name__ == '__main__':
    s = Stack()
    s.push('eat')
    s.push('sleep')
    s.push('code')
    s.pop()
    s.pop()
    s.pop()
    s.push('Hello Python')
    s.pop()


# Output:

"""
'code'
'sleep'
'eat'
'Hello Python'
"""



# Another option for otuput
"""
class Stack: 
    def __init__(self):
        self.stack = []
    # Check an empty stack
    def check_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)
        return print(item)
    def pop(self):
        if (self.check_empty()):
            return "stack is empty"


if __name__ == '__main__':
    s = Stack()
    s.push('eat')
    s.push('sleep')
    s.push('code')
    s.pop()
    s.pop()
    s.pop()
    s.push('Hello Python')
    s.pop()

# Output

# eat
# sleep
# code
# Hello Python
"""
