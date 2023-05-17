

# decorated_merge_sort.py

# merge_array.py

# Please note the original text has no return within the function decorated_merge_sort().
# If no return, it will None after calling. Here add 'return S' in order to return sorted 
# list. 


# from merge_array import merge_sort 


def merge(S1, S2, S):
    # Merge two sorted Python lists S1 and S2 into properly sized list S.
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]      # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]      # copy jth element of S2 as next item of S
            j += 1


def merge_sort(S):
    # Sort the elements of Python list S using the merge-sort algorithm.
    n = len(S)
    if n < 2:
        return                  # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]               # copy of first half
    S2 = S[mid:n]               # copy of second half
    # conquer (with recursion)
    merge_sort(S1)              # sort copy of first half
    merge_sort(S2)              # sort copy of second half
    # merge results
    merge(S1, S2, S)            # merge sorted halves back into S
    return S


class _Item:
    """Lightweight composite to store decorated value for sorting."""
    __slots__ = '_key', '_value'
    def __init__(self, k, v):
        self._key = k
        self._value = v
    def __lt__(self, other):
        return self._key < other._key    # compare items based on their keys


def decorated_merge_sort(data, key=None):
    # Demonstration of the decorate-sort-undecorate pattern.
    if key is not None:
        for j in range(len(data)):
            data[j] = _Item(key(data[j]), data[j]) # decorate each element
    merge_sort(data)                               # sort with existing algorithm
    if key is not None:
        for j in range(len(data)):
            data[j] = data[j]._value               # undecorate each element
    return data


if __name__ == '__main__':
    data = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    T = decorated_merge_sort(data)
    print(T)


# Output:

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""