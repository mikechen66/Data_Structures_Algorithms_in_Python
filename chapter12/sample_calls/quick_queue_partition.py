

# quick_queue.py


from linked_queue_iter import LinkedQueue


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
