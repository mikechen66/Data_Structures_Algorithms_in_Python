

# merge_array.py

# Please note the original text has no return within the function merge_sort().
# If no return, it will None after calling. Here add 'return S' in order to 
# return sorted list. 


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
    # Call the merge() function 
    merge(S1, S2, S)            # merge sorted halves back into S
    return S


if __name__ == '__main__':
    S = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    T = merge_sort(S)
    print(T)


# Output:

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""