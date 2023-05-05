

# power_fast.py


import time

def power(x, n):
    # Compute the value x**n for integer n.
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)   # rely on truncated division
        result = partial * partial
        if n % 2 == 1:               # if n odd, include extra factor of x
            result *= x                       
        return result


if __name__ == '__main__':
    x = 8 
    n = 9
    curr = time.time()
    p = power(x,n)
    print(time.time() - curr)
    print(p)


# Output:

"""
1.621246337890625e-05
134217728
"""