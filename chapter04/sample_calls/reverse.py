
# reverse.py

# Reversing the elements of a sequence using linear recursion


# Option 1:


import time


def reverse(S, start, stop):
    # Reverse elements in implicit slice S[start:stop].
    if start < stop - 1:                           # if at least 2 elements:
        S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
        reverse(S, start+1, stop-1)                # recur on rest


if __name__ == '__main__':
    S = [x for x in range(1000)]
    start = 0 
    stop = 1000
    curr = time.time()
    r = reverse(S, start, stop)
    print(time.time() - curr)
    print(r)

# Output:

"""
0.0005793571472167969
None
"""


##################################################################################


# Option 2: 


def reverse(n, r):
    if n==0:
        return r
    else:
        return reverse(n//10, r*10 + n%10)


if __name__ == '__main__':
    # Read number
    number = int(input("Enter number: "))
    curr = time.time()
    # Function call
    reversed_number = reverse(number,0)
    print(time.time() - curr)
    # Display output
    print("Reverse of %d is %d" %(number, reversed_number))


# Output:

"""
Enter number: 19999
1.6927719116210938e-05
Reverse of 19999 is 99991
"""