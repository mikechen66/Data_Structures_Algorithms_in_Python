#!/usr/bin/env
#encoding=utf-8


# radix_sort_math.py

####################################################################################################


# Option 1

# Give a range of integers - LSD 


import math


def sort(a, radix=10):
    # a is interger list and radix is base
    K = int(math.ceil(math.log(max(a), radix))) 
    bucket = [[] for i in range(radix)] 
    for i in range(1, K+1): 
        for val in a:
            # It is necessary to have int() function
            bucket[int(val%(radix**i)/(radix**(i-1)))].append(val)
        del a[:]
        for each in bucket:
            a.extend(each)
        bucket = [[] for i in range(radix)]


if __name__ == '__main__':
    a = list(range(99, 0, -1))
    sort(a, 10)
    print(a)


# Output:

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 
76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
"""

####################################################################################################


# Option 2

# Give a list of integers - LSD 

import math


def sort(a, radix=10):
    K = int(math.ceil(math.log(max(a), radix))) 
    # print(K)
    bucket = [[] for i in range(radix)] 
    # print(bucket)
    for i in range(1, K+1): 
        for val in a:
            bucket[int(val%(radix**i)/(radix**(i-1)))].append(val) 
        del a[:]
        for each in bucket:
            a.extend(each) # 桶合并
        bucket = [[] for i in range(radix)]


if __name__ == '__main__':
    a = [329, 457, 657, 839, 436, 720, 355]
    print(a)
    sort(a)
    print(a)


# Output:

"""
[329, 457, 657, 839, 436, 720, 355]
[329, 355, 436, 457, 657, 720, 839]
"""
