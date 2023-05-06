
# linked_deque_iter.py


from doubly_linked_base import _DoublyLinkedBase


class Empty(Exception):
    pass


class LinkedDeque(_DoublyLinkedBase):           # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""
    def __iter__(self):
        # Generate elements with forward iterations in the queue
        cursor = self._header._next
        while cursor._element is not None:
            yield cursor._element
            cursor = cursor._next
    def first(self):
        """
        Return (but do not remove) the element at the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element      # real item just after header
    def last(self):
        """
        Return (but do not remove) the element at the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element     # real item just before trailer
    def insert_first(self, e):
        # Add an element to the front of the deque.
        self._insert_between(e, self._header, self._header._next)   # after header
    def insert_last(self, e):
        # Add an element to the back of the deque.
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailer
    def delete_first(self):
        """
        Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)   # use inherited method
    def delete_last(self):
        """
        Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)  # use inherited method


if __name__ == '__main__':
    ld = LinkedDeque()
    ld.insert_first(9)
    ld.insert_last(5)
    print(len(ld))            # 2
    ld.insert_first(3)
    ld.insert_last(8)
    print(list(ld))           # [3, 9, 5, 8]
    print(ld.delete_first())  # 3
    print(list(ld))           # [9, 5, 8]
    print(ld.delete_last())   # 8
    print(len(ld))            # 2
    print(list(ld))           # [9, 5]


# Output:

"""
2
[3, 9, 5, 8]
3
[9, 5, 8]
8
2
[9, 5]
"""