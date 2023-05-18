

# quick_sort_queue.py


class Empty(Exception):
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage
        def __init__(self, element, next):
            self._element = element
            self._next = next
    #------------------------------- queue methods -------------------------------
    def __init__(self):
        # Create an empty queue.
        self._head = None
        self._tail = None
        self._size = 0                          # number of queue elements
    def __len__(self):
        # Return the number of elements in the queue.
        return self._size
    def __iter__(self):
        cur = self._head
        while cur is not None:
            yield cur._element
            cur = cur._next
    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0
    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element              # front aligned with head of list
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                     # special case as queue is empty
            self._tail = None                   # removed head had been the tail
        return answer
    def enqueue(self, e):
        # Add an element to the back of queue.
        newest = self._Node(e, None)            # node will be new tail node
        if self.is_empty():
            self._head = newest                 # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                     # update reference to tail node
        self._size += 1


# Function to find the partition position

def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for greater element
    i = low - 1
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


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
    quick_sort(res, 0, len(res)-1)
    print(res)



# Output:

"""
7
[6, 5, 4, 3, 2, 1]
[1, 2, 3, 4, 5, 6]
"""