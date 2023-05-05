
# Find minimum number 


def find_min(data):
    # Return the maximum element from a nonempty Python list.
    smallest = data[0]              # The initial value to beat
    for val in data:                # For each value:
        if val < smallest:          # if it is greater than the best so far,
            biggest = val           # we have found a new best (so far)
    return smallest                 # When loop ends, biggest is the max


if __name__ == '__main__':
    data = [0,1,2,3,4,5,6,7,8,9]
    f = find_min(data)
    print(f)


# Output:
"""
0
"""