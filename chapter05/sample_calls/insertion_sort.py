

# insertion_sort.py


# Option 1: show the list


def insertion_sort(A):
    # Sort list of comparable elements into nondecreasing order.
    for i in range(1, len(A)):       # from 1 to n-1
        cur = A[i]                   # current element to be inserted
        j = i                        # find correct index j for current
        while j > 0 and A[j-1] > cur:    # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur                       # cur is now in the right place


if __name__ == '__main__':
    A = [12, 11, 13, 5, 6]
    insertion_sort(A)
    print(A)



# Output:

"""
[5, 6, 11, 12, 13]
"""

#----------------------------------------------------------------------------------


# Option 1: show the for loop 


def insertion_sort(A):
    # Sort list of comparable elements into nondecreasing order.
    for i in range(1, len(A)):       # from 1 to n-1
        cur = A[i]                   # current element to be inserted
        j = i                        # find correct index j for current
        while j > 0 and A[j-1] > cur:    # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur                       # cur is now in the right place


# Driver code to test above
if __name__ == '__main__':
    A = [12, 11, 13, 5, 6]
    insertion_sort(A)
    for i in range(len(A)):
        print("% d" % A[i])


# Output:

"""
 5
 6
 11
 12
 13
 """

###################################################################################


# Option 2: 


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        array[j + 1] = key


if __name__ == '__main__':
    data = [9, 5, 1, 4, 3]
    insertionSort(data)
    print('Sorted Array in Ascending Order:')
    print(data)


# Output:

"""
Sorted Array in Ascending Order:
[1, 3, 4, 5, 9]
"""

#----------------------------------------------------------------------------------


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        array[j + 1] = key


if __name__ == '__main__':
    array = [12, 11, 13, 5, 6]
    insertionSort(array)
    for i in range(len(array)):
        print("% d" % array[i])


# Output:

"""
 5
 6
 11
 12
 13
"""

###################################################################################


# Option 3: 


# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position 
        # ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print(arr)

# Output:

"""
[5, 6, 11, 12, 13]
"""

#----------------------------------------------------------------------------------


# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position 
        # ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



# Driver code to test above
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    for i in range(len(arr)):
        print ("% d" % arr[i])


# Output:

"""
 5
 6
 11
 12
 13
"""

###################################################################################


# Option 4: 

def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        array[j + 1] = key


# Driver code to test above
if __name__ == '__main__':
    data = [9, 5, 1, 4, 3]
    insertion_sort(data)
    print('Sorted Array in Ascending Order:')
    print(data)


# Output:

"""
Sorted Array in Ascending Order:
[1, 3, 4, 5, 9]
"""

###################################################################################


# Option 5: 

from random import randint
from timeit import repeat


def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]
        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1
        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1
        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item
    return array


def run_sorting_algorithm(algorithm, array):
    times = repeat(stmt="insertion_sort", setup="from __main__ import insertion_sort", repeat=3, number=10)    
    print(f"Algorithm: insertion_sort. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    ARRAY_LENGTH = 10000
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    # Call the function using the name of the sorting algorithm
    # and the array we just created
    run_sorting_algorithm(algorithm="insertion_sort", array=array)


# Output:

"""
Algorithm: insertion_sort. Minimum execution time: 2.56000021181535e-07
"""