# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# unique1.py:

# function is equal to (n-1) + (n-2) + ... + 2 + 1

# Algo complexity: O(n^2)


def unique1(S):
    # Return True if there are no duplicate elements in sequence S.
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False        # found duplicate pair
    return True                     # if we reach this, elements were unique


if __name__ == '__main__':
    S1 = [1,2,3,4,5,6,6,7,8]
    S2 = [9,10,11,12,13,14,15,16]
    print(unique1(S1))
    print(unique1(S2))


# Output:

"""
False
True
"""

#################################################################################


# Use sorted function 

# Algo complexity: O(n log n)

# O(n log n): sorted(iterable, key=None, reverse=False)

def unique2(S):
    # Return True if there are no duplicate elements in sequence S.
    temp = sorted(S)                # create a sorted copy of S
    for j in range(1, len(temp)):   # O(n)
        if S[j-1] == S[j]:
            return False            # found duplicate pair
    return True                     # if we reach this, elements were unique


if __name__ == '__main__':
    S1 = [1,2,3,4,5,6,6,7,8]
    S2 = [9,10,11,12,13,14,15,16]
    print(unique2(S1))
    print(unique2(S2))


# Output:

"""
False
True
"""

#################################################################################


# Adopt it from C4 Recursion, Data Structures and Algorithm in Python


def unique3(S, start, stop):
    # Return True if there are no duplicate elements in slice S[start:stop].
    if stop - start <= 1: 
        return True                      # at most one item
    elif not unique3(S, start, stop-1): 
        return False                     # first part has duplicate
    elif not unique3(S, start+1, stop): 
        return False                     # second part has duplicate
    else: 
        return S[start] != S[stop-1]     # do first and last differ?

#################################################################################


# Adopt it form P3.58 - Confirm the maximum value of n


import time

class Unique():
    NUM_TESTS_PER_TIMECHECK = 10000
    def __init__(self):
        pass
    def tests_per_minute(func):
        def wrapper(*args, **kwargs):
            total_time = 60  #For one minute
            counter = 0
            while total_time >= 0:
                before = time.time()
                for _ in range(args[0].NUM_TESTS_PER_TIMECHECK):
                    out = func(*args, **kwargs)
                after = time.time()
                total_time -= after-before
                counter += 1
                #print (total_time)
            num_tests = counter * args[0].NUM_TESTS_PER_TIMECHECK
            return  num_tests
        return wrapper
    @tests_per_minute
    def unique1(self, S):
        for j in range(len(S)):
            for k in range(j+1, len(S)):
                if S[j] == S[k]:
                    return False
        return True
    @tests_per_minute
    def unique2(self, S):
        temp = sorted(S)
        for j in range(1, len(temp)):
            if S[j-1] == S[j]:
                return False
        return True
    # Note, we need this to prevent the decorator from calling itself infinitely
    def uniquer(self, S, start = 0, stop = None):
        if stop is None: 
            stop = len(S)
        if stop-start <= 1: 
            return True
        elif not self.uniquer(S, start, stop-1): 
            return False
        elif not self.uniquer(S, start+1, stop): 
            return False
        else: 
            return S[start] != S[stop-1]
    # This is from the next chapter...
    @tests_per_minute
    def unique3(self, S, start = 0, stop = None):
        if stop is None: 
            stop = len(S)
        if stop-start <= 1: 
            return True
        elif not self.uniquer(S, start, stop-1): 
            return False
        elif not self.uniquer(S, start+1, stop): 
            return False
        else: 
            return S[start] != S[stop-1]
    def test_each_algo(self, n):
        S = list(range(n))
        num_tests = {}
        for name, func in [('Unique1', self.unique1), ('Unique2', self.unique2), ('Unique3', self.unique3)]:
            num = func(S)
            num_tests[name] = num
        return num_tests


if __name__ == '__main__':     
    n = 5
    u = Unique()
    #u.unique3([1,2,3,4,5,6])
    results = u.test_each_algo(n)
    for key, value in results.items():
        print (f"The total number of tests for {key} is {value} for n = {n}")


# Output:

"""
The total number of tests for Unique1 is 23630000 for n = 5
The total number of tests for Unique2 is 59560000 for n = 5
The total number of tests for Unique3 is 10260000 for n = 5
"""