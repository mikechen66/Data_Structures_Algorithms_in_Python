

# find_boyer_moore.py


def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)                   # introduce convenient notations
    if m == 0: return 0                     # trivial search for empty string
    last = {}                               # build 'last' dictionary
    for k in range(m):
        last[ P[k] ] = k                    # later occurrence overwrites
    # align end of pattern at m-1
    i = m-1                                 # an index into T
    k = m-1                                 # an index into P
    while i < n:
        if T[i] == P[k]:                    # a matching character
            if k == 0:
                return i                    # pattern begins at index i of text
            else:
                i -= 1                      # examine previous character
                k -= 1                      # of both T and P
        else:
            j = last.get(T[i], -1)          # last(T[i]) is -1 if not found
            i += m - min(k, j + 1)          # case analysis for jump step
            k = m - 1                       # restart at end of pattern
    return -1


if __name__ == "__main__":
    T = "Two souls but a single thought, two hearts that beat as one."
    P1 = "Two"
    P2 = "souls"
    P3 = "single thought"
    P4 = "two hearts"
    P5 = " that beat"
    P6 = ""
    P7 = "as"
    P8 = "  "
    print(find_boyer_moore(T, P1))           # return 0
    print(find_boyer_moore(T, P2))           # return 4
    print(find_boyer_moore(T, P3))           # return 16
    print(find_boyer_moore(T, P4))           # return 32
    print(find_boyer_moore(T, P5))           # return 42
    print(find_boyer_moore(T, P6))           # return 0
    print(find_boyer_moore(T, P7))           # return 53
    print(find_boyer_moore(T, P8))           # return -1


# Output:

"""
0
4
16
32
42
0
53
-1
"""
