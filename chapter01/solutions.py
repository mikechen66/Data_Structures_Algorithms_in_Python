
# Python Primer

##############################################################################################################

# Part One. Reinforcement

##############################################################################################################


# R1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.


def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

##############################################################################################################


# R1.2 Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function cannot 
# use the multiplication, modulo, or division operators.


#（１). Use list function 

def is_even(n):
    l = list(bin(n))
    if l[-1] == '0':
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_even(10))     


# Output:

"""
True
"""

#------------------------------------------------------------------------------------------------------------


# (2). Use modular arithmetic operation 

def is_even(k):
    if k % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_even(10))


# Output:

"""
True
"""

#------------------------------------------------------------------------------------------------------------


# (3). USe abs() and bool() function 

def is_even(k):
    k = abs(k)
    while k > 1:
        k -= 2
    return bool(k)


if __name__ == '__main__':
    print(is_even(10))


# Output:

"""
False
"""

##############################################################################################################


# R1.3 Find out the max and min numbers in a sequence 

def minmax(data):
    max_number = data[0]
    min_number = data[0]
    for x in data:
        if x > max_number:
            max_number = x
        if x < min_number:
            min_number = x
    return max_number, min_number


if __name__ == '__main__':
    print(minmax([4, 2, 3, 4, 5, 6, 7, 8]))


# Output:

"""
(8, 2)
"""

##############################################################################################################


# R1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.


def square(n):
    sum_of_square = sum(map(lambda x: x**2, list(range(1,n+1))))
    return sum_of_square


if __name__ == '__main__':
    print(square(3))


# Output:

"""
14
"""

##############################################################################################################


# R1.5 Give a single command that computes the sum from Exercise R-1.4, relying on 
# Python’s comprehension syntax and the built-in sum function.


# (1). A general form 

n = 3
sum_of_square = sum([i**2  for i in range(1, n+1)])

print(sum_of_square)

#------------------------------------------------------------------------------------------------------------


# Use func() to realize the calling 


def func(n):
    sum_of_square = sum([i**2  for i in range(1, n+1)])
    return sum_of_square


if __name__ == '__main__':
    print(func(n=3))
    print(func(n=4))
    print(func(n=6))


# Output:

"""
14
30
91
"""

##############################################################################################################


# R1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.


def square(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            total += i**2
    return total


if __name__ == '__main__':
    print(square(3))


# Output:

"""
10
"""
##############################################################################################################


# R1.7 Give a single command that computes the sum from Exercise R-1.6, relying 
# on Python’s comprehension syntax and the built-in sum function.


# (1). A general sequential execution 

n = 3

sum_of_odds = sum([i**2 for i in range(n+1) if i % 2 == 1])


print(sum_of_odds)

# Output:

"""
10
"""

#------------------------------------------------------------------------------------------------------------


# Use func() to realize the calling 


def func(n):
    sum_of_odds = sum([i**2 for i in range(n+1) if i % 2 == 1])
    return sum_of_odds


if __name__ == '__main__':
    print(func(n=3))
    print(func(n=4))
    print(func(n=6))


# Output:

"""
10
10
35
"""

##############################################################################################################


# R1.8 Python allows negative integers to be used as indices into a sequence, such as a string. 
# If string s has length n, and expression s[k] is used for in\dex −n ≤ k < 0, what is the 
# equivalent index j ≥ 0 such that s[j] references the same element?


def index(s, k):
    tag = False
    length = len(s)
    k1 = abs(k)
    j = length - k1
    if s[k] == s[j]:
        tag = True
    return j, tag


if __name__ == '__main__':
    a = [1, 2, 3, 4, 6, 7, 8, 9]
    print(index(a, -3))


# Output:

"""
(5, True)
"""

##############################################################################################################


# R1.9 What parameters should be sent to the range constructor, to produce a


range(50,81,10)

##############################################################################################################


# R1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?


range(8,-9,-2)


##############################################################################################################


# R1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].


[2**i for i in range(0,9)]


# Output:

"""
[1, 2, 4, 8, 16, 32, 64, 128, 256]
"""

##############################################################################################################


# R1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module in-
# cludes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.


import random


def choose_a_number_randomly(data):
    length = len(data)
    i = random.randrange(0, length, 1)
    return data[i]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    print(choose_a_number_randomly(a))


# Output(randomly):

"""
4
"""

##############################################################################################################
##############################################################################################################


# Part Two. Creativity 


# C1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they were 
# before, and compare this method to an equivalent Python function for doing the 
# same thing


def reverse(data):
    length = len(data)
    data_reverse = []
    for i in range(1, length+1):
        data_reverse.append(data[-i])
    return data_reverse


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    print(a)
    a1 = reverse(a)
    a2 = sorted(a, reverse=True)
    print(a1, a2, sep='\n')
    a.sort(reverse=True)  
    print(a)


# Output:

"""
[1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1]
[6, 5, 4, 3, 2, 1]
[6, 5, 4, 3, 2, 1]
"""

##############################################################################################################


# C1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.


def product_is_odd(data):
    data1 = list(set(data))
    for key, value1 in enumerate(data1):
        for value2 in data1[key+1:]:
            if (value1 * value2) % 2 == 1:
                return True
    return False


if __name__ == '__main__':
    data1 = [2, 3, 4, 10, 9, 4]
    data2 = [2, 3, 4, 10, 6, 4]
    print(product_is_odd(data1), product_is_odd(data2))


# Output:

"""
True False
"""

##############################################################################################################


# C1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).


# (1) Use subscription and slicing：

def is_distinct(data):
    for i in range(len(data)):
        value = data[i]
        for value1 in data[i+1:]:
            if value == value1:
                return False
    return True
       

if __name__ == '__main__':
    a = [1, 2, 4, 5, 5, 5, 6, 7, 7]
    a1 = [1, 2, 4, 5, 6]
    print(is_distinct(a), is_distinct(a1))


# Output:

"""
False True
"""
#------------------------------------------------------------------------------------------------------------


# (2) Use the built-in enumerate()

def is_distinct(data):
    for key, value in enumerate(data):
        for value1 in data[key+1:]:
            if value == value1:
                return False
    return True
    

if __name__ == '__main__':
    a = [1, 2, 4, 5, 5, 5, 6, 7, 7]
    a1 = [1, 2, 4, 5, 6]
    print(is_distinct(a), is_distinct(a1))


# Output:

"""
False True
"""

##############################################################################################################

# C1.16 In our implementation of the scale function (page 25), the body of the loop
# executes the command data[j] = factor. We have discussed that numeric
# types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the
# actual parameter sent by the caller?

# omit 

##############################################################################################################


# C-1.17Had we implemented the scale function (page 25) as follows, does it work
# properly? Explain why or why not. 


def scale(data, factor):
    for val in data:
        val = factor


##############################################################################################################


# C1.18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].


a = [i*(i+1) for i in range(10)]
print(a)

##############################################################################################################


# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

a = [chr(i) for i in range(97, 123)]
print(a)


##############################################################################################################


# C1.20 Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possi-
# ble order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.


# (1) print a random 


import random


def equal_shuffle(data):
    length = len(data)
    data1 = []
    chose_index = []
    while len(data1) < length:
        x = random.randint(0, length-1)
        if x not in chose_index:
            data1.append(data[x])
            chose_index.append(x)
    return data1


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    print(equal_shuffle(a))


# Output:

"""
[1, 4, 3, 2]
"""

#-------------------------------------------------------------------------------------------------------------


# (2) print other random number in different sequence


import random

def equal_shuffle(data):
    length = len(data)
    data1 = []
    index = list(range(length))
    while index:
        x = random.randint(0, length-1)
        if x in index:
            index.remove(x)
            data1.append(data[x])
    return data1


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    print(equal_shuffle(a))


# Output:

"""
[2, 3, 4, 1]
"""

##############################################################################################################


# C1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).


def my_test():
    a = []
    try:
        while True:
            b = input("please input: ")
            a.append(b)
    except EOFError:
        for i in a[::-1]:
            print(i)


if __name__ == '__main__':     
  my_test()



# Output(interactively:

"""
please input: 123
please input: 456
please input: 789
...
"""

##############################################################################################################


# C1-22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.


def dot_product(a, b):
    c = []
    if len(a) != len(b):
        print("you should input same dimesion vectors!")
    else:
        for i in range(len(a)):
            dot = a[i] * b[i]
            c.append(dot)
        return c


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [2, 3, 4]
    print(dot_product(a, b))


# Output:

"""
[2, 6, 12]
"""

##############################################################################################################


# C1.23 Give an example of a Python code fragment that attempts to write an ele-
# ment to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# "Don’t try buffer overflow attacks in Python!""


try:
    a = [1,2,3]
    a[4] = 2
except IndexError:
    print("your index is out of index")


##############################################################################################################


# C1.24 Write a short Python function that counts the number of vowels in a given
# character string.


def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    n = 0
    for x in str:
        if x in vowels:
            n += 1
    return n


if __name__ == '__main__':
    str = 'hello'
    print(count_vowels(str))


# Output:

"""
2
"""

##############################################################################################################


# C1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example, if given 
# the string "Let s try, Mike.", this function would return "Lets try Mike".


import string
import re


def repalce_punctuation(str):
    pun = string.punctuation
    replaced_str = re.sub('['+pun+']', "", str)
    return replaced_str


if __name__ == '__main__':
    str = "Let's try, Mike"
    print(repalce_punctuation(str))


# Output:

"""
Lets try Mike
"""

##############################################################################################################


# C1.26 Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”


# Need to input the first line of code in the Terminal 
abc = input("Please input three numbers: ")


a = int(abc[0])
b = int(abc[1])
c = int(abc[2])


if a + b == c:
    print("These three numbers match contions!")
else:
    print("These three numbers don't match contions!")


# Output:

"""
>>> abc = input("Please input three numbers: ")
Please input three numbers: 235
>>> 
>>> a = int(abc[0])
>>> b = int(abc[1])
>>> c = int(abc[2])
>>> 
>>> 
>>> if a + b == c:
...     print("These three numbers match contions!")
... else:
...     print("These three numbers don't match contions!")
... 
These three numbers match contions!
"""

#-------------------------------------------------------------------------------------------------------------


# (2). Give a non-interactive function

def func(abc): 
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    return a, b, c

        
if __name__ == '__main__':
    a, b, c = func(abc='235')
    if a + b == c:
        print("These three numbers match contions!")
    else:
        print("These three numbers don't match contions!")


# Output:

"""
These three numbers don't match contions!
"""

##############################################################################################################


# C1.27 In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementa-
# tions, from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance ad-
# vantages


def factors(n):
    k = 1
    after = []
    while k * k < n:
        if n % k == 0:
            yield k
            after.append(n//k)
        k += 1
    if k * k == n:
        yield k
    for i in after[::-1]:
        yield i


if __name__ == '__main__':
    i = factors(10)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))


# Output:

"""
1
2
5
10
"""
