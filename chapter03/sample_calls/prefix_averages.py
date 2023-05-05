
# prefix_average.py

import time 


# Time complexity: O(n^2)
def prefix_average1(S):
    # Return list such that, for all j, A[j] equals average of S[0], ..., S[j].
    n = len(S)
    A = [0] * n                       # O(n): create new list of n zeros
    for j in range(n):                # O(n): execute n times: from 0 to n-1
        total = 0                     # begin computing S[0] + ... + S[j]
        for i in range(j + 1):        # execute n+1 times from 0 to n
            total += S[i]             # O(n^2): execute 1 + 2 + .. + n = n(n+1)/2 
        A[j] = total / (j+1)          # A[j] = (n(n+1)/2) /(j=n+1) = n/2
        print(A[j])
    return A


if __name__ == '__main__':
    data = [x for x in range(10)]
    print(data)
    curr = time.time()
    prefix_data = prefix_average1(S=data)
    print(time.time() - curr)
    print(prefix_data)


# Output:

"""
# Output:

>>> # print(A)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> # print(total)
0
0
0
0
0
0
0
0
0
0
>>> # print(total)
>>> # Round 1 as j(0) + 1 = 1
0   
>>> # Round 2 as j(1) + 1 = 2
0   
1   
>>> # Round 3 as j(2) + 1 = 3 
0
1
3
>>> # Round 4 as j(3) + 1 = 4
0
1
3
6
>>> # Round 5 as j(4) + 1 = 5
0
1
3
6
10
>>> # Round 6 as j(5) + 1 = 6 
0
1
3
6
10
15
>>> # Round 7
0
1
3
6
10
15
21
>>> # Round 8
0
1
3
6
10
15
21
28
>>> # Round 9
0
1
3
6
10
15
21
28
36
>>> # Round 10 as j(9) + 1 = 10
0
1
3
6
10
15
21
28
36
45
>>> # print(A[j]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
>>> # print(data)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> # print(time.time() - curr)
0.00013780593872070312
>>> # print(prefix_data)
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
>>>
"""

#------------------------------------------------------------------------------------------


import time 


# Time complexity: O(n^2)

def prefix_average1(S):
    # Return list such that, for all j, A[j] equals average of S[0], ..., S[j].
    n = len(S)
    A = [0] * n                       # O(n): create new list of n zeros
    for j in range(n):                # O(n): execute n times: from 0 to n-1
        total = 0                     # begin computing S[0] + ... + S[j]
        for i in range(j + 1):        # execute n+1 times from 0 to n
            total += S[i]             # O(n^2): execute 1 + 2 + .. + n = n(n+1)/2 
        A[j] = total / (j+1)          # A[j] = (n(n+1)/2) /(j=n+1) = n/2
        print(A[j])
    return A


if __name__ == '__main__':
    data = [x for x in range(1000)]
    print(data)
    curr = time.time()
    prefix_data = prefix_average1(data)
    print(time.time() - curr)
    print(prefix_data)


###########################################################################################


# prefix_average2.py


# Return list such that, for all j, A[j] equals average of S[0], ..., S[j].
# sum(S[0:j+1]) = S[0] + ... + S[j}]

import time

# Time complexity: O(n^2)

def prefix_average2(S):
    n = len(S)
    A = [0] * n                       # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)  # record the average (sum replace total total += S[i])
        print(sum(S[0:j+1]))          # sum = n(n+1)/2 = 9*(9+1)/2 = 45(for the last round)
        print(A[j])
    return A


if __name__ == '__main__':
    data = [x for x in range(10)]
    # print(data)
    curr = time.time()
    prefix_data = prefix_average2(data)
    # print(time.time() - curr)
    # print(prefix_data)


# Output:

"""
>>> print(A[j])
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
>>> print(sum(S[0:j+1]))
0
1
3
6
10
15
21
28
36
45
>>> print(data)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(time.time() - curr)
0.00034356117248535156
>>> print(prefix_data)
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
"""

###########################################################################################


# prefix_average3.py

import time

# Time complexity: O(n)

def prefix_average3(S):
    # Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)                      # O(1): initialize n 
    A = [0] * n                     # O(n): create new list of n zeros
    total = 0                       # O(1): compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j]               # O(n): update prefix sum to include S[j]
        print(total)
        A[j] = total / (j+1)        # O(n): compute average based on current sum
        print(A[j])
    return A


if __name__ == '__main__':
    data = [x for x in range(10)]
    print(data)
    curr = time.time()
    prefix_data = prefix_average3(data)
    print(time.time() - curr)
    print(prefix_data)


# Output:

"""
>>> print(total)
0
1
3
6
10
15
21
28
36
45
>>> print(A[j])
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
>>> print(data)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(time.time() - curr)
0.00012564659118652344
>>> print(prefix_data)
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
"""

###########################################################################################


class Prefix():
    def __init__(self):
        self._timer_array = []
    def timer(func):
        def wrapper(*args, **kwargs):
            before = time.time()
            for _ in range(20):
                func(*args, **kwargs)
            after = time.time()
            args[0]._timer_array.append((after-before)*100000)  # Note, since the first argument is self, this is how we access self
            print ('Total time is ', after-before)
        return wrapper
    @timer
    def prefix_average1(self, S):
        n = len(S)
        A = [0]*n
        for j in range(n):
            total = 0
            for i in range(j+1):
                total += S[i]
            A[j] = total/(j+1)
        return A
    @timer
    def prefix_average2(self, S):
        n = len(S)
        A = [0]*n
        for j in range(n):
            A[j] = sum(S[0:j+1])/(j+1)
        return A
    @timer
    def prefix_average3(self, S):
        n = len(S)
        A = [0]*n
        total = 0
        for j in range(n):
            total +=S[j]
            A[j] = total/(j+1)
        return A
    def _reset_timers(self):
        self._timer_array = []
    def test_timers(self, e_n = 5):
        results = {}
        for name, func in [('1',self.prefix_average1), ('2', self.prefix_average2), ('3', self.prefix_average3)]:
            for i in range(1, e_n):
                test_array = list(range(10**i))
                func(test_array)
            results[name] = self._timer_array
            self._reset_timers()
        x = list(map(lambda x: 10**x, range(1, e_n)))
        return x, results


if __name__ == '__main__':
    p = Prefix()
    x, results = p.test_timers(5)
    for f in results.values():
        plt.plot(x, f)
    plt.xscale('log')
    plt.yscale('log')


# Output:

"""
Total time is  0.00015115737915039062
Total time is  0.006754636764526367
Total time is  0.6034462451934814
Total time is  64.19077682495117
Total time is  7.987022399902344e-05
Total time is  0.0014948844909667969
Total time is  0.090484619140625
Total time is  64.19077682495117
Total time is  7.987022399902344e-05
Total time is  0.0014948844909667969
Total time is  0.090484619140625
"""