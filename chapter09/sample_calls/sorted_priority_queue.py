

# sorted_priority_queue.py


from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList


class Empty(Exception):
    pass


class SortedPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with a sorted list."""
    #------------------------------ public behaviors ------------------------------
    def __init__(self):
        # Create a new empty Priority Queue.
        self._data = PositionalList()
    def __len__(self):
        # Return the number of items in the priority queue."""
        return len(self._data)
    def add(self, key, value):
        # Add a key-value pair.
        newest = self._Item(key, value)             # make new item instance
        walk = self._data.last()       # walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)            # new key is smallest
        else:
            self._data.add_after(walk, newest)      # newest goes after walk
    def min(self):
        """
        Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)
    def remove_min(self):
        """
        Remove and return (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)


if __name__ == '__main__':
    heap = SortedPriorityQueue()
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
(1,A)
(2,B)
(3,C)
(4,D)
(5,E)
(6,F)
(7,G)
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