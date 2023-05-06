

# adaptable_heap_priority_queue.py


from heap_priority_queue import HeapPriorityQueue


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
    result = []
    for item in q._data:
        print(item)
        result.append(item)
    print(result)
    (token1, token2, token3, token4, token5, token6, token7, token8) = result
    print('Please the first client stand out of the queue：', q.min()[1]) 
    q.update(token5, 1, 'the CEO of Apple Computer')  
    print('Who is the next client：', q.min()[1])  
    q.remove(token1)  
    result_update = []
    for item in q._data:
        print(item)
        result_update.append(item)
    print(result_update) 


# Output:


"""
(4,Adam Grant)
(5,John Manning)
(6,Phllips Jordan)
(15,Harris Diamond)
(9,Steve Jobs)
(7,Bill Gates)
(20,Duncan Lee)
(16,Lewis Smith)
(4,Adam Grant)
(5,John Manning)
(6,Phllips Jordan)
(15,Harris Diamond)
(9,Steve Jobs)
(7,Bill Gates)
(20,Duncan Lee)
(16,Lewis Smith)
[(4,Adam Grant), (5,John Manning), (6,Phllips Jordan), (15,Harris Diamond), (9,Steve Jobs), (7,Bill Gates), (20,Duncan Lee), (16,Lewis Smith)]
Please the first client stand out of the queue： Adam Grant
Who is the next client： the CEO of Apple Computer
(4, 'Adam Grant')
(1,the CEO of Apple Computer)
(5,John Manning)
(6,Phllips Jordan)
(15,Harris Diamond)
(16,Lewis Smith)
(7,Bill Gates)
(20,Duncan Lee)
[(1,the CEO of Apple Computer), (5,John Manning), (6,Phllips Jordan), (15,Harris Diamond), (16,Lewis Smith), (7,Bill Gates), (20,Duncan Lee)]

"""