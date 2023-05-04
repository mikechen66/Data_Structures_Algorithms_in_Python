
# Stacks, Queues, and Deques

############################################################################################################################

# Part One. Reinforcement

############################################################################################################################


# R6.1 What values are returned during the following series of stack operations, if executed upon an 
# initially empty stack? push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), 
# pop(), push(7), push(6), pop(),pop(), push(4), pop(), pop(). Note we have 9 pushes and 8 pops, so 
# wehave one value left in the stack as expected.


# (1). Adopt ArrayStack class

class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        # Create an empty stack.
        self._data = []                       # nonpublic list instance
    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)
    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0
    def push(self, value):
        # Add element e to the top of the stack.
        self._data.append(value)              # new item stored at end of list
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()               # remove last item from list


if __name__ == '__main__':
    ask = ArrayStack()
    ask.push(5)
    ask.push(3)
    ask.pop()
    ask.push(2)
    ask.push(8)
    ask.pop()
    ask.pop()
    ask.push(9)
    ask.push(1)
    ask.pop() 
    ask.push(7) 
    ask.push(6)
    ask.pop()
    ask.pop() 
    ask.push(4)
    ask.pop()
    ask.pop()    


"""
3
8
2
1
6
7
4
9
"""

#--------------------------------------------------------------------------------------------------------------- 


# (2).Adopt ArrayQueue class 


# Code Fragment 6.6: Definition for an Empty exception class.
class Empty(Exception):
    pass


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10                      # moderate capacity for all new queues
    def __init__(self):
        # Create an empty queue.
        self._data = [None] * self.DEFAULT_CAPACITY # _data: list instance
        self._size = 0  # number of the elements stored in the queue
        self._front = 0 # index of the first element of self._data instance queue
    def __len__(self):
        # Return the number of elements in the queue.
        return self._size
    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0
    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    def enqueue(self, e):
        # Add an element to the back of queue.
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1        
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]       # self_data: list instance
        self._data[self._front] = None         # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer
    def _resize(self, cap):                    # we assume cap >= len(self)
        # Resize to a new list of capacity >= len(self).
        old = self._data                       # keep track of existing list
        self._data = [None] * cap              # allocate list with new capacity
        walk = self._front
        for k in range(self._size):            # only consider existing elements
            self._data[k] = old[walk]          # intentionally shift indices
            # What is the meanding 1 + walk, walk is self._front? 
            # It take the seond element as the first element 
            walk = (1 + walk) % len(old)       # use old size as modulus
        self._front = 0                        # front has been realigned


if __name__ == '__main__':
    aq = ArrayQueue()
    aq.enqueue(5)
    aq.enqueue(3)
    aq.dequeue()
    aq.enqueue(2)
    aq.enqueue(8)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(9)
    aq.enqueue(1)
    aq.dequeue()
    aq.enqueue(7)
    aq.enqueue(6)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(4)
    aq.dequeue()
    aq.dequeue() 


"""
3
8
2
1
6
7
4
9
"""

############################################################################################################################


# R6.2 Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, 
# and 10 pop operations, 3 of which raised Empty errors that were caught and ignored. What is the current 
# size of S?


# (1).Without top() fuinction


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        # Create an empty stack.
        self._data = []                       # nonpublic list instance
    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)
    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0
    def push(self, value):
        # Add element e to the top of the stack.
        self._data.append(value)              # new item stored at end of list
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            # raise Empty('Stack is empty')   # Comment it 
            print("Empty warning")            # Add print() for not raise Empty
            return None                       # add return None for not warning
        return self._data.pop()               # remove last item from list


if __name__ == '__main__':
    ask = ArrayStack()
    for i in range(7):
        ask.push(i)
    for i in range(10):
        ask.pop()
    for i in range(18):
        ask.push(i)
    for i in range(12):
        ask.top()


# Output:


"""
6
5
4
3
2
1
0
Empty warning
Empty warning
Empty warning
17
17
17
17
17
17
17
17
17
17
17
17
"""

#--------------------------------------------------------------------------------------------------------------------------


# (2).Including top() function


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        # Create an empty stack.
        self._data = []                       # nonpublic list instance
    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)
    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0
    def push(self, value):
        # Add element e to the top of the stack.
        self._data.append(value)              # new item stored at end of list
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            # raise Empty('Stack is empty')   # Comment it 
            print("Empty warning")            # Add print() for not raise Empty
            return None                       # add return None for not warning 
        return self._data.pop()               # remove last item from list


if __name__ == '__main__':
    ask = ArrayStack()
    for i in range(7):
        ask.push(i)
    for i in range(10):
        ask.pop()
    for i in range(18):
        ask.push(i)


# Output:

"""
6
5
4
3
2
1
0
EMPTY WARNING
EMPTY WARNING
EMPTY WARNING
"""

############################################################################################################################


# R6.3 Implement a function with signature transfer(S, T) that transfers all elements from stack S 
# onto stack T, so that the element that starts at the top of S is the first to be inserted onto T, 
# and the element at the bottom of S ends up at the top of T.


class Empty(Exception):
    pass


class ArrayStack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    """
    def top(self):
        return self._data[-1]
    """
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        poplist = []
        while not self.is_empty():
            poplist.append(self.pop())
        return poplist


def transfer(S, T):
    # while len(S) > 0: 
    while not S.is_empty():
        T.push(S.pop())


if __name__ == '__main__':
    S, T = ArrayStack(), ArrayStack()
    try: 
        S.pop()
    except Exception as e: 
        print(e)
    for i in range(10):
        S.push(i)
    print('Top of S is: ', S.top())
    transfer(S, T)  
    print('Top of T is: ', T.top())
    S.full_pop(), T.full_pop()


# Output:

"""
List is empty
Top of S is:  10
Top of T is:  0
([], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
"""

#---------------------------------------------------------------------------------------------------------------------------


# (3).Add transfer() method within ArrayStack


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        # Create an empty stack.
        self._data = []                       # nonpublic list instance
    def data(self):
        return self._data
    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)
    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0
    def push(self, e):
        # Add element e to the top of the stack.
        self._data.append(e)                  # new item stored at end of list
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()               # remove last item from list
    def full_pop(self):
        ans = []
        while not self.is_empty():
            ans.append(self.pop())
        return ans
    def transfer(self, S, T):
        while not S.is_empty():
            T.push(S.pop())


if __name__ == '__main__':
    Ask, S, T = ArrayStack(), ArrayStack(), ArrayStack()
    try: 
        S.pop()
    except Exception as e: 
        print(e)
    for i in range(10):
        S.push(i)
    print('Top of S is: ', S.top())
    Ask.transfer(S, T)  
    print('Top of T is: ', T.top())
    S.full_pop()
    T.full_pop()


# Output:

"""
List is empty
Top of S is:  19
Top of T is:  0
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

#---------------------------------------------------------------------------------------------------------------------------


# (4).Exclude @property and call it without bracket

# Please note the transfer function is quite strage 


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""
    def __init__(self):
        self._data = []
    def make_data(self):
        return self._data
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    """
    def transfer(self, S):
        while not S.is_empty():
            self.push(S.pop())
    """
    def transfer(self, S):
        stack_len = len(self._data)
        [S.push(self.pop()) for _ in range(stack_len)]


if __name__ == '__main__':
    Ask = ArrayStack()
    for i in range(10):
        Ask.push(i)
    print(Ask.make_data())
    S = ArrayStack()
    Ask.transfer(S)
    print(S.make_data())


# Output:

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

#---------------------------------------------------------------------------------------------------------------------------


# (5).Add @property


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""
    def __init__(self):
        self._data = []
    @property
    def make_data(self):
        return self._data
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    def transfer(self, S):
        stack_len = len(self._data)
        [S.push(self.pop()) for _ in range(stack_len)]


if __name__ == '__main__':
    Ask = ArrayStack()
    for i in range(10):
        Ask.push(i)
    # ask.make_data()         # TypeError: 'list' object is not callable
    print(Ask.make_data)
    S = ArrayStack()
    Ask.transfer(S)
    # ask.make_data()         # TypeError: 'list' object is not callable
    print(S.make_data)


# Output:

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

#---------------------------------------------------------------------------------------------------------------------------


# (6).Show pop(), pop() and full_pop()


import dis 
import sys  
sys.setrecursionlimit(1000)  


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        # Create an empty stack.
        self._data = []                       # nonpublic list instance
    def make_data(self):
        return self._data
    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)
    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0
    def push(self, n):
        # Add element e to the top of the stack.
        self._data.append(n)                  # new item stored at end of list
        return self._data
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if len(self._data) > 0:
            pdata = self._data[:-i-1]
            return pdata
        elif self.is_empty():
            raise Empty('Stack is empty')
    def full_pop(self):
        poplist = []
        if self.is_empty():
            poplist.append(self.pop())
        return poplist
    def transfer(self, S, T):
        while not S.is_empty():
            T.push(S.pop())


if __name__ == '__main__':
    ask = ArrayStack()
    print("The iterative push operation")
    for i in range(10):
        Push = ask.push(i)
        print(Push)
    print("The iterative pop operation")
    for i in range(10): 
        Pop = ask.pop()
        print(Pop)


# Output:

"""
The iterative push operation
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
The iterative pop operation
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4]
[0, 1, 2, 3]
[0, 1, 2]
[0, 1]
[0]
[]
"""

######################################################################################################


# R6.4 Give a recursive method for removing all the elements from a stack.


# (1).simple O(n) for normal or O(n^2) for in_order=True


class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    """
    def top(self):
        return self._data[-1]
    """
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()


class RStack(ArrayStack):
    def full_pop(self, in_order=False): #override the Stack.full_pop method
        if self.is_empty():
            return []
        else:
            ans = [self.pop()]
            data =  self.full_pop(in_order)
            if in_order: 
                ans, data = data, ans
            data.extend(ans)
            return data

if __name__ == '__main__':   
    S = RStack()
    for i in range(20):
        S.push(i)
    print(S.full_pop(in_order=True))


# Output:

"""
[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

#---------------------------------------------------------------------------------------------------------------------------


# (2). Switch the stack 


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""
    def __init__(self):
        self._data = []
    def make_data(self):
        return self._data
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            # raise Empty('Stack is empty')
            print("Empty Stack Warning")
            return None
        return self._data.pop()
    def transfer(self, S, T):
        while not S.is_empty():
            T.push(S.pop())
    def pop_all(self):
        if self.make_data():
            self.pop()
            return self.pop_all()


if __name__ == '__main__': 
    Ask, S, T = ArrayStack(), ArrayStack(), ArrayStack()
    for i in range(10):
        S.push(i)
    print('Top of S is: ', S.make_data())
    Ask.transfer(S, T)
    print('Top of T is: ', T.make_data())
    Ask.pop_all()


"""
Top of S is:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Top of T is:  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

############################################################################################################################


# R6.5 Implement a function that reverses a list of elements by pushing them onto a stack in one 
# order, and writing them back to the list in reversed order. Note, this relies on the stack 
# from R6.3


class Empty(Exception):
    pass


class Stack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        poplist = []
        while not self.is_empty():
            poplist.append(self.pop())
        return poplist


def reverse_list(S):
    temp = Stack()
    for elem in S:
        temp.push(elem)
    for i in range(len(S)):
        S[i] = temp.pop()


if __name__ == '__main__':
    lists = [[1,2,3,4,5,6],
            [3,2,5,6,7,8,9,5],
            [9,8,7,6,5,4,3,2,1]]
    for l in lists:
        print('Before: ', l)
        reverse_list(l)
        print('After:  ', l)
        print()


# Output:

"""
Before:  [1, 2, 3, 4, 5, 6]
After:   [6, 5, 4, 3, 2, 1]

Before:  [3, 2, 5, 6, 7, 8, 9, 5]
After:   [5, 9, 8, 7, 6, 5, 2, 3]

Before:  [9, 8, 7, 6, 5, 4, 3, 2, 1]
After:   [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

############################################################################################################################


# R6.6 Give a precise and complete definition of the concept of matching for grouping symbols in 
# an arithmetic expression. Your definition may berecursive.


class Empty(Exception):
    pass


class Stack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        ans = []
        while not self.is_empty():
            ans.append(self.pop())
        return ans


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


class AlgoStack(Stack):
    def __repr__(self):
        return str(self._data)
    OPEN, CLOSE, OPERATORS = '(', ')', '+-/*^'
    NUMBERS = '1234567890.'
    def pop_until_open(self):
        operator = True
        while not self.is_empty():
            ans = self.pop()
            if ans in self.OPERATORS:
                if operator: 
                    return False
                else: 
                    operator = True
            elif ans in self.NUMBERS:
                operator = False
            elif ans in self.CLOSE: 
                return False
            elif ans in self.OPEN: 
                self.push('3')
            # The else substatement is equal to return False not indented as follows
            """
            else: 
                return False  # if you don't find an open bracket, there is a mismatch
            """
        return False
    def check_expression(self, expression):
        for char in expression:
            if char in self.CLOSE:
                if not self.pop_until_open(): 
                    return False
            else: 
                self.push(char)
        return True


if __name__ == '__main__':  
    exps = ['(5+4)*(3/(2+3))',
           '(5+4+)*(3/(2+3))',
            '(5+4))*(3/(2+3))',
           '5+(5+4)*(3/(2+3))']
    for exp in exps:
        alst = AlgoStack()
        print(exp, alst.check_expression(exp))


# Output:

"""
(5+4)*(3/(2+3)) True
(5+4+)*(3/(2+3)) False
(5+4))*(3/(2+3)) False
5+(5+4)*(3/(2+3)) True
"""

############################################################################################################################


# R6.7 What values are returned during the following sequence of queue operations, if executed on 
# an initially empty queue? enqueue(5), enqueue(3),dequeue(), enqueue(2), enqueue(8), dequeue(), 
# dequeue(), enqueue(9),enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(), 
# enqueue(4), dequeue(), dequeue().


# Code Fragment 6.6: Definition for an Empty exception class.
class Empty(Exception):
    pass


# Code Fragment 6.2: Implementing a stack using a Python list as storage.
class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10                      # moderate capacity for all new queues
    def __init__(self):
        # Create an empty queue.
        self._data = [None] * self.DEFAULT_CAPACITY # _data: list instance
        self._size = 0  # number of the elements stored in the queue
        self._front = 0 # index of the first element of self._data instance queue
    def __len__(self):
        # Return the number of elements in the queue.
        return self._size
    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0
    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    def enqueue(self, e):
        # Add an element to the back of queue.
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1        
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]       # self_data: list instance
        self._data[self._front] = None         # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    def _resize(self, cap):                    # we assume cap >= len(self)
        # Resize to a new list of capacity >= len(self).
        old = self._data                       # keep track of existing list
        self._data = [None] * cap              # allocate list with new capacity
        walk = self._front
        for k in range(self._size):            # only consider existing elements
            self._data[k] = old[walk]          # intentionally shift indices
            # What is the meanding 1 + walk, walk is self._front? 
            # It take the seond element as the first element 
            walk = (1 + walk) % len(old)       # use old size as modulus
        self._front = 0                        # front has been realigned


if __name__ == '__main__':
    aq = ArrayQueue()
    aq.enqueue(5)
    aq.enqueue(3)
    aq.dequeue()
    aq.enqueue(2)
    aq.enqueue(8)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(9)
    aq.enqueue(1)
    aq.dequeue()
    aq.enqueue(7)
    aq.enqueue(6)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(4)
    aq.dequeue()
    aq.dequeue()


# Output:

"""
5
3
2
8
9
1
7
6
"""

############################################################################################################################


# R6.8 Suppose an initially empty queue Q has executed a total of 32 enqueue operations, 10 first 
# operations, and 15 dequeue operations, 5 of which raised Empty errors that were caught and ignored. 
# What is the current size of Q?

# Omit 


############################################################################################################################


# 6.9 Had the queue of the previous problem been an instance of ArrayQueue that used an initial array 
# of capacity 30, and had its size never been greater than 30, what would be the final value of the 
# front instance variable?

# Omit 


############################################################################################################################


# R6.10


"""
Consider what happens if the loop in the ArrayQueue. resize method at
lines 53–55 of Code Fragment 6.7 had been implemented as: 

for k in range(self. size):
    self. data[k] = old[k]    # rather than old[walk]

Give a clear explanation of what could go wrong.
"""


# Code Fragment 6.6: Definition for an Empty exception class.
class Empty(Exception):
    pass


# Code Fragment 6.2: Implementing a stack using a Python list as storage.
class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10                      # moderate capacity for all new queues
    def __init__(self):
        # Create an empty queue.
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY # _data: list instance
        self._size = 0  # number of the elements stored in the queue
        self._front = 0 # index of the first element of self._data instance queue
    def __len__(self):
        # Return the number of elements in the queue.
        return self._size
    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0
    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    def enqueue(self, e):
        # Add an element to the back of queue.
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1        
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]       # self_data: list instance
        self._data[self._front] = None         # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    def _resize(self, cap):                    # we assume cap >= len(self)
        # Resize to a new list of capacity >= len(self).
        old = self._data                       # keep track of existing list
        self._data = [None] * cap              # allocate list with new capacity
        walk = self._front
        for k in range(self._size):            # only consider existing elements
            self._data[k] = old[k]             # intentionally give a wrong k
            # What is the meanding 1 + walk, walk is self._front? 
            # It take the seond element as the first element 
            walk = (1 + walk) % len(old)       # use old size as modulus
        self._front = 0                        # front has been realigned


if __name__ == '__main__':
    aq = ArrayQueue()
    aq.enqueue(5)
    aq.enqueue(3)
    aq.dequeue()
    aq.enqueue(2)
    aq.enqueue(8)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(9)
    aq.enqueue(1)
    aq.dequeue()
    aq.enqueue(7)
    aq.enqueue(6)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(4)
    aq.dequeue()
    aq.dequeue()


# Output:

"""
5
2
8
9
1
7
6
"""

############################################################################################################################


# R6.11 Give a simple adapter that implements our queue ADT while using a collections.deque instance 
# for storage.

"""
popleft() in the collections module 
# https://docs.python.org/zh-cn/3/library/collections.html?highlight=deque
"""


import collections


class Queue():
    def __init__(self):
        self._data = collections.deque()
        self._size = 0
    def __len__(self):
        return self._size
    def first(self):
        return self._data[0]
    def enqueue(self, value):
        self._size += 1
        self._data.append(value)  # Append here to add an element to the end of the queue
    def is_empty(self):
        return self._size == 0
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            ans = self._data.popleft()
            self._size -= 1
            return ans


if __name__ == '__main__':          
    dq = Queue()
    for i in range(10):
        dq.enqueue(i)
    print('First', dq.first(), 'Length', len(dq))
    while not dq.is_empty():
        print( dq.dequeue(),  end = ', ')


# Output:

"""
First 0 Length 10
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, >>>
"""

############################################################################################################################


# R6.12 What values are returned during the following sequence of deque ADT operations, on initially 
# empty deque? add first(4), add last(8), add last(9), add first(5), back( ), delete first( ), delete 
# last(), add last(7), first( ), last( ), add last(6), delete first( ), delete first( ).

# Omit 

############################################################################################################################


# R6.13 Suppose you have a deque D containing the numbers (1, 2, 3, 4, 5, 6, 7, 8), in this order. 
# Suppose further that you have an initially empty queue Q. Give a code fragment that uses only 
# D and Q (and no other variables) and results in D storing the elements in the order as follows: 
# (1, 2, 3, 5, 4, 6, 7, 8).


import collections


class Queue():
    def __init__(self):
        self._data = collections.deque()
        self._size = 0
    def __len__(self):
        return self._size
    def first(self):
        return self._data[0]
    def enqueue(self, value):
        self._size += 1
        self._data.append(value)  # Append here to add an element to the end of the queue
    def is_empty(self):
        return self._size == 0
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            poplist = self._data.popleft()
            self._size -= 1
            return poplist


# Setup
D = collections.deque()
Q = Queue()
for i in range(1, 9, 1):
    D.append(i)


def rearrange_using_queue(D, Q):    
    for i in range(5):             #   D          Q
        Q.enqueue(D.popleft())     #[6,7,8], [1,2,3,4,5]
    for i in range(3):
        D.append(Q.dequeue())      #[6,7,8,1,2,3], [4,5]
    for i in range(2):
        D.appendleft(Q.dequeue())  #[5,4,6,7,8,1,2,3], []
    for i in range(3):
        Q.enqueue(D.pop())         #[5,4,6,7,8], [3,2,1]
    for i in range(3):
        D.appendleft(Q.dequeue())  #[1,2,3,5,4,6,7,8]


if __name__ == '__main__':     
    rearrange_using_queue(D, Q)
    print('Values of Q:')
    while not Q.is_empty():
        print(Q.dequeue())
    print('Values of D')
    while len(D) != 0:
        print(D.popleft())


# Output:

"""
Values of Q:
Values of D
1
2
3
5
4
6
7
8
"""

############################################################################################################################


# R6.14 Repeat the previous problem using the deque D and an initially empty stack S.


import collections


class Empty(Exception):
    pass


class Stack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        poplist = []
        while not self.is_empty():
            poplist.append(self.pop())
        return poplist


S = Stack()
D = collections.deque()


for i in range(1,9,1):
    D.append(i)


def rearrange_using_stack(D, S):
    for _ in range(4):
        S.push(D.popleft())    # [5,6,7,8], [1,2,3,4]  
    D.append(S.pop())          # [5,6,7,8,4], [1,2,3]
    S.push(D.popleft())        # [6,7,8,4], [1,2,3,5]
    S.push(D.pop())            # [6,7,8], [1,2,3,5,4]
    for _ in range(5):
        D.appendleft(S.pop())  # [1,2,3,5,4,6,7,8], []


if __name__ == '__main__': 
    rearrange_using_stack(D, S) 
    print('Values of S')
    while not S.is_empty():
        print(S.pop())
    print('Values of D:')
    while len(D) != 0:
        print(D.popleft())


# Output:

"""
Values of S
Values of D:
1
2
3
5
4
6
7
8
"""

############################################################################################################################
############################################################################################################################


# Part Two. Creativity


############################################################################################################################


# C6.15 Suppose Alice has picked three distinct integers and placed them into a stack S in random order. 
# Write a short, straight-line piece of pseudo-code (with no loops or recursion) that uses only one comparison 
# and only one variable x, yet that results in variable x storing the largest of Alice’s three integers 
# with probability 2/3. Argue why your method is correct.


import random


class Empty(Exception):
    pass


class Stack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        poplist = []
        while not self.is_empty():
            poplist.append(self.pop())
        return poplist


def max_picker(S, numbers):
    # Randomize
    random.shuffle(numbers)
    true_max = max(numbers)
    # Set up the stack
    for num in numbers:
        S.push(num)
    # Perform the test:
    x = S.pop()
    new = S.pop()
    return new if new > x else x


if __name__ == '__main__':  
    num_trials = 1000
    total = 0
    numbers = [1,2,3]
    S = Stack()
    for i in range(num_trials):
        if max_picker(S, numbers) == max(numbers): 
            total += 1
    print(f'The probability of you picking the correct number is: {total/num_trials*100}%')


# Output:

"""
The probability of you picking the correct number is: 65.5%
"""

############################################################################################################################


# C6.16

"""
Modify the ArrayStack implementation so that the stack’s capacity is limited to maxlen elements, where 
maxlen is an optional parameter to the constructor (that defaults to None). If push is called when the 
stack is at full capacity, throw a Full exception (defined similarly to Empty).
"""


class Empty(Exception):
    pass


class Full(Exception):
    pass


class ArrayStack():
    def __init__(self, maxlen=None):
        self._data = []
        self._maxlen = maxlen
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        #  if self._maxlen is not None and (len(self._data) >= self._maxlen):
        if self._maxlen is not None and len(self) == self._maxlen:
            raise Full('The array is full')
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


if __name__ == '__main__':
    astack = ArrayStack(10)
    for i in range(20):
        try: 
            astack.push(i)
            print(astack.top())
        except Full as e:
            print(e)


# Output:

"""
0
1
2
3
4
5
6
7
8
9
The array is full
The array is full
The array is full
The array is full
The array is full
The array is full
The array is full
The array is full
The array is full
The array is full
"""

############################################################################################################################
 

# C6.17 In the previous exercise, we assume that the underlying list is initially empty. Redo that 
# exercise, this time preallocating an underlying list with length equal to the stack’s maximum 
# capacity. Note for this one we now have to manage the number of elements we insert


# Option 1:


class Empty(Exception):
    pass


class Full(Exception):
    pass


class ArrayStackPrealloc():
    def __init__(self, maxlen=20):
        self._capacity = maxlen
        self._data = [None] * maxlen
        self._n = 0
    def __len__(self):
        return self._n
    def is_empty(self):
        return len(self) == 0
    def push(self, value):
        if self._n == self._capacity:
            raise Full('The stack is full')
        self._data[self._n] = value
        self._n += 1
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        ans = self._data[self._n - 1]
        self._data[self._n - 1] = None
        self._n -= 1
        return ans
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._n - 1]


if __name__ == '__main__':
    apstack = ArrayStackPrealloc(10)
    for i in range(20):
        try:
            apstack.push(i)
            print(apstack.top())
        except Full as e:
            print(e)


# Output:

"""
0
1
2
3
4
5
6
7
8
9
The stack is full
The stack is full
The stack is full
The stack is full
The stack is full
The stack is full
The stack is full
The stack is full
The stack is full
The stack is full
"""

#---------------------------------------------------------------------------------------------------------------------------


# Option 2: 


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Full(Exception):
    """Error when stack is full"""
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self, maxlen=None):
        # Create an empty stack.
        # self._data = [] if maxlen is None else [None] * maxlen
        if maxlen is None:
            self._data = []
        else:
            [None] * maxlen
        self._maxlen = maxlen
    def __len__(self):
        # Return the number of elements in the stack
        return len(self._data)
    def make_data(self):
        return self._data
    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0
    def push(self, e):
        # Add element e to the top of the stack.
        if self._maxlen is not None and (len(self._data) >= self._maxlen):
            raise Full('Stack is full.')
        self._data.append(e)
    def top(self):
        # Return (but do not remove) the element at the top of the stack.
        # Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        # Remove and return the element from the top of the stack (i.e.,LIFO)
        # Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


if __name__ == '__main__':
    astack = ArrayStack()
    astack.make_data()
    astack = ArrayStack(10)
    astack.make_data()


# Output:


"""
[]
[None, None, None, None, None, None, None, None, None, None]
"""


############################################################################################################################


# C6.18 Show how to use the transfer function, described in Exercise R-6.3, and two temporary stacks, 
# to replace the contents of a given stack S with those same elements, but in reversed order.


class Empty(Exception):
    pass


class Stack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        ans = []
        while not self.is_empty():
            poplist.append(self.pop())
        return poplist


s, s_orig = Stack(), Stack()   # Need Stack from R6-3


for i in range(10):
    s.push(i)
    s_orig.push(i)


def reverse_stack(S):
    s1 = Stack()
    s2 = Stack()
    while not S.is_empty():    
        s1.push(S.pop())
    while not s1.is_empty():   
        s2.push(s1.pop())
    while not s2.is_empty():   
        S.push(s2.pop())


if __name__ == '__main__':         
    reverse_stack(s)
    print('Reversed stack vs. original')
    while not s.is_empty():
        print('N:', s.pop(), '\tO:', s_orig.pop())


# Output:


"""
Reversed stack vs. original
N: 0    O: 9
N: 1    O: 8
N: 2    O: 7
N: 3    O: 6
N: 4    O: 5
N: 5    O: 4
N: 6    O: 3
N: 7    O: 2
N: 8    O: 1
N: 9    O: 0
"""

############################################################################################################################


# C6.19 In Code Fragment 6.5 we assume that opening tags in HTML have form <name>, as with <li>. More 
# generally, HTML allows optional attributes to be expressed as part of an opening tag. The general 
# form used is <name attribute1="value1" attribute2="value2">; for example, a table can be given a 
# border and additional padding by using an opening tag of <table border="3" cellpadding="5">. Modify 
# Code Frag- ment 6.5 so that it can properly match tags, even when an opening tag may include one or 
# more such attributes.


# Option 1: 


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        # Create an empty stack.
        self._data = []                   # nonpublic list instance
    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)
    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0
    def push(self, e):
        # Add element e to the top of the stack.
        self._data.append(e)              # new item stored at end of list
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]             # the last item in the list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()           # remove last item from list


def is_matched_html(raw):
    # Return True if all HTML tags are properly match; False otherwise.
    Stack = ArrayStack()
    j = raw.find('<')                     # find first '<' character (if any)
    print(j)
    while j != -1:                        # -1 means no including target string
        k = raw.find('>', j+1)            # find next '>' character
        print(k)
        if k == -1:                       # -1, as same as above 
            return False                  # invalid tag
        tag = raw[j+1:k]                  # strip away < >: 截取j+1到k-1的切片如html
        print(tag)
        # Equvalence: Add else and indent tag statement 
        """
        else: 
            tag = raw[j+1:k]              # strip away < >
            print(tag)
        """
        if not tag.startswith('/'):       # this is opening tag
            Stack.push(tag)                 
        else:                             # this is closing tag
            if Stack.is_empty():
                return False              # nothing to match with
            # if tag[1:k] != Stack.pop():
            if tag[1:] != Stack.pop():    # if tag[1:]切片不等于Array().pop()弹出的元素
                return False              # mismatched delimiter
        j = raw.find('<', k+1)            # find next '<' character (if any)
        print(j)
    return Stack.is_empty()               # were all opening tags matched?



if __name__ == '__main__':  
    html = """
    <body>
    <center>
    <h1> The Little Boat </h1>
    </center>
    <p> The storm tossed the little
    boat like a cheap sneaker in an
    old washing machine. The three
    drunken fishermen were used to
    such treatment, of course, but
    not the tree salesman, who even as
    a stowaway now felt that he
    had overpaid for the voyage. </p>
    <ol>
    <li> Will the salesman die? </li>
    <li> What color is the boat? </li>
    <li> And what about Naomi? </li>
    </ol>
    </body>
    """
    is_matched_html(html)


# Output:

"""
True
"""
#---------------------------------------------------------------------------------------------------------------------------


# Option 2: 


class Empty(Exception):
    pass


class Full(Exception):
    pass


class ArrayStack():
    def __init__(self, maxlen=None):
        self._data = []
        self._maxlen = maxlen
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        if self._maxlen is not None and len(self) == self._maxlen:
            raise Full('The array is full')
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


def is_matched_html(raw):
    S = ArrayStack()                    # Need ArrayStack() 
    j = raw.find('<')                   # find first '<' character (if any)
    # print(j) 
    while j != -1:                      # j!=-1 means no including target string
        k = raw.find('>', j+1)          # find next '>' character
        # print(k)
        if k == -1:
            return False                # Your tag didn't close
        s = raw.find(' ', j+1)          # find next ' ' space character
        # print(s)
        # tag = raw[j+1: s if 0<=s<k else k]
        if 0 <= s < k:
            tag = raw[j+1: s]           # strip away < space: 截取j+1到s-1(s为空格)之间的切片如p或/center
            # print(tag)
        else: 
            tag = raw[j+1: k]           # strip away < >: 截取j+1到k-1(k为>反括号)的切片如html
            # print(tag)
        if not tag.startswith('/'): 
            S.push(tag)
        else:
            if S.is_empty():
                return False #You closed a tag that has no opening
            if tag[1:k] != S.pop():  #You need to remove the forwardslash from the tag
                return False  
        j = raw.find('<', k+1)  
    return True


# Note the html add: name attribute1="value1" attribute2="value2" into the <p>

if __name__ == '__main__':  
    html = """
    <body>
    <center>
    <h1> The Little Boat </h1>
    </center attr = 'Test'>
    <p name attribute1="value1" attribute2="value2"> The storm tossed the little
    boat like a cheap sneaker in an
    old washing machine. The three
    drunken fishermen were used to
    such treatment, of course, but
    not the tree salesman, who even as
    a stowaway now felt that he
    had overpaid for the voyage. </p>
    <ol>
    <li attribute1="value1" attribute2="value2"> Will the salesman die? </li>
    <li> What color is the boat? </li>
    <li> And what about Naomi? </li>
    </ol>
    </body>
    """
    is_matched_html(html)


# Output:

"""
>>> # print(j) 
5
>>> # print(k)
10
23
32
54
82
135
413
422
471
500
509
539
548
576
586
598
>>> # print(s)
12
25
33
56
68
90
415
424
431
502
510
541
549
578
588
600
>>> # print(tag) if 0 <= s < k: tag = raw[j+1:s]
/center  
p   　　　
li       
>>> # print(tag) else: tag = raw[j+1:k] 
body
center
h1
/h1
/p
ol
/li
li
/li
li
/li
/ol
/body
>>> # Return True (or return S.is_empty())
True
>>> 
"""

############################################################################################################################


# C6.20 Describe a nonrecursive algorithm for enumerating all permutations of the numbers {1, 2,..., n} 
# using an explicit stack.


class Stack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        poplist = []
        while not self.is_empty():
            poplist.append(self.pop())
        return poplist


def find_permutations_stack(n):
    nums = {x for x in range(1, n+1, 1)}
    S = Stack()  # Need Stack from R6-3
    for num in nums:
        S.push(([num], nums-set([num])))
    while not S.is_empty():
        l, remaining = S.pop()
        if len(remaining) == 0:
            print (l)
        else:
            for n in remaining:
                l2 = l.copy()
                l2.append(n)
                S.push((l2, nums-set(l2)))


if __name__ == '__main__':    
    find_permutations_stack(5)

# Output:

"""
[5, 4, 3, 2, 1]
[5, 4, 3, 1, 2]
[5, 4, 2, 3, 1]
[5, 4, 2, 1, 3]
[5, 4, 1, 3, 2]
[5, 4, 1, 2, 3]
...
[1, 3, 2, 4, 5]
[1, 2, 5, 4, 3]
[1, 2, 5, 3, 4]
[1, 2, 4, 5, 3]
[1, 2, 4, 3, 5]
[1, 2, 3, 5, 4]
[1, 2, 3, 4, 5]
"""

############################################################################################################################


# C6.21 Show how to use a stack S and a queue Q to generate all possible subsets of an n-element set T 
# nonrecursively. We solved a similar problem in section 4 (Problem C4-15)


import collections


class Stack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        ans = []
        while not self.is_empty():
            ans.append(self.pop())
        return ans


class Queue():
    def __init__(self):
        self._data = collections.deque()
        self._size = 0
    def __len__(self):
        return self._size
    def first(self):
        return self._data[0]
    def enqueue(self, value):
        self._size += 1
        self._data.append(value)  # Note we append here to add an element to the end of the queue
    def is_empty(self):
        return self._size == 0
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            ans = self._data.popleft()
            self._size -= 1
            return ans


UNK = chr(1000)


def subsets_without_recursion(numbers):
    S = Stack()   # Need Stack from R6-3
    Q = Queue()   # Need Queue from R6-11
    for element in numbers:
        if Q.is_empty():
            Q.enqueue(set([element]))
            Q.enqueue(set([UNK]))
        else:
            # Process all the elements of the Queue
            while not Q.is_empty():
                val = Q.dequeue()
                new_set_1 = val.copy()
                new_set_1.add(element)
                S.push(new_set_1)
                new_set_2 = val.copy()
                new_set_2.add(UNK)
                S.push(new_set_2)
            # Repopulate the Queue for the next element
            while not S.is_empty():
                Q.enqueue(S.pop())
    # Once you are dont the loop, the Queue should be filled with sets
    while not Q.is_empty():
        output = Q.dequeue()
        print('{', str([x for x in output if x != UNK])[1:-1], '}')


if __name__ == '__main__':          
    subsets_without_recursion({1,2,3,4,5})


# Output:

"""
{ 1, 2, 4 }
{ 1, 2, 4, 5 }
{ 1, 2 }
{ 1, 2, 5 }
{ 1, 2, 3, 4 }
{ 1, 2, 3, 4, 5 }
{ 1, 2, 3 }
{ 1, 2, 3, 5 }
{ 1, 4 }
{ 1, 4, 5 }
{ 1 }
{ 1, 5 }
{ 3, 1, 4 }
{ 1, 3, 4, 5 }
{ 3, 1 }
{ 3, 1, 5 }
{ 2, 4 }
{ 2, 4, 5 }
{ 2 }
{ 2, 5 }
{ 3, 2, 4 }
{ 2, 3, 4, 5 }
{ 3, 2 }
{ 3, 2, 5 }
{ 4 }
{ 4, 5 }
{  }
{ 5 }
{ 3, 4 }
{ 3, 4, 5 }
{ 3 }
{ 3, 5 }
"""

############################################################################################################################


# C6.22 Postfix notation is an unambiguous way of writing an arithmetic expression without parentheses. 
# It is defined so that if “(exp 1 ) op (exp 2 )” is a normal, fully parenthesized expression whose 
# operation is op, the postfix version of this is “pexp 1 pexp 2 op”, where pexp 1 is the postfix 
# version of exp 1 and pexp 2 is the postfix version of exp 2 . The postfix version of a single number 
# or variable is just that number or variable. 
# For example, the postfix version of “((5 + 2) ∗ (8 − 3))/4” is “5 2 + 8 3 − ∗ 4 /”. Describe a non-
# recursive way of evaluating an expression in postfix notation.


import operator


class Empty(Exception):
    pass


class AdditionalValues(Exception):
    pass


class Stack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        ans = []
        while not self.is_empty():
            ans.append(self.pop())
        return ans


class prefix_notation_assessment():
    OPERATORS = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 '^': operator.pow,
                 '**': operator.pow}    # Power can be done in two ways
    def __init__(self):
        self._S = Stack()               # Relies on Stack from R6-3
    def _is_empty(self):
        return self._S.is_empty()
    def _pop(self):
        if self._S.is_empty():
            raise Empty('Operator without value')
        else:
            return self._S.pop()
    def _push(self, value):
        self._S.push(value)
    def _evaluate(self, operator):
        pexp2 = self._pop()
        pexp1 = self._pop()
        self._push(self.OPERATORS[operator](pexp1, pexp2)) # Add the result back to the stack
    def __call__(self, operation):
        self._S  = Stack()               # Need to reset the stack for the new operator!
        for item in operation:
            if item in self.OPERATORS:
                self._evaluate(item)
            elif isinstance(item, int) or isinstance(item, float):
                self._push(item)
        # Once you are done, there should only be one value left!
        result = self._pop()
        if self._is_empty(): 
            return result
        else: 
            raise AdditionalValues('Invalid Expression: you have entered more values than the operator processed')


if __name__ == '__main__':           
    pf_assess = prefix_notation_assessment()
    exps = [[5,2,'+',8,3,'-','*',4,'/'],
            [5,2,3,'+',8,3,'-','*',4,'/', '**'],
            # [5,2, 3,'+',8,3,'-','*',4,'/'],
            [5,2,'+',8,3,'-','*',4,'/', '*']        
           ]
    for exp in exps:
        try: 
            print(exp, '=', pf_assess(exp))
        except Exception as e:
            print (exp, 'failed with the following exception:', e)


# Output:

"""
[5, 2, '+', 8, 3, '-', '*', 4, '/'] = 8.75
[5, 2, 3, '+', 8, 3, '-', '*', 4, '/', '**'] = 23364.82470658157
[5, 2, '+', 8, 3, '-', '*', 4, '/', '*'] failed with the following exception: Operator without value
"""

############################################################################################################################


# C6.23 Suppose you have three nonempty stacks R, S, and T . Describe a sequence of operations that 
# results in S storing all elements originally in T below all of S’s original elements, with both 
# sets of those elements in their original order. The final configuration for R should be the same 
# as its original configuration. For example, if R = [1, 2, 3], S = [4, 5], and T = [6, 7, 8, 9], 
# the final configuration should have R = [1, 2, 3] and S = [6, 7, 8, 9, 4, 5].


def transfer_below(R, S, T):
    # We can treat the final stack as the target and the new_elements as an array
    # Step 1: Transfer 
    len_S = 0  #Alternatively,just use len(S) to get the length
    while not S.is_empty():
        R.push(S.pop())
        len_S += 1 
    # Step 2: Transfer T to R.  If we transfer directly to S, it will be reversed
    len_T = 0
    while not T.is_empty():
        R.push(T.pop())
        len_T += 1
    # Step 3: Transfer the values from each stack back to S
    for _ in range(len_T + len_S):
        S.push(R.pop())


def initialize_stacks(R, S, T, r, s, t):
    for i in r:
        R.push(i)
    for i in s:
        S.push(i)
    for i in t:
        T.push(i)


if __name__ == '__main__': 
    R, S, T = Stack(), Stack(), Stack()
    initialize_stacks(R, S, T, [1,2,3], [4,5], [6,7,8,9])
    transfer_below(R, S, T)
    print('Values of R:')
    while not R.is_empty():
        print(R.pop())
    print('Values of S:')
    while not S.is_empty():
        print(S.pop())
    print('Values of T:')
    while not T.is_empty():
        print(T.pop())


# Output:

"""
Values of R:
3
2
1
Values of S:
5
4
9
8
7
6
Values of T:
>>> 
"""

############################################################################################################################


# C6.24 Describe how to implement the stack ADT using a single queue as an instance variable, and 
# only constant additional local memory within the method bodies. What is the running time of the 
# push(), pop(), and top() methods for your design?


class Empty(Exception):
    pass


class StackUsingQueue():
    def __init__(self):
        self._data = Queue()
        self._n = 0  #number of elements
    def is_empty(self):
        return self._data.is_empty()
    def pop(self):
        if self.is_empty():
            raise Empty('Cannot pop from an empty stack')           
        ans = self._data.dequeue()
        self._n -= 1
        return ans
    def push(self, value):
        self._data.enqueue(value)
        self._n += 1
        for _ in range(self._n - 1):  #note that if n == 1, this does not happen
            self._data.enqueue(self._data.dequeue())
    def top(self):
        return self._data.first()
    def __len__(self):
        return self._n
    

if __name__ == '__main__':
    s = StackUsingQueue()
    for i in range(10):
        s.push(i)
    while not s.is_empty():
        print(s.top(), s.pop())

    
# Output: 

"""
9 9
8 8
7 7
6 6
5 5
4 4
3 3
2 2
1 1
0 0
"""

############################################################################################################################

# C6.25 Describe how to implement the queue ADT using two stacks as instance variables such that 
# all queue operations execute in amortized O(1) time. Give a formal proof of the amortized bound.


class Empty(Exception):
    pass


class QueueUsingStacks():
    def __init__(self):
        self._Dstack, self._nd = Stack(), 0   # Dequeuing Stack and num_elements
        self._Estack, self._ne = Stack(), 0   # Enqueuing Stack and num_elements 
    def is_empty(self):
        return (self._nd + self._ne) == 0
    def enqueue(self, value):
        self._Estack.push(value)
        self._ne += 1
    def _stack_transfer(self):
        while self._ne >0:
            self._Dstack.push(self._Estack.pop())
            self._ne -= 1
            self._nd += 1
    def dequeue(self):
        # If the dequeue stack is empty, pop all values over from the enqueue stack
        if self._nd == 0:
            if self._ne == 0: raise Empty('Your Queue is empty!')
            self._stack_transfer()  
        # Once the Dequeue stack has been repopulated, pop the top value
        poplist = self._Dstack.pop()
        self._nd -= 1
        return poplist
    def first(self):
        if self._nd == 0:
            if self._ne == 0: raise Empty('Your Queue is empty!')
            self._stack_transfer()
        return self._Dstack.top()


if __name__ == '__main__':   
    Q = QueueUsingStacks()
    for i in range(10):
        Q.enqueue(i)
    while not Q.is_empty():
        print(Q.first(), Q.dequeue())


# Output:

"""
0 0
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
"""
   
############################################################################################################################


# C6.26 Describe how to implement the double-ended queue ADT using two stacks as instance variables. 
# What are the running times of the methods?


class Empty(Exception):
    pass


class DequeUsingStacks():
    def __init__(self):
        self._Dstack, self._nd = Stack(), 0   # Dequeuing Stack and num_elements
        self._Estack, self._ne = Stack(), 0   # Enqueuing Stack and num_elements
    def is_empty(self):
        return (self._nd + self._ne) == 0
    def append(self, value):
        self._Estack.push(value)
        self._ne += 1
    def appendleft(self, value):
        self._Dstack.push(value)
        self._nd += 1
    def _stack_transfer(self, reverse = False):
        if reverse == False:
            while self._ne >0:
                self._Dstack.push(self._Estack.pop())
                self._ne -= 1
                self._nd += 1
        else:
            while self._nd >0:
                self._Estack.push(self._Dstack.pop())
                self._nd -= 1
                self._ne += 1
    def popleft(self):
        # If the dequeue stack is empty, pop all values over from the enqueue stack
        if self._nd == 0:
            print('Performing a transfer')
            if self._ne == 0: raise Empty('Your Queue is empty!')
            self._stack_transfer()  
        # Once the Dequeue stack has been repopulated, pop the top value
        ans = self._Dstack.pop()
        self._nd -= 1
        return ans
    def pop(self):
        # If the enqueue stack is empty, pop all values over from the dequeue stack
        if self._ne == 0:
            if self._nd == 0: raise Empty('Your Queue is empty!')
            self._stack_transfer(reverse = True)  
        # Once the Dequeue stack has been repopulated, pop the top value
        poplist = self._Estack.pop()
        self._ne -= 1
        return poplist
    def first(self):
        if self._nd == 0:
            if self._ne == 0: raise Empty('No first, Your Queue is empty!')
            self._stack_transfer()
        return self._Dstack.top()


if __name__ == '__main__':   
    Q = DequeUsingStacks()
    for i in range(100):
        Q.append(i)
    print(Q._Estack._data, Q._ne, Q._nd)    
    while not Q.is_empty():
        try: 
            print('Popleft:', Q.popleft())
            print('Pop:    ', Q.pop())
        except Empty as e:
            print(e)


# Output:

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 
 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99] 
100 0
Performing a transfer
Popleft: 0
Pop:     99
Performing a transfer
Popleft: 1
Pop:     98
Performing a transfer
Popleft: 2
Pop:     97
...
Performing a transfer
Popleft: 47
Pop:     52
Performing a transfer
Popleft: 48
Pop:     51
Performing a transfer
Popleft: 49
Pop:     50
"""

############################################################################################################################


# C6.27 Suppose you have a stack S containing n elements and a queue Q that is initially empty. Describe 
# how you can use Q to scan S to see if it contains a certain element x, with the additional constraint 
# that your algorithm must return the elements back to S in their original order. You may only use S, Q, 
# and a constant number of other variables.


class Queue():
    def __init__(self):
        self._data = collections.deque()
        self._size = 0
    def __len__(self):
        return self._size
    def first(self):
        return self._data[0]
    def enqueue(self, value):
        self._size += 1
        self._data.append(value)  #Note we append here to add an element to the end of the queue
    def is_empty(self):
        return self._size == 0
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            ans = self._data.popleft()
            self._size -= 1
            return ans


class Stack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, value):
        self._data.append(value)
    def top(self):
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('List is empty')
        return self._data.pop()
    def full_pop(self):
        ans = []
        while not self.is_empty():
            ans.append(self.pop())
        return ans


def find_element(S, element):
    found = False
    Q = Queue()
    for _ in range(2):
        while not S.is_empty():
            value = S.pop()
            if value == element: 
                found = True  
            Q.enqueue(value)
        while not Q.is_empty():
            S.push(Q.dequeue())    
    return found


if __name__ == '__main__': 
    S = Stack()
    for i in range(10):
        S.push(i)
    for val in [2,3,5,6,10, 14, 55]:
        print (f'Val {val} in the stack: {find_element(S, val)}')
    print('\nTo test that the stack is still in order:')
    while not S.is_empty():
        print (S.pop())
        

# Output:

"""
To test that the stack is still in order:
9
8
7
6
5
4
3
2
1
0
"""

############################################################################################################################


# C6.28 Modify the ArrayQueue implementation so that the queue’s capacity is limited to maxlen elements, 
# where maxlen is an optional parameter to the constructor (that defaults to None). If enqueue is called 
# when the queue is at full capacity, throw a Full exception (defined similarly to Empty).


class Empty(Exception): 
    pass


class Full(Exception): 
    pass


class CappedArrayQueue():
    DEFAULT_CAPACITY = 10
    def __init__(self, maxlen = 100):
        self._data = [None]*self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._maxlen = maxlen
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty(): 
            raise Empty('The queue is empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty(): 
            raise Empty('The queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  #Help with GC
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return answer
    def enqueue(self, value):
        if self._size == self._maxlen: 
            raise Full(f"The Queue has reached it's maximum length of {self._maxlen}")
        if self._size == len(self._data): 
            self._resize(min(self._size * 2, self._maxlen)) # don't make it bigger than the maxlen
        self._data[(self._front + self._size) % len(self._data)] = value
        self._size += 1
    def _resize(self, capacity):
        new_array = [None] * capacity
        for i in range(self._size):
            new_array[i] = self._data[(self._front + i) % len(self._data)]
        self._data = new_array
        self._front = 0


if __name__ == '__main__':    
    CAQ = CappedArrayQueue(50)
    print('Enqueue order')
    for i in range(60):
        try:
            CAQ.enqueue(i)
            print(i, end = ',')
        except Full as e:
            print(e)
    print('Dequeue order')
    while not CAQ.is_empty():
        print(CAQ.dequeue(), end = ', ')


# Output:

"""
Enqueue order
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,
36,37,38,39,40,41,42,43,44,45,46,47,48,49,The Queue has reached it's maximum length of 50
The Queue has reached it's maximum length of 50
The Queue has reached it's maximum length of 50
The Queue has reached it's maximum length of 50
The Queue has reached it's maximum length of 50
The Queue has reached it's maximum length of 50
The Queue has reached it's maximum length of 50
The Queue has reached it's maximum length of 50
The Queue has reached it's maximum length of 50
The Queue has reached it's maximum length of 50
Dequeue order
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, >>>
"""

############################################################################################################################


# C6.29 In certain applications of the queue ADT, it is common to repeatedly dequeue an element, process 
# it in some way, and then immediately enqueue the same element. Modify the ArrayQueue implementation to 
# include a rotate() method that has semantics identical to the combination, Q.enqueue(Q.dequeue( )). 
# However, your implementation should be more efficient than making two separate calls (for example, 
# because there is no need to modify._size).


class Empty(Exception): 
    pass


class Full(Exception): 
    pass


class ArrayQueueRotate():
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None]*self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty(): raise Empty('The queue is empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty(): raise Empty('The queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  #Help with GC
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return answer
    def enqueue(self, value):
        if self._size == len(self._data): self._resize(self._size * 2)
        self._data[(self._front + self._size)%len(self._data)] = value
        self._size += 1
    def _resize(self, capacity):
        new_array = [None]*capacity
        for i in range(self._size):
            new_array[i] = self._data[(self._front + i)%len(self._data)]
        self._data = new_array
        self._front = 0
    def rotate(self):
        if self.is_empty(): 
            raise Empty('The array is empty')
        self._data[(self._front + self._size)%len(self._data)] = self._data[self._front]
        self._front = (self._front + 1)%len(self._data)


if __name__ == '__main__':   
    AQR = ArrayQueueRotate()
    for i in range(100):
        AQR.enqueue(i)
    for i in range(300):
        print(AQR.first(), end = ', ')
        AQR.rotate()


# Output:

"""
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, >>> 
"""

############################################################################################################################


# C6.30 Alice has two queues, Q and R, which can store integers. Bob gives Alice 50 odd integers and 
# 50 even integers and insists that she store all 100 integers in Q and R. They then play a game where 
# Bob picks Q or Rat random and then applies the round-robin scheduler, described in the chapter, to 
# the chosen queue a random number of times. If the last number to be processed at the end of this game 
# was odd, Bob wins. Otherwise, Alice wins. How can Alice allocate integers to queues to optimize her 
# chances of winning? What is her chance of winning?


# Option 1: 


import random
from random import randint
import collections


# Code Fragment 6.6: Definition for an Empty exception class.
class Empty(Exception):
    pass


# Code Fragment 6.2: Implementing a stack using a Python list as storage.
class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10                      # moderate capacity for all new queues
    def __init__(self):
        # Create an empty queue.
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY # _data: list instance
        self._size = 0  # number of the elements stored in the queue
        self._front = 0 # index of the first element of self._data instance queue
    def __len__(self):
        # Return the number of elements in the queue.
        return self._size
    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0
    def do_first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    def enqueue(self, element):
        # Add an element to the back of queue.
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1        
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]       # self_data: list instance
        self._data[self._front] = None         # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer
    def _resize(self, cap):                    # we assume cap >= len(self)
        # Resize to a new list of capacity >= len(self).
        old = self._data                       # keep track of existing list
        self._data = [None] * cap              # allocate list with new capacity
        walk = self._front
        for k in range(self._size):            # only consider existing elements
            self._data[k] = old[walk]          # intentionally shift indices
            # What is the meanding 1 + walk, walk is self._front? 
            # It take the seond element as the first element 
            walk = (1 + walk) % len(old)       # use old size as modulus
        self._front = 0                        # front has been realigned
    def rotate(self):
        if self.is_empty():
            raise Empty('The array is empty')
        self._data[(self._front + self._size) % len(self._data)] = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)


def play_game(Q, R, num_turns=100, max_rotations=20):
    for i in range(num_turns):
        # carray = Q if random.random() > 0.5 else R
        if random.random() >= 0.5:
            carray = Q
        else:
            carray = R
        for j in range(random.randint(0, max_rotations)):
            final_value = carray.do_first()
            carray.rotate()
    return final_value % 2 == 0



def main(): 
    Q, R = ArrayQueue(), ArrayQueue()
    Q.enqueue(0)
    for i in range(1, 100): 
        R.enqueue(i)
    total_wins = 0
    num_games = 10000
    for game in range(num_games):
        if play_game(Q, R):
            total_wins += 1
    print(f'Alice won {total_wins / num_games * 100}% of her games')


if __name__ == '__main__':
    main()

# Output:

"""
Alice won 74.65% of her games
"""

#---------------------------------------------------------------------------------------------------------------------------

# Option 2: 


def play_game(Q, R, num_turns=100, max_rotations=20):
    for i in range(num_turns):
        # carray = Q if random.random() > 0.5 else R
        if random.random() == 0.5:
            carray = Q
        else:
            carray = R
        for j in range(random.randint(0, max_rotations)):
            final_value = carray.do_first()
            carray.rotate()
    return final_value % 2 == 0


# Output:

"""
Alice won 49.25% of her games
"""

#---------------------------------------------------------------------------------------------------------------------------


# Option 3: 

def play_game(Q, R, num_turns=100, max_rotations=20):
    for i in range(num_turns):
        # carray = Q if random.random() > 0.5 else R
        if random.random() < 0.5:
            carray = Q
        else:
            carray = R
        for j in range(random.randint(0, max_rotations)):
            final_value = carray.do_first()
            carray.rotate()
    return final_value % 2 == 0


# Output:

"""
Alice won 73.9% of her games
"""

############################################################################################################################


# C6.31 Suppose Bob has four cows that he wants to take across a bridge, but only one yoke, which can 
# hold up to two cows, side by side, tied to the yoke. The yoke is too heavy for him to carry across 
# the bridge, but he can tie (and untie) cows to it in no time at all. Of his four cows, Mazie can 
# cross the bridge in 2 minutes, Daisy can cross it in 4 minutes, Crazy can cross it in 10 minutes, 
# and Lazy can cross it in 20 minutes. Of course, when two cows are tied to the yoke, they must go at 
# the speed of the slower cow. Describe how Bob can get all his cows across the bridge in 34 minutes.


# Omit 


############################################################################################################################
############################################################################################################################


# Part Three Projects

############################################################################################################################


# P6.32 Give a complete ArrayDeque implementation of the double-ended queue ADT as sketched in Section 
# 6.3.2


class Empty(Exception): 
    pass


class ArrayDeque():
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0
    def is_empty(self):
        return self._size == 0
    def __len__(self):
        return self._size
    def first(self):
        if self.is_empty(): 
            raise Empty('Deque is empty')
        return self._data[self._front]
    def last(self):
        if self.is_empty(): 
            raise Empty('Deque is empty')
        return self._data[(self._front + self._size-1) % len(self._data)]
    def add_first(self, value):
        if self._size == len(self._data): 
            self._resize(self._size *2)
        self._data[(self._front-1) % len(self._data)] = value
        self._front = (self._front - 1) % len(self._data)
        self._size += 1
    def remove_first(self):
        if self.is_empty(): 
            raise Empty('Deque is empty')
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return ans
    def add_last(self, value):
        if self._size == len(self._data): 
            self._resize(self._size*2)
        self._data[(self._front+self._size) % len(self._data)] = value
        self._size += 1
    def remove_last(self):
        if self.is_empty(): 
            raise Empty('Deque is empty')
        ans = self._data[(self._front+ self._size-1) % len(self._data)]
        self._data[(self._front+ self._size) % len(self._data)] = None
        self._size -= 1
        return ans
    def _resize(self, capacity):
        old = self._data
        self._data = [None]*capacity
        for i in range(len(old)):
            self._data[i] = old[(self._front+i) % len(old)]
        self._front = 0


if __name__ == '__main__': 
    DEQ = ArrayDeque()
    print('Adding last')
    for i in range(10):
        DEQ.add_last(i)
        print (i, DEQ._data)
    print ('Adding first')
    for i in range(20, 10, -1):
        DEQ.add_first(i)
        print (i, DEQ._data)
    print('Performing the removals')
    while not DEQ.is_empty():
        print('Remove first', DEQ.first(), DEQ.remove_first(), 'Remove last', DEQ.last(), DEQ.remove_last())


############################################################################################################################


# P6.33 Give an array-based implementation of a dqueue supporting all of the public behaviors shown 
# in Table 6.4 for the collections.deque class, including use of the maxlen optional parameter. When 
# a length-limited deque is full, provide semantics similar to the collections.deque class, whereby 
# a call to insert an element on one end of a deque causes an element to be lost from the opposite side.


class Empty(Exception): 
    pass


class ArrayDequeMaxlen():
    DEFAULT_CAPACITY = 10
    def __init__(self, maxlen = None):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0
        self._maxlen = maxlen
    def is_empty(self):
        return self._size == 0
    def __len__(self):
        return self._size
    def __getitem__(self, index):
        if index < 0: 
            index = self._size + index   # Negative indices
        if not 0 <= index < self._size: 
            raise IndexError('Invalid index')
        return (self._data[(self._front + index) % len(self._data)])
    def __setitem__(self, index, value):
        if index < 0: 
            index = self._size + index   # Negative indices
        if not 0 <= index < self._size: 
            raise IndexError('Invalid index')
        self._data[(self._front + index) % len(self._data)] = value
    def appendleft(self, value):       
        if self._size == len(self._data): 
            self._resize(self._size *2)
        self._data[(self._front-1) % len(self._data)] = value
        self._front = (self._front - 1) % len(self._data)
        self._size = self._size + 1 if self._maxlen is None else min(self._size+1, self._maxlen)
    def popleft(self):
        if self.is_empty(): 
            raise Empty('Deque is empty')
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return ans
    def rotate(self, k):
        for _ in range(k):
            ans = self.pop()
            self.appendleft(ans)
    def append(self, value):
        if self._size == len(self._data): self._resize(self._size * 2)
        self._data[(self._front + self._size) % len(self._data)] = value
        if self._maxlen is not None and self._size == self._maxlen: 
            self._front += 1  # If you were at maxlen, you overwrote the previous first
        else:  self._size = self._size + 1
    def pop(self):
        if self.is_empty(): 
            raise Empty('Deque is empty')
        ans = self._data[(self._front+ self._size-1) % len(self._data)]
        self._data[(self._front + self._size - 1) % len(self._data)] = None
        self._size -= 1
        return ans
    def _resize(self, capacity):
        if self._maxlen is not None: 
            capacity = min (capacity, self._maxlen)
        old = self._data
        self._data = [None] * capacity
        for i in range(len(old)):
            self._data[i] = old[(self._front+i) % len(old)]
        self._front = 0
    def clear(self):
        self._data = [None] * len(self._data)
        self._size = 0
        self._front = 0
    def remove(self, value):
        if self.is_empty(): 
            raise Empty('Deque is empty')
        found  = False
        for i in range(self._size):
            ans = self.pop()
            if ans == value and not found:
                found = True              # Do not remove subsequent finds
            else: 
                self.appendleft(ans)
    def count(self, value):
        if self.is_empty(): 
            raise Empty('Deque is empty')
        total_count = 0
        for i in range(self._size):
            ans = self.pop()
            if ans == value: 
                total_count+= 1
            self.appendleft(ans)
        return total_count
        
                
if __name__ == '__main__': 
    AQM = ArrayDequeMaxlen(20)
    print('Adding last')
    for i in range(100):
        AQM.append(i)
        print(i, AQM._data)
    print('\nDelete 80', AQM.remove(80), AQM._data, AQM._front)
    AQM.clear()
    print('\nCleared Data:', AQM._data)
    for i in range(100):
        AQM.append(i%3)
    print('\nFound', AQM.count(2), '2s in ', AQM._data)    
    print('\nAdding first')
    for i in range(20, 10, -1):
        AQM.appendleft(i)
        print(i, AQM._data)
    print(AQM._front)
    print('\nRotating')    
    for i in range(20):
        AQM.rotate(1)
        print('Front is:', AQM[0])
    print('\nPerforming the removals')
    while not AQM.is_empty():
        print('Remove first', AQM[0], AQM.popleft(), 'Remove last', AQM[-1], AQM.pop())

############################################################################################################################


# P6.35 The introduction of Section 6.1 notes that stacks are often used to provide “undo” support in 
# applications like a Web browser or text editor. While support for undo can be implemented with an 
# unbounded stack, many applications provide only limited support for such an undo history, with a 
# fixed-capacity stack. When push is invoked with the stack at full capacity, rather than throwing 
# a Full exception (as described in Exercise C-6.16), a more typical semantic is to accept the pushed 
# element at the top while “leaking” the oldest element from the bottom of the stack to make room. 
# Give an implementation of such a LeakyStack abstraction, using a circular array with appropriate 
# storage capacity. This class should have a public interface similar to the bounded-capacity stack 
# in Exercise C-6.16, but with the desired leaky semantics when full.


class Empty(Exception): 
    pass


class LeakyStack():
    def __init__(self, capacity = 20):
        self._data = [None]*capacity
        self._capacity = capacity
        self._front = 0
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def push(self, value):
        self._data[(self._front + self._size)%len(self._data)] = value
        if self._size == self._capacity: self._front += 1
        else: self._size += 1
    def pop(self):
        if self.is_empty(): raise Empty('Stack is empty')
        ans = self._data[(self._front + self._size -1)%len(self._data)]
        self._data[(self._front + self._size -1)%len(self._data)] = None
        self._size -= 1
        return ans


if __name__ == '__main__': 
    undo = LeakyStack(30)
    for i in range(100):
        undo.push(i)
    print ('Leakiness check')
    while not undo.is_empty():
        print(undo.pop())


# Output:

"""
Leakiness check
99
98
97
96
95
94
93
92
91
90
89
88
87
86
85
84
83
82
81
80
79
78
77
76
75
74
73
72
71
70
"""

############################################################################################################################


# P6.35 When a share of common stock of some company is sold, the capital gain (or, sometimes, loss) is 
# the difference between the share’s selling price and the price originally paid to buy it. This rule is 
# easy to understand for a single share, but if we sell multiple shares of stock bought over a long 
# period of time, then we must identify the shares actually being sold. A standard accounting principle 
# for identifying which shares of a stock were sold in such a case is to use a FIFO protocol—the shares 
# sold are the ones that have been held the longest (indeed, this is the default method built into several 
# personal finance software packages). For example, suppose we buy 100 shares at $20 each on day 1, 20 
# shares at $24 on day 2, 200 shares at $36 on day 3, and then sell 150 shares on day 4 at $30 each. Then 
# applying the FIFO protocol means that of the 150 shares sold, 100 were bought on day 1, 20 were bought 
# on day 2, and 30 were bought on day 3. The capital gain in this case would therefore be100 · 10 + 20 · 6 
# + 30 · (−6), or $940. Write a program that takes as input a sequence of transactions of the form “buy x 
# share(s) at y each” or “sell x share(s) at y each,” assuming that the transactions occur on consecutive 
# days and the values x and y are integers. Given this input sequence, the output should be the total 
# capital gain (or loss) for the entire sequence, using the FIFO protocol to identify shares.


class Empty(Exception): 
    pass


class Full(Exception): 
    pass


class ArrayQueueRotate():
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None]*self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty(): 
            raise Empty('The queue is empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty(): 
            raise Empty('The queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  #Help with GC
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    def enqueue(self, value):
        if self._size == len(self._data): self._resize(self._size * 2)
        self._data[(self._front + self._size) % len(self._data)] = value
        self._size += 1
    def _resize(self, capacity):
        new_array = [None] * capacity
        for i in range(self._size):
            new_array[i] = self._data[(self._front + i) % len(self._data)]
        self._data = new_array
        self._front = 0
    def rotate(self):
        if self.is_empty(): 
            raise Empty('The array is empty')
        self._data[(self._front + self._size) % len(self._data)] = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)


class CapitalGainCalculator():
    def __init__(self):
        self.Q = ArrayQueueRotate()  #From exercise C6-29
        self._shares = 0
    def __call__(self, message):
        """
        Note, if we split by ' ', 
        we can assume that the message is always in the following order:
        message[0] = Buy or Sell
        message[1] = Number
        message[4] = Price
        """
        message = message.split(' ')
        if message[0].lower() == 'buy': 
            f = self.buy_shares
        elif message[0].lower() == 'sell': 
            f = self.sell_shares
        else: 
            print(f'First command was not buy/sell.  Received: {message[0]}')
            return False
        try: 
            number = int(message[1])  #shares can only be ints for this problem
        except:
            print(f'Second command should be an integer.  Recieved: {message[1]}')
            return False
        try:
            preprice = message[4]
            if preprice.startswith('$'): 
                preprice = preprice[1:]
            price = float(preprice)
        except:
            print(f'Fourth command should be a price.  Recieved: {message[4]}')
            return False
        return f(number, price)
    def _partial_sale(self, block):
        # Note we assume that you've checked whether this is a valid operation
        self.Q._data[self.Q._front] = block
    def sell_shares(self, sell_num, sell_price):
        print(f'Attempting to sell {sell_num} shares at ${sell_price}')
        total_capital_gain = 0
        number = sell_num
        if number > self._shares:
            print(f'You only have {self._shares} to sell')
            return 0   # Should you do a partial sale????
        while number > 0:
            buy_num, buy_price = self.Q.first()
            if buy_num < number:  #You can sell the entire block
                self.Q.dequeue()
                num_sold = buy_num
            else:
                num_sold = number
                self._partial_sale((buy_num-number, buy_price))
            total_capital_gain += (sell_price - buy_price) * num_sold
            number -= num_sold
        print('\t', f'Your capital gains on that transaction were ${total_capital_gain}')
        self._shares -= sell_num
        return total_capital_gain
    def buy_shares(self, buy_num, buy_price):
        print(f"Attempting to buy {buy_num} shares at ${buy_price}")
        self.Q.enqueue((buy_num, buy_price))
        self._shares += buy_num
        return True


if __name__ == '__main__': 
    SB = CapitalGainCalculator()   # SB is for sharebot
    seq = [('buy 200 shares at 20 each'),
           ('buy 200 shares at $15 each'),
           ('sell 100 shares at 100 each'),
           ('sell 200 shares at 10 each'),
           ('sell 100 shares at 10 each'),
           ('smell 100 shares at 10 each'),
           ('sell 100.5 shares at 10 each'),
           ('sell 100 shares at $10$ each'),
          ]
    for transaction in seq:
        SB(transaction)


# Output:

"""
Attempting to buy 200 shares at $20.0
True
Attempting to buy 200 shares at $15.0
True
Attempting to sell 100 shares at $100.0
     Your capital gains on that transaction were $8000.0
8000.0
Attempting to sell 200 shares at $10.0
     Your capital gains on that transaction were $-1500.0
-1500.0
Attempting to sell 100 shares at $10.0
     Your capital gains on that transaction were $-500.0
-500.0
First command was not buy/sell.  Received: smell
False
Second command should be an integer.  Recieved: 100.5
False
Fourth command should be a price.  Recieved: $10$
False
"""

############################################################################################################################


# P6.37 Design an ADT for a two-color, double-stack ADT that consists of two stacks—one “red” and one 
# “blue”—and has as its operations color-coded versions of the regular stack ADT operations. For example, 
# this ADT should support both a red push operation and a blue push operation. Give an efficient 
# implementation of this ADT using a single array whose capacity is set at some value N that is assumed 
# to always be larger than the sizes of the red and blue stacks combined.


class Empty(Exception): 
    pass


class ArrayDoubleStack():
    DEFAULT_CAPACITY = 20
    GROW_RATE = 2
    def __init__(self):
        self._sizer = 0
        self._sizeb = 0
        self._data = [None] * self.DEFAULT_CAPACITY
        self._rfront = 0
        self._bfront = self.DEFAULT_CAPACITY // 2
    def is_empty_blue(self):
        return self._sizeb == 0
    def is_empty_red(self):
        return self._sizer == 0    
    def is_full(self):
        return (self._sizer + self._sizeb) == len(self._data)
    def push_red(self, value):
        idx = (self._rfront + self._sizer) % len(self._data)
        if self.is_full() or idx == self._bfront: 
            self._resize(len(self._data)*self.GROW_RATE)
        new_idx = (self._rfront + self._sizer) % len(self._data)
        self._data[new_idx] = value
        self._sizer += 1
    def push_blue(self, value):
        idx = (self._bfront + self._sizeb) % len(self._data)
        if self.is_full() or idx == self._rfront: 
            self._resize(len(self._data)*self.GROW_RATE)
        new_idx = (self._bfront + self._sizeb) % len(self._data)
        self._data[new_idx] = value
        self._sizeb += 1
    def _pop(self, front, size):
        ans = self._data[(front + size-1) % len(self._data)]
        self._data[(front + size-1) % len(self._data)] = None
        return ans
    def pop_red(self):
        if self.is_empty_red(): 
            raise Empty('Red is empty')
        ans = self._pop(self._rfront, self._sizer)
        self._sizer -= 1
        return ans
    def pop_blue(self):
        if self.is_empty_bue(): 
            raise Empty('Blue is empty')
        ans = self._pop(value, self._bfront, self._sizeb)
        self._sizeb -= 1
        return ans
    def _resize (self, capacity):
        # Note, red walks, then blue takes half of the remaining space
        new_array = [None]*capacity
        for i in range(self._sizer):
            new_array[i] = self._data[(self._rfront + i)%len(self._data)]    
        new_frontb = self._sizer + (capacity-self._sizer - self._sizeb) // 2
        for i in range(self._sizeb):
            new_array[i + new_frontb] = self._data[(self._bfront+i) % len(self._data)]
        self._rfront = 0
        self._bfront = new_frontb
        self._data = new_array


if __name__ == '__main__': 
    dA = ArrayDoubleStack()
    for i in range(11):
        dA.push_blue(i)
        dA.push_red(100+i)
        print(dA._data, dA._sizer, dA._sizeb, '\n')
    while not dA.is_empty_red():
        print(dA.pop_red())