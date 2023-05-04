

# Recursion 

###########################################################################################################

# Part One. Reforcement

###########################################################################################################


# R4.1. Describe a recursive algorithm for finding the maximum element in a se-quence, 
# S, of n elements. What is your running time and space usage?

# (1). Functional programming


def rec_find_max(S,index):
    if index == len(S)-1:
        return S[index]
    return max(S[index], rec_find_max(S, index+1))


def find_max(S):
    return rec_find_max(S, 0)


if __name__ == '__main__':
    print(find_max([1,2,3,4,5,6,7,8]))
    print(find_max([1,2,774,5,6,7,8]))
    print(find_max([8,7,6,5,4,3,2,1]))

# Output

"""
8
774
8
"""

#----------------------------------------------------------------------------------------------------------


# Adopt a class 

class Algorithm:
    def __init__(self):
        pass
    def rec_find_max(self, s, index):
        if index == len(s)-1:
            return s[index]
        return max(s[index], self.rec_find_max(s, index+1))
    def find_max(self, s):
        return self.rec_find_max(s, 0)


if __name__ == '__main__':
    algo = Algorithm()
    print(algo.find_max([1,2,3,4,5,6,7,8]))
    print(algo.find_max([1,2,774,5,6,7,8]))
    print(algo.find_max([8,7,6,5,4,3,2,1]))


# Output

"""
8
774
8
"""

############################################################################################################


# R4.2 Plot power(2, 5)


def power(x,n):
    if n==0:
        return 1
    else:
        return x * power(x, n-1)


if __name__ == '__main__':
    print(power(2,5))


# Output:

"""
32
"""

############################################################################################################


# R4.3 power(2,18)


def power(x, n):
    if n==0:
        return 1
    else:
        partial = power(x, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= x
        return result


if __name__ == '__main__':
    print(power(2,18))


# Output:
# 262144

#----------------------------------------------------------------------------------------------------------


# (3). Define Recursion class


class Algorithm:
    def __init__(self):
        pass
    def power(self, x, n):
        if n==0:
            return 1
        else:
            partial = self.power(x, n//2)
            result = partial * partial
            if n%2 == 1:
                result *= x
            return result


if __name__ == '__main__':
    algo = Algorithm()
    power_result = algo.power(2,18)
    print(power_result)


# Output:
# 262144

############################################################################################################


# R4.4 raw the recursion trace for the execution of function reverse(S, 0, 5)
# (Code Fragment 4.10) on S = [4, 3, 6, 2, 6].


# (1). Functional programming


def reverse(S, start, stop):
    if start < stop-1:
        s[start], s[stop-1] = s[stop-1], s[start]
        reverse(s, start+1, stop-1)


if __name__ == '__main__':
    s = [4, 3, 6, 2, 6]
    reverse(s, 0, 5)
    print(s)


# Output:
# [6, 2, 6, 3, 4]

#----------------------------------------------------------------------------------------------------------


# (2). Adopt a class 


class Algorithm:
    def __init__(self, s):
        self.s = s
    def reverse(self, start, stop):
        if start < stop-1:
            self.s[start], self.s[stop-1] = self.s[stop-1], self.s[start]
            self.reverse(start+1, stop-1)


if __name__ == '__main__':
    s = [4, 3, 6, 2, 6]
    algo = Algorithm(s)
    rev_result = algo.reverse(0, 5)
    print(s)


# Output:

"""
[6, 2, 6, 3, 4]
"""

############################################################################################################


# R4.5 Plot the trace back of puzzle_solve(3,s,u) while s is empty and u = {a,b,c,d}


# (1). Define functions 


def solves(s):
    #Note, this is a random solution to the pseudoproblem
    return s == ['d','b','c']


def puzzle_solver(k, s, u):
    for e in sorted(u).copy():
        s.append(e)
        u.remove(e)
        if k==1:
            print(s)
            if solves(s):
                print(f'Solution found: {s}')
        else:
            puzzle_solver(k-1, s, u)
        u.add(s.pop())  #removes the last item of an array


if __name__ == '__main__':
    puzzle_solver(3, [], {'a','b','c','d'})


# Output:

"""
['a', 'b', 'c']
['a', 'b', 'd']
['a', 'c', 'b']
['a', 'c', 'd']
['a', 'd', 'b']
['a', 'd', 'c']
['b', 'a', 'c']
['b', 'a', 'd']
['b', 'c', 'a']
['b', 'c', 'd']
['b', 'd', 'a']
['b', 'd', 'c']
['c', 'a', 'b']
['c', 'a', 'd']
['c', 'b', 'a']
['c', 'b', 'd']
['c', 'd', 'a']
['c', 'd', 'b']
['d', 'a', 'b']
['d', 'a', 'c']
['d', 'b', 'a']
['d', 'b', 'c']
Solution found: ['d', 'b', 'c']
['d', 'c', 'a']
['d', 'c', 'b']
"""

#----------------------------------------------------------------------------------------------------------


# Define a class


class Algorithm:
    def __init__(self, s):
        self.s = s
    def solves(self):
        # Note this is a random solution to the pseudoproblem
        return self.s == ['d','b','c']
    def puzzle_solver(self, k, u):
        for e in sorted(u).copy():
            self.s.append(e)
            u.remove(e)
            if k==1:
                print(self.s)
                if self.solves():
                    print(f'Solution found: {self.s}')
            else:
                self.puzzle_solver(k-1, u)
            u.add(self.s.pop())  # removes the last item of an array


if __name__ == '__main__':
    algo = Algorithm(s=[])
    ps_result = algo.puzzle_solver(3, {'a','b','c','d'})


# Output:

"""
['a', 'b', 'c']
['a', 'b', 'd']
['a', 'c', 'b']
['a', 'c', 'd']
['a', 'd', 'b']
['a', 'd', 'c']
['b', 'a', 'c']
['b', 'a', 'd']
['b', 'c', 'a']
['b', 'c', 'd']
['b', 'd', 'a']
['b', 'd', 'c']
['c', 'a', 'b']
['c', 'a', 'd']
['c', 'b', 'a']
['c', 'b', 'd']
['c', 'd', 'a']
['c', 'd', 'b']
['d', 'a', 'b']
['d', 'a', 'c']
['d', 'b', 'a']
['d', 'b', 'c']
Solution found: ['d', 'b', 'c']
['d', 'c', 'a']
['d', 'c', 'b']
"""

############################################################################################################


# R4.6. Describe a recursive function for computing the n th Harmonic number,
# Hn = ∑_{i~n} 1/i.


# Function: Compute harmonic number


def harmonic_recursive(n):
    if n==1:
        return 1
    else:
        return 1/n + harmonic_recursive(n-1)


if __name__ == '__main__':
    print(harmonic_recursive(10))


# Output:
# 2.9289682539682538

#----------------------------------------------------------------------------------------------------------


# CLass: Compute harmonic number


class Algorithm:
    def __init__(self):
        pass
    def harmonic_recursive(self, n):
        if n==1:
            return 1
        else:
            return 1/n + self.harmonic_recursive(n-1)


if __name__ == '__main__':
    algo = Algorithm()
    har_result = algo.harmonic_recursive(10)
    print(har_result)


# Output:
# 2.9289682539682538

############################################################################################################


# R4.7. Describe a recursive function for converting a string of digits into the integer 
# it represents. For example, 13531 represents the integer 13, 531. Turn a string of number 
# into integers 


# Define a function
def str2int(string, index=0):
    length = len(string)
    if index == length-1:
        return int(string[index])
    else:
        return int(string[index])*10**(length-index-1) + str_2_int(string, index+1)


if __name__ == '__main__':
    ans = str2int('12342543')
    print (ans, type(ans))    


# Output:
# 12342543 <class 'int'>

#----------------------------------------------------------------------------------------------------------


class Algorithm:
    def __init__(self):
        pass
    def str2int(self, string, index = 0):
        length = len(string)
        if index == length-1:
            return int(string[index])
        else:
            return int(string[index])*10**(length-index-1) + self.str2int(string, index+1)


if __name__ == '__main__':
    algo = Algorithm()
    ans = algo.str2int('12342543')
    print(ans, type(ans))    


# Output:
# 12342543 <class 'int'>

############################################################################################################


# R4.8. Isabel has an interesting way of summing up the values in a sequence A of
# n integers, where n is a power of two. She creates a new sequence B of half the 
# size of A and sets B[i] = A[2i] + A[2i + 1], for i = 0, 1, . . . , (n/2) − 1. If
# B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and repeats 
# the process. What is the running time of her algorithm?


# (1). Define a function 


import math


def isabel_method(A):
    assert math.log(len(A),2)%1 == 0, 'Your array must be a length that is a power of 2'
    if len(A) == 1:
        return A[0]
    else:
        B = [None]*(len(A)//2)
        for i in range(len(B)):
            B[i] = A[2*i] + A[2*i-1]           
        return isabel_method(B)


if __name__ == '__main__':                
    print(isabel_method([0, 1,2,3,4,5,6,7]))
    try:
        print(isabel_method([1,2,3,4,5,6,7]))
    except Exception as e:
        print(e)


# Output:

"""
28
Your array must be a length that is a power of 2
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class 


import math


class Algorithm:
    def __init__(self):
        pass
    def isabel_method(self, A):
        assert math.log(len(A),2) % 1 == 0, 'Your array must be a length that is a power of 2'
        if len(A) == 1:
            return A[0]
        else:
            B = [None] * (len(A)//2)
            for i in range(len(B)):
                B[i] = A[2*i] + A[2*i-1]           
            return self.isabel_method(B)


if __name__ == '__main__':   
    algo = Algorithm()             
    print(algo.isabel_method([0, 1,2,3,4,5,6,7]))
    try:
        print(algo.isabel_method([1,2,3,4,5,6,7]))
    except Exception as e:
        print(e)


# Output:

"""
28
Your array must be a length that is a power of 2
"""

############################################################################################################
############################################################################################################


# Part Two. Creativity

############################################################################################################


# C4.9

# Write a short recursive Python function that finds the minimum and maximum values 
# in a sequence without using any loops. It is similar to R4.1


# (1). Define a minmax function 


def minmax(s, index=0):
    if index == len(s) - 1:
        return s[index], s[index]  #The current min and max VALUEs
    else:
        min_c, max_c = minmax(s, index+1)
        return min(s[index], min_c), max(s[index], max_c)


if __name__ == '__main__': 
    print(minmax([1,2,3,4,5,6,7,8]))
    print(minmax([-45,2,774,5,6,7,8]))
    print(minmax([8,7,6,5,4,3,2,1]))


# Output:

"""
(1, 8)
(-45, 774)
(1, 8)
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class 


class Algorithm:
    def __init__(self):
        pass
    def minmax(self, s, index=0):
        if index == len(s) - 1:
            return s[index], s[index]  #The current min and max VALUEs
        else:
            min_c, max_c = self.minmax(s, index+1)
            return min(s[index], min_c), max(s[index], max_c)


if __name__ == '__main__': 
    algo = Algorithm()
    print(algo.minmax([1,2,3,4,5,6,7,8]))
    print(algo.minmax([-45,2,774,5,6,7,8]))
    print(algo.minmax([8,7,6,5,4,3,2,1]))


# Output:

"""
(1, 8)
(-45, 774)
(1, 8)
"""

############################################################################################################


# C4.10. Describe a recursive algorithm to compute the integer part of the base-two
# logarithm of n using only addition and integer division.


# (1). Defina log2int() function 

import math


def log2int(n):
    if n < 2:
        return 0   #If you are less than 2, you don't get to accumulate any more divisions.  Note it isn't <=2
    else:
        return 1 + log2int(n//2)


if __name__ == '__main__': 
    for n in [100, 5, 7, 1.9, 0.1, 6]:
        print(n, log2int(n), math.log(n, 2))


# Output:

"""
100 6 6.643856189774725
5 2 2.321928094887362
7 2 2.807354922057604
1.9 0 0.925999418556223
0.1 0 -3.321928094887362
6 2 2.584962500721156
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class


import math


class Algorithm:
    def __init__(self):
        pass
    def log2int(self, n):
        if n < 2:
            return 0   #If you are less than 2, you don't get to accumulate any more divisions.  Note it isn't <=2
        else:
            return 1 + self.log2int(n//2)


if __name__ == '__main__': 
    algo = Algorithm()
    for n in [100, 5, 7, 1.9, 0.1, 6]:
        print(n, algo.log2int(n), math.log(n, 2))


# Output:

"""
100 6 6.643856189774725
5 2 2.321928094887362
7 2 2.807354922057604
1.9 0 0.925999418556223
0.1 0 -3.321928094887362
6 2 2.584962500721156
"""

############################################################################################################


# C4-11 Describe an efficient recursive function for solving the element uniqueness 
# problem, which runs in time that is at most O(n 2 ) in the worst case without using 
# sorting.


# (1). Defina aa function


def unique_no_dict(s, index = 0):
    if index == len(s) - 1:
        return True    # The trivialgo case is true
    else:
        unique = True
        for i in range(index+1, len(s)):
            if s[index] == s[i]: 
                unique = False
        # Note this return will short-circuit if unique is False, therefore saving time
        return unique and unique_no_dict(s, index+1)


if __name__ == '__main__':     
    for s in [[1,2,3,4,5,6], 
              [3,4,5,2,3,4,6,7],
              [234,654,32,543,652]
             ]:
        print(unique_no_dict(s))


# Output:

"""
True
False
True
"""

#----------------------------------------------------------------------------------------------------------


# Define a class 

class Algorithm:
    def __init__(self):
        pass
    def unique_no_dict(self, s, index = 0):
        if index == len(s) - 1:
            return True    
        else:
            unique = True
            for i in range(index+1, len(s)):
                if s[index] == s[i]: 
                    unique = False
            # The return will short-circuit if unique is False, therefore saving time
            return unique and self.unique_no_dict(s, index+1)


if __name__ == '__main__': 
    algo = Algorithm()    
    for s in [[1,2,3,4,5,6], 
              [3,4,5,2,3,4,6,7],
              [234,654,32,543,652]
             ]:
        print(algo.unique_no_dict(s))


# Output:

"""
True
False
True
"""

############################################################################################################


# C4.12 Give a recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction.


# Define a function 

def prod(m, n):
    if not n: #ie. if n==0
        return 0
    else:
        return m + prod(m, n-1)


if __name__ == '__main__':     
    for x, y in [(1,2),
                 (3,6),
                 (10, 10)
                ]:
        print(f'The product of {x} and {y} is {prod(x, y)}')


# Output:

"""
The product of 1 and 2 is 2
The product of 3 and 6 is 18
The product of 10 and 10 is 100
"""

#----------------------------------------------------------------------------------------------------------


# Define a class 


class Algorithm:
    def __init__(self):
        pass
    def prod(self, m, n):
        if not n: #ie. if n==0
            return 0
        else:
            return m + self.prod(m, n-1)


if __name__ == '__main__':    
    algo = Algorithm() 
    for x, y in [(1,2),
                 (3,6),
                 (10, 10)
                ]:
        print(f'The product of {x} and {y} is {algo.prod(x, y)}')


# Output:

"""
The product of 1 and 2 is 2
The product of 3 and 6 is 18
The product of 10 and 10 is 100
"""

############################################################################################################


# C4.In Section 4.2 we prove by induction that the number of lines printed by
# a call to draw interval(c) is 2 c − 1. Another interesting question is how
# many dashes are printed during that process. Prove by induction that the
# number of dashes printed by draw interval(c) is 2 c+1 − c − 2.


# F(C) = 2*(2**(c+1-1) - (c-1) -2) + c = 2**(c+1) - 2*(c-1) - 4 + c

"""
2**(c+1) - 2*(c-1) - 4 + c 
= 2**(c+1) - 2c +2 -4 +c
= 2**(c+1) -c -2 as required
"""

############################################################################################################


# C4.4 In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,
# b, and c, sticking out of it. On peg a is a stack of n disks, each larger than
# the next, so that the smallest is on the top and the largest is on the bottom.
# The puzzle is to move all the disks from peg a to peg c, moving one disk at a 
# time, so that we never place a larger disk on top of a smaller one. See Figure 
# 4.15 for an example of the case n = 4. Describe a recursive algorithm for solving 
# the Towers of Hanoi puzzle for arbitrary n. (Hint: Consider first the subproblem 
# of moving all but the n th disk from peg a to another peg using the third as 
# “temporary storage.”)


# Define a function 
import sys
import stdio


def moves(n, left):
    if n == 0:
        return
    moves(n-1, not left)
    if left:
        stdio.writeln(str(n) + ' left')
    else:
        stdio.writeln(str(n) + ' right')
    moves(n-1, not left)


if __name__ == '__main__':
    n = 5
    moves(n, True)


# Output:

"""
1 left
2 right
1 left
3 left
1 left
2 right
1 left
4 right
1 left
2 right
1 left
3 left
1 left
2 right
1 left
5 left
1 left
2 right
1 left
3 left
1 left
2 right
1 left
4 right
1 left
2 right
1 left
3 left
1 left
2 right
1 left
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class 


import sys
import stdio


class HanoiTower:
    def __init__(self):
        pass
    def moves(self, n, left):
        if n == 0:
            return
        self.moves(n-1, not left)
        if left:
            stdio.writeln(str(n) + ' left')
        else:
            stdio.writeln(str(n) + ' right')
        self.moves(n-1, not left)


if __name__ == '__main__':
    hv = HanoiTower()
    n = 5
    hv.moves(n, True)


# Output:

"""
1 left
2 right
1 left
3 left
1 left
2 right
1 left
4 right
1 left
2 right
1 left
3 left
1 left
2 right
1 left
5 left
1 left
2 right
1 left
3 left
1 left
2 right
1 left
4 right
1 left
2 right
1 left
3 left
1 left
2 right
1 left
"""

#----------------------------------------------------------------------------------------------------------


# (3). Print the vivid return 


import time
from IPython.display import clear_output


class TowerOfHanoi():
    def __init__(self, n=4):
        self._n = n
        self._array = [[], [], list(reversed(range(n)))]
        self._lengths = [0, 0, n]
    def draw_towers(self):
        rows = []
        rows.append(['\t  1\t', '\t  2\t', '\t  3\t'])
        rows.append(['\t_____\t', '\t_____\t', '\t_____\t'])
        for i in range(max(self._lengths)):
            row = []
            for j in range(3):
                if i<self._lengths[j]:
                    row.append('\t  ' + str(self._array[j][i]) + '\t')
                else:
                    row.append('\t  \t')
            rows.append(row)
        for r in reversed(rows):
            print(''.join(r))    
    def __getitem__(self, index):
        return self._array[index]
    def pop(self, index):
        self._lengths[index] -= 1
        return self[index].pop()
    def getlen(self):
        return self._lengths
    def __setitem__(self, index, VALUE):
        if self[index] and self[index][-1] < VALUE:
            raise VALUEError (f'Illegalgo move. Cannot place block with size {VALUE} on block {self[index][-1]}')
        else: 
            self[index].append(VALUE)
            self._lengths[index] += 1
    def _move_stack(self, n_disks, start_peg, help_peg, target_peg):
        time.sleep(0.5)
        clear_output()  # Only for iPython 
        self.draw_towers()
        if n_disks == 1:
            self._count += 1
            VALUE = self.pop(start_peg)
            try:
                self[target_peg] = VALUE
            except Exception as e:
                print(e)
                self[start_peg]
        else:
            # Move the upper stack to the helper peg
            self._move_stack(n_disks-1, start_peg, target_peg, help_peg)
            # Move the lowest item to the target peg
            self._move_stack(1, start_peg, help_peg, target_peg)
            # Move the upper stack to the target peg
            self._move_stack(n_disks-1, help_peg, start_peg, target_peg)
    def solve_hanoi(self):
        self._count = 0
        self._move_stack(self.getlen()[2], 2, 1, 0)
        time.sleep(0.5)
        clear_output()
        self.draw_towers()
        print(f'\nThis took a total of {self._count} moves!')


if __name__ == '__main__':
    t = TowerOfHanoi(5)
    t.solve_hanoi()


# Output:


"""
                      0 
                      1 
                      2 
                      3 
                      4 
    _____       _____       _____   
      1       2       3 
                      0 
                      1 
                      2 
                      3 
                      4 
    _____       _____       _____   
      1       2       3 
                      0 
                      1 
                      2 
                      3 
                      4 
    _____       _____       _____   
      1       2       3 
                      0 
                      1 
                      2 
                      3 
                      4 
    _____       _____       _____   
      1       2       3 
                      0 
                      1 
                      2 
                      3 
                      4 
    _____       _____       _____   
      1       2       3 
                      1 
                      2 
                      3 
      0               4 
    _____       _____       _____   
      1       2       3 
                      2 
                      3 
      0       1       4 
    _____       _____       _____   
      1       2       3 
                      2 
              0       3 
              1       4 
    _____       _____       _____   
      1       2       3 
              0       3 
      2       1       4 
    _____       _____       _____   
      1       2       3 
              0       3 
      2       1       4 
    _____       _____       _____   
      1       2       3 
                      0 
                      3 
      2       1       4 
    _____       _____       _____   
      1       2       3 
                      0 
      1               3 
      2               4 
    _____       _____       _____   
      1       2       3 
      0                 
      1               3 
      2               4 
    _____       _____       _____   
      1       2       3 
      0                 
      1                 
      2       3       4 
    _____       _____       _____   
      1       2       3 
      0                 
      1                 
      2       3       4 
    _____       _____       _____   
      1       2       3 
      0                 
      1                 
      2       3       4 
    _____       _____       _____   
      1       2       3 
      1       0         
      2       3       4 
    _____       _____       _____   
      1       2       3 
              0       1 
      2       3       4 
    _____       _____       _____   
      1       2       3 
                      0 
                      1 
      2       3       4 
    _____       _____       _____   
      1       2       3 
                      0 
              2       1 
              3       4 
    _____       _____       _____   
      1       2       3 
                      0 
              2       1 
              3       4 
    _____       _____       _____   
      1       2       3 
              2       1 
      0       3       4 
    _____       _____       _____   
      1       2       3 
              1         
              2         
      0       3       4 
    _____       _____       _____   
      1       2       3 
              0         
              1         
              2         
              3       4 
    _____       _____       _____   
      1       2       3 
              0         
              1         
              2         
      4       3         
    _____       _____       _____   
      1       2       3 
              0         
              1         
              2         
      4       3         
    _____       _____       _____   
      1       2       3 
              0         
              1         
              2         
      4       3         
    _____       _____       _____   
      1       2       3 
              0         
              1         
              2         
      4       3         
    _____       _____       _____   
      1       2       3 
              1         
              2         
      4       3       0 
    _____       _____       _____   
      1       2       3 
      1       2         
      4       3       0 
    _____       _____       _____   
      1       2       3 
      0                 
      1       2         
      4       3         
    _____       _____       _____   
      1       2       3 
      0                 
      1                 
      4       3       2 
    _____       _____       _____   
      1       2       3 
      0                 
      1                 
      4       3       2 
    _____       _____       _____   
      1       2       3 
      1       0         
      4       3       2 
    _____       _____       _____   
      1       2       3 
              0       1 
      4       3       2 
    _____       _____       _____   
      1       2       3 
                      0 
                      1 
      4       3       2 
    _____       _____       _____   
      1       2       3 
                      0 
      3               1 
      4               2 
    _____       _____       _____   
      1       2       3 
                      0 
      3               1 
      4               2 
    _____       _____       _____   
      1       2       3 
                      0 
      3               1 
      4               2 
    _____       _____       _____   
      1       2       3 
      0                 
      3               1 
      4               2 
    _____       _____       _____   
      1       2       3 
      0                 
      3                 
      4       1       2 
    _____       _____       _____   
      1       2       3 
      3       0         
      4       1       2 
    _____       _____       _____   
      1       2       3 
      2                 
      3       0         
      4       1         
    _____       _____       _____   
      1       2       3 
      2                 
      3       0         
      4       1         
    _____       _____       _____   
      1       2       3 
      2                 
      3                 
      4       1       0 
    _____       _____       _____   
      1       2       3 
      1                 
      2                 
      3                 
      4               0 
    _____       _____       _____   
      1       2       3 
          0                               
      1                 
      2                 
      3                 
      4                 
    _____       _____       _____   
      1       2       3 

This took a total of 31 moves!
"""

############################################################################################################


# C4.15 Write a recursive function that will output all the subsets of a set of n
# elements (without repeating any subsets).


# (1). Definea functions 


UNK = chr(1000)


def subsets(u, s):
    """
    U is the current set
    S is the remaining sequence
    """
    if len(s) == 0:
        print('{', str([i for i in u if i!= UNK])[1:-1], '}')
    else:
        v = s.pop()
        u.append(UNK)
        subsets(u, s)
        u.pop()
        u.append(v)
        subsets(u, s)
        u.pop()
        s.append(v)


def print_subsets (u):
    subsets([], list(u))


if __name__ == '__main__':   
    print_subsets({1,2,3,4,5})


# Output:

"""
{  }
{ 1 }
{ 2 }
{ 2, 1 }
{ 3 }
{ 3, 1 }
{ 3, 2 }
{ 3, 2, 1 }
{ 4 }
{ 4, 1 }
{ 4, 2 }
{ 4, 2, 1 }
{ 4, 3 }
{ 4, 3, 1 }
{ 4, 3, 2 }
{ 4, 3, 2, 1 }
{ 5 }
{ 5, 1 }
{ 5, 2 }
{ 5, 2, 1 }
{ 5, 3 }
{ 5, 3, 1 }
{ 5, 3, 2 }
{ 5, 3, 2, 1 }
{ 5, 4 }
{ 5, 4, 1 }
{ 5, 4, 2 }
{ 5, 4, 2, 1 }
{ 5, 4, 3 }
{ 5, 4, 3, 1 }
{ 5, 4, 3, 2 }
{ 5, 4, 3, 2, 1 }
"""

#----------------------------------------------------------------------------------------------------------


# Define a call 


UNK = chr(1000)


class Algorithm:
    def __init__(self):
        pass
    def subsets(self, u, s):
        """
        u is the current set
        s is the remaining sequence
        """
        if len(s) == 0:
            print('{', str([i for i in u if i!= UNK])[1:-1], '}')
        else:
            v = s.pop()
            u.append(UNK)
            self.subsets(u, s)
            u.pop()
            u.append(v)
            self.subsets(u, s)
            u.pop()
            s.append(v)
    def print_subsets(self, u):
        self.subsets([], list(u))



if __name__ == '__main__': 
    algo = Algorithm()  
    algo.print_subsets({1,2,3,4,5})

# Output:

"""
{  }
{ 1 }
{ 2 }
{ 2, 1 }
{ 3 }
{ 3, 1 }
{ 3, 2 }
{ 3, 2, 1 }
{ 4 }
{ 4, 1 }
{ 4, 2 }
{ 4, 2, 1 }
{ 4, 3 }
{ 4, 3, 1 }
{ 4, 3, 2 }
{ 4, 3, 2, 1 }
{ 5 }
{ 5, 1 }
{ 5, 2 }
{ 5, 2, 1 }
{ 5, 3 }
{ 5, 3, 1 }
{ 5, 3, 2 }
{ 5, 3, 2, 1 }
{ 5, 4 }
{ 5, 4, 1 }
{ 5, 4, 2 }
{ 5, 4, 2, 1 }
{ 5, 4, 3 }
{ 5, 4, 3, 1 }
{ 5, 4, 3, 2 }
{ 5, 4, 3, 2, 1 }
"""

############################################################################################################


# C4.16. Write a short recursive Python function that takes a character string s and
# outputs its reverse. For example, the reverse of pots&pans would be snap&stop .


# (1). Define a recursive function 

def reversestring(s, index = 0):
    if index == len(s)-1:
        return [s[index]]
    else:
        ans = reversestring(s, index + 1)
        ans.append (s[index])
        if index == 0:
            ans = ''.join(ans)
        return ans


if __name__ == '__main__':
    reversestring('pots&pans')


# Output:

"""
'snap&stop'
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class


class Algorithm:
    def __init__(self):
        pass
    def reversestring(self, s, index=0):
        if index == len(s)-1:
            return [s[index]]
        else:
            ans = self.reversestring(s, index + 1)
            ans.append (s[index])
            if index == 0:
                ans = ''.join(ans)
            return ans


if __name__ == '__main__':
    algo = Algorithm()
    algo.reversestring('pots&pans')


# Output:

"""
'snap&stop'
"""

############################################################################################################


# C4.17. Write a short recursive Python function that determines if a string s is a
# palindrome, that is, it is equal to its reverse. For example, racecar and
# gohangasalamiimalasagnahog are palindromes.


# Define a recursive palindrome recursion


def palindrome_checker(s, index=0):
    l = len(s)
    if l == 1:
        return True
    elif index >= l//2:
        # You actually want the (last index + 1)//2, but since the last index is l-1, it becomes (l+1-1)//2, or just l//2
        return s[index] == s[l//2]   #For odd this will be the same index, for even it will not be
    else:
        # Note you want to put the terms in this order to shortcircuit the recursive check.  If it's going to fail, it's
        # likely to fail around the first few indices in most normalgo cases
        return (s[index] == s[l-index-1]) and palindrome_checker(s, index+1)


if __name__ == '__main__':    
    strings_list = ['racecar', 'gohangasalamiimalasagnahog', 'notapalindrome', 'bob', 'a', 'hat']
    for s in strings_list:
        print(palindrome_checker(s), s)

# Output:

"""
True racecar
True gohangasalgoamiimalgoasagnahog
False notapalgoindrome
True bob
True a
False hat
"""

#----------------------------------------------------------------------------------------------------------


# Define a class


class Algorithm:
    def __init__(self):
        pass
    def palindrome_checker(self, s, index=0):
        l = len(s)
        if l == 1:
            return True
        elif index >= l//2:
            # You actually want the (last index + 1)//2, but since the last index is l-1, it becomes (l+1-1)//2, or just l//2
            return s[index] == s[l//2]   #For odd this will be the same index, for even it will not be
        else:
            # Note you want to put the terms in this order to shortcircuit the recursive check.  If it's going to fail, it's
            # likely to fail around the first few indices in most normalgo cases
            return (s[index] == s[l-index-1]) and self.palindrome_checker(s, index+1)


if __name__ == '__main__':    
    algo = Algorithm()
    strings_list = ['racecar', 'gohangasalamiimalasagnahog', 'notapalindrome', 'bob', 'a', 'hat']
    for s in strings_list:
        print(algo.palindrome_checker(s), s)


# Output:

"""
True racecar
True gohangasalgoamiimalgoasagnahog
False notapalgoindrome
True bob
True a
False hat
"""

############################################################################################################


# C4.18 Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.


# Define functions

VOWELLS = {'a','e','i','o','u'}


def c_or_v(s, index = 0):
    a = -1 if s[index] in VOWELLS else 1
    if index == len(s)-1:
        return a
    else:
        return (a + c_or_v(s, index +1))

    
def check_vowells(s):
    ans = c_or_v(s)
    if ans>0:
        return (f'There are more consonants by {ans}')
    elif ans<0:
        return (f'There are more vowells by {ans}')
    else:
        return (f'There are an equal number of each {ans}')
    

if __name__ == '__main__': 
    strings_list = ['racecar', 'gohangasalamiimalasagnahog', 'notapalindrome', 'bob', 'a', 'hat']
    for s in strings_list:
        print(check_vowells(s), s)


# Output:

"""
There are more consonants by 1 racecar
There are more consonants by 2 gohangasalgoamiimalgoasagnahog
There are more consonants by 2 notapalgoindrome
There are more consonants by 1 bob
There are more vowells by -1 a
There are more consonants by 1 hat
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class


VOWELLS = {'a','e','i','o','u'}


class Algorithm:
    def __init__(self):
        pass
    def c_or_v(self, s, index = 0):
        a = -1 if s[index] in VOWELLS else 1
        if index == len(s)-1:
            return a
        else:
            return (a + self.c_or_v(s, index +1))
    def check_vowells(self, s):
        ans = self.c_or_v(s)
        if ans>0:
            return (f'There are more consonants by {ans}')
        elif ans<0:
            return (f'There are more vowells by {ans}')
        else:
            return (f'There are an equal number of each {ans}')
    

if __name__ == '__main__': 
    algo = Algorithm()
    strings_list = ['racecar', 'gohangasalamiimalasagnahog', 'notapalindrome', 'bob', 'a', 'hat']
    for s in strings_list:
        print(algo.check_vowells(s), s)


# Output:

"""
There are more consonants by 1 racecar
There are more consonants by 2 gohangasalamiimalasagnahog
There are more consonants by 2 notapalindrome
There are more consonants by 1 bob
There are more vowells by -1 a
There are more consonants by 1 hat
"""

############################################################################################################


# C4.19. Write a short recursive Python function that rearranges a sequence of integer 
# values so that all the even values appear before all the odd values. Permutate event 
# before the odd numbers 


# Define functions 


def evenoddbylists(s, index=0):
    if index == len(s)-1:
        if len(s) == 1:
            return s
        elif s[index]%2==0:
            return [s[index]], []
        else:
            return [], [s[index]]  
    else:
        evens, odds = evenoddbylists(s, index+1)
        if s[index] %2 == 0: 
            evens.append(s[index])
        else: 
            odds.append(s[index])
        if index == 0: 
            return evens+odds
        else: 
            return evens, odds


def evenoddbyappending(s, index=0):
    if index == len(s)-1:
        return [s[index]]
    
    else:
        if s[index]%2 == 1: #If odd, we want to add it to the end of the list
            return evenoddbyappending(s, index+1) + [s[index]]
        else:
            return [s[index]] + evenoddbyappending(s, index+1)


if __name__ == '__main__':    
    sequences = [[1,2,3,4,5,6,7,8], [4,3,65,23,5,46,765,3,45,23], [1], [2,2]]
    print('Two lists approach')
    for s in sequences:
        print(evenoddbylists(s))  
    print('\n\nAdding each element approach')
    for s in sequences:
        print(evenoddbyappending(s))


# Output:

"""
Two lists approach
[8, 6, 4, 2, 7, 5, 3, 1]
[46, 4, 23, 45, 3, 765, 5, 23, 65, 3]
[1]
[2, 2]


Adding each element approach
[2, 4, 6, 8, 7, 5, 3, 1]
[4, 46, 23, 45, 3, 765, 5, 23, 65, 3]
[1]
[2, 2]
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class


class Algorithm:
    def __init__(self):
        pass
    def evenoddbylists(self, s, index=0):
        if index == len(s)-1:
            if len(s) == 1:
                print(s)
                return s
            elif s[index]%2 == 0:
                print([s[index]], [])
                return [s[index]], []
            else:
                print([s[index]], [])
                return [], [s[index]]  
        else:
            evens, odds = self.evenoddbylists(s, index+1)
            if s[index] %2 == 0: 
                evens.append(s[index])
                print(evens)
            else: 
                odds.append(s[index])
                print(odds)
            if index == 0: 
                print(evens+odds)
                return evens+odds
            else: 
                return evens, odds
    def evenoddbyappending(self, s, index=0):
        if index == len(s)-1:
            print([s[index]])
            return [s[index]]
        else:
            if s[index]%2 == 1: # If odd, we want to add it to the end of the list
                return self.evenoddbyappending(s, index+1) + [s[index]]
            else:
                return [s[index]] + self.evenoddbyappending(s, index+1)


if __name__ == '__main__':    
    sequences = [[1,2,3,4,5,6,7,8], [4,3,65,23,5,46,765,3,45,23], [1], [2,2]]
    algo = Algorithm()
    print('Two lists approach')
    for s in sequences:
        print(algo.evenoddbylists(s))  
    print('\n\nAdding each element approach')
    for s in sequences:
        print(algo.evenoddbyappending(s))


# Output:

"""
Two lists approach
[8] []
[7]
[8, 6]
[7, 5]
[8, 6, 4]
[7, 5, 3]
[8, 6, 4, 2]
[7, 5, 3, 1]
[8, 6, 4, 2, 7, 5, 3, 1]
[8, 6, 4, 2, 7, 5, 3, 1]
[23] []
[23, 45]
[23, 45, 3]
[23, 45, 3, 765]
[46]
[23, 45, 3, 765, 5]
[23, 45, 3, 765, 5, 23]
[23, 45, 3, 765, 5, 23, 65]
[23, 45, 3, 765, 5, 23, 65, 3]
[46, 4]
[46, 4, 23, 45, 3, 765, 5, 23, 65, 3]
[46, 4, 23, 45, 3, 765, 5, 23, 65, 3]
[1]
[1]
[2] []
[2, 2]
[2, 2]
[2, 2]


Adding each element approach
[8]
[2, 4, 6, 8, 7, 5, 3, 1]
[23]
[4, 46, 23, 45, 3, 765, 5, 23, 65, 3]
[1]
[1]
[2]
[2, 2]
"""

############################################################################################################


# C4.20 Given an unsorted sequence, S, of integers and an integer k, describe a
# recursive algorithm for rearranging the elements in S so that all elements
# less than or equal to k come before any elements larger than k. What is
# the running time of your algorithm on a sequence of n values?



# (1). Define functions 


def add_lists(a,b):
    if a and b:
        return a+b
    else:
        return b or a #if one of them is [], return the other


def split_by_k(S, k, index=0):
    if len(S)==1:
        return S 
    elif index == len(S)-1:    #we use this line for too many of these exercises...
        if S[index] <k:
            return [S[index]], [], []
        elif S[index] >k:
            return [], [], [S[index]]
        else:
            return [], [S[index]], []  #Should return k in the middle list
    else:
        low, med, high = split_by_k(S, k, index+1)
        if S[index] <k:
            low = add_lists(low, [S[index]])
        elif S[index] >k:
            high = add_lists(high, [S[index]])
        else:
            med = add_lists(med, [S[index]])
        if index == 0:
            return add_lists(low, add_lists(med, high)) #This is not very elegant...
        else:
            return low, med, high


if __name__ == '__main__':
    sequence = [11,2,33,4,5,6,7,8,9,10]
    for i in range(0, 30, 2):
        print('Splitting by: ', i, 'produces', split_by_k(sequence, i))


# Output:

"""
Splitting by:  0 produces [10, 9, 8, 7, 6, 5, 4, 33, 2, 11]
Splitting by:  2 produces [2, 10, 9, 8, 7, 6, 5, 4, 33, 11]
Splitting by:  4 produces [2, 4, 10, 9, 8, 7, 6, 5, 33, 11]
Splitting by:  6 produces [5, 4, 2, 6, 10, 9, 8, 7, 33, 11]
Splitting by:  8 produces [7, 6, 5, 4, 2, 8, 10, 9, 33, 11]
Splitting by:  10 produces [9, 8, 7, 6, 5, 4, 2, 10, 33, 11]
Splitting by:  12 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  14 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  16 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  18 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  20 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  22 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  24 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  26 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  28 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class 


class Algorithm:
    def __init__(self):
        pass
    def add_lists(self, a, b):
        if a and b:
            return a+b
        else:
            return b or a #if one of them is [], return the other
    def split_by_k(self, S, k, index=0):
        if len(S)==1:
            return S 
        elif index == len(S)-1:    #we use this line for too many of these exercises...
            if S[index] < k:
                return [S[index]], [], []
            elif S[index] > k:
                return [], [], [S[index]]
            else:
                return [], [S[index]], []  #Should return k in the middle list
        else:
            low, med, high = self.split_by_k(S, k, index+1)
            if S[index] < k:
                low = self.add_lists(low, [S[index]])
            elif S[index] > k:
                high = self.add_lists(high, [S[index]])
            else:
                med = self.add_lists(med, [S[index]])
            if index == 0:
                return self.add_lists(low, self.add_lists(med, high)) #This is not very elegant...
            else:
                return low, med, high


if __name__ == '__main__':
    algo = Algorithm()
    sequence = [11,2,33,4,5,6,7,8,9,10]
    for i in range(0, 30, 2):
        print('Splitting by: ', i, 'produces', algo.split_by_k(sequence, i))


# Output:

"""
Splitting by:  0 produces [10, 9, 8, 7, 6, 5, 4, 33, 2, 11]
Splitting by:  2 produces [2, 10, 9, 8, 7, 6, 5, 4, 33, 11]
Splitting by:  4 produces [2, 4, 10, 9, 8, 7, 6, 5, 33, 11]
Splitting by:  6 produces [5, 4, 2, 6, 10, 9, 8, 7, 33, 11]
Splitting by:  8 produces [7, 6, 5, 4, 2, 8, 10, 9, 33, 11]
Splitting by:  10 produces [9, 8, 7, 6, 5, 4, 2, 10, 33, 11]
Splitting by:  12 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  14 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  16 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  18 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  20 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  22 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  24 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  26 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
Splitting by:  28 produces [10, 9, 8, 7, 6, 5, 4, 2, 11, 33]
"""

############################################################################################################


# C4.21. Suppose you are given an n-element sequence, S, containing distinct integers 
# that are listed in increasing order. Given a number k, describe a recursive algorithm 
# to find two integers in S that sum to k, if such a pair exists. What is the running 
# time of your algorithm?


# (1). Define a function 

def find_pair(S, target, key_set = None, index=0):
    if key_set is None:
        key_set = set()
    key = target - S[index]
    if len(S) <= 1:
        return None
    elif index == len(S)-1:
        if key in key_set: return (key, S[index])
        else: return None
    else:
        if key in key_set: return (key, S[index])
        else:
            key_set.add(S[index])
            return find_pair(S, target, key_set, index+1)


if __name__ == '__main__':
    sequence = [1,2,3,4,5,6,7,8]
    for i in range(20):
        print(f'For the VALUE {i}, the resulting pair is {find_pair(sequence, i)}')


# Output:

"""
For the VALUE 0, the resulting pair is None
For the VALUE 1, the resulting pair is None
For the VALUE 2, the resulting pair is None
For the VALUE 3, the resulting pair is (1, 2)
For the VALUE 4, the resulting pair is (1, 3)
For the VALUE 5, the resulting pair is (2, 3)
For the VALUE 6, the resulting pair is (2, 4)
For the VALUE 7, the resulting pair is (3, 4)
For the VALUE 8, the resulting pair is (3, 5)
For the VALUE 9, the resulting pair is (4, 5)
For the VALUE 10, the resulting pair is (4, 6)
For the VALUE 11, the resulting pair is (5, 6)
For the VALUE 12, the resulting pair is (5, 7)
For the VALUE 13, the resulting pair is (6, 7)
For the VALUE 14, the resulting pair is (6, 8)
For the VALUE 15, the resulting pair is (7, 8)
For the VALUE 16, the resulting pair is None
For the VALUE 17, the resulting pair is None
For the VALUE 18, the resulting pair is None
For the VALUE 19, the resulting pair is None
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class 


class Algorithm:
    def __init__(self):
        pass
    def find_pair(self, S, target, key_set = None, index=0):
        if key_set is None:
            key_set = set()
        key = target - S[index]
        if len(S) <= 1:
            return None
        elif index == len(S)-1:
            if key in key_set: return (key, S[index])
            else: return None
        else:
            if key in key_set: return (key, S[index])
            else:
                key_set.add(S[index])
                return self.find_pair(S, target, key_set, index+1)


if __name__ == '__main__':
    algo = Algorithm()
    sequence = [1,2,3,4,5,6,7,8]
    for i in range(20):
        print(f'For the VALUE {i}, the resulting pair is {algo.find_pair(sequence, i)}')


# Output:

"""
For the VALUE 0, the resulting pair is None
For the VALUE 1, the resulting pair is None
For the VALUE 2, the resulting pair is None
For the VALUE 3, the resulting pair is (1, 2)
For the VALUE 4, the resulting pair is (1, 3)
For the VALUE 5, the resulting pair is (2, 3)
For the VALUE 6, the resulting pair is (2, 4)
For the VALUE 7, the resulting pair is (3, 4)
For the VALUE 8, the resulting pair is (3, 5)
For the VALUE 9, the resulting pair is (4, 5)
For the VALUE 10, the resulting pair is (4, 6)
For the VALUE 11, the resulting pair is (5, 6)
For the VALUE 12, the resulting pair is (5, 7)
For the VALUE 13, the resulting pair is (6, 7)
For the VALUE 14, the resulting pair is (6, 8)
For the VALUE 15, the resulting pair is (7, 8)
For the VALUE 16, the resulting pair is None
For the VALUE 17, the resulting pair is None
For the VALUE 18, the resulting pair is None
For the VALUE 19, the resulting pair is None
"""

############################################################################################################


# C4-22. Develop a nonrecursive implementation of the version of power from
# Code Fragment 4.12 that uses repeated squaring.


# (1). Define a function


def power_loop(x, n):
    factor = n
    partial = 1
    counter = 0
    while factor:
        factor = factor >>1
        counter += 1
    while counter+1:
        partial *= partial
        if n>>counter&1:
            partial *= x        
        counter -=1
    return partial


if __name__ == '__main__':    
    combos = [ (2,13), (2, 15), (3, 15), (10, 7), (2, 5)]
    for b, p in combos:
        print('\n', power_loop(b, p), b**p)


# Output:

"""
 8192 8192

 32768 32768

 14348907 14348907

 10000000 10000000

 32 32
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class


class Algorithm:
    def __init__(self):
        pass
    def power_loop(self, x, n):
        factor = n
        partial = 1
        counter = 0
        while factor:
            factor = factor >>1
            counter += 1
        while counter+1:
            partial *= partial
            if n>>counter&1:
                partial *= x        
            counter -=1
        return partial


if __name__ == '__main__': 
    algo = Algorithm()   
    combos = [ (2,13), (2, 15), (3, 15), (10, 7), (2, 5)]
    for b, p in combos:
        print('\n', algo.power_loop(b, p), b**p)


# Output:


"""
 8192 8192

 32768 32768

 14348907 14348907

 10000000 10000000

 32 32
"""

############################################################################################################
############################################################################################################


# Part Three Projects


############################################################################################################


# P4.23. Implement a recursive function with signature find(path, filename) that
# reports all entries of the file system rooted at the given path having the
# given file name.


import os

def find(path, filename):
    if os.path.isdir(path):
        for obj in os.listdir(path):
            if os.path.isdir(os.path.join(path, obj)):
                find(os.path.join(path, obj), filename)
            elif obj == filename:
                print(os.path.join(path, obj))
                
                
find(r'SampleFiles/Ch4FileStructure', 'target.txt')

############################################################################################################


# P4.24. Write a program for solving summation puzzles by enumerating and testing 
# all possible configurations. Using your program, solve the three puzzles given
# in Section 4.4.3.


class SummationSolver():
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._max_len = len(c) #c cannot be shorter than a or b under the rules
        self._count = 0
    def _t2i(self, text, lookup): #text to int
        total = 0
        length = len(text)
        for i in range(length):
            total += int(lookup[text[i]])*10**(length-i-1) 
        return total
    def summation_check(self, a, b, c, U):
        """
        a + b = c using the keys, VALUE pairs in U
        """
        if self._t2i(a, U) + self._t2i(b, U) == self._t2i(c, U):
            self._count += 1
            print(f'One solution is: {self._t2i(a, U)} + {self._t2i(b, U)} = {self._t2i(c, U)}.  Check:{self._t2i(a, U) + self._t2i(b, U)}')
            print('Dictionary is :', U)
            print('\n')
            return True
        else:
            return False
    def _solver_r(self, a, b, c, S, index, U, nums):
        if index >= len(S):  #Note, this means we are past the Final index
            #print(U)
            return self.summation_check(a, b, c, U)
        elif S[index] in U:  #If the next letter in the sequence is algoready in the dictionary, skip it
            return self._solver_r(a,b,c,S,index+1, U, nums) 
        else:
            for number in nums.copy():
                U[S[index]] = number
                nums.remove(number)
                ans = self._solver_r(a,b,c,S, index+1, U, nums)
                nums.add(number)
                del U[S[index]]
    def solve(self):
        U = {}
        nums = set(range(10))
        S = list(self._a) + list(self._b) + list(self._c)
        self._count = 0
        self._solver_r(self._a, self._b, self._c, S, 0, U, nums)
        if self._count == 0:
            print ('Sorry, no solution found! :(')  
        else:
            print(f'There are a total of {self._count} solutions')


if __name__ == '__main__':
    #a = SummationSolver('pot', 'pan', 'bib')
    a = SummationSolver('boy', 'girl', 'babys')
    #a = SummationSolver('boy', 'girl', 'babysda')
    a.solve()


# Output:

"""
One solution is: 31 + 4986 = 5017.  Check:5017
Dictionary is : {'b': 0, 'o': 3, 'y': 1, 'g': 4, 'i': 9, 'r': 8, 'l': 6, 'a': 5, 's': 7}


One solution is: 31 + 6984 = 7015.  Check:7015
Dictionary is : {'b': 0, 'o': 3, 'y': 1, 'g': 6, 'i': 9, 'r': 8, 'l': 4, 'a': 7, 's': 5}



One solution is: 41 + 2975 = 3016.  Check:3016
Dictionary is : {'b': 0, 'o': 4, 'y': 1, 'g': 2, 'i': 9, 'r': 7, 'l': 5, 'a': 3, 's': 6}

...

There are a total of 46 solutions
"""

############################################################################################################


# P4.25. Provide a nonrecursive implementation of the draw interval function for
# the English ruler project of Section 4.1.2. There should be precisely 2 c − 1
# lines of output if c represents the length of the center tick. If incrementing
# a counter from 0 to 2 c − 2, the number of dashes for each tick line should
# be exactly one more than the number of consecutive 1’s at the end of the
# binary representation of the counter.


# (1). Define a function 


def english_ruler(n=3, repeats=10):
    limit = repeats*(2**n -2)
    counter = 0
    while counter<=limit:
        dashes = 1
        sub_counter = counter 
        while sub_counter & 1:
            dashes += 1
            sub_counter = sub_counter >> 1
        dashes = min(dashes, n)
        print('-'*dashes)
        counter += 1


if __name__ == '__main__':
    english_ruler(4, 3)
            

# Output:

"""
-
--
-
---
-
--
-
----
-
--
-
---
-
--
-
----
-
--
-
---
-
--
-
----
-
--
-
---
-
--
-
----
-
--
-
---
-
--
-
----
-
--
-
"""

#----------------------------------------------------------------------------------------------------------


# (2). Define a class


class Algorithm:
    def __init__(self):
        pass
    def english_ruler(self, n=3, repeats=10):
        limit = repeats*(2**n -2)
        counter = 0
        while counter<=limit:
            dashes = 1
            sub_counter = counter 
            while sub_counter & 1:
                dashes += 1
                sub_counter = sub_counter >> 1
            dashes = min(dashes, n)
            print('-'*dashes)
            counter += 1


if __name__ == '__main__':
    algo = Algorithm()
    algo.english_ruler(4, 3)
            

# Output:

"""
As sames as above 
"""

############################################################################################################


# P4.26 Write a program that can solve instances of the Tower of Hanoi problem
# (from Exercise C-4.14).

# towerHanoi.py


# Set up towers A, B, and C. The end of the list is the top of the tower.
total_DISKS = 6

# Populate Tower A:
TOWERS = {'A': list(reversed(range(1, total_DISKS + 1))),
          'B': [],
          'C': []}


def printDisk(diskNum):
    # Print a single disk of width diskNum.
    emptySpace = ' ' * (total_DISKS - diskNum)
    if diskNum == 0:
        # Just draw the pole.
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # Draw the disk.
        diskSpace = '@' * diskNum
        diskNumLabel = str(diskNum).rjust(2, '_')
        print(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace, end='')


def printTowers():
    # Print all three towers.
    for level in range(total_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else:
                printDisk(tower[level])
        print()
    # Print the tower labels A, B, and C.
    emptySpace = ' ' * (total_DISKS)
    print('%s A%s%s B%s%s C\n' % (emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))


def moveOneDisk(startTower, endTower):
    # Move the top disk from startTower to endTower.
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)


def solve(numberOfDisks, startTower, endTower, tempTower):
    # Move the top numberOfDisks disks from startTower to endTower.
    if numberOfDisks == 1:
        # BASE CASE
        moveOneDisk(startTower, endTower)
        printTowers()
        return
    else:
        # RECURSIVE CASE
        solve(numberOfDisks - 1, startTower, tempTower, endTower)
        moveOneDisk(startTower, endTower)
        printTowers()
        solve(numberOfDisks - 1, tempTower, endTower, startTower)
        return


if __name__ == '__main__': 
    # Solve
    printTowers()
    solve(total_DISKS, 'A', 'B', 'C')

# Uncomment to enable interactive mode:
#while True:
#    printTowers()
#    print('Enter letter of start tower and the end tower. (A, B, C) Or Q to quit.')
#    move = input().upper()
#    if move == 'Q':
#        sys.exit()
#    elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
#        moveOneDisk(move[0], move[1])


# Output:

"""

      ||            ||            ||      
     @_1@           ||            ||      
    @@_2@@          ||            ||      
   @@@_3@@@         ||            ||      
  @@@@_4@@@@        ||            ||      
 @@@@@_5@@@@@       ||            ||      
@@@@@@_6@@@@@@      ||            ||      
       A             B             C

      ||            ||            ||      
      ||            ||            ||      
    @@_2@@          ||            ||      
   @@@_3@@@         ||            ||      
  @@@@_4@@@@        ||            ||      
 @@@@@_5@@@@@       ||            ||      
@@@@@@_6@@@@@@      ||           @_1@     
       A             B             C

      ||            ||            ||      
      ||            ||            ||      
      ||            ||            ||      
   @@@_3@@@         ||            ||      
  @@@@_4@@@@        ||            ||      
 @@@@@_5@@@@@       ||            ||      
@@@@@@_6@@@@@@    @@_2@@         @_1@     
       A             B             C

      ||            ||            ||      
      ||            ||            ||      
      ||            ||            ||      
   @@@_3@@@         ||            ||      
  @@@@_4@@@@        ||            ||      
 @@@@@_5@@@@@      @_1@           ||      
@@@@@@_6@@@@@@    @@_2@@          ||      
       A             B             C

      ||            ||            ||      
      ||            ||            ||      
      ||            ||            ||      
      ||            ||            ||      
  @@@@_4@@@@        ||            ||      
 @@@@@_5@@@@@      @_1@           ||      
@@@@@@_6@@@@@@    @@_2@@       @@@_3@@@   
       A             B             C

      ||            ||            ||      
      ||            ||            ||      
      ||            ||            ||      
     @_1@           ||            ||      
  @@@@_4@@@@        ||            ||      
 @@@@@_5@@@@@       ||            ||      
@@@@@@_6@@@@@@    @@_2@@       @@@_3@@@   
       A             B             C
"""

############################################################################################################



# P4.27 Python’s os module provides a function with signature walk(path) that
# is a generator yielding the tuple (dirpath, dirnames, filenames) for each
# subdirectory of the directory identified by string path, such that string
# dirpath is the full path to the subdirectory, dirnames is a list of the names
# of the subdirectories within dirpath, and filenames is a list of the names
# of non-directory entries of dirpath. For example, when visiting the cs016
# subdirectory of the file system shown in Figure 4.6, the walk would yield
# ( /user/rt/courses/cs016 , [ homeworks , programs ], [ grades ]) .
# Give your own implementation of such a walk function.


import os


def our_walk(path):
    folders = []
    files = []
    
    for obj in os.listdir(path):
        new_path = os.path.join(path, obj)
        if os.path.isdir(new_path):
            folders.append(obj)
            yield from our_walk (new_path)  #Note the use of yield from
        elif os.path.isfile(new_path):
            files.append(obj)
        else:
            print('Unknown object:', obj)
    yield(path, folders, files)


if __name__ == '__main__':
    for i in os.walk('SampleFiles'):
        print(i)
    print('\n')
    for i in our_walk('SampleFiles'):
        print(i)
