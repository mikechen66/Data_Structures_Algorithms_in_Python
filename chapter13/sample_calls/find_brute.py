

# find_brute.py

"""

John Keats: 
"Two souls but a single thought, two hearts that beat as one."

"""

def find_brute(T, P):
  # Return the lowest index of T at which substring P begins (or else -1).
    n, m = len(T), len(P)                      # introduce convenient notations
    for i in range(n-m+1):                     # try every potential starting index within T
        k = 0                                  # an index into pattern P
        while k < m and T[i + k] == P[k]:      # kth character of P matches
            k += 1
        if k == m:                             # if we reached the end of pattern,
            return i                           # substring T[i:i+m] matches P
    return -1                                  # failed to find a match starting with any i


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
    print(find_brute(T, P1))    # return 0
    print(find_brute(T, P2))    # return 4
    print(find_brute(T, P3))    # return 16
    print(find_brute(T, P4))    # return 32
    print(find_brute(T, P5))    # return 42
    print(find_brute(T, P6))    # return 0
    print(find_brute(T, P7))    # return 53
    print(find_brute(T, P8))    # return -1


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