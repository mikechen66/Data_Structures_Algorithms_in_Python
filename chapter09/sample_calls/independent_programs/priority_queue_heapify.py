

# priority_queue_heapify.py


"""
A priority queue is a special type of queue in which each element is associated 
with a priority value. And, elements are served on the basis of their priority.
That is, higher priority elements are served first.

In a queue, the first-in-first-out rule is implemented whereas, in a priority 
queue, the values are removed on the basis of priority. The element with the 
highest priority is removed first.
"""


# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    return largest

# Function to insert an element into the tree
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


# Function to delete an element from the tree
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    array[i], array[size - 1] = array[size - 1], array[i]
    array.remove(size - 1)
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


if __name__ == '__main__':
    arr = []
    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)
    print("Max-Heap array: " + str(arr))
    deleteNode(arr, 4)
    print("After deleting an element: " + str(arr))



# Output:

"""
Max-Heap array: [9, 5, 4, 3, 2]
After deleting an element: [9, 5, 2, 3]
"""