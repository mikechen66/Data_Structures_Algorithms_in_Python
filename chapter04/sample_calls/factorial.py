
# factorial.py


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    print(factorial(9))
    print(factorial(11))
    print(factorial(13))

# Output:

"""
362880
39916800
6227020800
"""