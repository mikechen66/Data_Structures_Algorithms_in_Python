

# quick_sort_queue.py


class Empty(Exception):
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage
        def __init__(self, element, next):
            self._element = element
            self._next = next
    #------------------------------- queue methods -------------------------------
    def __init__(self):
        # Create an empty queue.
        self._head = None
        self._tail = None
        self._size = 0                          # number of queue elements
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
        return self._head._element              # front aligned with head of list
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                     # special case as queue is empty
            self._tail = None                   # removed head had been the tail
        print(answer)
        return answer
    def enqueue(self, e):
        # Add an element to the back of queue.
        newest = self._Node(e, None)            # node will be new tail node
        if self.is_empty():
            self._head = newest                 # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                     # update reference to tail node
        self._size += 1
        # return e


def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return None                             # list is already sorted
    # divide the queue
    p = S.first()                               # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():                     # divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:                                   # S.first() must equal pivot
            E.enqueue(S.dequeue())
    # conquer with recursion
    quick_sort(L)                               # sort elements less than p
    quick_sort(G)                               # sort elements greater than p
    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


if __name__ == '__main__':
    lq = LinkedQueue()
    lq.enqueue(6)
    lq.enqueue(3)
    lq.enqueue(1)
    lq.enqueue(4)
    lq.enqueue(2)
    quick_sort(lq)


# Output:

"""
6
3
1
4
2
3
1
4
2
1
2
1
2
1
2
3
4
1
2
3
4
6
"""