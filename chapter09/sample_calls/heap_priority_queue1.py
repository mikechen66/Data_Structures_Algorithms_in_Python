

from heap_priority_queue import HeapPriorityQueue


class HeapPriorityQueue1(HeapPriorityQueue):
    def _upheap(self, j):
        # j and i both are index
        parent = self._parent(j)
        while (j > 0 and self._data[j] < self._data[parent]):
            self._swap(j, parent)
            j=parent
            parent=self._parent(j)         
    def _downheap(self, j):
        walk = self._left(j) if (self._data[self._left(j)]<self._data[self._right(j)]
                               or not self._has_right()) else self._right(j) # find the min node
        while(j<len(self) and self._data[j]>self._data[walk]):
            self._swap(j,walk)
            walk=self._left(j) if (self._data[self._left(j)]<self._data[self._right(j)]
                               or not self._has_right()) else self._right(j) # find the min node 
    def heappushpop(self, key, value):
        # push and pop
        self._data[0]=self._Item(key,value)   # chang the root node
        self._downheap(0)                     # bubbling the node
        return self.min()
    def heapreplace(self, key, value):
        # pop and push        
        self.min()
        self._data[0] = self._Item(key,value)   # chang the root node
        self._downheap(0)                     # bubbling the node
        return self.min()


if __name__ == '__main__':
    heap = HeapPriorityQueue1() 
    for i in range(10, 0, -1):
        heap.add(i,chr(i*10))
    print(heap.min())
    print(heap.heappushpop(-1,')'))
    print(heap.min())


# Output:

"""
(1, '\n')
(-1, ')')
(-1, ')')
"""