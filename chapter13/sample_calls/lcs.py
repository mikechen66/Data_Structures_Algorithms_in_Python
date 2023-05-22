

# lcs.py

"""
Please note that thw two functios of lcs() and lcs_solution() are different function, 
but used here to make different presentation. 
"""


def lcs(X, Y):
    # Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k].
    n, m = len(X), len(Y)                      # introduce convenient notations
    L = [[0] * (m+1) for k in range(n+1)]      # (n+1) x (m+1) table
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:                   # align this match
                L[j+1][k+1] = L[j][k] + 1            
            else:                              # choose to ignore one character
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L


def lcs_solution(X, Y, L):
    # Return the longest common substring of X and Y, given LCS table L.
    solution = []
    j, k = len(X), len(Y)
    while L[j][k] > 0:                         # common characters remain
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -=1
        else:
            k -= 1
    return ''.join(reversed(solution))         # return left-to-right version


if __name__ == '__main__':
    # Test 1: Identical
    X = "abcdef"
    Y = "abcdef"
    L = lcs(X, Y)
    print("Test 1")
    for j in range(len(X)+1):
        for k in range(len(Y)+1):
            print(L[j][k], end = " ")
        print()
    print(lcs_solution(X, Y, L))
    # Test 2: One subsequence of the other
    print()
    X = "bdf"
    Y = "abcdef"
    L = lcs(X, Y)
    print("Test 2")
    for j in range(len(X)+1):
        for k in range(len(Y)+1):
            print(L[j][k], end = " ")
        print()
    print(lcs_solution(X, Y, L))
    # Test 3: Totally different
    print()
    X = "GTTCCTAATA"
    Y = "CGATAATTGAGA"
    L = lcs(X, Y)
    print("Test 3")
    for j in range(len(X)+1):
        for k in range(len(Y)+1):
            print(L[j][k], end = " ")
        print()
    print(lcs_solution(X, Y, L))


# Output:


"""
Test 1
0 0 0 0 0 0 0 
0 1 1 1 1 1 1 
0 1 2 2 2 2 2 
0 1 2 3 3 3 3 
0 1 2 3 4 4 4 
0 1 2 3 4 5 5 
0 1 2 3 4 5 6 
abcdef

Test 2
0 0 0 0 0 0 0 
0 0 1 1 1 1 1 
0 0 1 1 2 2 2 
0 0 1 1 2 2 3 
bdf

Test 3
0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 1 1 1 1 1 1 1 1 1 1 1 
0 0 1 1 2 2 2 2 2 2 2 2 2 
0 0 1 1 2 2 2 3 3 3 3 3 3 
0 1 1 1 2 2 2 3 3 3 3 3 3 
0 1 1 1 2 2 2 3 3 3 3 3 3 
0 1 1 1 2 2 2 3 4 4 4 4 4 
0 1 1 2 2 3 3 3 4 4 5 5 5 
0 1 1 2 2 3 4 4 4 4 5 5 6 
0 1 1 2 3 3 4 5 5 5 5 5 6 
0 1 1 2 3 4 4 5 5 5 6 6 6 
GTTTAA
"""