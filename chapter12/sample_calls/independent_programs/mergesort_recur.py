

# mergesort_recur.py



def marge(left, right):
    result = []
    # Two sequences have values
    while len(left) > 0 and len(right) > 0:
        # Put the least number in the front in each sequence
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # Add until there is no vlaue in any sequence
    result += left
    result += right
    return result


def mergesort(arr):
    if len(arr) == 1:
        return arr
    # Divide the sequence into two sub sequences
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # Recursivelt call the merge_sort
    return marge(mergesort(left), mergesort(right))

if __name__ == '__main__':
    mergesort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22])


# Output:

"""
[11, 11, 22, 33, 33, 36, 39, 44, 55, 66, 69, 77, 88, 99]
"""