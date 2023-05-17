

# quick_queue.py

"""

It does not work since 'list' object has no attribute (methods) in LinkedQueue
The following snippets can not get the data. 

data = []
for i in lq:
    data.append(i)
# merge_sort(data)

"""


from linked_queue_iter import LinkedQueue


def quick_sort(S):
    # Sort the elements of queue S using the quick-sort algorithm.
    n = len(S)
    if n < 2:
        return                          # list is already sorted
    # divide
    p = S.first()                       # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():             # divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:                           # S.first() must equal pivot
            E.enqueue(S.dequeue())
    # conquer (with recursion)
    quick_sort(L)                       # sort elements less than p
    quick_sort(G)                       # sort elements greater than p
    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


if __name__ == '__main__':
    lq = LinkedQueue()
    lq.enqueue(6)
    lq.enqueue(3)
    lq.enqueue(1)
    lq.enqueue(4)
    lq.enqueue(2)
    [i for i in lq]
    # It does not work since 'list' object has no attribute (methods) in LinkedQueue
    quick_sort(lq)



# Output:

"""
[6, 3, 1, 4, 2]
"""
