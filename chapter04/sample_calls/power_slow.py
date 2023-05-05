

# power_slow.py


import time

def power(x, n):
    # Compute the value x**n for integer n.
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


if __name__ == '__main__':
    x = 8 
    n = 9
    curr = time.time()
    p = power(x,n)
    print(time.time() - curr)
    print(p)


# Output:

"""
1.0967254638671875e-05
134217728
"""