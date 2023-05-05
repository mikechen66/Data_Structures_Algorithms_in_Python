

# linear_sum.py


# Option 1:


from dis import dis


def linear_sum(S, n):
    # Return the sum of the first n numbers of sequence S.
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


if __name__ == '__main__':
    S = [1,2,3,4,5,6,7,8,9]
    n = len(S)
    print(linear_sum(S,n))


# Output:

"""
45
"""

>>> dis(linear_sum)
  3           0 LOAD_FAST                1 (n)
              2 LOAD_CONST               1 (0)
              4 COMPARE_OP               2 (==)
              6 POP_JUMP_IF_FALSE       12

  4           8 LOAD_CONST               1 (0)
             10 RETURN_VALUE

  6     >>   12 LOAD_GLOBAL              0 (linear_sum)
             14 LOAD_FAST                0 (S)
             16 LOAD_FAST                1 (n)
             18 LOAD_CONST               2 (1)
             20 BINARY_SUBTRACT
             22 CALL_FUNCTION            2
             24 LOAD_FAST                0 (S)
             26 LOAD_FAST                1 (n)
             28 LOAD_CONST               2 (1)
             30 BINARY_SUBTRACT
             32 BINARY_SUBSCR
             34 BINARY_ADD
             36 RETURN_VALUE
             38 LOAD_CONST               0 (None)
             40 RETURN_VALUE
>>> 


#-----------------------------------------------------------------------------------------


# Option 2:


from dis import dis


class Algorithm:
    def __init__(self):
        pass
    def linear_sum(self, s, n):
        # Return the sum of the first n numbers of sequence S.
        if n == 0:
            return 0
        else:
            return self.linear_sum(s, n-1) + s[n-1]


if __name__ == '__main__':
    s = [1,2,3,4,5,6,7,8,9]
    n = len(s)
    al = Algorithm()
    print(al.linear_sum(s, n))


# Output:
# 45

>>> dis(Algorithm)
Disassembly of __init__:
  3           0 LOAD_CONST               0 (None)
              2 RETURN_VALUE

Disassembly of linear_sum:
  6           0 LOAD_FAST                2 (n)
              2 LOAD_CONST               1 (0)
              4 COMPARE_OP               2 (==)
              6 POP_JUMP_IF_FALSE       12

  7           8 LOAD_CONST               1 (0)
             10 RETURN_VALUE

  9     >>   12 LOAD_FAST                0 (self)
             14 LOAD_METHOD              0 (linear_sum)
             16 LOAD_FAST                1 (s)
             18 LOAD_FAST                2 (n)
             20 LOAD_CONST               2 (1)
             22 BINARY_SUBTRACT
             24 CALL_METHOD              2
             26 LOAD_FAST                1 (s)
             28 LOAD_FAST                2 (n)
             30 LOAD_CONST               2 (1)
             32 BINARY_SUBTRACT
             34 BINARY_SUBSCR
             36 BINARY_ADD
             38 RETURN_VALUE
             40 LOAD_CONST               0 (None)
             42 RETURN_VALUE

>>> 
