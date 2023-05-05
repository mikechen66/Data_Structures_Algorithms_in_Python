 
 
# compute_average.py


# Perform n appends to an empty list and return average time elapsed


import time


def compute_average(n):
    data = []
    start = time.time()
    for k in range(n):
        data.append(None)
    end = time.time()
    return (end - start) / n


if __name__ == '__main__':
    n = 1000000
    compute_average(n)


# Output:

"""
6.626319885253906e-08
"""