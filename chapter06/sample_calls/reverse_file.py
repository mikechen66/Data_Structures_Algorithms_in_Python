# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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


def reverse_file(filename):
    # Overwrite given file with its contents line-by-line reversed.
    S = ArrayStack()
    original = open(filename)       
    for line in original:
        S.push(line.rstrip('\n'))     # we will re-insert newlines when writing
    original.close()
    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')      # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')  # re-insert newline characters
    output.close()



# It works for file of the sample.txt with line by line 
if __name__ == '__main__':
    filename = 'sample2reverse.txt'
    reverse_file(filename)