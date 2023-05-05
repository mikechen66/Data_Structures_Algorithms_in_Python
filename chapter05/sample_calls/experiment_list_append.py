

# experiment_list_append.py


import sys
from time import time


try:
    maxN = int(sys.argv[1])
except:
    maxN = 10000000


def compute_average(n):
    # Perform n appends to an empty list and return average time elapsed.
    data = []
    start = time()                 # record the start time (in seconds)
    for k in range(n):
        data.append(None)
    end = time()                   # record the end time (in seconds)
    return (end - start) / n       # compute average per operation


if __name__ == '__main__':
    n = 10
    while n <= maxN:
        print('Average of {0:.3f} for n {1}'.format(compute_average(n)*1000000, n))
        n *= 10


# Output:

"""
Average of 0.787 for n 10
Average of 0.169 for n 100
Average of 0.129 for n 1000
Average of 0.112 for n 10000
Average of 0.072 for n 100000
Average of 0.065 for n 1000000


Average of 0.064 for n 10000000
"""