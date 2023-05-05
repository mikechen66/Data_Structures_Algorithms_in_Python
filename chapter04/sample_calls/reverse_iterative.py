

# reverse_iterative.py


def reverse_iterative(S):
    # Reverse elements in sequence S.
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
        start, stop = start + 1, stop - 1          # narrow the range


if __name__ == '__main__':
    S = [x for x in range(1000000)]
    curr = time.time()
    r = reverse_iterative(S)
    print(time.time() - curr)
    print(r)


# Output:

"""
0.1359999179840088
None
"""