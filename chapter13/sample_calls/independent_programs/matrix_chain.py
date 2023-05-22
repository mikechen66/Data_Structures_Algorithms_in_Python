


# matrix_chain.py


"""
Given the dimension of a sequence of matrices in an array arr[], where the dimension 
of the ith matrix is (arr[i-1] * arr[i]), the task is to find the most efficient way 
to multiply these matrices together such that the total number of element multipli-
cations is minimum.
"""


import sys


# Matrix A[i] has dimension p[i-1] x p[i] for i = 1..n
def matrix_chain_order(p, i, j):
    if i == j:
        return 0
    _min = sys.maxsize
    # Place parenthesis at different places
    # between first and last matrix,
    # recursively calculate count of multiplications
    # for each parenthesis placement
    # and return the minimum count
    for k in range(i, j):
        count = (matrix_chain_order(p, i, k)
                + matrix_chain_order(p, k + 1, j)
                + p[i-1] * p[k] * p[j])
        if count < _min:
            _min = count
    # Return minimum count
    return _min


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3]
    N = len(arr)
    # Function call
    print("Minimum number of multiplications is ",
    matrix_chain_order(arr, 1, N-1))


# Output:

"""
Minimum number of multiplications is  30
"""
