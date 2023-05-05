
# fibonacci.py


def bad_fibonacci(n):
    # Return the nth Fibonacci number.
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)


if __name__ == '__main__':
    print(bad_fibonacci(11))
    print(bad_fibonacci(17))
    print(bad_fibonacci(23))


# Output:

"""
89
1597
28657
"""


##################################################################################


def good_fibonacci(n):
    # Return pair of Fibonacci numbers, F(n) and F(n-1).
    if n <= 1:
        return (n,0)
    else:
        (a,b) = good_fibonacci(n-1)
        return (a+b, a)


if __name__ == '__main__':
    print(good_fibonacci(11))
    print(good_fibonacci(17))
    print(good_fibonacci(23))


# Output:

"""
(89, 55)
(1597, 987)
(28657, 17711)
"""