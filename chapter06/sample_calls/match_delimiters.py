

# match_delimiters.py

"""

# dis module
# import dis
# dis.dis(function or class)
# dis.show_code(function)

1st column：code line ordere行号; 
2nd column: current command，表示为 --> ;
3rd column: a tokenized command such as >>; 
4th column：address of cpommand 指令的地址;
5th column: opname;
6th column: operation parameters；
7th column: explaination of parameter

(1)|(2)|(3)|(4)|          (5)         |(6)|  (7)
---|---|---|---|----------------------|---|-------
  2|   |   |  0|LOAD_FAST             |  0|(num)
   |-->|   |  2|LOAD_CONST            |  1|(42)
   |   |   |  4|COMPARE_OP            |  2|(==)
   |   |   |  6|POP_JUMP_IF_FALSE     | 12|
   |   |   |   |                      |   |
  3|   |   |  8|LOAD_CONST            |  2|(True)
   |   |   | 10|RETURN_VALUE          |   |
   |   |   |   |                      |   |
  4|   |>> | 12|LOAD_CONST            |  3|(False)
   |   |   | 14|RETURN_VALUE          |   |

"""


# Option 1:


import dis 


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


def is_matched(expr):
    # Return True if all delimiters are properly match; False otherwise.
    lefty = '({['                               # opening delimiters
    righty = ')}]'                              # respective closing delims
    Stack = ArrayStack()                        # S is array stack 
    for char in expr:                           # expr is variable
        if char in lefty:
            Stack.push(char)                    # push left delimiter on stack
        elif char in righty:
            if Stack.is_empty():
                return False                    # nothing to match with
            if righty.index(char) != lefty.index(Stack.pop()):
                return False                    # mismatched
    return Stack.is_empty()                     # were all symbols matched?


if __name__ == '__main__': 
    expr_list = ['[(5+x)-(y+z)]', '(5+x))*y', '{[1+(x+y)]}*[(3*z)]']
    for expr in expr_list:
        Flag = is_matched(expr)
        print('%s is matched: %s' %(expr, Flag))


# Omit the result
dis.dis(is_matched)


# Output:

"""
... 
[(5+x)-(y+z)] is matched: True
(5+x))*y is matched: False
{[1+(x+y)]}*[(3*z)] is matched: True
>>> 
"""

#------------------------------------------------------------------------------------------------------------


# Option 2: Implement the Match class 
# Left delimiter： ({[
# Right delimiter: )}]


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


class Match:
    def __init__(self):
        pass
    def is_matched(self, expr):
        # Return True if all delimiters are properly match; False otherwise.
        lefty = '({['                         # opening delimiters
        righty = ')}]'                        # respective closing delims
        Stack = ArrayStack()
        # print(S)
        for char in expr:
            if char in lefty:
                Stack.push(char)              # push left delimiter on stack
                # print(S)
            elif char in righty:
                if Stack.is_empty():
                    return False              # nothing to match with
                if righty.index(char) != lefty.index(Stack.pop()):
                    return False              # mismatched
        return Stack.is_empty()               # were all symbols matched?


if __name__ == '__main__': 
    ma = Match()
    expr_list = ['[(5+x)-(y+z)]', '(5+x))*y', '{[1+(x+y)]}*[(3*z)]']
    for expr in expr_list:
        Flag = ma.is_matched(expr)
        print('%s is matched: %s' %(expr, Flag))


# Output:


"""
[(5+x)-(y+z)] is matched: True
(5+x))*y is matched: False
{[1+(x+y)]}*[(3*z)] is matched: True
"""

#------------------------------------------------------------------------------------------------------------


# Option 3: 


import dis


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
    def is_matched(self, expr):
        # Return True if all delimiters are properly match; False otherwise.
        lefty = '({['                         # opening delimiters
        righty = ')}]'                        # respective closing delims
        Stack = ArrayStack()
        # print(S)
        for char in expr:
            if char in lefty:
                Stack.push(char)              # push left delimiter on stack
                # print(S)
            elif char in righty:
                if Stack.is_empty():
                    return False              # nothing to match with
                if righty.index(char) != lefty.index(Stack.pop()):
                    return False              # mismatched
        return Stack.is_empty()               # were all symbols matched?


if __name__ == '__main__': 
    arst =  ArrayStack()
    expr_list = ['[(5+x)-(y+z)]', '(5+x))*y', '{[1+(x+y)]}*[(3*z)]']
    for expr in expr_list:
        Flag = arst.is_matched(expr)
        print('%s is matched: %s' %(expr, Flag))



# Omit the dis result 
dis.dis(ArrayStack.top)
dis.show_code(ArrayStack.top)
dis.dis(ArrayStack.is_matched)
dis.show_code(ArrayStack.is_matched)


# Output:

"""
[(5+x)-(y+z)] is matched: True
(5+x))*y is matched: False
{[1+(x+y)]}*[(3*z)] is matched: True

"""

#------------------------------------------------------------------------------------------------------------


# Option 4: 

# lefty = '{[('                               
# righty = '}])'                              


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


def is_matched(expr):
    # Return True if all delimiters are properly match; False otherwise.
    lefty = '{[('                               # opening delimiters
    righty = '}])'                              # respective closing delims
    S = ArrayStack()                            # S is array stack 
    for c in expr:                              # expr is variable
        if c in lefty:
            S.push(c)                           # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False                    # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
            # if lefty.index(S.pop()) != righty.index(c):
                return False                    # mismatched
    return S.is_empty()                         # were all symbols matched?



if __name__ == '__main__': 
    expr_list = ['[(5+x)-(y+z)]', '(5+x))*y', '{[1+(x+y)]}*[(3*z)]']
    for expr in expr_list:
        Flag = is_matched(expr)
        print('%s is matched: %s' %(expr, Flag))


# Output:


"""
[(5+x)-(y+z)] is matched: True
(5+x))*y is matched: False
{[1+(x+y)]}*[(3*z)] is matched: True
"""