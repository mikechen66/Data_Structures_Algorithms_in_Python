

# priority_queue_base.py


class Empty(Exception):
    pass


class PriorityQueueBase:
    """Abstract base class for a priority queue."""
    #------------------------------ nested _Item class ------------------------------
    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v
        def __lt__(self, other):
            return self._key < other._key    # compare items based on their keys
        def __repr__(self):
            return '({0},{1})'.format(self._key, self._value)
    #------------------------------ public behaviors ------------------------------
    def is_empty(self):                  # concrete method assuming abstract len
        # Return True if the priority queue is empty."""
        return len(self) == 0
    def __len__(self):
        # Return the number of items in the priority queue.
        raise NotImplementedError('must be implemented by subclass')
    def add(self, key, value):
        # Add a key-value pair.
        raise NotImplementedError('must be implemented by subclass')
    def min(self):
        """
        Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        raise NotImplementedError('must be implemented by subclass')
    def remove_min(self):
        """
        Remove and return (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        raise NotImplementedError('must be implemented by subclass')


if __name__ == '__main__':
    heap = HeapPriorityQueue()
    heap.add(4, "D")
    heap.add(3, "C")
    heap.add(1, "A")
    heap.add(5, "E")
    heap.add(2, "B")
    heap.add(7, "G")
    heap.add(6, "F")
    heap.add(26, "Z")
    for item in heap._data:
        print(item)


# Output:

"""
... 
(1,A)
(2,B)
(3,C)
(5,E)
(4,D)
(7,G)
(6,F)
(26,Z)
"""