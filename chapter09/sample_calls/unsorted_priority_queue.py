

# unsorted_priority_queue.py


from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList


class Empty(Exception):
    pass


class UnsortedPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with an unsorted list."""
    #------------------------------ public behaviors ------------------------------
    def __init__(self):
        # Create a new empty Priority Queue.
        self._data = PositionalList()
    def __len__(self):
        # Return the number of items in the priority queue.
        return len(self._data)
    def add(self, key, value):
        # Add a key-value pair."""
        self._data.add_last(self._Item(key, value))
    def min(self):
        """
        Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)
    def remove_min(self):
        """
        Remove and return (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
    #----------------------------- nonpublic behavior -----------------------------
    def _find_min(self):
        # Return Position of item with minimum key.
        if self.is_empty():               # is_empty inherited from base class
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small


if __name__ == '__main__':
    heap = UnsortedPriorityQueue()
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
    print("min is: ")
    print(heap.min())
    print()
    print("remove min: ")
    print(heap.remove_min())
    print("Now min is: ")
    print(heap.min())
    print()
    print("remove min: ")
    print(heap.remove_min())
    print("Now min is: ")
    print(heap.min())
    print()
    heap.add(1, "A")
    print("Now min is: ")
    print(heap.min())
    print()


# Output:

"""
(4,D)
(3,C)
(1,A)
(5,E)
(2,B)
(7,G)
(6,F)
(26,Z)
min is: 
(1, 'A')

remove min: 
(1, 'A')
Now min is: 
(2, 'B')

remove min: 
(2, 'B')
Now min is: 
(3, 'C')

Now min is: 
(1, 'A')

"""