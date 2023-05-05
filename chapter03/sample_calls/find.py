
# find.py


def find(S, val):
    # Return index j such that S[j] == val, or -1 if no such element.
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j     # a match was found at index j
        j += 1
    return -1


if __name__ == '__main__':
    S = [9,2,3,8,7,11,5,4,1]
    val = 2
    find(S, val)


# Output:

"""
1
"""