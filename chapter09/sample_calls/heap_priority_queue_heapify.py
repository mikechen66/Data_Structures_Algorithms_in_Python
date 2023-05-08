

# heap_priority_queue.py


from priority_queue_base import PriorityQueueBase


class Empty(Exception):
    pass


class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""
    #------------------------------ public behaviors ------------------------------
    def __init__(self, contents=()):
        # Create a new empty Priority Queue.
        self._data = [self._Item(k,v) for k,v in contents]  # empty by default
        if len(self._data) > 1:
            self.heapify
    def __len__(self):
        # Return the number of items in the priority queue.
        return len(self._data)
    #------------------------------ public behaviors ------------------------------
    def add(self, key, value):
        # Add a key-value pair to the priority queue.
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)        # upheap newly added position
    def min(self):
        """
        Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)
    def remove_min(self):
        """
        Remove and return (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)       # put minimum item at the end
        item = self._data.pop()                  # and remove it from the list;
        self._downheap(0)                        # then fix new root
        return (item._key, item._value)
    #------------------------------ nonpublic behaviors ------------------------------
    def _parent(self, j):
        return (j-1) // 2
    def _left(self, j):
        return 2*j + 1
    def _right(self, j):
        return 2*j + 2
    def _has_left(self, j):
        return self._left(j) < len(self._data)   # index beyond end of list?
    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of list?
    def _swap(self, i, j):
        # Swap the elements at indices i and j of array.
        self._data[i], self._data[j] = self._data[j], self._data[i]
    def _heapify(self):
        start = self._parent(len(self) - 1)      # start at PARENTof last leaf
        for j in range(start, -1, -1):           # going to and include the root
            self._downheap(j)
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)                 # recur at position of parent
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left                   # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)      # recur at position of small child


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
    result = []
    for item in heap._data:
        print(item)
        result.append(item)
    print(result)
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
(5,E)
(4,D)
(7,G)
(6,F)
(26,Z)
[(1,A), (2,B), (3,C), (5,E), (4,D), (7,G), (6,F), (26,Z)]
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