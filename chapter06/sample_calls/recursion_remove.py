# R 6.4 recursion_remove.py

# https://www.codenong.com/cs106523132/


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack."""
        self._data = []  # nonpublic list instance
    def __len__(self):
        """Return  the number of elements in the stack."""
        return len(self._data)
    def is_empty(self):
        """Return True if  the stack is empty."""
        return len(self._data) == 0
    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)  # new item stored at end of list
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data[-1]  # the last item in the list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i e ..,LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data.pop()
    def get_data(self):
        return self._data
    def clear(self):
        if self.is_empty():
            return self.get_data()
        else:
            self.pop()
            self.clear()


if __name__ == "__main__":
    S = ArrayStack()
    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.push(5)
    print(S.get_data())
    S.clear()
    print(S.get_data())


# Output:

"""
[1, 2, 3, 4, 5]
[]
"""