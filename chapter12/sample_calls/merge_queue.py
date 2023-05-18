

# merge_queue.py


# Please note the original text has no return within the function decorated_merge_sort().
# If no return, it will None after calling. Here add 'return S' in order to return sorted 
# list. 


from linked_queue_iter import LinkedQueue


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



if __name__ == '__main__':
    lq = LinkedQueue()
    lq.enqueue(7)
    lq.enqueue(6)
    lq.enqueue(5)
    lq.enqueue(4)
    lq.enqueue(3)
    lq.enqueue(2)
    lq.enqueue(1)
    lq.dequeue()
    res = [i for i in lq]
    print(res)
    merge_sort(res)


# Output:

"""
7
[6, 5, 4, 3, 2, 1]
[1, 2, 3, 4, 5, 6]
"""