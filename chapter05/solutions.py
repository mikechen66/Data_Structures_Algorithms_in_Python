
# Array-based Sequence 
# Code Exercises for Array-based sequence 


# Part One. Reinforcement

####################################################################################################


# R5.1 Execute the experiment from Code Fragment 5.1 and compare the results on your 
# system to those we report in Code Fragment 5.2.


# (1).Define a function without replacement 


import sys


def func(n):
    data = []
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)   
        print('Length: {:4d}, Size in bytes: {:4d}'.format(a, b))
        data.append(None)


if __name__ == '__main__':        
    func(100)


# Output:

"""
Length:    0, Size in bytes:   72
Length:    1, Size in bytes:  104
Length:    2, Size in bytes:  104
Length:    3, Size in bytes:  104
Length:    4, Size in bytes:  104
Length:    5, Size in bytes:  136
Length:    6, Size in bytes:  136
...
Length:   99, Size in bytes:  920
"""

#---------------------------------------------------------------------------------------------------


# (2).Use the replacement 

import sys


def func(n):
    data = []
    max_size = sys.getsizeof(data)
    for i in range(0, n, 2):
        length = len(data)
        new_size = sys.getsizeof(data)
        max_size = new_size
        print('Length:{0:3d}; Size in bytes:{1:4d}'.format(length, new_size))
        data.append(None)


if __name__ == '__main__':        
    func(100)


# Output:

"""
Length:   0; size in bytes:   72
Length:   1; size in bytes:  104
Length:   2; size in bytes:  104
Length:   3; size in bytes:  104
Length:   4; size in bytes:  104
Length:   5; size in bytes:  136
Length:   6; size in bytes:  136
...
Length:  49; size in bytes:  536
"""

#---------------------------------------------------------------------------------------------------


# (3).Jumpy over the previous max_size 


import sys


def func(n):
    data = []
    max_size = sys.getsizeof(data)
    for i in range(n):
        length = len(data)
        new_size = sys.getsizeof(data)
        print(f'Length: {length:3d}; size in bytes: {new_size:4d}', end='')
        if max_size != new_size:
            print('\t\tA jump of: {0} bytes, or a ratio of {1}'.format((new_size-max_size), (new_size/max_size)))
        else:
            print('')
        data.append(None)
        max_size = new_size


if __name__ == '__main__':        
    func(100)


# Output:

"""
Length:   0; size in bytes:   72
Length:   1; size in bytes:  104        A jump of: 32 bytes, or a ratio of 1.4444444444444444
Length:   2; size in bytes:  104
Length:   3; size in bytes:  104
Length:   4; size in bytes:  104
Length:   5; size in bytes:  136        A jump of: 32 bytes, or a ratio of 1.3076923076923077
Length:   6; size in bytes:  136
...
Length:  98; size in bytes:  920
Length:  99; size in bytes:  920
"""

####################################################################################################


# R5.2 In Code Fragment 5.1, we perform an experiment to compare the length of a Python
# list to its underlying memory usage. Determining the sequence of array sizes requires 
# a manual inspection of the output of that program. Redesign the experiment so that the 
# program outputs only those values of k at which the existing capacity is exhausted. 
# For example, on a system consistent with the results of Code Fragment 5.2, your program 
# should output that the sequence of array capacities are 0, 4, 8, 16, 25,...


import sys


def func(n):
    data = []
    max_size = 0
    for i in range(n):
        length = len(data)
        print(length)
        size = sys.getsizeof(data)
        # print(size)
        if max_size == 0:
            max_size = size
        if max_size < size:
            max_size = size
            # length can be a-1, a, a+1 or a+2
            print('Length:{0:3d}, Size in bytes:{1:4d}'.format(length-1, max_size))
        data.append(None)
        

if __name__ == '__main__':
    func(100)


# Output:

"""
>>> # Output:
 
>>> # print(a)
0
1
>>> # print(b), just print less than the original
72
104
Length:  0, Size in bytes: 104
>>> # print(a)
2
3
4
5
>>> # print(b)
104
104
104
136
Length:  4, Size in bytes: 136
>>> # print(a)
6
7
8
9
Length:  8, Size in bytes: 200
>>> # print(a)
10
11
12
13
14
15
16
17
Length: 16, Size in bytes: 272
>>> # print(a)
18
19
20
21
22
23
24
25
26
Length: 25, Size in bytes: 352
>>> # print(a)
27
28
29
30
31
32
33
34
35
36
Length: 35, Size in bytes: 440
>>> # print(a)
37
38
39
40
41
42
43
44
45
46
47
Length: 46, Size in bytes: 536
>>> # print(a)
48
49
50
51
52
53
54
55
56
57
58
59
Length: 58, Size in bytes: 648
>>> # print(a)
60
61
62
63
64
65
66
67
68
69
70
71
72
73
Length: 72, Size in bytes: 776
>>> # Print(a)
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
>>> # print(b)
776
776
776
776
776
776
776
776
776
776
776
776
776
776
776
920
Length: 88, Size in bytes: 920
>>> # print(a)
90
91
92
93
94
95
96
97
98
99
>>> # print(b)
920
920
920
920
920
920
920
920
920
920
"""

#---------------------------------------------------------------------------------------------------


# (2).Has the complete string as same as the textbook


import sys
import dis 


def func(n):
    data = []  # empty list is 72 bytes 
    max_size = 0
    times = 0
    for i in range(n):      
        a = len(data)
        # print(a)
        b = sys.getsizeof(data)  
        # print(b)
        if max_size == b:
            times += 1
        else:
            times = 0
        max_size = b
        # print(temp)  temp is same as b 
        if times == 0 and a:
            print('Length:{0:3d}, Size in bytes:{1:4d}'.format(a-1, max_size))
        data.append(None)


if __name__ == '__main__':        
    func(100)


# Output:

"""
Length:  0, Size in bytes: 104
Length:  4, Size in bytes: 136
Length:  8, Size in bytes: 200
Length: 16, Size in bytes: 272
Length: 25, Size in bytes: 352
Length: 35, Size in bytes: 440
Length: 46, Size in bytes: 536
Length: 58, Size in bytes: 648
Length: 72, Size in bytes: 776
Length: 88, Size in bytes: 920
"""


####################################################################################################


# R5.3 Modify the experiment from Code Fragment 5.1 in order to demonstrate that 
# Python’s list class occasionally shrinks the size of its underlying array when 
# elements are popped from a list. Modify insert() method to support the occasional 
# shrinking of list 


# (1).Gradual pop-out from the stack 


def func(n):
    data = [None] * n
    for i in range(n):
        length = len(data)
        size = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(length, size))
        data.pop()


if __name__ == '__main__':        
    func(100)


# Output:

"""
Length: 100; Size in bytes:  872
Length:  99; Size in bytes:  872
Length:  98; Size in bytes:  872
Length:  97; Size in bytes:  872
Length:  96; Size in bytes:  872
Length:  95; Size in bytes:  872
Length:  94; Size in bytes:  872
...
Length:   6; Size in bytes:  168
Length:   5; Size in bytes:  136
Length:   4; Size in bytes:  136
Length:   3; Size in bytes:  120
Length:   2; Size in bytes:  112
Length:   1; Size in bytes:  104
"""

#---------------------------------------------------------------------------------------------------


# (2).Occassional decreasing 

import sys


def grow_shrink(n, lower_limit=0.2):
    data = []
    max_size = 0
    current_limit = 10
    for i in range(n):
        if i == current_limit:
            while len(data) > current_limit * lower_limit:
                data.pop()
                new_size = sys.getsizeof(data)
                print(f'Length: {len(data):3d}; Size in bytes: {new_size:4d}', end='\t')
                if new_size < max_size:
                    print('Size decreased from', max_size, 'to', new_size)
                else: 
                    print("")
                max_size = new_size
            current_limit *= 10
        data.append(None)
        

if __name__ == '__main__':        
    grow_shrink(1000)


# Output:

"""
Length:   9; Size in bytes:  200    
Length:   8; Size in bytes:  200    
Length:   7; Size in bytes:  152    Size decreased from 200 to 152
Length:   6; Size in bytes:  152    
Length:   5; Size in bytes:  152    
Length:   4; Size in bytes:  128    Size decreased from 152 to 128
Length:   3; Size in bytes:  128    
Length:   2; Size in bytes:  112    Size decreased from 128 to 112
Length:  91; Size in bytes:  936    
... 
Length:  33; size in bytes:  592    
Length:  32; size in bytes:  592    
Length:  31; size in bytes:  392    Size decreased from: 592 to 392
"""

####################################################################################################


# 5.4 Our DynamicArray class, as given in Code Fragment 5.3, does not support use of 
# negative indices with getitem . Update that method to better match the semantics 
# of a Python list.

# self.A[i-1] to support negative index


import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        # Create an empty array.
        self.n = 0                          # count actual elements
        self.capacity = 1                   # default array capacity
        self.A = self._make_array(self.capacity)   # low-level array
    def is_empty(self):
        # Return True if array is empty
        return self.n == 0
    def __len__(self):
        # Return numbers of elements stored in the array.
        return self.n
    def __getitem__(self, i):
        # Return element at index i.
        if i < 0: 
            i += self.n
        # Check it i index is in bounds of array
        return self.A[i]
    def append(self, obj):
        # Add object to end of the array.
        if self.n == self.capacity:
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
    def _make_array(self, c):
        # Return new array with capacity c. 
        return (c * ctypes.py_object)()


if __name__ == '__main__':
    mylist = DynamicArray()
    # Append new element
    mylist.append(4)
    mylist.append(1)
    mylist.append(3)
    print(mylist[-3])
    print(mylist[-2])
    print(mylist[-1])
    print(mylist[0])
    print(mylist[1])
    print(mylist[2]) 


# Output:

"""
4
1
3
4
1
3
"""

#---------------------------------------------------------------------------------------------------


# (2).Complete code including A[-1] condition 


import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        # Create an empty array.
        self.n = 0                          # count actual elements
        self.capacity = 1                   # default array capacity
        self.A = self._make_array(self.capacity)   # low-level array
    def is_empty(self):
        # Return True if array is empty
        return self.n == 0
    def __len__(self):
        # Return numbers of elements stored in the array.
        return self.n
    """
    def __getitem__(self, i):
        if self.n > i >= 0:
            return self.A[i]
        else:
            return self.A[i-1]
    """
    def __getitem__(self, i):
        if  0 <= i < self.n:
            return self.A[i]
        elif i < 0:
            return self.A[i-1] 
        else:
            return self.A[-1]    
    def append(self, obj):
        # Add object to end of the array.
        if self.n == self.capacity:
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
    def _make_array(self, c):
        # Return new array with capacity c. 
        return (c * ctypes.py_object)()


if __name__ == '__main__':
    mylist = DynamicArray()
    # Append new element
    mylist.append(4)
    mylist.append(1)
    mylist.append(3)
    print(mylist[-3])
    print(mylist[-2])
    print(mylist[-1])
    print(mylist[0])
    print(mylist[1])
    print(mylist[2])


# Output:

"""
4
1
3
4
1
3
"""

#---------------------------------------------------------------------------------------------------


# (3).Set the conditin as 0 <= i < self.n:


import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        # Create an empty array.
        self.n = 0                          # count actual elements
        self.capacity = 1                   # default array capacity
        self.A = self._make_array(self.capacity)   # low-level array
    def is_empty(self):
        # Return True if array is empty
        return self.n == 0
    def __len__(self):
        # Return numbers of elements stored in the array.
        return self.n
    def __getitem__(self, i):
        if 0 <= i < self.n:
            return self.A[i]
        else:
            return self.A[i-1]
    def append(self, obj):
        # Add object to end of the array.
        if self.n == self.capacity:
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
    def _make_array(self, c):
        # Return new array with capacity c. 
        return (c * ctypes.py_object)()


if __name__ == '__main__':
    mylist = DynamicArray()
    # Append new element
    mylist.append(4)
    mylist.append(1)
    mylist.append(3)
    print(mylist[-3])
    print(mylist[-2])
    print(mylist[-1])
    print(mylist[0])
    print(mylist[1])
    print(mylist[2])


# The output is as sames as above

#---------------------------------------------------------------------------------------------------


# (4).self.A[i-1] support negative index 


import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        # Create an empty array.
        self.n = 0                          # count actual elements
        self.capacity = 1                   # default array capacity
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
            # self.A[i-1] to support negative index
            return self.A[i-1]
        else:
            return self.A[i]
    def append(self, obj):
        # Add object to end of the array.
        if self.n == self.capacity:
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
    def _make_array(self, c):
        # Return new array with capacity c. 
        return (c * ctypes.py_object)()


if __name__ == '__main__':
    mylist = DynamicArray()
    # Append new element
    mylist.append(4)
    mylist.append(1)
    mylist.append(3)
    print(mylist[-3])
    print(mylist[-2])
    print(mylist[-1])
    print(mylist[0])
    print(mylist[1])
    print(mylist[2]) 

####################################################################################################


# R5.6 Our implementation of insert for the DynamicArray class, as given in Code 
# Fragment 5.5, has the following inefficiency. In the case when a resize occurs, 
# the resize operation takes time to copy all the elements from an old array to 
# a new array, and then the subsequent loop in the body of insert shifts many of 
# those elements. Give an improved implementation of the insert method, so that, 
# in the case of a resize, the elements are shifted into their final position 
# during that operation, thereby avoiding the subsequent shifting.


# (1). Define the subclass DynamicInsert


import ctypes
import time


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        # Create an empty array.
        self.n = 0                          # count actual elements
        self.capacity = 1                   # default array capacity
        self.A = self._make_array(self.capacity)   # low-level array
    def is_empty(self):
        # Return True if array is empty
        return self.n == 0
    def __len__(self):
        # Return numbers of elements stored in the array.
        return self.n
    def __getitem__(self, i):
        # Return element at index i.
        if i < 0: 
            i += self.n
        # Check it i index is in bounds of array
        return self.A[i]
    def append(self, obj):
        # Add object to end of the array.
        if self.n == self.capacity:
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
    def insert(self, k, value):
        # Insert value at index k
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
    def _make_array(self, c):
        # Return new array with capacity c. 
        return (c * ctypes.py_object)()


class DynamicInsert(DynamicArray):
    """A dynamic array class akin to a simplified Python list"""
    def __init__(self):
        # Create an empty array
        super().__init__()
    def improved_insert(self, k, value):
        # Insert value at index k, shifting subsequent value rightward
        if self.n == self.capacity:
            B = self._make_array(2*self.capacity)
            for i in range(k):
                B[i] = self.A[k]
            B[k] = value
            for i in range(k, self.n):
                B[i+1] = self.A[i]
            self.A = B
            self.capacity *= 2
        else:
            for i in range(self.n, k, -1):
                self.A[i] = self.A[i-1]
            self.A[k] = value
        self.n += 1


if __name__ == '__main__':
    insert_num = [i * 500 for i in range(1, 10)]
    time_orig = []
    time_impr = []
    darray = DynamicInsert()
    darray.append(4)
    darray.append(3)
    darray.append(2)
    darray.append(1)
    darray.append(0)
    for trial in insert_num:
        start = time.time()
        for i in range(trial):
            darray.improved_insert(0, -1)
        end = time.time()
        time_impr.append(end-start)
    print(time_impr)


# Output:

"""
[0.05279231071472168, 0.37353038787841797, 1.285707950592041, 2.907965898513794, 5.7804248332977295, 
9.873901605606079, 15.712406158447266, 23.43644070625305, 34.09468197822571]
"""

#---------------------------------------------------------------------------------------------------


# (2).Do not use the class heritance 
# Add "_" underscore before the attributes for forming self._n, self._capacity and
# self._A.


import ctypes
import time


class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""
    def __init__(self):
        # Create an empty array.
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    def __len__(self):
        # Return number of elements stored in the array
        return self._n
    def __getitem__(self, k):
        if 0<= k < self._n:
            return self._A[k]
        else:
            return self._A[k - 1]
    def append(self, obj):
        # Add object to end of the array.
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):
        # Resize internal array to capacity c.
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    def _make_array(self, c):
        # Return new array with capacity c.
        return (c * ctypes.py_object)()
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
    def improved_insert(self, k, value):
        if self._n == self._capacity:
            tmp = self._make_array(2 * self._capacity)
            self._capacity *= 2
            tmp[:k] = self._A[:k]
            tmp[k + 1: k + len(self._A[k:]) + 1] = self._A[k:]
            self._A = tmp
        else:
            self._A[k + 1 : self._n + 1] = self._A[k: self._n]
        self._A[k] = value
        self._n += 1


if __name__ == '__main__':
    insert_num = [i * 500 for i in range(1, 10)]
    time_orig = []
    time_impr = []
    darray = DynamicArray()
    darray.append(4)
    darray.append(3)
    darray.append(2)
    darray.append(1)
    darray.append(0)
    for trial in insert_num:
        start = time.time()
        for i in range(trial):
            darray.improved_insert(0, -1)
        end = time.time()
        time_impr.append(end-start)
    print(time_impr)


# Output:

"""
[0.03439450263977051, 0.21795964241027832, 0.7297482490539551, 1.7753376960754395, 
 3.4645192623138428, 6.044097185134888, 9.50731873512268, 14.284402132034302, 
 21.041977405548096]
"""

####################################################################################################


#　R5.7 FLet A be an array of size n ≥ 2 containing integers from 1 to n − 1, inclusive, 
# with exactly one repeated. Describe a fast algorithm for finding the integer in A that 
# is repeated.


# (1).Use list comprehension 


def find_repeat(numbers): 
    # numbers = find_repeat()
    duplicates = [number for number in numbers if numbers.count(number) > 1]
    # unique_duplicates = *set(duplicates)
    unique_duplicates = list(set(duplicates))
    return unique_duplicates


if __name__ == '__main__':
    numbers = [5,11,3,5,8,2,6,7]
    find_repeat(numbers)

# Output:
"""
[5]
"""

#---------------------------------------------------------------------------------------------------

# (2). Adopt dict() method 


def find_repeat(numbers): 
    duplicates = [number for number in numbers if numbers.count(number) > 1]
    # unique_duplicates = *set(duplicates)
    unique_duplicates = list(set(duplicates))
    return unique_duplicates


if __name__ == '__main__':
    # numbers = [1,2,3,3,4,5,6]
    numbers = [5,11,3,5,8,2,6,7]
    dnumbers = find_repeat(numbers)
    print(dnumbers)

# Output:

"""
[5]
"""

####################################################################################################


# R5.8 Experimentally evaluate the efficiency of the pop method of Python’s list class 
# when using varying indices as a parameter, as we did for insert on page 205. Report 
# your results akin to Table 5.5.


# (1).Adopt insert() and pop() functions 


from time import time
import pandas as pd


def benchmark(test_func):
    insert_df = pd.DataFrame(index=['start', 'middle', 'end'],
                             columns=['100', '1000', '10000', '100000'])
    insert_df.index.name = 'Time(microseconds)'
    for n in list(insert_df.columns):
        insert_df[n] = [test_func(int(n), mode) for mode in insert_df.index]
    return insert_df


# insert test

def insert_average(n, mode='start'):
    data = []
    start = time()
    if mode == 'start':
        for _ in range(n):
            data.insert(0, None)
    elif mode == 'middle':
        for _ in range(n):
            data.insert(n//2, None)
    elif mode == 'end':
        for _ in range(n):        
            data.insert(n, None)
    end = time()
    return (end - start) * 1000000 / n


# poptest

def pop_average(n, mode='start'):
    data = [None] * n
    start = time()
    if mode == 'start':
        for _ in range(n):
            data.pop(0)
    elif mode == 'middle':
        count = n
        while count > 0:
            data.pop(count // 2)
            count -= 1
    elif mode == 'end':
        for _ in range(n):
            data.pop(-1)
    end = time()
    return (end - start) * 1000000 / n


if __name__ == '__main__':
    benchmark(insert_average)
    benchmark(pop_average)


# Output:

"""
                         100      1000     10000     100000
Time(microseconds)                                         
start               0.283718  0.434160  3.403783  29.967792
middle              0.312328  0.224113  0.905299   7.548211
end                 0.207424  0.110626  0.108933   0.103683
                         100      1000     10000     100000
Time(microseconds)                                         
start               0.152588  0.234127  1.403522  17.540274
middle              0.183582  0.240326  0.767255   7.455316
end                 0.107288  0.103712  0.099182   0.101004

"""

#---------------------------------------------------------------------------------------------------


# (2).Define time_pops() functions


import time
import pandas as pd
import matplotlib.pyplot as plt


def time_pops(test_array):
    results = pd.DataFrame()
    for test_len in test_array: 
        for position in [0, 0.5, 1]:
            start = time.time()
            for _ in range (100):    # Lower this to speed up the program
                data = [None] * test_len
                while len(data) > 1: # stop early to avoid a negative index
                    data.pop(int((len(data)-1)*position))
            end = time.time()
            results.loc[position, test_len] = (end-start)/test_len
    return results


if __name__ == '__main__':
    test_array = [10**i for i in range(2, 6)]
    results = time_pops(test_array)
    for i in range(len(results)):
        plt.plot(results.iloc[i])
    plt.legend()
    plt.show()
    print(results)


# Output:

"""
[<matplotlib.lines.Line2D object at 0x7fd9b8825c90>]
[<matplotlib.lines.Line2D object at 0x7fd9ac058cd0>]
[<matplotlib.lines.Line2D object at 0x7fd9a712b250>]
No handles with labels found to put in legend.
<matplotlib.legend.Legend object at 0x7fd9b8c89810>
       100       1000      10000     100000
0.0  0.000038  0.000051  0.000170  0.001811
0.5  0.000043  0.000049  0.000107  0.000787
1.0  0.000036  0.000038  0.000040  0.000040
"""

#---------------------------------------------------------------------------------------------------


# (3).Adopt enumerate() and range()


import timeit


Ns = []

# creating result lists
k_0 = []
k_equal_n_over_2 = []
k_equal_n = []
running_times = [k_0, k_equal_n_over_2, k_equal_n]

min_N_magnitude = 2
max_N_magnitude = 6

ks = ["0", "n//2", "-1"]


# Verifying runtime
for index, running_time in enumerate(running_times):
    for new_int in range(min_N_magnitude, max_N_magnitude):
        n = 10**new_int
        Ns.append(n)
        j = n//10   # testing the method on n//10 elements
        stmt = """
for i in range({}):
    lst.pop({})""".format(j, ks[index])
        setup = """n = {}

lst = [i for i in range(n)]""".format(n)
        t = timeit.Timer(stmt, setup=setup)
        number = 10  # number of repetition to obtain average result
        total_time = sum(t.repeat(number, 1))
        avg_time = total_time / (number*j)  # divide by number and by j


if __name__ == '__main__':
    print("""\n
    Average runtime of using pop() method on n/10 element of lists of length n
    Lines test for varying positions for the index k, pop(k) for k = 0, n//2, n
    Rows test for varying lengths of the list, going from {} to {} by factors of 10\n""".format(min_N_magnitude, max_N_magnitude-1))
    [print(i) for i in running_times]
    print("""\n
    It is clear that using pop() at the end of the list is O(1), 
    but using it at the beginning or in the middle is O(n)""")


# Output:

"""

    Average runtime of using pop() method on n/10 element of lists of length n
    Lines test for varying positions for the index k, pop(k) for k = 0, n//2, n
    Rows test for varying lengths of the list, going from 2 to 5 by factors of 10

[1.9656006770674138e-07, 6.621729990001768e-07, 3.4648291984922253e-06, 3.576458442999865e-05]
[1.9661012629512697e-07, 2.5768801424419507e-07, 1.3429586993879638e-06, 1.4868392960052006e-05]
[1.5314006304834038e-07, 9.696299821371213e-08, 1.0140689992113039e-07, 1.09088979952503e-07]
[None, None, None]


    It is clear that using pop() at the end of the list is O(1), 
    but using it at the beginning or in the middle is O(n)
"""

####################################################################################################


# R5.9 Explain the changes that would have to be made to the program of Code Fragment 
# 5.11 so that it could perform the Caesar cipher for messages that are written in an 
# alphabet-based language other than English, such as Greek, Russian, or Hebrew.


# (1).Define Caesarpher class for Greek 


class CaesarCipher():
    def __init__(self, shift, language = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        ll = sorted(list(language)) #ll = language_list
        lang_len = len(ll)
        self._encoder = {}
        self._decoder = {}
        for i in range(lang_len):
            self._encoder[ll[i]] = ll[(i+shift)%lang_len]
            self._decoder[ll[i]] = ll[(i-shift)%lang_len]
    def encrypt(self, message):
        return self._transform(message, self._encoder)
    def decrypt(self, message):
        return self._transform(message, self._decoder)
    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k] in code:  #This is an O(1) check because code is a dictionary
                msg[k] = code[msg[k]]
        return ''.join(msg)


if __name__ == '__main__':
    print('English Cipher')
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Answer: ', answer)
    print('\nGreek Cipher')
    cipher_greek = CaesarCipher(3, language='ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσςΤτΥυΦφΧχΨψΩω')
    message = "μηδείς αγεωµετρητος εισιτω µον την στεγην"
    coded = cipher_greek.encrypt(message)
    print('Secret: ', coded)
    answer = cipher_greek.decrypt(coded)
    print('Answer: ', answer)


# Output:

"""
English Cipher
Secret:  WKH HDJOH LV LQ SODB; PHHW DW MRH'V
Answer:  THE EAGLE IS IN PLAY; MEET AT JOE'S

Greek Cipher
Secret:  οκηθίυ δζθΓµθχτκχςυ θμφμχΓ µςπ χκπ φχθζκπ
Answer:  μηδείς αγεωµετρητος εισιτω µον την στεγην
"""

#---------------------------------------------------------------------------------------------------


# (2).Define Caesarpher class for Cyrillic


class CaesarCipher():
    def __init__(self, shift, language = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        ll = sorted(list(language)) #ll = language_list
        lang_len = len(ll)
        self._encoder = {}
        self._decoder = {}
        for i in range(lang_len):
            self._encoder[ll[i]] = ll[(i+shift)%lang_len]
            self._decoder[ll[i]] = ll[(i-shift)%lang_len]
    def encrypt(self, message):
        return self._transform(message, self._encoder)
    def decrypt(self, message):
        return self._transform(message, self._decoder)
    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k] in code:  #This is an O(1) check because code is a dictionary
                msg[k] = code[msg[k]]
        return ''.join(msg)


if __name__ == '__main__':
    print('English Cipher')
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Answer: ', answer)
    print('\nCyrillic Cipher')
    cipher_cyrillic = CaesarCipher(3, language='АБВГҐДЂЃЕЀЁЄЖЗЗ́ЅИЍІЇЙЈКЛЉМНЊОПРСС́ТЋЌУЎФХЦЧЏШЩЪЫЬЭЮЯ')
    message = "μηδείς αγεωµετρητος εισιτω µον την στεγην"
    coded = cipher_cyrillic.encrypt(message)
    print('Secret: ', coded)
    answer = cipher_cyrillic.decrypt(coded)
    print('Answer: ', answer)


# Output:

"""
English Cipher
Secret:  WKH HDJOH LV LQ SODB; PHHW DW MRH'V
Answer:  THE EAGLE IS IN PLAY; MEET AT JOE'S

Cyrillic Cipher
Secret:  μηδείς αγεωµετρητος εισιτω µον την στεγην
Answer:  μηδείς αγεωµετρητος εισιτω µον την στεγην
>>> 

"""

####################################################################################################


# 5.10 The constructor for the CaesarCipher class in Code Fragment 5.11 can be 
# implemented with a two-line body by building the forward and backward strings 
# using a combination of the join method and an appropriate comprehension syntax. 
# Give such an implementation.


# (1).Use join() method to rewrite CaesarCipher class

class CaesarCipher:
    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder = [None] * 26  # temp array for encryption
        decoder = [None] * 26  # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)  # will store as string
        self._backward = ''.join(decoder)  # since fixed
    def encrypt(self, message):
        return self._transform(message, self._forward)
    def decrypt(self, message):
        return self._transform(message, self._backward)
    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Answer: ', answer)


# Output:

"""
Secret:  WKH HDJOH LV LQ SODB; PHHW DW MRH'V
Answer:  THE EAGLE IS IN PLAY; MEET AT JOE'S
"""

#---------------------------------------------------------------------------------------------------


# (2).Use simplified join() method to rewrite CaesarCipher class


class CaesarCipher:
    def __init__(self, shift):
        self._forward = "".join([chr((k + shift) % 26 + ord("A")) for k in range(26)])
        self._backward = "".join([chr((k - shift) % 26 + ord("A")) for k in range(26)])
    def encrypt(self, message):
        return self._transform(message, self._forward)
    def decrypt(self, message):
        return self._transform(message, self._backward)
    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Answer: ', answer)


# Output:

"""
Secret:  WKH HDJOH LV LQ SODB; PHHW DW MRH'V
Answer:  THE EAGLE IS IN PLAY; MEET AT JOE'S
"""
####################################################################################################


# R5.11 Use standard control structures to compute the sum of all numbers in an n × n 
# data set, represented as a list of lists.


# (1).Gaussian Sum：1 + 2 + 3 + ... + n


def sum_2d(array):
    total = 0
    for i in range(len(array)):   #loop over the outer list
        for j in range(len(array[i])):
            total += array[i][j]
    return total


if __name__ == '__main__':
    # Create a list from 1 to 100, which should have the sum (101)(100)/2 = 5050
    list_of_lists = [list(range(i, i+10)) for i in range(1,100, 10)]
    print(sum_2d(list_of_lists))


# Output:

"""
5050
"""

#---------------------------------------------------------------------------------------------------


# (2).Array works as double lists

def sum_list_of_list(lst):
    total = 0
    for line in lst:
        for element in line:
            total += element
    return total


if __name__ == '__main__':
    n = 3
    my_list = [[n*j + i  for i in range(3)] for j in range(3)]
    print(my_list)
    print(sum_list_of_list(my_list))


# Output:

"""
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
36
"""

#---------------------------------------------------------------------------------------------------


# (3).Sum for simple two dimentoinal array


from typing import List, TypeVar
Num = TypeVar('Num', int, float)


def sum_matrix(matrix: List[List[Num]]) -> Num:
    total = 0
    for column in matrix:
        for row in column:
            total += row
    return total


if __name__ == '__main__':
    sum_matrix([[1, 2], [3, 4]])


# Output:

"""
10
"""

####################################################################################################


# R5.12 Describe how the built-in sum function can be combined with Python’s list 
# comprehension syntax to compute the sum of all numbers in an n × n data set, 
# represented as a list of lists.


# (1).List comprehension


def func(n):
    my_list = [[n*j + i for i in range(3)] for j in range(3)]
    return my_list


if __name__ == '__main__':
    my_list = func(n=3)
    total = sum([sum(line) for line in my_list])
    print(my_list)
    print(total)


# Output:

"""
>>> print(my_list)
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
>>> print(total)
36
"""
#---------------------------------------------------------------------------------------------------


# (2).Use generator comprehension


from typing import List, TypeVar
Num = TypeVar('Num', int, float)


def sum_matrix_plus(matrix: List[List[Num]]) -> Num:
    return sum(num for raw in matrix for num in raw)


if __name__ == '__main__':
    sum_matrix_plus([[1, 2], [3, 4]])


# Output:

"""
10
"""  

####################################################################################################
####################################################################################################


# Part Two. Creativity


####################################################################################################


# C5.13 In the experiment of Code Fragment 5.1, we begin with an empty list. If data 
# vwere initially constructed with nonempty length, does this affect the sequence of 
# vvalues at which the underlying array is expanded? Perform your own experiments, 
# and comment on any relationship you see between the initial length and the expansion 
#v sequence.


# (1). Call the array_jump() function 

import sys
import matplotlib.pyplot as plt


def array_jump(n, initial_length=0):
    data = [None] * initial_length
    size_old = 0
    data_jumps = []
    for i in range(n):
        size = sys.getsizeof(data)
        if size != size_old:
            data_jumps.append(len(data))
        size_old = size
        data.append([None])
    return data_jumps


if __name__ == '__main__':
    result = array_jump(10000, 0)
    x = list(range(len(result)))
    plt.plot(x, result, label='Actual')
    plt.plot(list(range(20)), [2**i for i in range(20)], label='If doubling')
    plt.ylim((0, 10000))
    plt.legend()
    plt.show()


# Output:

"""
[<matplotlib.lines.Line2D object at 0x7f3a6b2d8f90>]
[<matplotlib.lines.Line2D object at 0x7f3a6b2e9590>]
(0.0, 10000.0)
<matplotlib.legend.Legend object at 0x7f3a6b2e9390>
"""

#---------------------------------------------------------------------------------------------------


# (2).Test the array

import sys
import matplotlib.pyplot as plt


def array_jump(n, initial_length=0):
    data = [None] * initial_length
    size_old = 0
    data_jumps = []
    for i in range(n):
        size = sys.getsizeof(data)
        if size != size_old:
            data_jumps.append(len(data))
        size_old = size
        data.append([None])
    return data_jumps


if __name__ == '__main__':
    test_array = [0, 4, 25, 106, 526, 527]
    print('Jumping Lengths')
    for x in test_array:
        print(f'The results for {x} are: ', end = '')
        print(array_jump(10000, x))
        print('\n')
    print('Growth comparisons')
    for x in test_array:
        print(f'The relative lengths for {x} are: ', end = '')
        print([(a-x) for a in array_jump(10000, x)])
        print('\n')


# Output:

"""
Jumping Lengths
The results for 0 are: [0, 1, 5, 9, 17, 26, 36, 47, 59, 73, 89, 107, 127, 149, 174, 202, 
234, 270, 310, 355, 406, 463, 527, 599, 680, 772, 875, 991, 1121, 1268, 1433, 1619, 1828, 
2063, 2327, 2624, 2959, 3335, 3758, 4234, 4770, 5373, 6051, 6814, 7672, 8638, 9724]

The results for 4 are: [4, 5, 9, 17, 26, 36, 47, 59, 73, 89, 107, 127, 149, 174, 202, 234, 
270, 310, 355, 406, 463, 527, 599, 680, 772, 875, 991, 1121, 1268, 1433, 1619, 1828, 2063, 
2327, 2624, 2959, 3335, 3758, 4234, 4770, 5373, 6051, 6814, 7672, 8638, 9724]
...
"""

####################################################################################################


# C5.14 The shuffle method, supported by the random module, takes a Python list and r
# earranges it so that every possible ordering is equally likely. Implement your own 
# version of such a function. You may rely on the randrange(n) function of the random 
# module, which returns a random number between 0 and n − 1 inclusive.


# (1).Use the lambda function 


import random
from typing import List, TypeVar
Num = TypeVar('Num', int, float)


def shuffule(nums: List[Num]) -> List[Num]:
    return sorted(nums, key=lambda x: random.random())


if __name__ == '__main__':
    l = list(range(8))
    print(shuffule(l))
    print(shuffule(l))
    print(shuffule(l))


# Output:

"""
[2, 1, 7, 4, 5, 0, 6, 3]
[5, 1, 7, 3, 2, 4, 6, 0]
[4, 6, 5, 0, 7, 3, 1, 2]
"""

#---------------------------------------------------------------------------------------------------


# (2).Use list() with enumerate() and randrange(n)


from random import randrange 


def shuffle(lst):
    n = len(lst)
    for index, value in enumerate(lst):
        new_index = randrange(n)
        lst[index], lst[new_index] = lst[new_index], lst[index]
    return lst


if __name__ == '__main__':
    lst = list(range(10))
    print(lst)
    lst = shuffle(lst)
    print(lst)


# Output:

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 4, 5, 0, 7, 6, 8, 9, 2, 3]
"""

#---------------------------------------------------------------------------------------------------


# (3).Use shuffle() and randrange(n) with returning random number between 0~n-1


import random


def shuffle(array):
    for i in range(len(array)):
        index = random.randrange(len(array)-i)+i 
        array[i], array[index] = array[index], array[i] # swap positions
    return (a)


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,0]
    shuffle(a)
    total_ints = []
    n_tests = 100000
    for _ in range(n_tests):
        shuffle(a)
        total_ints.append(a[0])
    # Test if all of the values are equally likely to be in the first position 
    for i in range(10):
        print(f'Count of {i} is: {total_ints.count(i)} \t {(total_ints.count(i)/n_tests *100):.2f}%')


# Output:

"""
...
[2, 5, 1, 8, 7, 6, 4, 0, 3, 9]
[3, 8, 0, 6, 9, 2, 4, 1, 7, 5]
[0, 2, 3, 4, 9, 8, 6, 1, 7, 5]
Count of 0 is: 9913      9.91%
Count of 1 is: 10006     10.01%
Count of 2 is: 10049     10.05%
Count of 3 is: 9834      9.83%
Count of 4 is: 10052     10.05%
Count of 5 is: 9987      9.99%
Count of 6 is: 10118     10.12%
Count of 7 is: 10048     10.05%
Count of 8 is: 10113     10.11%
Count of 9 is: 9880      9.88%
"""

####################################################################################################


# C 5.15 Consider an implementation of a dynamic array, but instead of copying the 
# elements into an array of double the size (that is, from N to 2N) when its capacity 
# is reached, we copy the elements into an array with N/4 additional cells, going 
# from capacity N to capacity N + N/4. Prove that performing a sequence of n append 
# operations still runs in O(n) time in this case.


# Omit: N + N/4 Expansion of Array Size


####################################################################################################


# C5.16 Implement a pop method for the DynamicArray class, given in Code Fragment 
# 5.3, that removes the last element of the array, and that shrinks the capacity, N, 
# of the array by half any time the number of elements in the array goes below N/4.


# (1).Inherit DynamicArray class 


import ctypes

class DynamicArray():
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    def __len__(self):
        return self._n
    def __getitem__(self, k):
        if not 0<=k <self._n:
            raise IndexError('invalid index')
        else:
            return self._A[k]
    def append(self, obj):
        if self._n == self._capacity:
            print('Growing to c:', 2*self._capacity, self._n)
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):
        temp = self._make_array(c)
        for k in range(self._n):
            temp[k] = self._A[k]
        self._A = temp
        self._capacity = c
    def _insert_resize(self, c, k):
        # Don't add anything, just leave a space for the future insertion
        B = self._make_array(c)
        for i in range(self._n):
            if i < k: 
                temp[i] = self._A[i]
            else: 
                temp[i+1] = self._A[i]
        self._A = temp
        self._capacity = c 
    def insert(self, k, value):
        if self._n == self._capacity:
            self._insert_resize(2*self._capacity, k)
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
    def _make_array(self, c):
        # return (c*ctypes.py_object)()
        return ([None]*c)
    

class DynamicArrayShrink(DynamicArray):
    """
    important class variables:
    _A: the array
    _capacity: the capacity
    _n the number of items in the array
    """
    def pop(self):
        if self._n == 0: raise IndexError('The list is empty')
        ans = self[self._n-1]
        self._n-=1       
        if self._n < self._capacity/4:
            print('Shrinking array to', self._capacity//2, 'from', self._capacity,  'n:', self._n)
            self._resize(self._capacity//2)
        return ans


if __name__ == '__main__':       
    array = DynamicArrayShrink()
    for i in range(100):
        array.append(i)
    for i in range(100):
        array.pop()


# Output:


"""
Growing to c: 2 1
Growing to c: 4 2
Growing to c: 8 4
Growing to c: 16 8
Growing to c: 32 16
Growing to c: 64 32
Growing to c: 128 64
99
98
97
...
38
37
36
35
34
33
32
Shrinking array to 64 from 128 n: 31
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
Shrinking array to 32 from 64 n: 15
15
14
13
12
11
10
9
8
"""

#---------------------------------------------------------------------------------------------------


# (2).print length and capacity 


import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""
    def __init__(self):
        # Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    def __len__(self):
        # Return number of elements stored in the array
        return self._n
    def __getitem__(self, k):
        if 0<= k < self._n:
            return self._A[k]
        else:
            return self._A[k - 1]
    def append(self, obj):
        # Add object to end of the array.
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):
        # Resize internal array to capacity c.
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    def _make_array(self, c):
        # Return new array with capacity c.
        return (c * ctypes.py_object)()
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
    def pop(self):
        value = x._A[self._n - 1]
        x._A[self._n - 1] = None
        self._n -= 1
        if self._n < self._capacity // 4:
            print("Reducing capacity from {} to {}".format(self._capacity, self._capacity//2))
            self._resize(self._capacity // 2)        
        return value


if __name__ == '__main__':  
    x = DynamicArray()
    for i in range(200):
        x.append(i)
    print(len(x))
    print(x._capacity)       
    for i in range(192):
        x.pop()
    print(len(x))
    print(x._capacity)


# Output:

"""
200
256
...
"""

####################################################################################################


# C5.17 Prove that when using a dynamic array that grows and shrinks as in the previous 
# exercise, the following series of 2n operations takes O(n) time: n append operations 
# on an initially empty array, followed by n pop operations.


# (1).2n operations with O(n): append(obj) based on the empty array and then 
# pop() operation


import time
import ctypes


class DynamicArrayTimed():
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    def timer(fnc):
        def wrapper(*args, **kwargs):
            start = time.time()
            for i in range(1000):
                fnc(*args, **kwargs)
            end = time.time()
            return (end-start)
        return wrapper
    def __len__(self):
        return self._n
    def __getitem__(self, k):
        if not 0<=k <self._n:
            raise IndexError('invalid index')
        else:
            return self._A[k]
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c  
    def _insert_resize(self, c, k):
        #Don't add anything here, just leave a space for the future insertion
        B = self._make_array(c)
        for i in range(self._n):
            if i<k: B[i] = self._A[i]
            else: B[i+1] = self._A[i]
        self._A = B
        self._capacity = c 
    def insert(self, k, value):
        if self._n == self._capacity:
            self._insert_resize(2*self._capacity, k)
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1  
    def pop(self):
        if self._n == 0: raise IndexError('The list is empty')
        ans = self[self._n-1]
        self._n-=1       
        if self._n < self._capacity/4:
            self._resize(self._capacity//2)
        return ans
    def _make_array(self, c):
        #return (c*ctypes.py_object)()
        return ([None]*c)
    @timer
    def _append_pop(self, tests):
        for i in range(tests):
            self.append(None)    
        for i in range(tests):
            self.pop()
        return None
    def test_append_pop(self, tests):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        return (self._append_pop(tests))


if __name__ == '__main__':     
    dat = DynamicArrayTimed()
    for n in [10, 100, 1000, 10000, 100000]:
        print(f'The average time for {n} is {dat.test_append_pop(n)/n}')


# Output:

"""
The average time for 10 is 0.0024031400680541992
The average time for 100 is 0.0012339162826538086
The average time for 1000 is 0.0011735885143280029
...
"""

#---------------------------------------------------------------------------------------------------


# (2).Adopt list comprehension to call the method


import time
import ctypes
import matplotlib.pyplot as plt


class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""
    def __init__(self):
        # Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    def __len__(self):
        # Return number of elements stored in the array
        return self._n
    def __getitem__(self, k):
        if 0<= k < self._n:
            return self._A[k]
        else:
            return self._A[k - 1]
    def append(self, obj):
        # Add object to end of the array.
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):
        # Resize internal array to capacity c.
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    def _make_array(self, c):
        # Return new array with capacity c.
        return (c * ctypes.py_object)()
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
    def pop(self):
        value = x._A[self._n - 1]
        x._A[self._n - 1] = None
        self._n -= 1
        if self._n < self._capacity // 4:
            print("Reducing capacity from {} to {}".format(self._capacity, self._capacity // 2))
            self._resize(self._capacity // 2)        
        return value


if __name__ == '__main__':
    insert_num = [i * 1000 for i in range(1, 300)]
    elapsed = list()
    for i in insert_num:
        start = time.time()
        x = DynamicArray()
        for i in range(i):
            x.append(i)
        for i in range(i):
            x.append(i)
        end = time.time()
        elapsed.append(end-start)
    plt.plot(elapsed)
    plt.grid()


# Output:

"""
[<matplotlib.lines.Line2D object at 0x7f1877f41250>]
"""

####################################################################################################


# C5.18 ~ C5.20

# Omit


####################################################################################################


# C5.21 In Section 5.4.2, we described four different ways to compose a long string: 
# (1) repeated concatenation, 
# (2) appending to a temporary list and then joining, 
# (3) using list comprehension with join, 
# (4) using generator comprehension with join. 
# Develop an experiment to test the efficiency of all four of these approaches and 
# report your findings.


# (1).Code with decorator:


import time
import matplotlib.pyplot as plt
import pandas as pd


class string_comparitor():
    def __init__(self, num_tests = 100):
        self._num_tests = num_tests
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(args[0]._num_tests):
                func(*args)
            end = time.time()
            return(end-start)
        return wrapper
    @timer
    def _string_append(self, string):
        S = ''
        for char in string:
            S += char
        return S
    @timer
    def _list_then_join(self, string):
        S = []
        for char in string:
            S.append(char)
        return ''.join(S)
    @timer
    def _join_lc(self, string):
        return ''.join([x for x in string])
    @timer
    def _join_generator(self, string):
        return ''.join(x for x in string)
    def test_methods(self, test_cases):
        results = pd.DataFrame()
        for n in test_cases:
            string = 'a'*n
            for name, func in [('String Append', self._string_append),
                         ('List then Join', self._list_then_join),
                         ('Join List Comprehension', self._join_lc), 
                         ('Join Generator', self._join_generator)]:
                results.loc[name, n] = func(string)/n
        return results
        

if __name__ == '__main__':         
    tester = string_comparitor()
    tester.test_methods([10**x for x in range(8)])      


# Output:

"""
String Append            0.000016  0.000006  0.000005  0.000006  0.000007  0.000007  0.000007
List then Join           0.000031  0.000009  0.000006  0.000006  0.000006  0.000006  0.000006
Join List Comprehension  0.000033  0.000006  0.000004  0.000003  0.000003  0.000003  0.000003
Join Generator           0.000049  0.000009  0.000005  0.000005  0.000004  0.000004  0.000004
"""

#---------------------------------------------------------------------------------------------------


# (2).Need to write timeit into the functions 


import timeit


document = 'Hello, World!' * 1000


def w1_concatenation():
    """
    1.95 ms ± 146 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    """
    letters = ''
    for c in document:
        if c.isalpha():
            letters += c
    return letters


def w2_appending():
    """
    1.71 ms ± 155 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    """
    temp = []
    for c in document:
        if c.isalpha():
            temp.append(c)
    letters = ''.join(temp)
    return letters


def w3_list_comp():
    """
    1.26 ms ± 223 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    """
    letters = ''.join([c for c in document if c.isalpha()])
    return letters


def w4_generator():
    """
    1.66 ms ± 318 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    """
    letters = ''.join(c for c in document if c.isalpha())
    return letters


if __name__ == '__main__':
    timeit.timeit(stmt="w1_concatenation", setup="from __main__ import w1_concatenation", number=1000)
    timeit.repeat(stmt="w1_concatenation", setup="from __main__ import w1_concatenation", number=1000, repeat=3)
    timeit.timeit(stmt="w2_appending", setup="from __main__ import w2_appending", number=1000)
    timeit.repeat(stmt="w2_appending", setup="from __main__ import w2_appending", number=1000, repeat=3)
    timeit.timeit(stmt="w3_list_comp", setup="from __main__ import w3_list_comp", number=1000)
    timeit.repeat(stmt="w3_list_comp", setup="from __main__ import w3_list_comp", number=1000, repeat=3)
    timeit.timeit(stmt="w4_generator", setup="from __main__ import w4_generator", number=1000)
    timeit.repeat(stmt="w4_generator", setup="from __main__ import w4_generator", number=1000, repeat=3)


# Output:

"""
2.6294001145288348e-05
[2.4459997803205624e-05, 2.38799984799698e-05, 2.3688000510446727e-05]
2.4091998056974262e-05
[2.480500188539736e-05, 2.4323999241460115e-05, 2.426599894533865e-05]
2.376200063736178e-05
[2.3462001990992576e-05, 2.316999962204136e-05, 2.3005999537417665e-05]
2.5434001145185903e-05
[2.4144002964021638e-05, 2.3754000721964985e-05, 2.372299786657095e-05]
"""

####################################################################################################


# C5.22 Develop an experiment to compare the relative efficiency of the extend method 
# of Python’s list class versus using repeated calls to append to accomplish the 
# equivalent task.


# (1). Compare list.append(obj) and list.extend()


import time


def append2extend(i):
    l1 = []
    t1 = time.time()
    for i in range(i):
        l1.append(None)
    t2 = time.time()
    print('append:{}'.format(t2 - t1), end='\n')
    l1 = []
    t1 = time.time()
    for i in range(i):
        l1.extend((None,))
    t2 = time.time()
    print('extend:{}'.format(t2 - t1), end='\n')
    l1 = []
    l2 = [1, 2, 3]
    t1 = time.time()
    for i in range(i):
        for j in l2:
            l1.append(j)
    t2 = time.time()
    print('append:{}'.format(t2 - t1), end='\n')
    l1 = []
    l2 = [1, 2, 3]
    t1 = time.time()
    for i in range(i):
        l1.extend(l2)
    t2 = time.time()
    print('extend:{}'.format(t2 - t1), end='\n')


if __name__ == '__main__':
    append2extend(1000)


# Output:

"""
append:0.00014400482177734375
extend:0.00014162063598632812
append:0.00043010711669921875
extend:0.00014591217041015625
"""

#---------------------------------------------------------------------------------------------------


# (2).Definbe a class 


import time
import matplotlib.pyplot as plt


class ExtensionTester():
    def __init__(self, num_tests=1000):
        self._num_tests = num_tests
    def __call__(self, test_cases, blocksize = 40):
        return (self.tester(test_cases, blocksize))
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(args[0]._num_tests):
                func(*args, **kwargs)
                
            end = time.time()
            return (end-start)
        return wrapper
    @timer
    def _extend_by_append(self, n):
        S = []
        for _ in range(n):
            S.append(None)
    @timer
    def _extend_by_extension(self, n, blocksize):
        S = []
        block = [None]*blocksize
        n_mode = n//blocksize
        for _ in range(n_mode):
            S.extend(block)
    def tester(self, test_cases, blocksize = 40):
        """
        n = final length of the array
        blocksize = chunksize for the extension route
        """
        x = test_cases
        names = ['Append', 'Extend']
        results = [[] for i in range(2)]
        for n in test_cases:
            results[0].append(self._extend_by_append(n)/n)
            results[1].append(self._extend_by_extension(n, blocksize)/(n/blocksize))
        return x, names, results
    

if __name__ == '__main__':  
    test_cases = [10**x for x in range(2, 8)]    
    t = ExtensionTester()
    x, names, results = t(test_cases)         
    for i in range(len(results)):
        plt.plot(x, results[i], label = names[i])
    plt.legend()
    plt.show()


# Output:

"""
[<matplotlib.lines.Line2D object at 0x7f18710137d0>]
[<matplotlib.lines.Line2D object at 0x7f18702eb950>]
<matplotlib.legend.Legend object at 0x7f18702eb7d0>
"""

####################################################################################################


# C5.23 Based on the discussion of page 207, develop an experiment to compare the 
# efficiency of Python’s list comprehension syntax versus the construction of a 
# list by means of repeated calls to append.


# (1). Compare list comprehension and list.append(obj)


import timeit


def compare(i):
    import time
    t1 = time.time()
    l1 = []
    for i in range(i):
        l1.append(i)
    t2 = time.time()
    time1 = t2 - t1
    l1 = []
    t1 = time.time()
    l1 = [i for i in range(i)]
    t2 = time.time()
    time2 = t2 - t1
    return time2 / time1


if __name__ == '__main__':
    compare(1000)


# Output:

"""
0.4144144144144144
"""

#---------------------------------------------------------------------------------------------------


# (2).Define AppendComparitor class


import time
import matplotlib.pyplot as plt
import pandas as pd


class AppendComparitor():
    def __init__(self, num_tests=10000):
        self._num_tests = num_tests
    def __call__(self, test_cases):
        return self.tester(test_cases)
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(args[0]._num_tests):
                func(*args, **kwargs)                   
            end = time.time()
            return end-start
        return wrapper
    @timer
    def _by_comprehension(self, n):
        return [None for i in range(n)]
    @timer
    def _by_append(self, n):
        S = []
        for _ in range(n):
            S.append(None)
        return S
    def tester(self, test_cases):
        results = pd.DataFrame()
        for name, func in [('Append', self._by_append), ('Compehension', self._by_comprehension)]:
            for n in test_cases:
                results.loc[name, n] = func(n)/n      
        return results
 

if __name__ == '__main__': 
    a = AppendComparitor()
    a([10**x for x in range(5)])


# Output:

"""
                 1         10        100       1000      10000
Append        0.007502  0.001042  0.000604  0.000634  0.000657
Compehension  0.004699  0.000666  0.000289  0.000292  0.000307
"""

####################################################################################################


# C5.24 Perform experiments to evaluate the efficiency of the remove method of Python’s 
# list class, as we did for insert on page 205. Use known values so that all removals 
# occur either at the beginning, middle, or end of the list. Report your results akin to 
# Table 5.5.


# (1).Evaluate remove() function 


import pandas as pd
import time
import copy


def func(): 
    N = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
    df = pd.DataFrame(columns=N)
    for n in N:
        lst = [i for i in range(n)]
        rm_fst = copy.deepcopy(lst)
        rm_mid = copy.deepcopy(lst)
        rm_fin = copy.deepcopy(lst)
        elapsed = []
        start = time.time()
        rm_fst.remove(0)
        end = time.time()
        elapsed.append(end - start)
        start = time.time()
        rm_fst.remove(n // 2)
        end = time.time()
        elapsed.append(end - start)
        start = time.time()
        rm_fst.remove(n - 1)
        end = time.time()
        elapsed.append(end - start)
        df[n] = elapsed
    return df


if __name__ == '__main__':
    value = func()
    value.insert(0, column='k', value=['k=0', 'k=n//2', 'k=n'])
    print(value)


# Output:

"""
        k       100      1000     10000    100000   1000000  10000000
0     k=0  0.000001  0.000002  0.000010  0.000098  0.001163  0.014071
1  k=n//2  0.000001  0.000007  0.000063  0.000601  0.006706  0.065763
2     k=n  0.000002  0.000012  0.000117  0.001241  0.011623  0.116585
>>> 
"""

#---------------------------------------------------------------------------------------------------


# (2).Evaluate remove() method: Remove elements in the beginning or middle 


import ctypes
import pandas as pd


class DynamicArray():
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    def __len__(self):
        return self._n
    def __getitem__(self, index):
        if not 0<=index<self._n: 
            raise IndexError('Invalid Index')
        return self._A[index]
    def __repr__(self):
        return (str(self._A[:self._n]))
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
    # It is the original, not the one from R5.6
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None
                self._n -= 1
                return
        raise ValueError('value not found')
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    def _make_array(self, c):
        return [None for _ in range(c)]
    def _subsequent_removes(self, index_mult):
        start = time.time()
        while self._n >0:
            target = self[int((self._n-1)*index_mult)]
            self.remove(target)
        end = time.time()
        return end-start
    def remove_tester(self, test_cases):
        results = pd.DataFrame()
        for mult in [0, 0.5, 1]:
            for n in test_cases:
                # Reconstruct the array
                for i in range(n):
                    self.append(i)
                results.loc[mult, n] = self._subsequent_removes(mult)/n
        return results


if __name__ == '__main__': 
    da = DynamicArray()
    da.remove_tester([10**x for x in range(5)])


# Output:

"""
        1         10        100       1000      10000
0.0  0.000011  0.000005  0.000010  0.000073  0.000744
0.5  0.000005  0.000002  0.000006  0.000054  0.000556
1.0  0.000004  0.000002  0.000004  0.000037  0.000373
"""

####################################################################################################


# R5.25 The syntax data.remove(value) for Python list data removes only the first
# occurrence of element value from the list. Give an implementation of a function, 
# with signature remove all(data, value), that removes all occurrences of value 
# from the given list, such that the worst-case running time of the function is 
# O(n) on a list with n elements. Not that it is not efficient enough in general 
# to rely on repeated calls to remove


import ctypes
import pandas as pd


class DynamicArray():
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    def __len__(self):
        return self._n
    def __getitem__(self, index):
        if not 0<=index<self._n: 
            raise IndexError('Invalid Index')
        return self._A[index]
    def __repr__(self):
        return (str(self._A[:self._n]))
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
    # It is newly created 
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None
                self._n -= 1
                return
        raise ValueError('value not found')
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    def _make_array(self, c):
        return [None for _ in range(c)]
    def _subsequent_removes(self, index_mult):
        start = time.time()
        while self._n >0:
            target = self[int((self._n-1)*index_mult)]
            self.remove(target)
        end = time.time()
        return end-start
    def remove_tester(self, test_cases):
        results = pd.DataFrame()
        for mult in [0, 0.5, 1]:
            for n in test_cases:
                # Reconstruct the array
                for i in range(n):
                    self.append(i)
                results.loc[mult, n] = self._subsequent_removes(mult)/n
        return results


class DynamicArray_RemoveAll(DynamicArray):
    def __setitem__(self, index, value):
        if not 0 <= index < self._n: 
            raise IndexError('Index out of range')
        self._A[index] = value
    def remove_all(self, value):
        num_removed = 0
        for i in range(self._n):
            if self[i] == value:
                num_removed += 1
                self[i] = None # Note this is not necessary since it will be overwritten
            else:
                self[i-num_removed] = self[i]    
        self._n -= num_removed


if __name__ == '__main__': 
    dra = DynamicArray_RemoveAll()
    for i in range(10000):
        if i%100:
            dra.append(i)
        else:
            dra.append(5)
    dra.remove_all(5)
    dra

# Output:

"""
>>> # Many numbers 
"""

####################################################################################################


# C5.26 Let B be an array of size n ≥ 6 containing integers from 1 to n − 5, inclusive, 
# with exactly five repeated. Describe a good algorithm for finding the five integers in 
# B that are repeated. Find 5 repeated elements


# Option 1


def find_repeat(numbers): 
    # numbers = find_repeat()
    duplicates = [number for number in numbers if numbers.count(number) > 1]
    # unique_duplicates = *set(duplicates)
    unique_duplicates = list(set(duplicates))
    return unique_duplicates


if __name__ == '__main__':
    numbers = [5,11,3,5,8,2,6,7,11,12,13,8,3,2,7]
    find_repeat(numbers)


# Output:

"""
# [2, 3, 5, 7, 8, 11]
"""

#---------------------------------------------------------------------------------------------------


# Option 2: 

def find_repeat(A):
    ref = {k:0 for k in A}
    repeated = []
    for e in A:
        ref[e] += 1
    for e in ref:
        if ref[e] > 1:
            repeated.append(e)
    return repeated


if __name__ == '__main__':
    A = [5,11,3,5,8,2,6,7,11,12,13,8,3,2,7]
    find_repeat(numbers)


# Output:

"""
# [2, 3, 5, 7, 8, 11]
"""

#---------------------------------------------------------------------------------------------------


# Option 3


def find_5_set(S):
    prev_nums = set()
    repeats = []
    for element in S:
        if element in prev_nums:
            repeats.append(element)
        else:
            prev_nums.add(element)
    return repeats


def find_5_sorted(S):
    S2 = sorted(S)
    repeats = []
    for i in range(len(S)-1):
        if S2[i] == S2[i+1]: repeats.append(S2[i])
    return repeats


if __name__ == '__main__': 
    S = list(range(100))
    # Insert the repeats
    for index, value in [(4,36), (83, 80), (20, 56), (54, 32), (10, 21)]:
        S[index] = value
    print(find_5_set(S))
    print(find_5_sorted(S))


# Output:

"""
[21, 36, 32, 56, 80]
[21, 32, 36, 56, 80]
"""

####################################################################################################


# C5.27 Given a Python list L of n positive integers, each represented with k =
# logn + 1 bits, describe an O(n)-time method for finding a k-bit integer not in L.


# (1).Adopted from C3.45 Algorithm Analysis


def find_missing(S):
    total_list = list(range(len(S)+1))
    # print(total_list)
    total = 1
    for x in total_list:
        total *= x+1
        print(total)
    for x in S:
        total /= x+1
        print(total)
    return int(total-1)


if __name__ == '__main__':
    find_missing([0,1,2,3,4,6,7,8,9])


# Output:

"""
1
2
6
24
120
720
5040
40320
362880
3628800
3628800.0
1814400.0
604800.0
151200.0
30240.0
4320.0
540.0
60.0
6.0
5
"""

#---------------------------------------------------------------------------------------------------


# (2).Adopted from C3.45 Algo Analysis


import random
import math

def find_missing(S):
    total_list = list(range(len(S)+1))
    # print(total_list)
    total = 1
    for x in total_list: # compute the factorial 10! = 3628800
        total *= x+1
        print(total)
    for x in S:
        total /= x+1
        print(total)
    return int(total-1)


if __name__ == '__main__':
    S = [i for i in range(10)]
    # print(S)
    S.remove(5)
    # S.append(10)
    # print(S)
    find_missing(S)


# Output:

"""
1
2
6
24
120
720
5040
40320
362880
3628800
3628800.0
1814400.0
604800.0
151200.0
30240.0
4320.0
540.0
60.0
6.0
5
"""

####################################################################################################


# C5.29 A useful operation in databases is the natural join. If we view a database
# c as a list of ordered pairs of objects, then the natural join of databases A and 
# B is the list of all ordered triples (x, y, z) such that the pair (x, y) is in A 
# and the pair (y, z) is in B. Describe and analyze an efficient algorithm for computing 
# the natural join of a list A of n pairs and a list B of m pairs.


# (1). Typical example 

def natural_join(A, B):
    # First we create a mapping...
    Y_map = {}
    for x, y in A:
        if y in Y_map: Y_map[y].add(x)
        else: Y_map[y] = set({x})
    natural_join = []
    for y, z in B:
        if y in Y_map:
            natural_join.extend([(x, y, z) for x in Y_map[y]])
    return natural_join


if __name__ == '__main__': 
    A = [(1,1), (1,3), (3,4), (3,5), (5,6), (4,5)]
    B = [(1,4), (1, 5), (4, 2), (5, 1)]
    print('Typical example', natural_join(A, B))


# Output:

"""
Typical example [(1, 1, 4), (1, 1, 5), (3, 4, 2), (3, 5, 1), (4, 5, 1)]
"""

#---------------------------------------------------------------------------------------------------


# (2).Worst Case Example


def natural_join(A, B):
    # First we create a mapping
    Y_map = {}
    for x, y in A:
        if y in Y_map: Y_map[y].add(x)
        else: Y_map[y] = set({x})
    natural_join = []
    for y, z in B:
        if y in Y_map:
            natural_join.extend([(x, y, z) for x in Y_map[y]])
    return natural_join


if __name__ == '__main__': 
    A = [(x, 1) for x in range(10)]
    B = [(1, x) for x in range(10)]
    print('\n\nWorst Case Example', natural_join(A, B))


# Output:

"""
Worst Case Example [(0, 1, 0), (1, 1, 0), (2, 1, 0), (3, 1, 0), (4, 1, 0), (5, 1, 0), 
(6, 1, 0), (7, 1, 0), (8, 1, 0), (9, 1, 0), (0, 1, 1), (1, 1, 1), (2, 1, 1), (3, 1, 1),
(4, 1, 1), (5, 1, 1), (6, 1, 1), (7, 1, 1), (8, 1, 1), (9, 1, 1), (0, 1, 2), (1, 1, 2), 
(2, 1, 2), (3, 1, 2), (4, 1, 2), (5, 1, 2), (6, 1, 2), (7, 1, 2), (8, 1, 2), (9, 1, 2),
(0, 1, 3), (1, 1, 3), (2, 1, 3), (3, 1, 3), (4, 1, 3), (5, 1, 3), (6, 1, 3), (7, 1, 3),
(8, 1, 3), (9, 1, 3), (0, 1, 4), (1, 1, 4), (2, 1, 4), (3, 1, 4), (4, 1, 4), (5, 1, 4), 
(6, 1, 4), (7, 1, 4), (8, 1, 4), (9, 1, 4), (0, 1, 5), (1, 1, 5), (2, 1, 5), (3, 1, 5), 
(4, 1, 5), (5, 1, 5), (6, 1, 5), (7, 1, 5), (8, 1, 5), (9, 1, 5), (0, 1, 6), (1, 1, 6), 
(2, 1, 6), (3, 1, 6), (4, 1, 6), (5, 1, 6), (6, 1, 6), (7, 1, 6), (8, 1, 6), (9, 1, 6), 
(0, 1, 7), (1, 1, 7), (2, 1, 7), (3, 1, 7), (4, 1, 7), (5, 1, 7), (6, 1, 7), (7, 1, 7), 
(8, 1, 7), (9, 1, 7), (0, 1, 8), (1, 1, 8), (2, 1, 8), (3, 1, 8), (4, 1, 8), (5, 1, 8),
(6, 1, 8), (7, 1, 8), (8, 1, 8), (9, 1, 8), (0, 1, 9), (1, 1, 9), (2, 1, 9), (3, 1, 9), 
(4, 1, 9), (5, 1, 9), (6, 1, 9), (7, 1, 9), (8, 1, 9), (9, 1, 9)]
"""

#---------------------------------------------------------------------------------------------------


# (3).Other example


def natural_join(l1,l2):
    dic1 = {}
    dic2 = {}
    if len(l1) > len(l2):
        l1, l2 = l2, l1
    for i in l1:
        dic1[i[0]] = set(i[1])
    for i in l2:
        dic2[i[0]] = set(i[1])
        if i[0] in dic1:
            dic2[i[0]] = dic2[i[0]].union(dic1[i[0]])
        dic2[i[0]].add(i[0])
    return [tuple(dic2[i]) for i in dic2]


if __name__ == '__main__': 
    l1 = [('a','b'),('c','e')]
    l2 = [('a','c')]
    print(natural_join(l1, l2))

# Output:

"""
[('c', 'b', 'a'), ('c', 'e')]
"""

####################################################################################################


# C5.30 Bob Alice Packet: When Bob wants to send Alice a message M on the Internet, 
# the breaks M into n data packets, numbers the packets consecutively, and injects 
# them into the network. When the packets arrive at Alice’s computer, they may
# be out of order, so Alice must assemble the sequence of n packets in order before 
# she can be sure she has the entire message. Describe an efficient scheme for Alice 
# to do this, assuming that she knows the value of n. What is the running time of 
# this algorithm?


# (1). Worst Case Example


import random


def binary_search(array, low, high, target):
    if low>=high:
        return low
    mid = (low+high)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, low, mid-1, target)
    else:
        return binary_search(array, mid+1, high, target)


# Note simulate the order of the packets using a list of integers from 1-10
def packet_reciever(S):
    final_array = []
    for i in range(len(S)):
        packet = S[i] #simulates her recieving that packet
        index = binary_search(final_array, 0, len(final_array), packet)
        index = min(index, len(final_array)-1)
        if final_array and final_array[index] < packet:
            index += 1
        final_array.insert(index, packet)
        print(f'New Packet: {packet} ->', '\t', final_array)


if __name__ == '__main__':         
    S = list(range(17))
    random.shuffle(S)
    packet_reciever(S)


# Output:

"""
New Packet: 11 ->    [11]
New Packet: 13 ->    [11, 13]
New Packet: 14 ->    [11, 13, 14]
New Packet: 1 ->     [1, 11, 13, 14]
New Packet: 5 ->     [1, 5, 11, 13, 14]
New Packet: 9 ->     [1, 5, 9, 11, 13, 14]
New Packet: 10 ->    [1, 5, 9, 10, 11, 13, 14]
New Packet: 15 ->    [1, 5, 9, 10, 11, 13, 14, 15]
New Packet: 3 ->     [1, 3, 5, 9, 10, 11, 13, 14, 15]
New Packet: 6 ->     [1, 3, 5, 6, 9, 10, 11, 13, 14, 15]
New Packet: 8 ->     [1, 3, 5, 6, 8, 9, 10, 11, 13, 14, 15]
New Packet: 4 ->     [1, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15]
New Packet: 12 ->    [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15]
New Packet: 16 ->    [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]
New Packet: 0 ->     [0, 1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]
New Packet: 2 ->     [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]
New Packet: 7 ->     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""

#---------------------------------------------------------------------------------------------------


# (2).Alterative Approach - Insertion Sort!


def insertion_sort(S, current_position):
    i = current_position
    while i>0 and S[i]<S[i-1]: #Note, this will short circuit at i = 0 so you will never check S[0-1]
        S[i], S[i-1] = S[i-1], S[i]
        i -= 1

def packet_reciever_2(S):
    final_array = [None]*len(S)
    for i in range (len(S)):
        final_array[i] = S[i]
        insertion_sort(final_array, i)
        print(f'New Packet: {S[i]} ->', '\t', final_array)


if __name__ == '__main__':         
    print('\n\nApproach 2 - Insertion Sort')        
    packet_reciever_2(S)


# Output:

"""
Approach 2 - Insertion Sort
New Packet: 11 ->    [11, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
New Packet: 13 ->    [11, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
New Packet: 14 ->    [11, 13, 14, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
New Packet: 1 ->     [1, 11, 13, 14, None, None, None, None, None, None, None, None, None, None, None, None, None]
New Packet: 5 ->     [1, 5, 11, 13, 14, None, None, None, None, None, None, None, None, None, None, None, None]
New Packet: 9 ->     [1, 5, 9, 11, 13, 14, None, None, None, None, None, None, None, None, None, None, None]
New Packet: 10 ->    [1, 5, 9, 10, 11, 13, 14, None, None, None, None, None, None, None, None, None, None]
New Packet: 15 ->    [1, 5, 9, 10, 11, 13, 14, 15, None, None, None, None, None, None, None, None, None]
New Packet: 3 ->     [1, 3, 5, 9, 10, 11, 13, 14, 15, None, None, None, None, None, None, None, None]
New Packet: 6 ->     [1, 3, 5, 6, 9, 10, 11, 13, 14, 15, None, None, None, None, None, None, None]
New Packet: 8 ->     [1, 3, 5, 6, 8, 9, 10, 11, 13, 14, 15, None, None, None, None, None, None]
New Packet: 4 ->     [1, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, None, None, None, None, None]
New Packet: 12 ->    [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None]
New Packet: 16 ->    [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, None, None, None]
New Packet: 0 ->     [0, 1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, None, None]
New Packet: 2 ->     [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, None]
New Packet: 7 ->     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""

####################################################################################################


# C5.31 Describe a way to use recursion to add all the numbers in an n × n data set, 
# represented as a list of lists.


def list_r(S):
    total = 0
    if not isinstance(S, list):
        return S
    else:
        for element in S: 
            total+= list_r(element)
    return total

def sum_list(S):
    total = list_r(S)
    return total


if __name__ == '__main__':
    l = [[1,1,1,1,1], [2,2], 5]
    sum_list(l)


# Output:

"""
14
"""

####################################################################################################
####################################################################################################


# Part Three. Projects

####################################################################################################


# P5.32 Write a Python function that takes two three-dimensional numeric data
# sets and adds them componentwise.


# (1). Adopt operator module 

import operator


class Matrix():
    # For subclassing...
    @classmethod
    def _get_cls(cls):
        return cls
    def __init__(self, data, num_dims = 3):
        self._data = data
        self._dimensions = []
        self._ndims = num_dims
        temp = data
        for i in range(num_dims):
            self._dimensions.append(len(temp))
            temp = temp[0]   
    def __getitem__(self, index):
        return self._data[index]
    def __len__(self):
        return (self._dimensions[0])
    def __repr__(self):
        return (f'{self._ndims}D Matrix with dimensions {self._dimensions}:' + '\n' + f'{self._data}')
    def _create_empty_3D_dataset(self, dimensions):
        a = None
        for d in reversed(dimensions):
            a = [None for _ in range(d)] if a is None else [a.copy() for _ in range(d)]
        return self._get_cls()(a, len(dimensions))
    def _op_lists_r(self, a, b, c, operation):
        # a + b = c
        assert len(a) == len(b) == len(c), 'Length mismatch'
        for i in range(len(a)):
            if isinstance(a[i], list): self._op_lists_r(a[i], b[i], c[i], operation)
            else: c[i] = operation(a[i],b[i])
        return c
    def __add__(self, other):
        assert self._dimensions == other._dimensions, f'Dimension mismatch {self._dimensions}, {other._dimensions}'
        c = self._create_empty_3D_dataset(self._dimensions)
        return (self._op_lists_r(self._data, other._data, c, operator.add))


if __name__ == '__main__':       
    m1 = Matrix([[[i for i in range(10)] for i in range(7)] for i in range(4)])
    m2 = Matrix([[[i for i in range(10)] for i in range(7)] for i in range(4)])
    print(m1)
    print(m1 + m2)


# Output:

"""
3D Matrix with dimensions [4, 7, 10]:
[[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], 
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]]
3D Matrix with dimensions [4, 7, 10]:
[[[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]], [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]], [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]], 
[[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]]]
"""

#---------------------------------------------------------------------------------------------------


# (2).Related matrix operation 


def matrix(data1, data2):
    temp = list(data1)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            for k in range(len(temp[i][j])):
                temp[i][j][k] += data2[i][j][k]
    return temp


if __name__ == '__main__':  
    data = [[[1,1],[2,1]],[[3,1],[4,1]]]
    print(matrix(data,data))


# Output:

"""
[[2, 2], [4, 2]], [[6, 2], [8, 2]]]
"""

####################################################################################################


# P5.33 Write a Python program for a matrix class that can add and multiply two-
# dimensional arrays of numbers, assuming the dimensions agree appropriately for 
# the operation.


import operator


class Matrix():
    # For subclassing...
    @classmethod
    def _get_cls(cls):
        return cls
    def __init__(self, data, num_dims = 3):
        self._data = data
        self._dimensions = []
        self._ndims = num_dims
        temp = data
        for i in range(num_dims):
            self._dimensions.append(len(temp))
            temp = temp[0]   
    def __getitem__(self, index):
        return self._data[index]
    def __len__(self):
        return (self._dimensions[0])
    def __repr__(self):
        return (f'{self._ndims}D Matrix with dimensions {self._dimensions}:' + '\n' + f'{self._data}')
    def _create_empty_3D_dataset(self, dimensions):
        a = None
        for d in reversed(dimensions):
            a = [None for _ in range(d)] if a is None else [a.copy() for _ in range(d)]
        return self._get_cls()(a, len(dimensions))
    def _op_lists_r(self, a, b, c, operation):
        # a + b = c
        assert len(a) == len(b) == len(c), 'Length mismatch'
        for i in range(len(a)):
            if isinstance(a[i], list): self._op_lists_r(a[i], b[i], c[i], operation)
            else: c[i] = operation(a[i],b[i])
        return c
    def __add__(self, other):
        assert self._dimensions == other._dimensions, f'Dimension mismatch {self._dimensions}, {other._dimensions}'
        c = self._create_empty_3D_dataset(self._dimensions)
        return (self._op_lists_r(self._data, other._data, c, operator.add))


class MatrixwMult(Matrix):
    def __mul__(self, other):
        assert self._dimensions == other._dimensions, f'Dimension mismatch {self._dimensions}, {other._dimensions}'
        c = self._create_empty_3D_dataset(self._dimensions)
        return (self._op_lists_r(self._data, other._data, c, operator.mul))
    def dot_product(self, other):
        assert len(self._dimensions) == 2, 'Dot product not implemented for rank>2'
        ar, ac = self._dimensions
        br, bc = other._dimensions
        c = self._create_empty_3D_dataset([ar, bc])
        a = self._data
        b = other._data
        print(c._dimensions)
        for i in range(ar):
            for j in range(bc):
                total = 0
                for k in range(ac):
                    total += a[i][k]*b[k][j]
                    #print (total, a[i][k], b[k][j], 'Index', i, j, k)
                c._data[i][j] = total              
        return c


if __name__ == '__main__':   
    mm1 = MatrixwMult([[[i for i in range(10)] for i in range(7)] for i in range(4)])
    mm2 = MatrixwMult([[[i for i in range(10)] for i in range(7)] for i in range(4)])
    print(mm1*mm2)
    mmm1 = MatrixwMult([[1,2,3],[4,5,6]], 2)
    mmm2 = MatrixwMult([[1,2,3],[1,2,3],[1,2,3]], 2)
    mmm1.dot_product(mmm2)


# Output:

"""
3D Matrix with dimensions [4, 7, 10]:
[[[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]], [[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]], 
[[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]], [[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]]]
[2, 3]
2D Matrix with dimensions [2, 3]:
[[6, 12, 18], [15, 30, 45]]
"""

####################################################################################################


# P5.34 Write a program that can perform the Caesar cipher for English messages
# that include both upper- and lowercase characters.


# (1). To make each first alphabat lower case 

class CaesarCipher():
    def __init__(self, shift=5):
        self._shift = shift
    def encode(self, message):
        return self._transform(message, self._shift)
    def decode(self, message):
        return self._transform(message, -self._shift)
    def _transform(self, message, shift):
        output = []
        for char in message:
            num = ord(char)
            if ord('A')<=num<=ord('Z'):
                output.append(chr((num+shift-ord('A'))%26 + ord('A')))
            elif ord('a')<=num<=ord('z'):
                output.append(chr((num+shift-ord('a'))%26 + ord('a')))
            else:
                output.append(char)
        return ''.join(output)


if __name__ == '__main__':   
    cipher = CaesarCipher(3)
    secret = cipher.encode('Hello Darkness My Old Friend')
    print(secret)
    original = cipher.decode(secret)
    print(original)


# Output:

"""
Khoor Gdunqhvv Pb Rog Iulhqg
Hello Darkness My Old Friend
"""

#---------------------------------------------------------------------------------------------------


# (2).Make all the alphabats uppercase 


class CaesarCipher:
    """Class for doing encryption and decrpytion using a Caesar cipher."""
    def __init__(self, shift):
        # Construct Caesar cipher using given integer shift for rotation.
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
    def encrpyt(self, message):
        # Return string representing encripted message.
        return self._transform(message, self._forward)
    def decrpyt(self, secret):
        # Return decrpyted message given encrpyted secret.
        return self._transform(secret, self._backward)
    def _transform(self, original, code):
        # Utility to perform transformation based on given code string.
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
            elif msg[k].islower():
                j = ord(msg[k]) - ord('a')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "TEST MESSAGE GO, lower case"
    coded = cipher.encrpyt(message)
    coded  
    answer = cipher.decrpyt(coded)
    answer


# Output:


"""
'WHVW PHVVDJH JR, ORZHU FDVH'
'TEST MESSAGE GO, LOWER CASE'
"""

#---------------------------------------------------------------------------------------------------


# (3).To make a mix upper and lower case


class CaesarCipher:
    # Class for doing encryption and decryption using a Caesar cipher.
    def __init__(self, shift):
        # Construct Caesar cipher using given integer shift for rotation.
        encoder = [None] * 26                # temp array for encryption
        decoder = [None] * 26                # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)     # will store as string
        self._backward = ''.join(decoder)    # since fixed
    def encrypt(self, message):
        # Return string representing encripted message.
        return  self._transform(message, self._forward)
    def decrypt(self, secret):
        # Return decrypted message given encrypted secret.
        return  self._transform(secret, self._backward)
    def _transform(self, original, code):
        # Utility to perform transformation based on given code string.
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')   # index from 0 to 25
                msg[k] = code[j]             # replace this character
        return ''.join(msg)


class CaesarCipher_(CaesarCipher):
    """docstring for CaesarCipher_"""
    def _transform(self, original, code):
        # Utility to perform transformation based on given code string.
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                # index from 0 to 25
                j = ord(msg[k]) - ord('A')
                # replace this character
                msg[k] = code[j]
            if msg[k].islower():
                # index from 0 to 25
                j = ord(msg[k]) - ord('a')
                # replace this character
                msg[k] = code[j].lower()
        return ''.join(msg)


if __name__ == '__main__':
    string='I have a BAD guy'
    c=CaesarCipher_(3)
    coded=c.encrypt(string)
    print(coded)
    answer=c.decrypt(coded)
    print(answer)

# Output:

"""
L kdyh d EDG jxb
I have a BAD guy
"""

####################################################################################################


# P5.35 Implement a class, SubstitutionCipher, with a constructor that takes a string 
# with the 26 uppercase letters in an arbitrary order and uses that for the forward 
# mapping for encryption (akin to the self. forward string in our CaesarCipher class 
# of Code Fragment 5.11). You should derive the backward mapping from the forward 
# version.


class SubstitutionCipher():
    def __init__(self, code = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'):
        self._forward = code
        temp_bwd = [None]*26
        for i in range(len(code)):
            index = ord(self._forward[i])-ord('A')
            temp_bwd[index] = chr(i + ord('A'))
        self._backward = ''.join(temp_bwd) 
    def _translate(self, message, code):
        result = []
        for char in message:
            if char.isupper():
                result.append(code[ord(char)-ord('A')])
            else:
                result.append(char)
        return ''.join(result)
    def encode(self, message):
        return self._translate(message, self._forward)
    def decode(self, message):
        return self._translate(message, self._backward)


if __name__ == '__main__':                     
    sc = SubstitutionCipher()   
    secret = sc.encode("I'VE COME TO TALK TO YOU AGAIN")
    print(secret)
    message = sc.decode(secret)
    print(message)


# Output:

"""
J'WF DPNF UP UBML UP ZPV BHBJO
I'VE COME TO TALK TO YOU AGAIN
"""

####################################################################################################


# P5.36 Redesign the CaesarCipher class as a subclass of the SubstitutionCipher
# from the previous problem.


# (1) Write a modified class 


class SubstitutionCipher:
    def __init__(self, code = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'):
        self._forward = code
        temp_bwd = [None]*26
        for i in range(len(code)):
            index = ord(self._forward[i])-ord('A')
            temp_bwd[index] = chr(i + ord('A'))
        self._backward = ''.join(temp_bwd)
    def encode(self, message):
        return self._transform(message, self._forward)
    def decode(self, message):
        return self._transform(message, self._backward)
    def _transform(self, message, code):
        result = []
        for char in message:
            if char.isupper():
                result.append(code[ord(char)-ord('A')])
            else:
                result.append(char)
        return ''.join(result)


class CaesarCipher2(SubstitutionCipher):
    def __init__(self, shift=3):
        forward = ''.join(chr((i+shift)%26 + ord('A')) for i in range(26))
        super().__init__(forward)


if __name__ == '__main__': 
    sc = CaesarCipher2()
    secret = sc.encode("BECAUSE A VISION SOFTLY CREEPING")
    print(secret)
    message = sc.decode(secret)
    print(message)


# Output:

"""
EHFDXVH D YLVLRQ VRIWOB FUHHSLQJ
BECAUSE A VISION SOFTLY CREEPING
"""

####################################################################################################


# P5.37 Design a RandomCipher class as a subclass of the SubstitutionCipher
# from Exercise P-5.35, so that each instance of the class relies on a random
# permutation of letters for its mapping.


import random


class SubstitutionCipher:
    def __init__(self, code = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'):
        self._forward = code
        temp_bwd = [None]*26
        for i in range(len(code)):
            index = ord(self._forward[i])-ord('A')
            temp_bwd[index] = chr(i + ord('A'))
        self._backward = ''.join(temp_bwd)
    def encode(self, message):
        return self._transform(message, self._forward)
    def decode(self, message):
        return self._transform(message, self._backward)
    def _transform(self, message, code):
        result = []
        for char in message:
            if char.isupper():
                result.append(code[ord(char)-ord('A')])
            else:
                result.append(char)
        return ''.join(result)


class RandomCipher(SubstitutionCipher):
    def __init__(self):
        forward = [chr(i+ord('A')) for i in range(26)]
        random.shuffle(forward)
        super().__init__(''.join(forward))


if __name__ == '__main__':
    for _ in range(10):
        rc = RandomCipher()
        secret = rc.encode("LEFT IT'S SEEDS WHILE I WAS SLEEPING")
        print(secret)
        message = rc.decode(secret)
        print(message, end = '\n\n')


# Output:

"""
RMQP ZP'A AMMLA YKZRM Z YVA ARMMWZNO
LEFT IT'S SEEDS WHILE I WAS SLEEPING

IQRG JG'S SQQXS YZJIQ J YLS SIQQHJTC
LEFT IT'S SEEDS WHILE I WAS SLEEPING

UFYD ID'Q QFFVQ EKIUF I EWQ QUFFOIMC
LEFT IT'S SEEDS WHILE I WAS SLEEPING

GSBI LI'M MSSNM EXLGS L EVM MGSSWLUR
LEFT IT'S SEEDS WHILE I WAS SLEEPING

CBRI MI'H HBBZH AYMCB M APH HCBBLMSU
LEFT IT'S SEEDS WHILE I WAS SLEEPING

QSMP CP'G GSSAG DVCQS C DXG GQSSHCLZ
LEFT IT'S SEEDS WHILE I WAS SLEEPING

DRNS LS'G GRRIG CTLDR L CJG GDRRFLOQ
LEFT IT'S SEEDS WHILE I WAS SLEEPING

GYRV KV'Z ZYYTZ LFKGY K LSZ ZGYYIKXO
LEFT IT'S SEEDS WHILE I WAS SLEEPING

MKZU OU'C CKKRC JDOMK O JVC CMKKBOSW
LEFT IT'S SEEDS WHILE I WAS SLEEPING

PCJA VA'L LCCSL KZVPC V KNL LPCCBVDH
LEFT IT'S SEEDS WHILE I WAS SLEEPING
"""