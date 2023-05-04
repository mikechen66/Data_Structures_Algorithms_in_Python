
# Algorithm Analysis 

########################################################################################################

# Part One. Reinforcement

########################################################################################################


# R-3.1 Graph the functions 8n, 4n log n, 2n 2 , n 3 , and 2 n using a logarithmic scale
# for the x- and y-axes; that is, if the function value f (n) is y, plot this as a
# point with x-coordinate at log n and y-coordinate at log y.


# (1). General Usage with the for loop

import math
import numpy as np
import matplotlib.pyplot as plt


x = [10**i for i in range(10)]


funcs = [lambda x: 8*x,
         # lambda x: 4*x*math.log10(x),
         # lambda x: 2*x**2,
         # lambda x: x**3,
         # lambda x: 2**x,
        ]


if __name__ == '__main__':
    ys = []
    for func in funcs:
        ys.append(list(map(func, x)))
        m = map(func, x)
        print(m)
        a = list(map(func, x))
        print(a)
        print(ys)
    for y in ys:
        plt.plot(x, y)
    plt.yscale('log')
    plt.xscale('log')


# Output

"""
>>> # print(m)
<map object at 0x7f04edf43d90>
>>> # print(a)
[8, 80, 800, 8000, 80000, 800000, 8000000, 80000000, 800000000, 8000000000]
>>> # print(ys)
[[8, 80, 800, 8000, 80000, 800000, 8000000, 80000000, 800000000, 8000000000]]
>>> # plot
[<matplotlib.lines.Line2D object at 0x7f04edf4c710>]
"""

#----------------------------------------------------------------------------------


# (2). Use func within the for loop


import math
import numpy as np
import matplotlib.pyplot as plt


x = [10**i for i in range(10)]


funcs = [lambda x: 8*x,
         lambda x: 4*x*math.log(x),  # e as base number 
         lambda x: 2*x**2, 
         lambda x: 2*math.pow(x,3),
         # lambda x: np.exp2(x),
        ]


if __name__ == '__main__':
    ys = []
    for func in funcs:
        ys.append(list(map(func, x)))
        print(ys)
    for y in ys:
        plt.plot(x, y)
    plt.yscale('log')
    plt.xscale('log')

########################################################################################################


# R3.23. Give a big-Oh characterization, in terms of n, of the running time of the
# example1 function shown in Code Fragment 3.10.


def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    count = 0
    num_calc = []
    for j in range(n):
        total += S[j]
        count += 1
        num_calc.append(count)
    return total, num_calc


if __name__ == '__main__':
    s = np.random.randint(0, 100, size=(100,))
    total, num_calc = example1(s)
    plt.plot(num_calc)


# Output:

"""
[<matplotlib.lines.Line2D object at 0x7fd961370f90>]
"""

########################################################################################################


# R3.24. Give a big-Oh characterization, in terms of n, of the running time of the
# example2 function shown in Code Fragment 3.10.


def example2(S):
    """Return the sum of the elemnets in sequnce S."""
    n = len(S)
    total = 0
    count = 0
    num_calc = []
    for j in range(0, n, 2):
        total += S[j]
        count += 1
        num_calc.append(count)
    return total, num_calc


if __name__ == '__main__':
    total, num_calc = example2(s)
    plt.plot(num_calc)


# Output:

"""
[<matplotlib.lines.Line2D object at 0x7fd96138d590>]
"""

########################################################################################################


# R3.25. Give a big-Oh characterization, in terms of n, of the running time of the
# example3 function shown in Code Fragment 3.10.


def example3(S):
    """Return the sum of the elemnets in sequnce S."""
    n = len(S)
    total = 0
    count = 0
    num_calc = []
    for j in range(n):
        for k in range(1+j):
            total += S[j]
            count += 1
        num_calc.append(count)
    return total, num_calc


if __name__ == '__main__':
    total, num_calc = example3(s)
    plt.plot(num_calc)

########################################################################################################


# R3.26. Give a big-Oh characterization, in terms of n, of the running time of the
# example4 function shown in Code Fragment 3.10.


def example4(S):
    """Return the sum of the elemnets in sequnce S."""
    n = len(S)
    prefix = 0
    total = 0
    count = 0
    num_calc = []
    for j in range(n):
        prefix += S[j]
        total += prefix
        count += 1
        num_calc.append(count)
    return total, num_calc


if __name__ == '__main__':
    total, num_calc = example4(s)
    plt.plot(num_calc)

########################################################################################################


# R3.27. Give a big-Oh characterization, in terms of n, of the running time of the
# example5 function shown in Code Fragment 3.10.


def example5(A, B):
    """Return the number of elements in B equal to the sum of prefix sums in A."""
    n = len(A)
    count = 0
    num_calc = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
                num_calc += 1
        if B[i] == total:
            count+=1
    return count, num_calc


def get_time_complexity_2(n=100):
    op_nums = []
    for i in range(1, n):
        A = np.random.randint(0, 100, size=(i, ))
        B = np.random.randint(0, 100, size=(i, ))
        _, num_calc = example5(A, B)
        op_nums.append(num_calc)
    plt.plot(op_nums)
    plt.plot(range(n), [i**2 for i in range(n)])
    plt.plot(range(n), [i**3 for i in range(n)])
    plt.legend(['example5', '$n^2$', '$n^3$'])
    plt.title('example5')
    plt.show()


if __name__ == '__main__':
    get_time_complexity_2()


########################################################################################################


# R3.28. For each function f (n) and time t in the following table, determine the
# largest size n of a problem P that can be solved in time t if the algorithm
# for solving P takes f (n) microseconds (one entry is already completed).
# Confirm the miliseconds of algorithms


import math
import numpy as np
import pandas as pd


second = 10e6
rel_lengths = [1, 60*60]

x = [second*x for x in rel_lengths]


functions = [lambda x: math.log(x), 
             lambda x: x,
             lambda x: x*math.log(x),  # This one can't be solved easily...
             lambda x: x**2,
             # lambda x: np.exp2(x),
            ]


if __name__ == '__main__':
    names = ['logn', 'n', 'nlogn', 'n^2', '2^n']
    df = pd.DataFrame(columns=['seconds','hours'])
    for i in range(len(functions)):
        inp = list(map(functions[i], x))
        print(inp)
        df.loc[names[i]] = inp 
    df.loc[names[0]] = [10e3000, np.nan]
    df.loc[names[2]] = [87847*x for x in rel_lengths]
    df


# Output: 

"""
>>> print(inp)
[16.11809565095832, 24.30678477540252]
[10000000.0, 36000000000.0]
[161180956.5095832, 875044251914.4907]
[100000000000000.0, 1.296e+21]
>>> # df
            seconds         hours
logn            inf           NaN
n      1.000000e+07  3.600000e+10
nlogn  8.784700e+04  3.162492e+08
n^2    1.000000e+14  1.296000e+21
"""

#######################################################################################################


# R3.34. There is a well-known city (which will go nameless here) whose inhabitants 
# have the reputation of enjoying a meal only if that meal is the best they have ever 
# experienced in their life. Otherwise, they hate it. Assuming meal quality is 
# distributed uniformly across a person’s life, describe the expected number of times 
# inhabitants of this city are happy with their meals?


import math
import matplotlib.pyplot as plt


print(math.log(10000, math.e))
print(math.log(1, math.e))  # This is trivial


x = list(range(1, 10000))
y = list(map(lambda x: math.log(x, math.e), x))
plt.plot(x, y)
plt.xlabel('Total Restaurants')
plt.ylabel('Enjoyed Restaurants')
plt.show()


########################################################################################################
########################################################################################################


# Part Two. Creativity

########################################################################################################


# C3-36. Describe an efficient algorithm for finding the ten largest elements in a
# sequence of size n. What is the running time of your algorithm?

# Find 10 largest number in the sequence length as n 


def last_10(array):
    if len(array)>=10:   
        return sorted(array)[-10:]
    else: 
        return array


if __name__ == '__main__': 
    print(last_10([1,2,3,4,5,6,7,4,3,2,65,7,5,4]))
    print(last_10([x^2 + 3*x for x in range(30)]))
    print(last_10([1,2,3,5,4]))


# Output:

"""
[3, 4, 4, 4, 5, 5, 6, 7, 7, 65]
[42, 68, 72, 74, 74, 80, 82, 82, 84, 84]
[1, 2, 3, 5, 4]
"""


"""
Additional operation: 
>>> list = [1,2,3,4,5,6,7,4,3,2,65,7,5,4]
>>> newlist = sorted(list)
>>> newlist
[1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 7, 65]
>>> truncated_list = newlist[-10:]
>>> truncated_list
[3, 4, 4, 4, 5, 5, 6, 7, 7, 65]
>>> 
"""

########################################################################################################


# C3.37. Give an example of a positive function f (n) such that f (n) is neither O(n)
# nor Ω(n).


import matplotlib.pyplot as plt
import math


x = list(range(100))
print(x)
y = list(map(lambda x: x**2*(1+math.cos(x)), x))
print(y)
plt.plot(x, y)


# Output:

"""
>>> # print(x)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> # print(y)
[0.0, 1.5403023058681398, 2.3354126538114306, 0.09006753059599126, 5.541702066182209, 32.09155463658065, 70.56613031941318, 85.94121046282193, 54.687997836248734, 7.198448787341168, 
16.092847092354756, 121.53550945655415, 265.5149700574789, 322.3585060650832, 222.8004947687354, 54.07021960676521, 10.839173037213527, 209.47779530308847, 537.9426134710819, 717.9223671653876, 
563.2328247253567, 199.45139624109765, 0.01896002499563121, 247.1313322436327, 820.3271082261102, 1244.5017574146711, 1113.3174618941607, 516.0308084330335, 29.31700081016379, 211.88361753155075, 
1038.8263048988256, 1840.0674058501545, 1878.2447211586664, 1074.5416222740882, 175.05276234899637, 117.97704876290427, 1130.1590582428835, 2416.851837113175, 2823.1263420042937, 1926.5639001194647, 
532.899101356381, 21.282674482447753, 1058.4259043605484, 2875.404494511637, 3871.69664554193, 3088.777027355903, 1201.5114686238092, 16.930948645598413, 829.1074418629639, 3122.722697528473, 
4912.4150712302835, 4531.343065912649, 2263.2729287284124, 229.54365353015802, 497.73252737105406, 3091.933437692416, 5811.698257818023, 6172.66732082291, 3764.9219756498283, 796.8697438210828, 
171.31327050543726, 2760.6038126737067, 6432.961531971865, 7882.023532301139, 5701.047215839437, 1848.632478518723, 1.5356818105795629, 2164.7313687449114, 6659.221336021693, 9490.531597857735, 
8003.26409512287, 3483.216427314838, 169.77295038819344, 1405.8290045666336, 6416.324163865338, 10809.850892201714, 10537.337768477253, 5745.349036865618, 865.1259806974941, 649.2453210775992, 
5693.521639430096, 11656.836728043922, 13109.63284056222, 8608.081872718327, 2257.7542151357375, 112.87875147804763, 4558.166301151709, 11881.440280054145, 15483.146708935044, 11962.11237298296, 
4470.6037093537225, 46.643056053563406, 3161.7741928868904, 11394.4408394439, 17402.14296389601, 15614.816387978248, 7553.15297933337, 704.2868281643415, 1735.5556922208252, 10191.284448733153]
>>> # plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x7f648b761890>]
"""

########################################################################################################


# C3.41 Describe an algorithm for finding both the minimum and maximum of n
# numbers using fewer than 3n/2 comparisons. (Hint: First, construct a group 
# of candidate minimums and a group of candidate maximums.) 


def minmax(list):
    newlist = sorted(list, key=None, reverse=False)
    return (newlist[0], newlist[4])


if __name__ == '__main__':
    list = [13, 22, 6, 99, 11]
    minmax(list)


# Output:

"""
(6, 99)
"""

####################################################################################################


# C3.45. A sequence S contains n − 1 unique integers in the range [0, n − 1], i.e,, 
# there is one number from this range that is not in S. Design an O(n)-time algorithm 
# for finding that number. You are only allowed to use O(1) additional space besides 
# the sequence S itself.


# (1). A general function 

def find_missing(S):
    total_list = list(range(len(S)+1))
    # print(total_list)
    total = 1
    for x in total_list:
        total *= x+1
        print(total)
    for x in S:
        total /= x+1
        print(total)
    return int(total-1)


if __name__ == '__main__':
    find_missing([0,1,2,3,4,6,7,8,9])


# Output

"""
1
2
6
24
120
720
5040
40320
362880
3628800
3628800.0
1814400.0
604800.0
151200.0
30240.0
4320.0
540.0
60.0
6.0
5

"""

#--------------------------------------------------------------------------------------------------


# (2). Add remove() function


def find_missing(S):
    # len(S) + 1后等于main()函数中的数组中第一个S
    total_list = list(range(len(S)+1))
    # print(total_list)
    total = 1
    for x in total_list: # compute the factorial 10! = 3628800
        total *= x+1
        print(total)
    for x in S:
        total /= x+1
        print(total)
    return int(total-1)


if __name__ == '__main__':
    S = [i for i in range(10)]
    # print(S)
    S.remove(5)
    # S.append(10)
    # print(S)
    find_missing(S)


# Output:

"""
1
2
6
24
120
720
5040
40320
362880
3628800
3628800.0
1814400.0
604800.0
151200.0
30240.0
4320.0
540.0
60.0
6.0
5
"""

####################################################################################################


# C3.49. Consider the Fibonacci function, F(n) (see Proposition 3.20). Show by
# induction that F(n) is Ω((3/2) n ).


def output_fibbo():
    smaller = True
    F0 = 0
    F1 = 1
    power = 1
    counter = 0
    while F1 <= power:
        counter += 1
        F1, F0 = F1+F0, F1
        power *= (3/2)
        print(counter, F1, power)


if __name__ == '__main__':
    output_fibbo()


# Output:

"""
1 1 1.5
2 2 2.25
3 3 3.375
4 5 5.0625
5 8 7.59375
"""

####################################################################################################


# C3. 50 Horner's Algorithm for Newton's Polynomial


"""
a)
Loop from 0 to n as i
    Loop from 0 to i, calculating the value of xi as ai*=x
    
This would take n*(n+1)/2 or O(n**2)

In other words, every time we increase n, we have to do one extra addition and n multiplications, 
which means we have an arithmetically increasing sum that 


b) If you kept a running total of x, you would just need to multiply it again to get the new value of x**i
since x**i = x**(i-1)*x


So for each step, you say: 

x = 1

for a in polynomials:
    total += a*(x_total)
    x_total *= x

return total

This seems like it would only take O(n) time, so I'm not sure...


c) Using horner's method, we only need O(n) multiplications and O(n) additions

"""


def polynomial(x, coefficients):
    x_tot = 1
    total = 0
    for a in coefficients:
        total += a*x_tot
        x_tot *= x
    return total


if __name__ == '__main__':
   polynomial(5, [1, 2, 3])


# Output:
# 86

####################################################################################################


# C3.54


# The algorithm below works in O(n) time, but uses O(n) space as well


import random


def find_most_frequent(n):
    S = []
    for _ in range(n):
        S.append(random.randint(0, 4*n-1))
    print(S)
    counts = [0]*(4*n)
    max_int = 0
    for num in S:
        counts[num] += 1
        if counts[num] >= counts[max_int]:
            max_int = num
    print(max_int, counts[max_int])
    if counts[max_int] == 1: 
        return False
    else: 
        return max_int

if __name__ == '__main__':
    find_most_frequent(1000)


####################################################################################################
####################################################################################################


# Part Three. Project

####################################################################################################


# P3.55. Perform an experimental analysis of the three algorithms prefix average1,
# prefix average2, and prefix average3, from Section 3.3.3. Visualize their
# running times as a function of the input size with a log-log chart.


import time
import matplotlib.pyplot as plt 


class Prefix():
    def __init__(self):
        self._timer_array = []
    def timer(func): # Add timer() decorator 
        def wrapper(*args, **kwargs):
            before = time.time()
            for _ in range(20):
            # for i in range(20): 
                func(*args, **kwargs)
            after = time.time()
            args[0]._timer_array.append((after-before)*100000)  # Since the 1st arg is self, we access it with args[0]
            # self._timer_array.append((after-before)*100000)   # self is wrong
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
Total time is  0.0002655982971191406
Total time is  0.0070378780364990234
Total time is  0.5870871543884277
Total time is  64.76023435592651
Total time is  7.963180541992188e-05
Total time is  0.0015132427215576172
Total time is  0.09247279167175293
Total time is  9.318366289138794
Total time is  3.7670135498046875e-05
Total time is  0.0002472400665283203
Total time is  0.002610445022583008
Total time is  0.02959585189819336
[<matplotlib.lines.Line2D object at 0x7f5419c64d90>]
[<matplotlib.lines.Line2D object at 0x7f5419c89350>]
[<matplotlib.lines.Line2D object at 0x7f5419c89890>]
"""

####################################################################################################


# P3.56. Perform an experimental analysis that compares the relative running times
# of the functions shown in Code Fragment 3.10.


# (1). Simplified form 


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
            args[0]._timer_array.append((after-before)*100000)  # Access it with args[0] rather than self
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


#--------------------------------------------------------------------------------------------------------


# (2). Inherited form 


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
            args[0]._timer_array.append((after-before)*100000)  # Since the 1st arg is self, we access it with args[0]
            print('Total time is ', after-before)
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
    def test_timers(self, e_n=5):
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

####################################################################################################


# P3.57 Perform experimental analysis to test the hypothesis that Python’s sorted
# method runs in O(n log n) time on average.


import random
import time
import matplotlib.pyplot as plt


def test_sorted(n_e_max=4, num_tests=10000):
    xs = [list(range(2**x)) for x in range(1, n_e_max)]
    output_times = []
    times = []
    nlogns = []
    for x in xs:      
        random.shuffle(x)
        before = time.time()
        # for j in range(num_tests):
        for _ in range(num_tests):
            sorted(x)
        after = time.time()
        times.append(after-before)
        nlogns.append(2**((after-before)/len(x)))
    return (times, nlogns)


if __name__ == '__main__':     
    n_e_max = 15
    times, y = test_sorted(n_e_max)
    x = [2**x for x in range(1, n_e_max)]
    plt.plot(x, y)
    plt.show()


# Output: 
# [<matplotlib.lines.Line2D object at 0x7f7cc1c32090>]

####################################################################################################


# P3.58. For each of the three algorithms, unique1, unique2, and unique3, which
# solve the element uniqueness problem, perform an experimental analysis
# to determine the largest value of n such that the given algorithm runs in
# one minute or less.


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
                # print (total_time)
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
    # Need the code to prevent the decorator from calling itself infinitely
    def uniquer(self, S, start=0, stop=None):
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
    def unique3(self, S, start=0, stop=None):
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
        print(f"The total number of tests for {key} is {value} for n = {n}")


# Output:

"""
The total number of tests for Unique1 is 23630000 for n = 5
The total number of tests for Unique2 is 59560000 for n = 5
The total number of tests for Unique3 is 10260000 for n = 5
"""
