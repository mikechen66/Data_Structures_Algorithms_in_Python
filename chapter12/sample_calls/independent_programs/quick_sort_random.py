

# quick_sort_random.py


import random
import dis


def quicksort(S, i=0, j=None):
    if j is None:
        j = len(S) - 1
    if i >= j:
        return None
    rand = random.randint(i, j)   # <--- random pivoting
    pivot = S[rand]
    S[rand], S[j] = S[j], S[rand] # put pivot at the end of the list
    low = i
    high = j -1 
    while low <= high:
        while low <= high and S[low] < pivot:
            low += 1
        while low <= high and S[high] > pivot:
            high -= 1
        if low <= high:
            S[low], S[high] = S[high], S[low]
            low, high = low + 1, high -1
    S[low], S[j] = S[j], S[low]
    quicksort(S, i, low-1)
    quicksort(S, low+1, j)
    return S


if __name__ == "__main__":
    n = 10
    S = [random.randint(0, 50) for k in range(n)]
    print(S)
    quicksort(S)


# Output:

"""
[13, 34, 8, 36, 42, 8, 23, 6, 44, 39]
[6, 8, 8, 13, 23, 34, 36, 39, 42, 44]
"""


dis.dis(quicksort)

"""
  2           0 LOAD_FAST                2 (j)
              2 LOAD_CONST               0 (None)
              4 COMPARE_OP               8 (is)
              6 POP_JUMP_IF_FALSE       20

  3           8 LOAD_GLOBAL              0 (len)
             10 LOAD_FAST                0 (S)
             12 CALL_FUNCTION            1
             14 LOAD_CONST               1 (1)
             16 BINARY_SUBTRACT
             18 STORE_FAST               2 (j)

  4     >>   20 LOAD_FAST                1 (i)
             22 LOAD_FAST                2 (j)
             24 COMPARE_OP               5 (>=)
             26 POP_JUMP_IF_FALSE       32

  5          28 LOAD_CONST               0 (None)
             30 RETURN_VALUE

  6     >>   32 LOAD_GLOBAL              1 (random)
             34 LOAD_METHOD              2 (randint)
             36 LOAD_FAST                1 (i)
             38 LOAD_FAST                2 (j)
             40 CALL_METHOD              2
             42 STORE_FAST               3 (rand)

  7          44 LOAD_FAST                0 (S)
             46 LOAD_FAST                3 (rand)
             48 BINARY_SUBSCR
             50 STORE_FAST               4 (pivot)

  8          52 LOAD_FAST                0 (S)
             54 LOAD_FAST                2 (j)
             56 BINARY_SUBSCR
             58 LOAD_FAST                0 (S)
             60 LOAD_FAST                3 (rand)
             62 BINARY_SUBSCR
             64 ROT_TWO
             66 LOAD_FAST                0 (S)
             68 LOAD_FAST                3 (rand)
             70 STORE_SUBSCR
             72 LOAD_FAST                0 (S)
             74 LOAD_FAST                2 (j)
             76 STORE_SUBSCR

  9          78 LOAD_FAST                1 (i)
             80 STORE_FAST               5 (low)

 10          82 LOAD_FAST                2 (j)
             84 LOAD_CONST               1 (1)
             86 BINARY_SUBTRACT
             88 STORE_FAST               6 (high)

 11          90 SETUP_LOOP             132 (to 224)
        >>   92 LOAD_FAST                5 (low)
             94 LOAD_FAST                6 (high)
             96 COMPARE_OP               1 (<=)
             98 POP_JUMP_IF_FALSE      222

 12         100 SETUP_LOOP              32 (to 134)
        >>  102 LOAD_FAST                5 (low)
            104 LOAD_FAST                6 (high)
            106 COMPARE_OP               1 (<=)
            108 POP_JUMP_IF_FALSE      132
            110 LOAD_FAST                0 (S)
            112 LOAD_FAST                5 (low)
            114 BINARY_SUBSCR
            116 LOAD_FAST                4 (pivot)
            118 COMPARE_OP               0 (<)
            120 POP_JUMP_IF_FALSE      132

 13         122 LOAD_FAST                5 (low)
            124 LOAD_CONST               1 (1)
            126 INPLACE_ADD
            128 STORE_FAST               5 (low)
            130 JUMP_ABSOLUTE          102
        >>  132 POP_BLOCK

 14     >>  134 SETUP_LOOP              32 (to 168)
        >>  136 LOAD_FAST                5 (low)
            138 LOAD_FAST                6 (high)
            140 COMPARE_OP               1 (<=)
            142 POP_JUMP_IF_FALSE      166
            144 LOAD_FAST                0 (S)
            146 LOAD_FAST                6 (high)
            148 BINARY_SUBSCR
            150 LOAD_FAST                4 (pivot)
            152 COMPARE_OP               4 (>)
            154 POP_JUMP_IF_FALSE      166

 15         156 LOAD_FAST                6 (high)
            158 LOAD_CONST               1 (1)
            160 INPLACE_SUBTRACT
            162 STORE_FAST               6 (high)
            164 JUMP_ABSOLUTE          136
        >>  166 POP_BLOCK

 16     >>  168 LOAD_FAST                5 (low)
            170 LOAD_FAST                6 (high)
            172 COMPARE_OP               1 (<=)
            174 POP_JUMP_IF_FALSE       92

 17         176 LOAD_FAST                0 (S)
            178 LOAD_FAST                6 (high)
            180 BINARY_SUBSCR
            182 LOAD_FAST                0 (S)
            184 LOAD_FAST                5 (low)
            186 BINARY_SUBSCR
            188 ROT_TWO
            190 LOAD_FAST                0 (S)
            192 LOAD_FAST                5 (low)
            194 STORE_SUBSCR
            196 LOAD_FAST                0 (S)
            198 LOAD_FAST                6 (high)
            200 STORE_SUBSCR

 18         202 LOAD_FAST                5 (low)
            204 LOAD_CONST               1 (1)
            206 BINARY_ADD
            208 LOAD_FAST                6 (high)
            210 LOAD_CONST               1 (1)
            212 BINARY_SUBTRACT
            214 ROT_TWO
            216 STORE_FAST               5 (low)
            218 STORE_FAST               6 (high)
            220 JUMP_ABSOLUTE           92
        >>  222 POP_BLOCK

 19     >>  224 LOAD_FAST                0 (S)
            226 LOAD_FAST                2 (j)
            228 BINARY_SUBSCR
            230 LOAD_FAST                0 (S)
            232 LOAD_FAST                5 (low)
            234 BINARY_SUBSCR
            236 ROT_TWO
            238 LOAD_FAST                0 (S)
            240 LOAD_FAST                5 (low)
            242 STORE_SUBSCR
            244 LOAD_FAST                0 (S)
            246 LOAD_FAST                2 (j)
            248 STORE_SUBSCR

 20         250 LOAD_GLOBAL              3 (quicksort)
            252 LOAD_FAST                0 (S)
            254 LOAD_FAST                1 (i)
            256 LOAD_FAST                5 (low)
            258 LOAD_CONST               1 (1)
            260 BINARY_SUBTRACT
            262 CALL_FUNCTION            3
            264 POP_TOP

 21         266 LOAD_GLOBAL              3 (quicksort)
            268 LOAD_FAST                0 (S)
            270 LOAD_FAST                5 (low)
            272 LOAD_CONST               1 (1)
            274 BINARY_ADD
            276 LOAD_FAST                2 (j)
            278 CALL_FUNCTION            3
            280 POP_TOP

 22         282 LOAD_FAST                0 (S)
 """


dis.show_code(quicksort)


"""
Name:              quicksort
Filename:          <stdin>
Argument count:    3
Kw-only arguments: 0
Number of locals:  7
Stack size:        5
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: None
   1: 1
Names:
   0: len
   1: random
   2: randint
   3: quicksort
Variable names:
   0: S
   1: i
   2: j
   3: rand
   4: pivot
   5: low
   6: high
"""