

# binary_search.py


# Option 1: 

def binary_search(data, target, low, high):
    # Return True if target is found in indicated portion of a Python list.
    # The search only considers the portion from data[low] to data[high] inclusive.
    if low > high:
        return False                    # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:         # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)


if __name__ == "__main__":
    data = [ 2, 3, 4, 10, 40 ]
    target = 10
    result = binary_search(data, target, 0, len(data)-1)
    print(result)


# Output:

"""
True
"""

#------------------------------------------------------------------------------------

# Option 2: 


class Algorithm:
    def binary_search(self, data, target, low, high):
        # Return True if target is found in indicated portion of a Python list.
        # The search only considers the portion from data[low] to data[high] inclusive.
        if low > high:
            return False                    # interval is empty; no match
        else:
            mid = (low + high) // 2
            if target == data[mid]:         # found a match
                return True
            elif target < data[mid]:
                # recur on the portion left of the middle
                return self.binary_search(data, target, low, mid - 1)
            else:
                # recur on the portion right of the middle
                return self.binary_search(data, target, mid + 1, high)


if __name__ == "__main__":
    alg = Algorithm()
    data = [ 2, 3, 4, 10, 40 ]
    target = 10
    result = alg.binary_search(data, target, 0, len(data)-1)
    print(result)


# Output:

"""
True
"""
#-----------------------------------------------------------------------------------


# Option 3: 

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1


if __name__ == "__main__":
    # Test array
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10
    # Function call
    result = binary_search(arr, 0, len(arr)-1, x)
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

def binary_search(arr, low, high, number):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == number:
           return mid
        elif arr[mid] > number:
           return binary_search(arr, low, mid-1, number)
        else:
           return binary_search(arr, mid+1, high, number)
    else:
        return -1


if __name__ == "__main__":    
    arr = [5, 12, 17, 19, 22, 30]
    number = 22
    r = binary_search(arr, 0, len(arr)-1, number)
    if r != -1:
        print("Element found at index", str(r))
    else:
        print("Element is not present in array") 


# Output:

"""
Element found at index 4
"""