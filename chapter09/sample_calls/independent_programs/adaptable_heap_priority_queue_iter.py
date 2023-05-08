

# adaptable_heap_priority_queue_iter.py


############################################################################################

# 1.piorirty_queue_base


class PriorityQueueBase:
    """Abstract base class for a priority queue."""
    #-------------------------------- nested _Item class ------------------------------
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
    #------------------------------- construction behaviors ---------------------------
    def __iter__(self):
        pass
    def __len__(self):
        # Return the number of items in the priority queue.
        raise NotImplementedError('must be implemented by subclass')
    def __str__(self):
        return str(list(self))
    #-------------------------------- public behaviors --------------------------------
    def is_empty(self):                  # concrete method assuming abstract len
        # Return True if the priority queue is empty."""
        return len(self) == 0
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

############################################################################################


# 2.heap_priority_queue


class Empty(Exception):
    pass


class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""
    #------------------------------ public behaviors ------------------------------
    def __init__(self):
        # Create a new empty Priority Queue.
        self._data = []
    def __len__(self):
        # Return the number of items in the priority queue.
        return len(self._data)
    def __iter__(self):
        # Generate all records of priority queue iteratively
        for each in self._data:
            yield each
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

############################################################################################


# 3.adaptable_heap_priority_queue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""
    #------------------------------ nested Locator class ------------------------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = '_index'                 # add index as additional field
        def __init__(self, k, v, j):
            super().__init__(k,v)
            self._index = j
    #------------------------------ nonpublic behaviors ------------------------------
    # Override swap to record new indices
    def _swap(self, i, j):
        super()._swap(i,j)                   # perform the swap
        self._data[i]._index = i             # reset locator index (post-swap)
        self._data[j]._index = j             # reset locator index (post-swap)
    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)
    #------------------------------ public behaviors ------------------------------
    def add(self, key, value):
        # Add a key-value pair.
        token = self.Locator(key, value, len(self._data)) # initiaize locator index
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token
    def update(self, loc, newkey, newval):
        # Update the key and value for the entry identified by Locator loc.
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        loc._key = newkey
        loc._value = newval
        self._bubble(j)
    def remove(self, loc):
        # Remove and return the (k,v) pair identified by Locator loc.
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        if j == len(self) - 1:               # item at last position
            self._data.pop()                 # just remove it
        else:
            self._swap(j, len(self)-1)       # swap item to the last position
            self._data.pop()                 # remove it from the list
            self._bubble(j)                  # fix item displaced by the swap
        return (loc._key, loc._value)             


if __name__ == '__main__':
    q = AdaptableHeapPriorityQueue()
    q.add(4,  'Adam Grant')
    q.add(5,  'John Manning')
    q.add(6,  'Phllips Jordan')
    q.add(15, 'Harris Diamond')
    q.add(9,  'Steve Jobs')
    q.add(7,  'Bill Gates')
    q.add(20, 'Duncan Lee')
    q.add(16, 'Lewis Smith')
    print(q)
    (token1, token2,token3, token4, token5, token6,token7, token8) = q
    print('Please the first client stand out of the queue：', q.min()[1]) 
    q.update(token5, 1, 'the CEO of Apple Computer')  
    print('Who is the next client：', q.min()[1])  
    q.remove(token1)  
    print(q) 



# Output:

"""
(4, 'Adam Grant')
(5, 'John Manning')
(6, 'Phllips Jordan')
(15, 'Harris Diamond')
(9, 'Steve Jobs')
(7, 'Bill Gates')
(20, 'Duncan Lee')
(16, 'Lewis Smith')
[(4, 'Adam Grant'), (5, 'John Manning'), (6, 'Phllips Jordan'), (15, 'Harris Diamond'), (9, 'Steve Jobs'), (7, 'Bill Gates'), (20, 'Duncan Lee'), (16, 'Lewis Smith')]
Please the first client stand out of the queue： Adam Grant
Who is the next client： the CEO of Apple Computer
(4, 'Adam Grant')
[(1, 'the CEO of Apple Computer'), (5, 'John Manning'), (6, 'Phllips Jordan'), (15, 'Harris Diamond'), (16, 'Lewis Smith'), (7, 'Bill Gates'), (20, 'Duncan Lee')]
"""
