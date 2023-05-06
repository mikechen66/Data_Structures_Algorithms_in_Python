

# linked_stack.py


class Empty(Exception):
    pass


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""
    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage
        def __init__(self, element, next):      # initialize node's fields
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node
    #------------------------------- stack methods -------------------------------
    def __init__(self):
        # Create an empty stack.
        self._head = None                       # reference to the head node
        self._size = 0                          # number of stack elements
    def __len__(self):
        # Return the number of elements in the stack.
        return self._size
    def __iter__(self):
        cur = self._head
        while cur is not None:
            yield cur._element
            cur = cur._next
    def is_empty(self):
        # Return True if the stack is empty.
        return self._size == 0
    def push(self, e):
        # Add element e to the top of the stack.
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element              # top of stack is at head of list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next           # bypass the former top node
        self._size -= 1
        return answer


if __name__ == '__main__':
    L = LinkedStack()
    L.push(5)
    L.push(4)
    L.push(3)
    [i for i in L]
    M = LinkedStack()
    M.push(3)
    M.push(2)
    M.push(1)
    [i for i in M]
    N = list(L) + list(M)
    print(N)



# Output:

"""
[3, 4, 5]
[1, 2, 3]
[3, 4, 5, 1, 2, 3]
"""