
# binary_sum.py


import time


def binary_sum(s, start, stop):
    # Return the sum of the numbers in implicit slice S[start:stop].
    if start >= stop:                      # zero elements in slice
        return 0
    elif start == stop-1:                  # one element in slice
        return s[start]
    else:                                  # two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(s, start, mid) + binary_sum(s, mid, stop)


if __name__ == '__main__':
    s = [x for x in range(1000000)]
    start = 0 
    stop = 1000000
    curr = time.time()
    b = binary_sum(s, start, stop)
    print(time.time() - curr)
    print(b)


# Output:

"""
0.37051892280578613
499999500000
"""

#------------------------------------------------------------------------------------


# binary_sum.py


import time


class Algorithm:
    def __init__(self, s):
        self.s = s
    def binary_sum(self, start, stop):
        # Return the sum of the numbers in implicit slice S[start:stop].
        if start >= stop:                      # zero elements in slice
            return 0
        elif start == stop-1:                  # one element in slice
            return self.s[start]
        else:                                  # two or more elements in slice
            mid = (start + stop) // 2
            return self.binary_sum(start, mid) + self.binary_sum(mid, stop)


if __name__ == '__main__':
    s = [x for x in range(1000000)]
    al = Algorithm(s)
    start = 0 
    stop = 1000000
    curr = time.time()
    b = al.binary_sum(start, stop)
    print(time.time() - curr)
    print(b)


# Output:

"""
0.44672107696533203
499999500000
"""