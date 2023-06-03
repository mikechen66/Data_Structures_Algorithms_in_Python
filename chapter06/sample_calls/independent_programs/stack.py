

# stack.py

"""
We define a class named Stack and implement the Stack using python lists. In the Stack 
class, we have a list containing the data added to the Stack and a variable storing the 
size of the Stack. All the operations such as push, pop, checking the size of the stack, 
checking the topmost element of stack and checking the stack if it is empty will be 
executed in constant time and thus will have O(1) time complexity.

# __init__()

The stacklist is initialized as an empty list and stacksize is initialized to 0.

# push()

To insert an item into the stack i.e. to push an element into the stack, we simply append 
the element in the list and then increment the stacksize variable by 1.

# pop()

To remove an item from the stack we remove the element from the stack which was added 
last to it. As we append the element to the list in stack, the last element in the list 
is the most recent element and is removed from the stack. So we simply delete the last 
element from the list. 

# check_size()

We simply check the value of the stackSize variable. For this operation, we implement the 
check_size() method which returns the value of stackSize variable as follows.

# is_empty()

We implementis_Empty() method which returns True if the stacksize variable is 0 or returns 
false otherwise.

# top()

To check the topmost element of the stack, we return the last element in the list in the 
stack. Implement the top() method which first checks if the stack is empty i.e. stacksize 
is 0 or not, if yes then it shows a message that the stack is empty. Otherwise it return 
the last element of the list. 
"""


class Stack:
    def __init__(self):
        self.stacklist = []
        self.stacksize = 0
    def push(self, item):
        self.stacklist.append(item)
        self.stacksize += 1
    def pop(self):
        try:
            if self.stacksize == 0:
                raise Exception("Stack is Empty, returning None")
            temp = self.stacklist.pop()
            self.stacksize -= 1
            return temp
        except Exception as e:
            print(str(e))
    def check_size(self):
        return self.stacksize
    def is_empty(self):
        if self.stacksize == 0:
            return True
        else:
            return False
    def top(self):
        try:
            if self.stacksize == 0:
                raise Exception("Stack is Empty, returning None")
            return self.stacklist[-1]
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("popped element is:")
    print(s.pop())
    s.push(4)
    print("topmost element is:")
    print(s.top())


# Output:

"""
popped element is:
3
topmost element is:
4
"""