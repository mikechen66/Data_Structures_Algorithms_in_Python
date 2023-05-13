

# unsorted_table_map.py


"""

The original code in the textbook could not be called visually. Here add the utility 
function of __str__() for the purpose method call. 

Add the __str__() utility function 

def __str__(self):
    # Return the string representation of map objects.
    return str(dict(self.items()))

covert the following object

<__main__.UnsortedTableMap object at 0x7f08f64ddf50>
...
<__main__.UnsortedTableMap object at 0x7f08f64ddf50>


to the dict as follows

{}
...
{'K': 2, 'B': 4, 'U': 2, 'V': 8}
"""


from map_base import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""
    def __init__(self):
        # Create an empty map.
        self._table = []                            # list of _Item's
    def __getitem__(self, k):
        # Return value associated with key k (raise KeyError if not found).
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))
    def __setitem__(self, k, v):
        # Assign value v to key k, overwriting existing value if present
        for item in self._table:
            if k == item._key:                      # Found a match:
                item._value = v                     # reassign value
                return                              # and quit    
        # did not find match for key
        self._table.append(self._Item(k,v))
    def __delitem__(self, k):
        # Remove item associated with key k (raise KeyError if not found).
        for j in range(len(self._table)):
            if k == self._table[j]._key:            # Found a match:
                self._table.pop(j )                 # remove item
                return None                         # and quit    
        raise KeyError('Key Error: ' + repr(k))
    def __len__(self):
        # Return number of items in the map.
        return len(self._table)
    def __iter__(self):                             
        # Generate iteration of the map's keys.
        for item in self._table:
            yield item._key                         # yield the KEY
    def __str__(self):
        # Return the string representation of map objects.
        return str(dict(self.items()))


if __name__ == '__main__':
    m = UnsortedTableMap()
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
{'K': 2, 'B': 4}
{'K': 2, 'B': 4, 'U': 2}
{'K': 2, 'B': 4, 'U': 2, 'V': 8}
4
None
5
9
4
{'K': 9, 'B': 4, 'U': 2}
9
{'B': 4, 'U': 2}
4
1
{'B': 4, 'U': 2, 'A': 1}
"""