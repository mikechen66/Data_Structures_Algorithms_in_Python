

# matrix_chain.py

"""
Return solution to the matrix chain problem.

d is a list of n+1 numbers describing the dimensions of a chain of n matrices 
such that kth matrix has dimensions d[k]-by-d[k+1].

Return an n-by-n table such that N[i][j] represents the minimum number of
multiplications needed to compute the product of Ai through Aj inclusive.
"""


def matrix_chain(d):
    n = len(d) - 1                       # number of matrices
    N = [[0] * n for i in range(n)]      # initialize n-by-n result to zero
    for b in range(1, n):                # number of products in subchain
        for i in range(n-b):             # start of subchain
            j = i + b                    # end of subchain
            # for loop
            N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i,j))
    return N


if __name__ == '__main__':
    # Test 1: Single matrix
    print("Test 1")
    d = [3, 4]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end= " ")
        print()
    # Test 2: Two matrices
    print()
    print("Test 2")
    d = [3, 4, 5]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end=" ")
        print()
    # Test 3: Three matrices
    print()
    print("Test 3")
    d = [3, 4, 5, 6]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end=" ")
        print()
    # Test 4: Four matrices of the same size
    print()
    print("Test 4")
    d = [5, 5, 5, 5, 5]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end=" ")
        print()
    # Test 5: Five matrices
    print()
    print("Test 5")
    d = [3, 4, 5, 6, 7, 8]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end=" ")
        print()
    # Test 6: Five matrices
    print()
    print("Test 6")
    d = [3, 4, 5, 6, 7, 8, 9]
    N = matrix_chain(d)
    for i in range(len(d)-1):
        for j in range(len(d)-1):
            print(N[i][j], end=" ")
        print()


# Output:

"""
Test 1
0 

Test 2
0 60 
0  0 

Test 3
0 60 150 
0  0 120 
0  0   0 

Test 4
0 125 250 375 
0   0 125 250 
0   0   0 125 
0   0   0   0 

Test 5
0 60 150 276 444 
0  0 120 288 512 
0  0  0  210 490 
0  0  0    0 336 
0  0  0    0   0 

Test 6
0 60 150 276 444 660 
0  0 120 288 512 800 
0  0   0 210 490 850 
0  0   0   0 336 768 
0  0   0   0   0 504 
0  0   0   0   0   0 

"""