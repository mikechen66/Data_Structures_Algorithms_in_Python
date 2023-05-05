

# dynamic_array.py

# Option 1: Original array in the book 


import ctypes                                          # provides low-level arrays
 

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        # Create an empty array.
        self._n = 0                                    # count actual elements
        self._capacity = 1                             # default array capacity
        self._A = self._make_array(self._capacity)     # low-level array
    def __len__(self):
        # Return number of elements stored in the array.
        return self._n
    def __getitem__(self, k):
        # Return element at index k.
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        else:
            return self._A[k]                          # retrieve from array
    def append(self, obj):
        # Add object to end of the array.
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)           # so double capacity
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):                              # nonpublic utitity
        # Resize internal array to capacity c.
        B = self._make_array(c)                        # new (bigger) array
        for k in range(self._n):                       # for each existing value
            B[k] = self._A[k]
        self._A = B                                    # use the bigger array
        self._capacity = c
    def _make_array(self, c):                          # nonpublic utitity
        # Return new array with capacity c.   
        return (c * ctypes.py_object)()               # see ctypes documentation
    # Add the method of insert()
    def insert(self, k, value):
        # Insert value at index k, shifting subsequent values rightward.
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)           # so double array capacity
        for j in range(self._n, k, -1):                # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                             # store newest element
        self._n += 1
    # Add the method of remove()
    def remove(self, value):
        # Remove first occurrence of value (or raise ValueError).
        for k in range(self._n):
            if self._A[k] == value:                    # found a match!
                for j in range(k, self._n - 1):        # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None            # help garbage collection
                self._n -= 1                           # we have one less item
                return                                 # exit immediately
        raise ValueError('value not found')            # only reached if no match
    # Add the function of _print()
    def _print(self):
        for i in range(self._n):
            print(self._A[i], end=' ')
        print()


if __name__=="__main__":
    mylist = DynamicArray()
    print('size was: ', str(len(mylist)))
    mylist.append(10)
    mylist.append(20)
    mylist.append(30)
    mylist.insert(0, 0)
    mylist.insert(1, 5)
    mylist.insert(3, 15)
    mylist._print()
    mylist.remove(20)
    mylist._print()
    print('size is: ', str(len(mylist)))


# Output:

"""
size was:  0
0 5 10 15 20 30 
0 5 10 15 30 
size is:  5
"""

###################################################################################################


# Option 2: 


import ctypes
import random, sys


class DynamicArray:
    """A dynamic array class that works like a list."""
    def __init__(self):
        self._n = 0                     # number of elements
        self._capacity = 1              # default array capacity
        self._A = self._make_array(self._capacity) # low-level guts
    def __len__(self):
        # Return number of elements stored in the array
        return self._n
    def __getitem__(self, k):
        if 0 <= k < self._n:
            return self._A[k]
        elif -self._n <= k < 0:
            return self._A[self._n+k]
        else:
            raise IndexError("Invalid index: Requested index {0} exceeds number of elements {1}".format(k, self._n))
    def append(self,obj):
        # Add obj to end of array
        if self._n == self._capacity:
            # Being out of space, so resize will update capacity.
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    # Add the method of pop()
    def pop(self):
        # Pop obj from end of array
        self._A[self._n] = None
        self._n -= 1
        if self._capacity//4 > self._n:
            self._resize(self._capacity//2)
    def _resize(self, c):
        # Resize to capacity c (private): 0: the 0th element, 4: min width space, d: decimal
        print("Resizing array: {0:4d} elements, {1:5d} capacity".format(self._n,c))
        B = self._make_array(c)         # bigger array
        for k in range(self._n):
            B[k] = self._A[k]           # copy existing elements only
        self._A = B                     # forget the old array
        self._capacity = c              # update capacity
    def _make_array(self,n):
        # Make the internal array (private)
        return (n * ctypes.py_object)()


if __name__=="__main__":
    a = DynamicArray()
    print("Appending 1,000 elements to array...")
    for j in range(1000):
        a.append(random.randint(0,9))
    print("Done.\n")
    print("Accessing array at individual positive/negative indices...")
    for ix in [0, 10, 35, -10, -999, 999, -1000]:
        print("Index {0:4d}\tDynamicArray value: {1:2d}".format(ix,a[ix]))
    print("Done.\n")
    print("Accessing array at invalid index...")
    try:
        ix = 1000
        print("Index {0:4d}\tDynamicArray value: {1:2d}".format(ix,a[ix]))
    except IndexError:
        print("Correctly throws IndexError for index {0}.".format(ix))
    print("Done.\n")
    print("Popping 995 elements from array...")
    for j in range(995):
        a.pop()


# Outpout: 

"""
Appending 1,000 elements to array...
Resizing array:    1 elements,     2 capacity
Resizing array:    2 elements,     4 capacity
Resizing array:    4 elements,     8 capacity
Resizing array:    8 elements,    16 capacity
Resizing array:   16 elements,    32 capacity
Resizing array:   32 elements,    64 capacity
Resizing array:   64 elements,   128 capacity
Resizing array:  128 elements,   256 capacity
Resizing array:  256 elements,   512 capacity
Resizing array:  512 elements,  1024 capacity
Done.

Accessing array at individual positive/negative indices...
Index    0  DynamicArray value:  2
Index   10  DynamicArray value:  7
Index   35  DynamicArray value:  1
Index  -10  DynamicArray value:  3
Index -999  DynamicArray value:  8
Index  999  DynamicArray value:  2
Index -1000 DynamicArray value:  2
Done.

Accessing array at invalid index...
Correctly throws IndexError for index 1000.
Done.

Popping 995 elements from array...
Resizing array:  255 elements,   512 capacity
Resizing array:  127 elements,   256 capacity
Resizing array:   63 elements,   128 capacity
Resizing array:   31 elements,    64 capacity
Resizing array:   15 elements,    32 capacity
Resizing array:    7 elements,    16 capacity
"""

###################################################################################################


# Option 3: 

import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        # Create an empty array.
        self.n = 0                        # count actual elements
        self.capacity = 1                 # default array capacity
        self.A = self._make_array(self.capacity)   # low-level array
    def is_empty(self):
        # Return True if array is empty
        return self.n == 0
    def __len__(self):
        # Return numbers of elements stored in the array.
        return self.n
    def __getitem__(self, i):
        # Return element at index i.
        if not 0 <= i < self.n:
            # Check it i index is in bounds of array
            raise ValueError('invalid index')
        return self.A[i]
    def append(self, obj):
        # Add object to end of the array.
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)
        self.A[self.n] = obj                # Set self.n index to obj
        self.n += 1
    def _resize(self, c):
        # Resize internal array to capacity c.
        B = self._make_array(c)             # New bigger array
        for k in range(self.n):             # Reference all existing values
            B[k] = self.A[k]
        self.A = B                          # Call A the new bigger array
        self.capacity = c                   # Reset the capacity
    @staticmethod
    def _make_array(c):
        # Return new array with capacity c. 
        return (c * ctypes.py_object)()
    def insert(self, k, value):
        # Insert value at position k.
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        for j in range(self.n, k, -1):
            self.A[j] = self.A[j-1]
        self.A[k] = value
        self.n += 1
    def pop(self, index=0):
        # Remove item at index (default first).
        if index >= self.n or index < 0:
            raise ValueError('invalid index')
        for i in range(index, self.n-1):
            self.A[i] = self.A[i+1]
        self.A[self.n - 1] = None
        self.n -= 1
    def remove(self, value):
        # Remove the first occurrence of a value in the array.
        for k in range(self.n):
            if self.A[k] == value:
                for j in range(k, self.n - 1):
                    self.A[j] = self.A[j+1]
                self.A[self.n - 1] = None
                self.n -= 1
                return
        raise ValueError('value not found')
    def _print(self):
        """Print the array."""
        for i in range(self.n):
            print(self.A[i], end=' ')
        print()


if __name__ == '__main__':
    # Instantiate
    mylist = DynamicArray()
    # Append new element
    mylist.append(10)
    mylist.append(9)
    mylist.append(8)
    # Insert new element in given position
    mylist.insert(1, 1024)
    mylist.insert(2, 2019)
    # Check length
    print('The array length is: ', mylist.__len__())
    # Print the array
    print('Print the array：')
    mylist._print()
    # Index
    print('The element at index 1 is :', mylist[1])
    # Remove element
    print('Remove 2019 in array:')
    mylist.remove(2019)
    mylist._print()
    # Pop element in given position
    print('Pop pos 2 in array:')
    # mylist.pop()
    mylist.pop(2)
    mylist._print()


# Output:

"""
The array length is:  5
Print the array：
10 1024 2019 9 8 
The element at index 1 is : 1024
Remove 2019 in array:
10 1024 9 8 
Pop pos 2 in array:
10 1024 8 
>>>
"""

###################################################################################################


# Option 4: 


import ctypes


class DynamicArray(object): 
    def __init__(self): 
        self.n = 0 
        self.size = 1 
        self.A = self.make_array(self.size)
    def __len__(self):
        return self.n
    def add(self, ele): 
        if self.n == self.size: 
            self._reshape(2 * self.size) 
        self.A[self.n] = ele
        self.n += 1
    def remove(self): 
        if self.n==0: 
            print("Array is empty, Please add an element to delete") 
            return  
        self.A[self.n-1]=0
        self.n-=1
    def appendAt(self, item, ind):
        if ind < 0 or ind > self.n:
            print("Please enter with the range of the index !")
            return
        if self.n == self.size:
            self._reshape(2*self.size)
        for i in range(self.n-1, ind-1, -1):
            self.A[i+1] = self.A[i]
        self.A[ind] = item
        self.n += 1
    def deleteAt(self, ind):
        if self.n == 0:
            print("Array is empty, Please add an element first !!")
            return
        if ind < 0 or ind >= self.n:
            return indError("The index is not within the range !! ")
        if ind == self.n-1:
            self.A[ind] = 0
            self.n -= 1
            return
        for i in range(ind, self.n-1):
            self.A[i] = self.A[i+1]
        self.A[self.n-1] = 0
        self.n -= 1
    def __getiele__(self, k):
        if not 0 <= k < self.n:
            return indError('k is out of bounds !')
        return self.A[k]
    def _reshape(self, new_size):
        B = self.make_array(new_size)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.size = new_size
    def make_array(self, new_size):
        return (new_size * ctypes.py_object)()


if __name__ == '__main__':
    arr = DynamicArray()
    arr.add(1)
    arr.add(23)
    arr.appendAt(25,2)
    arr.add(12)
    arr.add(34)
    print(arr.__len__())
    print(arr.__getiele__(1))
    arr.remove()
    print(arr.__getiele__(3))
    print(arr.__len__())
    arr.add(10)
    arr.add(70)
    print(arr.__len__())
    arr.deleteAt(1)
    print(arr.__getiele__(2))
    print(arr.__len__())


# Outpout:

"""
5
23
12
4
6
12
5
"""