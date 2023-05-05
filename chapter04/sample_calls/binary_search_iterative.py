
# binary_search_iterative.py


# Option 1: 


def binary_search_iterative(data, target):
    # Return True if target is found in the given Python list.
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:       # found a match
            return True
        elif target < data[mid]:
            high = mid - 1            # only consider values left of mid
        else:
            low = mid + 1             # only consider values right of mid
    return False                      # loop ended without success


if __name__ == "__main__":
    data = [ 2, 3, 4, 10, 40 ]
    target = 10
    result = binary_search_iterative(data,target)
    print(result)


# Output:

"""
True
"""

#------------------------------------------------------------------------------------


# Option 2:


class Algorithm:
    def __init__(self, target):
        self.target = target
    def binary_search_iterative(self, data):
        # Return True if target is found in the given Python list.
        low = 0
        high = len(data)-1
        while low <= high:
            mid = (low + high) // 2
            if self.target == data[mid]:       # found a match
                return True
            elif self.target < data[mid]:
                high = mid - 1            # only consider values left of mid
            else:
                low = mid + 1             # only consider values right of mid
        return False                      # loop ended without success


if __name__ == "__main__":
    target = 10
    alg = Algorithm(target)
    data = [ 2, 3, 4, 10, 40 ]
    result = alg.binary_search_iterative(data)
    print(result)


# Output:

"""
True
"""

#------------------------------------------------------------------------------------


# Option 3:


# It returns index of x in given array arr if present, else returns -1


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1


if __name__ == "__main__":
    # Test array
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10
    # Function call
    result = binary_search(arr, x)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")


# Output:

"""
Element is present at index 3
"""

#------------------------------------------------------------------------------------


# Option 4:


def binary_search(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else: 
            return mid
    return -1


if __name__ == "__main__": 
    array = [4, 7, 9, 16, 20, 25]
    n = 7
    r = binary_search(array, n)
    if r != -1:
        print("Element found at index", str(r))
    else: 
        print("Element is not present in the array")


"""
Element found at index 1
"""