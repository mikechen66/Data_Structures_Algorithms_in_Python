

# unique.py


def unique1(S):
    # Return True if there are no duplicate elements in sequence S.
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False        # found duplicate pair
    return True                     # if we reach this, elements were unique


def unique2(S):
    # Return True if there are no duplicate elements in sequence S.
    temp = sorted(S)                # create a sorted copy of S
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return False            # found duplicate pair
    return True                     # if we reach this, elements were unique


# WARNING: this is a terribly inefficient algorithm
def unique3(S, start=0, stop=9):
    # Return True if there are no duplicate elements in slice S[start:stop].
    if stop - start <= 1: 
        return True                      # at most one item
    elif not unique3(S, start, stop-1): 
        return False                     # first part has duplicate
    elif not unique3(S, start+1, stop): 
        return False                     # second part has duplicate
    else: 
        return S[start] != S[stop-1]     # do first and last differ?


if __name__ == '__main__':
    S1 = [10,9,8,7,6,5,4,3,2,1]
    unique1(S1)
    unique2(S1)
    unique3(S1)
    S2 = [10,8,8,7,6,5,4,3,2,1]
    unique1(S2)
    unique2(S2)
    unique3(S2)


# Output:

"""
True
True
True
False
False
False
"""