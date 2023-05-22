

# find_kmp.py


def compute_kmp_fail(P):
    # Utility that computes and returns KMP 'fail' list.
    m = len(P)
    fail = [0] * m                   # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m:                     # compute f(j) during this pass, if nonzero
        if P[j] == P[k]:             # k + 1 characters match thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:                  # k follows a matching prefix
            k = fail[k-1]
        else:                        # no match found starting at j
            j += 1
    return fail


def find_kmp(T, P):
    # Return the lowest index of T at which substring P begins (or else -1).
    n, m = len(T), len(P)            # introduce convenient notations
    if m == 0: 
        return 0                     # trivial search for empty string
    fail = compute_kmp_fail(P)       # rely on utility to precompute
    j = 0                            # index into text
    k = 0                            # index into pattern
    while j < n:
        if T[j] == P[k]:             # P[0:1+k] matched thus far
            if k == m - 1:           # match is complete
                return j - m + 1           
            j += 1                   # try to extend match
            k += 1
        elif k > 0:                    
            k = fail[k-1]            # reuse suffix of P[0:k]
        else:
            j += 1
    return -1                        # reached end without match


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
    print(find_kmp(T, P1))    # return 0
    print(find_kmp(T, P2))    # return 4
    print(find_kmp(T, P3))    # return 16
    print(find_kmp(T, P4))    # return 32
    print(find_kmp(T, P5))    # return 42
    print(find_kmp(T, P6))    # return 0
    print(find_kmp(T, P7))    # return 53
    print(find_kmp(T, P8))    # return -1


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
