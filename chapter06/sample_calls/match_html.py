

# match_html.py


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
    while j != -1:
        k = raw.find('>', j+1)            # find next '>' character
        if k == -1:
            return False                  # invalid tag
        # Equvalence: Add else and indent tag statement 
        else: 
            tag = raw[j+1:k]              # strip away < >
        if not tag.startswith('/'):       # this is opening tag
            Stack.push(tag)                 
        else:                             # this is closing tag
            if Stack.is_empty():
                return False              # nothing to match with
            if tag[1:] != Stack.pop():   
                return False              # mismatched delimiter
        j = raw.find('<', k+1)            # find next '<' character (if any)
    return Stack.is_empty()               # were all opening tags matched?


if __name__ == '__main__':
    # Test whether a html text mathc label function
    html_content = '''
    <html>
    <head>
    <title>My first HTML page</title>
    </head>
    <body>
    <p>body Most of the elements will be seen in the browser.</p>
    <p>title Some of the elements will been seen in the title.</p>
    </body>
    </html>
    '''
    print(is_matched_html(html_content))


# Output:

"""
True
"""

#--------------------------------------------------------------------------------------------------


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
    while j != -1:                        # -1 means no inlcuding target string
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
    # Test whether a html text mathc label function
    html_content = '''
    <html>
    <head>
    <title>My first HTML page</title>
    </head>
    <body>
    <p>body Most of the elements will be seen in the browser.</p>
    <p>title Some of the elements will been seen in the title.</p>
    </body>
    </html>
    '''
    print(is_matched_html(html_content))


# Output:

"""
>>> # print(j)
5
>>> # print(k)
10
21
33
59
71
82
90
148
156
215
227
239
>>> # print(tag)
html
head
title
/title
/head
body
p
/p
p
/p
/body
/html
>>> # print(j) again
16
27
52
65
77
88
145
154
212
221
233
-1
>>> # print(is_matched_html(html_content))
True
"""