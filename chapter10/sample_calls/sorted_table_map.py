

# sorted_table_map.py


"""

1. _find_index():


The most notable feature of the design is the inclusion of a find index utility function. 
The method using the binary search algorithm, but by convention returns the index of the 
left-most item in the search interval having key greater than or equal to k

Return index of the leftmost item with key greater than or equal to k.
Return high + 1 if no such item qualifies.
That is, j will be returned such that:
   all items of slice table[low:j] have key < k
   all items of slice table[j:high+1] have key >= k

2. __str__()


Add the __str__() utility function 

def __str__(self):
    # Return the string representation of map objects.
    return str(dict(self.items()))


covert

<__main__.SortedTableMap object at 0x7f5bcbbcb390>
...
<__main__.SortedTableMap object at 0x7f5bcbbcb390>

to 

{}
...
{'B': 4, 'K': 2, 'U': 2, 'V': 8}

"""


from map_base import MapBase


class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""
    #------------------------------- magic method behaviors ---------------------------
    def __init__(self):
        # Create an empty map.
        self._table = []
    def __len__(self):
        # Return number of items in the map."""
        return len(self._table)
    def __getitem__(self, k):
        # Return value associated with key k (raise KeyError if not found).
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value
    def __setitem__(self, k, v):
        # Assign value v to key k, overwriting existing value if present.
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v                         # reassign value
        else:
            self._table.insert(j, self._Item(k,v))            # adds new item
    def __delitem__(self, k):
        # Remove item associated with key k (raise KeyError if not found).
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)                                    # delete item
    def __iter__(self):
        # Generate keys of the map ordered from minimum to maximum.
        for item in self._table:
            yield item._key
    def __str__(self):
        # Return the string representation of map objects.
        return str(dict(self.items()))
    def __reversed__(self):
        # Generate keys of the map ordered from maximum to minimum.
        for item in reversed(self._table):
            yield item._key
    #-------------------------------- nonpublic behaviors ------------------------------
    def _find_index(self, k, low, high):
        if high < low:
            return high + 1                                   # no element qualifies
        else:
            mid = (low + high) // 2 
            if k == self._table[mid]._key:
                return mid                                    # found exact match
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)      # Note: may return mid
            else:
                return self._find_index(k, mid + 1, high)     # answer is right of mid
    #-------------------------------- public behaviors --------------------------------
    def find_min(self):
        # Return (key,value) pair with minimum key (or None if empty).
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None
    def find_max(self):
        # Return (key,value) pair with maximum key (or None if empty).
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None
    def find_le(self, k):
        """
        Return (key,value) pair with greatest key less than or equal to k.
        Return None if there does not exist such a key.
        """
        j = self._find_index(k, 0, len(self._table) - 1)      # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            return (self._table[j]._key, self._table[j]._value)      # exact match
        elif j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)  # Note use of j-1
        else:
            return None
    def find_ge(self, k):
        """
        Return (key,value) pair with least key greater than or equal to k.
        Return None if there does not exist such a key.
        """
        j = self._find_index(k, 0, len(self._table) - 1)      # j's key >= k
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None
    def find_lt(self, k):
        """
        Return (key,value) pair with greatest key strictly less than k.
        Return None if there does not exist such a key.
        """
        j = self._find_index(k, 0, len(self._table) - 1)      # j's key >= k
        if j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)  # Note use of j-1
        else:
            return None
    def find_gt(self, k):
        """
        Return (key,value) pair with least key strictly greater than k.
        Return None if there does not exist such a key.
        """
        j = self._find_index(k, 0, len(self._table) - 1)      # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            j += 1                                       # advanced past match
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None
    def find_range(self, start, stop):
        """
        Iterate all (key,value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table)-1)   # find first result
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1


if __name__ == '__main__':
    m = SortedTableMap()
    print(m)                             # {}
    m['K'] = 2
    print(m)                             # {'K': 2}
    m['B'] = 4
    print(m)                             # {'K': 2, 'B': 4}
    m['U'] = 2
    print(m)                             # {'K': 2, 'B': 4, 'U': 2}
    m['V'] = 8
    print(m)                             # {'K': 2, 'B': 4, 'U': 2, 'V': 8}
    m['K'] = 9
    for k, v in m.find_range('C', 'V'):
        print('(' + repr(k) + ': ' + repr(v) + ')')  # ('K': 9) ('U': 2)
    print(m['B'])                        # 4
    print(m.get('F'))                    # None
    print(m.get('F', 5))                 # 5
    print(m.get('K', 5))                 # 9
    print(len(m))                        # 4
    del m['V']
    print(m)                             # {'K': 9, 'B': 4, 'U': 2}
    print(m.pop('K'))                    # 9
    print(m)                             # {'B': 4, 'U': 2}
    print(m.setdefault('B', 1))          # 4
    print(m.setdefault('A', 1))          # 1
    print(m)                             # {'B': 4, 'U': 2, 'A': 1}


# Output:

"""
{}
{'K': 2}
{'B': 4, 'K': 2}
{'B': 4, 'K': 2, 'U': 2}
{'B': 4, 'K': 2, 'U': 2, 'V': 8}
('K': 9)
('U': 2)
4
None
5
9
4
{'B': 4, 'K': 9, 'U': 2}
9
{'B': 4, 'U': 2}
4
1
{'A': 1, 'B': 4, 'U': 2}
"""
