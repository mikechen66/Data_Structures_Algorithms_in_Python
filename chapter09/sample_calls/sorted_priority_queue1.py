

from priority_queue_base import PriorityQueueBase


class SortedPriorityQueue1(PriorityQueueBase):
    """base of array ADT"""
    def __init__(self):
        self._data=[]
    def __len__(self):
        return len(self._data)
    def add(self,k,value):
        # append a item to the data,and sort it
        self._data.append(self._Item(k,value))
        walk=self._data[-1]
        for i in range(len(self._data)-1,-1,-1):    # bubble sort 
            if self._data[i] > walk:
                walk,self._data[i]=self._data[i],walk
                walk=self._data[i]
    def min(self):
        return self._data[0]._key,self._data[0]._value
    def remove_min(self):
        temp=self._data.pop(0)
        return temp._key,temp._value


if __name__ == '__main__':
    t = SortedPriorityQueue1()
    for i in range(10,0,-1):
        t.add(i,str(i))
    print(t.remove_min())


# Output:

"""
(1, '1')
"""