

# stack_queue.py

# It is originally from the exercise of C6.27


import random
from queue import Queue


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack."""
        self._data = []  # nonpublic list instance
        self._size = 0
        self._length = 10
    def __len__(self):
        """Return  the number of elements in the stack."""
        return self._size
    def is_empty(self):
        """Return True if  the stack is empty."""
        return self._size == 0
    def push(self, e):
        """Add element e to the top of the stack"""
        if self._length == self._size:
            self._resize(2 * self._length)
        self._data.append(e)  # new item stored at end of list
        self._size += 1
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data[self._size-1]  # the last item in the list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i e ..,LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("stack is empty")
        value = self._data.pop()
        self._size -= 1
        return value
    def get_data(self):
        return self._data
    def clear(self):
        if self.is_empty():
            return self.get_data()
        else:
            self.pop()
            self.clear()
    def _resize(self, item):
        self._length = item


def find(stack, queue, value):
    i = len(stack) - 1
    while len(stack) != 0:
        val = stack.pop()
        if val == value:
            queue.put(val)
            break
        queue.put(val)
        i -= 1
    if i == -1:
        while not queue.empty():
            stack.push(queue.get())
        while len(stack) != 0:
            queue.put(stack.pop())
        while not queue.empty():
            stack.push(queue.get())
        return i
    else:
        while not queue.empty():
            stack.push(queue.get())
        key = len(stack)-i
        for i in range(key):
            queue.put(stack.pop())
        while not queue.empty():
            stack.push(queue.get())
        return len(stack)-i-1


if __name__ == "__main__":
    stack = ArrayStack()
    queue = Queue()
    random.seed(1)
    [stack.push(random.randint(1, 100)) for i in range(1, 11)]
    print(stack.get_data())
    print(find(stack, queue, 9))
    print(stack.get_data())


# Output:

"""
[None, None, None, None, None, None, None, None, None, None]
[18, 73, 98, 9, 33, 16, 64, 98, 58, 61]
3
[18, 73, 98, 9, 33, 16, 64, 98, 58, 61]
"""