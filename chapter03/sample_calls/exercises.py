
# exercises.py


def example1(S):
    # Return the sum of the elements in sequence S.
    n = len(S)
    total = 0
    for j in range(n):           # loop from 0 to n-1
        total += S[j]
    return total


def example2(S):
    # Return the sum of the elements with even index in sequence S.
    n = len(S)
    total = 0
    for j in range(0, n, 2):     # note the increment of 2
        total += S[j]
    return total


def example3(S):
    # Return the sum of the prefix sums of sequence S.
    n = len(S)
    total = 0
    for j in range(n):            # loop from 0 to n-1
        for k in range(1+j):      # loop from 0 to j
            total += S[k]
    return total


def example4(S):
    # Return the sum of the prefix sums of sequence S.
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total


def example5(A, B):               # assume that A and B have equal length
    # Return the number of elements in B equal to the sum of prefix sums in A.
    n = len(A)                  
    count = 0
    for i in range(n):            # loop from 0 to n-1
        total = 0
        for j in range(n):        # loop from 0 to n-1
            for k in range(1+j):  # loop from 0 to j
                total += A[k]
        if B[i] == total:
            count += 1
    return count

#############################################################################################################################



import time
import matplotlib.pyplot as plt 


# class SumTimer(Prefix):
class SumTimer():
    def __init__(self):
        # super().__init__()
        self._timer_array = []
    def timer(func):
        def wrapper(*args, **kwargs):
            before = time.time()
            for _ in range(20):
                func(*args, **kwargs)
            after = time.time()
            args[0]._timer_array.append((after-before)*100000)  # Since the 1st arg is self, we access it with args[0]
            print('Total time is ', after-before)
        return wrapper
    @timer
    def example1(self,S):
        n = len(S)
        total = 0
        for j in range(n):
            total+= S[j]
        return total
    @timer
    def example2(self, S):
        n = len(S)
        total = 0
        for j in range(0, n, 2):
            total += S[j]
        return total
    @timer
    def example3(self, S):
        n = len(S)
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += S[k]
        return total
    @timer
    def example4(self, S):
        n = len(S)
        prefix = 0
        total = 0
        for j in range(n):
            prefix += S[j]
            total += prefix
        return total
    @timer
    def example5(self, A,B):
        n = len(A)
        count = 0
        for i in range(n):
            total = 0
            for j in range(n):
                for k in range(1+j):
                    total += A[k]
            if B[i] == total:
                count  += 1
        return count
    def _reset_timers(self):
        self._timer_array = []
    def test_timers(self, e_n = 5):
        results = {}
        for name, func in [('1',self.example1), ('2', self.example2), ('3', self.example3), ('4', self.example4), ('5', self.example5)]:
            for i in range(1, e_n):
                test_array = list(range(10**i))
                if name == '5': 
                    func(test_array, test_array)
                else: 
                    func(test_array)
            results[name] = self._timer_array
            self._reset_timers()
        x = list(map(lambda x: 10**x, range(1, e_n)))
        return x, results


# Note even at 4 it takes 454 seconds for the last step of example5.  Increase at your own risk!
if __name__ == '__main__':
    s = SumTimer()
    x, results = s.test_timers(4)  
    for f in results.values():
        plt.plot(x, f)
    plt.xscale('log')
    plt.yscale('log')


# Output:

"""
Total time is  3.910064697265625e-05
Total time is  0.00022101402282714844
Total time is  0.0025370121002197266
Total time is  2.9325485229492188e-05
Total time is  0.00011944770812988281
Total time is  0.0012829303741455078
Total time is  0.00022530555725097656
Total time is  0.00965428352355957
Total time is  0.5823299884796143
Total time is  2.1219253540039062e-05
Total time is  0.0001819133758544922
Total time is  0.0019745826721191406
Total time is  0.0009758472442626953
Total time is  0.5561339855194092
...
"""

#############################################################################################################################


# Note I am subclassing Prefix so you have to run that cell first

import time
import matplotlib.pyplot as plt 


class Prefix():
    def __init__(self):
        self._timer_array = []
    def timer(func):
        def wrapper(*args, **kwargs):
            before = time.time()
            for _ in range(20):
                func(*args, **kwargs)
            after = time.time()
            args[0]._timer_array.append((after-before)*100000)  #  Since the 1st arg is self, we access it with args[0]
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


class SumTimer(Prefix):
    def __init__(self):
        super().__init__()
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
    def example1(self,S):
        n = len(S)
        total = 0
        for j in range(n):
            total+= S[j]
        return total
    @timer
    def example2(self, S):
        n = len(S)
        total = 0
        for j in range(0, n, 2):
            total += S[j]
        return total
    @timer
    def example3(self, S):
        n = len(S)
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += S[k]
        return total
    @timer
    def example4(self, S):
        n = len(S)
        prefix = 0
        total = 0
        for j in range(n):
            prefix += S[j]
            total += prefix
        return total
    @timer
    def example5(self, A,B):
        n = len(A)
        count = 0
        for i in range(n):
            total = 0
            for j in range(n):
                for k in range(1+j):
                    total += A[k]
            if B[i] == total:
                count  += 1
        return count
    def test_timers(self, e_n = 5):
        results = {}
        for name, func in [('1',self.example1), ('2', self.example2), ('3', self.example3), ('4', self.example4), ('5', self.example5)]:
            for i in range(1, e_n):
                test_array = list(range(10**i))
                if name == '5': func(test_array, test_array)
                else: func(test_array)
            results[name] = self._timer_array
            self._reset_timers()
        x = list(map(lambda x: 10**x, range(1, e_n)))
        return x, results


# Note even at 4 it takes 454 seconds for the last step of example5.  Increase at your own risk!
if __name__ == '__main__':
    s = SumTimer()
    x, results = s.test_timers(4)  
    for f in results.values():
        plt.plot(x, f)
    plt.xscale('log')
    plt.yscale('log')


# Output:

"""
Total time is  3.933906555175781e-05
Total time is  0.0002200603485107422
Total time is  0.002554655075073242
Total time is  2.86102294921875e-05
Total time is  0.000118255615234375
Total time is  0.0012781620025634766
Total time is  0.00021505355834960938
Total time is  0.010835409164428711
Total time is  0.5882172584533691
Total time is  3.0517578125e-05
Total time is  0.00018906593322753906
Total time is  0.0020797252655029297
Total time is  0.0010344982147216797
Total time is  0.573540210723877
...
"""