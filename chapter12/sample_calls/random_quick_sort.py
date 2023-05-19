

# random_quick_sort.py

"""

1. Origial quick_inplace.py

def inplace_quick_sort(S, a, b):
    # Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm.
    if a >= b: 
        return                                     # range is trivially sorted
    pivot = S[b]                                   # last element of range is pivot
    left = a                                       # will scan rightward
    right = b-1                                    # will scan leftward
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:                          # scans did not strictly cross
            S[left], S[right] = S[right], S[left]  # swap values
            left, right = left + 1, right - 1      # shrink range
    # Put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)
    return S


if __name__ == '__main__':
    S = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(S)
    T = inplace_quick_sort(S, a=0, b=len(S)-1)
    print(T)


2. change the original to the random quicksort with the following changes

1). Add if statment as follows

    if b is None:
        b = len(S) - 1

    if no if statement, it will generate the error as follows.
    TypeError: '>=' not supported between instances of 'int' and 'NoneType'

2). Add the pivot assignment and the swap between S[b] and S[ramn_num]

    pivot = S[rand_num]                            # Choose a random number as pivot
    S[rand_num], S[b] = S[b], S[rand_num]          # Swatch S[randoma] and S[j]

3). Add the following statements

    n = 10
    S = [random.randint(0, 50) for i in range(n)]

"""


import random


def random_quick_sort(S, a, b):
    # Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm.
    if b is None:
        b = len(S) - 1
    if a >= b: 
        return None                                # range is trivially sorted
    pivot = S[rand_num]                            # Choose a random number as pivot
    S[rand_num], S[b] = S[b], S[rand_num]          # Swatch S[randoma] and S[j]
    left = a                                       # will scan rightward
    right = b-1                                    # will scan leftward
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:                          # scans did not strictly cross
            S[left], S[right] = S[right], S[left]  # swap values
            left, right = left + 1, right - 1      # shrink range
    # Put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    random_quick_sort(S, a, left - 1)
    random_quick_sort(S, left + 1, b)
    return S


if __name__ == '__main__':
    n = 10
    S = [random.randint(0, 50) for i in range(n)]
    print(S)
    random_quick_sort(S, a=0, b=None)


# Output:

"""
[13, 30, 39, 22, 2, 8, 0, 34, 45, 6]
[0, 2, 6, 8, 13, 22, 30, 34, 39, 45]
"""