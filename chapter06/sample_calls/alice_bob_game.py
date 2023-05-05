# Alice-Bob Game


"""
import opcode

for op in range(len(opcode.opname)):
    print('ox%.2X(%.3d): %s' % (op, op, opcode.opname[op]))

  6 ox00(000): <0>
  7 ox01(001): POP_TOP
  8 ox02(002): ROT_TWO
  9 ox03(003): ROT_THREE
 10 ox04(004): DUP_TOP
 11 ox05(005): DUP_TOP_TWO
...
148 ox8E(142): CALL_FUNCTION_VAR_KW
149 ox8F(143): SETUP_WITH
150 ox90(144): EXTENDED_ARG
151 ox91(145): LIST_APPEND
152 ox92(146): SET_ADD
153 ox93(147): MAP_ADD
...
"""
import random
# from random import randint
import collections
import dis


# Code Fragment 6.6: Definition for an Empty exception class.
class Empty(Exception):
    pass


# Code Fragment 6.2: Implementing a stack using a Python list as storage.
class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10                      # moderate capacity for all new queues
    def __init__(self):
        # Create an empty queue.
        self._data = [None] * self.DEFAULT_CAPACITY # _data: list instance
        self._size = 0  # number of the elements stored in the queue
        self._front = 0 # index of the first element of self._data instance queue
    def __len__(self):
        # Return the number of elements in the queue.
        return self._size
    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0
    def do_first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    def enqueue(self, element):
        # Add an element to the back of queue.
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)  
        self._data[avail] = element
        self._size += 1        
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]       # subscription(下标取值)
        self._data[self._front] = None         # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer
    def _resize(self, cap):                    # we assume cap >= len(self)
        # Resize to a new list of capacity >= len(self).
        current = self._data                       # keep track of existing list
        self._data = [None] * cap              # allocate list with new capacity
        walk = self._front
        for k in range(self._size):            # only consider existing elements
            self._data[k] = current[walk]          # intentionally shift indices
            # What is the meanding 1 + walk, walk is self._front? 
            # It take the seond element as the first element 
            walk = (1 + walk) % len(current)       # use old size as modulus
        self._front = 0                        # front has been realigned
    def rotate(self):
        if self.is_empty():
            raise Empty('The array is empty')
        self._data[(self._front + self._size) % len(self._data)] = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)


def play_game(Q, R, num_turns=100, max_rotations=20):
    for i in range(num_turns):
        # carray = Q if random.random() > 0.5 else R
        if random.random() > 0.5:
            carray = Q
        else:
            carray = R
        for j in range(random.randint(0, max_rotations)):
            final_value = carray.do_first()
            carray.rotate()
    return final_value % 2 == 0


def main(): 
# if __name__ == '__main__':
    Q, R = ArrayQueue(), ArrayQueue()
    Q.enqueue(0)
    for i in range(1, 100): 
        R.enqueue(i)
    total_wins = 0
    num_games = 10000
    for game in range(num_games):
        if play_game(Q, R):
            total_wins += 1
    print(f'Alice won {total_wins / num_games * 100}% of her games')


if __name__ == '__main__':
    main()


# Output:

"""
Alice won 74.77000000000001% of her games
"""


>>> dis.dis(ArrayQueue)
Disassembly of __init__:
  6           0 LOAD_CONST               0 (None)
              2 BUILD_LIST               1
              4 LOAD_GLOBAL              0 (ArrayQueue)
              6 LOAD_ATTR                1 (DEFAULT_CAPACITY)
              8 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             12 STORE_ATTR               2 (_data)

  7          14 LOAD_CONST               1 (0)
             16 LOAD_FAST                0 (self)
             18 STORE_ATTR               3 (_size)

  8          20 LOAD_CONST               1 (0)
             22 LOAD_FAST                0 (self)
             24 STORE_ATTR               4 (_front)
             26 LOAD_CONST               0 (None)
             28 RETURN_VALUE

Disassembly of __len__:
 11           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (_size)
              4 RETURN_VALUE

Disassembly of _resize:
 46           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (_data)
              4 STORE_FAST               2 (old)

 47           6 LOAD_CONST               0 (None)
              8 BUILD_LIST               1
             10 LOAD_FAST                1 (cap)
             12 BINARY_MULTIPLY
             14 LOAD_FAST                0 (self)
             16 STORE_ATTR               0 (_data)

 48          18 LOAD_FAST                0 (self)
             20 LOAD_ATTR                1 (_front)
             22 STORE_FAST               3 (walk)

 49          24 SETUP_LOOP              48 (to 74)
             26 LOAD_GLOBAL              2 (range)
             28 LOAD_FAST                0 (self)
             30 LOAD_ATTR                3 (_size)
             32 CALL_FUNCTION            1
             34 GET_ITER
        >>   36 FOR_ITER                34 (to 72)
             38 STORE_FAST               4 (k)

 50          40 LOAD_FAST                2 (old)
             42 LOAD_FAST                3 (walk)
             44 BINARY_SUBSCR
             46 LOAD_FAST                0 (self)
             48 LOAD_ATTR                0 (_data)
             50 LOAD_FAST                4 (k)
             52 STORE_SUBSCR

 53          54 LOAD_CONST               1 (1)
             56 LOAD_FAST                3 (walk)
             58 BINARY_ADD
             60 LOAD_GLOBAL              4 (len)
             62 LOAD_FAST                2 (old)
             64 CALL_FUNCTION            1
             66 BINARY_MODULO
             68 STORE_FAST               3 (walk)
             70 JUMP_ABSOLUTE           36
        >>   72 POP_BLOCK

 54     >>   74 LOAD_CONST               2 (0)
             76 LOAD_FAST                0 (self)
             78 STORE_ATTR               1 (_front)
             80 LOAD_CONST               0 (None)
             82 RETURN_VALUE

Disassembly of dequeue:
 35           0 LOAD_FAST                0 (self)
              2 LOAD_METHOD              0 (is_empty)
              4 CALL_METHOD              0
              6 POP_JUMP_IF_FALSE       16

 36           8 LOAD_GLOBAL              1 (Empty)
             10 LOAD_CONST               1 ('Queue is empty')
             12 CALL_FUNCTION            1
             14 RAISE_VARARGS            1

 37     >>   16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (_data)
             20 LOAD_FAST                0 (self)
             22 LOAD_ATTR                3 (_front)
             24 BINARY_SUBSCR
             26 STORE_FAST               1 (answer)

 38          28 LOAD_CONST               2 (None)
             30 LOAD_FAST                0 (self)
             32 LOAD_ATTR                2 (_data)
             34 LOAD_FAST                0 (self)
             36 LOAD_ATTR                3 (_front)
             38 STORE_SUBSCR

 39          40 LOAD_FAST                0 (self)
             42 LOAD_ATTR                3 (_front)
             44 LOAD_CONST               3 (1)
             46 BINARY_ADD
             48 LOAD_GLOBAL              4 (len)
             50 LOAD_FAST                0 (self)
             52 LOAD_ATTR                2 (_data)
             54 CALL_FUNCTION            1
             56 BINARY_MODULO
             58 LOAD_FAST                0 (self)
             60 STORE_ATTR               3 (_front)

 40          62 LOAD_FAST                0 (self)
             64 DUP_TOP
             66 LOAD_ATTR                5 (_size)
             68 LOAD_CONST               3 (1)
             70 INPLACE_SUBTRACT
             72 ROT_TWO
             74 STORE_ATTR               5 (_size)

 41          76 LOAD_CONST               4 (0)
             78 LOAD_FAST                0 (self)
             80 LOAD_ATTR                5 (_size)
             82 DUP_TOP
             84 ROT_THREE
             86 COMPARE_OP               0 (<)
             88 POP_JUMP_IF_FALSE      108
             90 LOAD_GLOBAL              4 (len)
             92 LOAD_FAST                0 (self)
             94 LOAD_ATTR                2 (_data)
             96 CALL_FUNCTION            1
             98 LOAD_CONST               5 (4)
            100 BINARY_FLOOR_DIVIDE
            102 COMPARE_OP               0 (<)
            104 POP_JUMP_IF_FALSE      132
            106 JUMP_FORWARD             4 (to 112)
        >>  108 POP_TOP
            110 JUMP_FORWARD            20 (to 132)

 42     >>  112 LOAD_FAST                0 (self)
            114 LOAD_METHOD              6 (_resize)
            116 LOAD_GLOBAL              4 (len)
            118 LOAD_FAST                0 (self)
            120 LOAD_ATTR                2 (_data)
            122 CALL_FUNCTION            1
            124 LOAD_CONST               6 (2)
            126 BINARY_FLOOR_DIVIDE
            128 CALL_METHOD              1
            130 POP_TOP

 43     >>  132 LOAD_FAST                1 (answer)
            134 RETURN_VALUE

Disassembly of do_first:
 20           0 LOAD_FAST                0 (self)
              2 LOAD_METHOD              0 (is_empty)
              4 CALL_METHOD              0
              6 POP_JUMP_IF_FALSE       16

 21           8 LOAD_GLOBAL              1 (Empty)
             10 LOAD_CONST               1 ('Queue is empty')
             12 CALL_FUNCTION            1
             14 RAISE_VARARGS            1

 22     >>   16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (_data)
             20 LOAD_FAST                0 (self)
             22 LOAD_ATTR                3 (_front)
             24 BINARY_SUBSCR
             26 RETURN_VALUE

Disassembly of enqueue:
 25           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (_size)
              4 LOAD_GLOBAL              1 (len)
              6 LOAD_FAST                0 (self)
              8 LOAD_ATTR                2 (_data)
             10 CALL_FUNCTION            1
             12 COMPARE_OP               2 (==)
             14 POP_JUMP_IF_FALSE       36

 26          16 LOAD_FAST                0 (self)
             18 LOAD_METHOD              3 (_resize)
             20 LOAD_CONST               1 (2)
             22 LOAD_GLOBAL              1 (len)
             24 LOAD_FAST                0 (self)
             26 LOAD_ATTR                2 (_data)
             28 CALL_FUNCTION            1
             30 BINARY_MULTIPLY
             32 CALL_METHOD              1
             34 POP_TOP

 27     >>   36 LOAD_FAST                0 (self)
             38 LOAD_ATTR                4 (_front)
             40 LOAD_FAST                0 (self)
             42 LOAD_ATTR                0 (_size)
             44 BINARY_ADD
             46 LOAD_GLOBAL              1 (len)
             48 LOAD_FAST                0 (self)
             50 LOAD_ATTR                2 (_data)
             52 CALL_FUNCTION            1
             54 BINARY_MODULO
             56 STORE_FAST               2 (avail)

 28          58 LOAD_FAST                1 (element)
             60 LOAD_FAST                0 (self)
             62 LOAD_ATTR                2 (_data)
             64 LOAD_FAST                2 (avail)
             66 STORE_SUBSCR

 29          68 LOAD_FAST                0 (self)
             70 DUP_TOP
             72 LOAD_ATTR                0 (_size)
             74 LOAD_CONST               2 (1)
             76 INPLACE_ADD
             78 ROT_TWO
             80 STORE_ATTR               0 (_size)
             82 LOAD_CONST               0 (None)
             84 RETURN_VALUE

Disassembly of is_empty:
 14           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (_size)
              4 LOAD_CONST               1 (0)
              6 COMPARE_OP               2 (==)
              8 RETURN_VALUE

Disassembly of rotate:
 56           0 LOAD_FAST                0 (self)
              2 LOAD_METHOD              0 (is_empty)
              4 CALL_METHOD              0
              6 POP_JUMP_IF_FALSE       16

 57           8 LOAD_GLOBAL              1 (Empty)
             10 LOAD_CONST               1 ('The array is empty')
             12 CALL_FUNCTION            1
             14 RAISE_VARARGS            1

 58     >>   16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                2 (_data)
             20 LOAD_FAST                0 (self)
             22 LOAD_ATTR                3 (_front)
             24 BINARY_SUBSCR
             26 LOAD_FAST                0 (self)
             28 LOAD_ATTR                2 (_data)
             30 LOAD_FAST                0 (self)
             32 LOAD_ATTR                3 (_front)
             34 LOAD_FAST                0 (self)
             36 LOAD_ATTR                4 (_size)
             38 BINARY_ADD
             40 LOAD_GLOBAL              5 (len)
             42 LOAD_FAST                0 (self)
             44 LOAD_ATTR                2 (_data)
             46 CALL_FUNCTION            1
             48 BINARY_MODULO
             50 STORE_SUBSCR

 59          52 LOAD_FAST                0 (self)
             54 LOAD_ATTR                3 (_front)
             56 LOAD_CONST               2 (1)
             58 BINARY_ADD
             60 LOAD_GLOBAL              5 (len)
             62 LOAD_FAST                0 (self)
             64 LOAD_ATTR                2 (_data)
             66 CALL_FUNCTION            1
             68 BINARY_MODULO
             70 LOAD_FAST                0 (self)
             72 STORE_ATTR               3 (_front)
             74 LOAD_CONST               0 (None)
             76 RETURN_VALUE

>>> 

>>> dis.show_code(ArrayQueue.enqueue)
Name:              enqueue
Filename:          <stdin>
Argument count:    2
Kw-only arguments: 0
Number of locals:  3
Stack size:        5
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: None
   1: 2
   2: 1
Names:
   0: _size
   1: len
   2: _data
   3: _resize
   4: _front
Variable names:
   0: self
   1: element
   2: avail
>>>

>>> dis.show_code(ArrayQueue.dequeue)
Name:              dequeue
Filename:          <stdin>
Argument count:    1
Kw-only arguments: 0
Number of locals:  2
Stack size:        4
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: '\n        Remove and return the first element of the queue (i.e., FIFO).\n        Raise Empty exception if the queue is empty.\n        '
   1: 'Queue is empty'
   2: None
   3: 1
   4: 0
   5: 4
   6: 2
Names:
   0: is_empty
   1: Empty
   2: _data
   3: _front
   4: len
   5: _size
   6: _resize
Variable names:
   0: self
   1: answer
>>>

>>> dis.show_code(ArrayQueue._resize)
Name:              _resize
Filename:          <stdin>
Argument count:    2
Kw-only arguments: 0
Number of locals:  5
Stack size:        4
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: None
   1: 1
   2: 0
Names:
   0: _data
   1: _front
   2: range
   3: _size
   4: len
Variable names:
   0: self
   1: cap
   2: old
   3: walk
   4: k
>>> 

>>> dis.show_code(ArrayQueue.rotate)
Name:              rotate
Filename:          <stdin>
Argument count:    1
Kw-only arguments: 0
Number of locals:  1
Stack size:        5
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: None
   1: 'The array is empty'
   2: 1
Names:
   0: is_empty
   1: Empty
   2: _data
   3: _front
   4: _size
   5: len
Variable names:
   0: self
>>> 

#---------------------------------------------------------------------------------------------------------------------------

>>> dis.dis(play_game)
  2           0 SETUP_LOOP              80 (to 82)
              2 LOAD_GLOBAL              0 (range)
              4 LOAD_FAST                2 (num_turns)
              6 CALL_FUNCTION            1
              8 GET_ITER
        >>   10 FOR_ITER                68 (to 80)
             12 STORE_FAST               4 (i)

  4          14 LOAD_GLOBAL              1 (random)
             16 LOAD_METHOD              1 (random)
             18 CALL_METHOD              0
             20 LOAD_CONST               1 (0.5)
             22 COMPARE_OP               4 (>)
             24 POP_JUMP_IF_FALSE       32

  5          26 LOAD_FAST                0 (Q)
             28 STORE_FAST               5 (carray)
             30 JUMP_FORWARD             4 (to 36)

  7     >>   32 LOAD_FAST                1 (R)
             34 STORE_FAST               5 (carray)

  8     >>   36 SETUP_LOOP              40 (to 78)
             38 LOAD_GLOBAL              0 (range)
             40 LOAD_GLOBAL              1 (random)
             42 LOAD_METHOD              2 (randint)
             44 LOAD_CONST               2 (0)
             46 LOAD_FAST                3 (max_rotations)
             48 CALL_METHOD              2
             50 CALL_FUNCTION            1
             52 GET_ITER
        >>   54 FOR_ITER                20 (to 76)
             56 STORE_FAST               6 (j)

  9          58 LOAD_FAST                5 (carray)
             60 LOAD_METHOD              3 (do_first)
             62 CALL_METHOD              0
             64 STORE_FAST               7 (final_value)

 10          66 LOAD_FAST                5 (carray)
             68 LOAD_METHOD              4 (rotate)
             70 CALL_METHOD              0
             72 POP_TOP
             74 JUMP_ABSOLUTE           54
        >>   76 POP_BLOCK
        >>   78 JUMP_ABSOLUTE           10
        >>   80 POP_BLOCK

 11     >>   82 LOAD_FAST                7 (final_value)
             84 LOAD_CONST               3 (2)
             86 BINARY_MODULO
             88 LOAD_CONST               2 (0)
             90 COMPARE_OP               2 (==)
             92 RETURN_VALUE
>>>

>>> dis.show_code(play_game)
Name:              play_game
Filename:          <stdin>
Argument count:    4
Kw-only arguments: 0
Number of locals:  8
Stack size:        6
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: None
   1: 0.5
   2: 0
   3: 2
Names:
   0: range
   1: random
   2: randint
   3: do_first
   4: rotate
Variable names:
   0: Q
   1: R
   2: num_turns
   3: max_rotations
   4: i
   5: carray
   6: j
   7: final_value
>>>

>>> dis.dis(main)
  3           0 LOAD_GLOBAL              0 (ArrayQueue)
              2 CALL_FUNCTION            0
              4 LOAD_GLOBAL              0 (ArrayQueue)
              6 CALL_FUNCTION            0
              8 ROT_TWO
             10 STORE_FAST               0 (Q)
             12 STORE_FAST               1 (R)

  4          14 LOAD_FAST                0 (Q)
             16 LOAD_METHOD              1 (enqueue)
             18 LOAD_CONST               1 (0)
             20 CALL_METHOD              1
             22 POP_TOP

  5          24 SETUP_LOOP              28 (to 54)
             26 LOAD_GLOBAL              2 (range)
             28 LOAD_CONST               2 (1)
             30 LOAD_CONST               3 (100)
             32 CALL_FUNCTION            2
             34 GET_ITER
        >>   36 FOR_ITER                14 (to 52)
             38 STORE_FAST               2 (i)

  6          40 LOAD_FAST                1 (R)
             42 LOAD_METHOD              1 (enqueue)
             44 LOAD_FAST                2 (i)
             46 CALL_METHOD              1
             48 POP_TOP
             50 JUMP_ABSOLUTE           36
        >>   52 POP_BLOCK

  7     >>   54 LOAD_CONST               1 (0)
             56 STORE_FAST               3 (total_wins)

  8          58 LOAD_CONST               4 (10000)
             60 STORE_FAST               4 (num_games)

  9          62 SETUP_LOOP              34 (to 98)
             64 LOAD_GLOBAL              2 (range)
             66 LOAD_FAST                4 (num_games)
             68 CALL_FUNCTION            1
             70 GET_ITER
        >>   72 FOR_ITER                22 (to 96)
             74 STORE_FAST               5 (game)

 10          76 LOAD_GLOBAL              3 (play_game)
             78 LOAD_FAST                0 (Q)
             80 LOAD_FAST                1 (R)
             82 CALL_FUNCTION            2
             84 POP_JUMP_IF_FALSE       72

 11          86 LOAD_FAST                3 (total_wins)
             88 LOAD_CONST               2 (1)
             90 INPLACE_ADD
             92 STORE_FAST               3 (total_wins)
             94 JUMP_ABSOLUTE           72
        >>   96 POP_BLOCK

 12     >>   98 LOAD_GLOBAL              4 (print)
            100 LOAD_CONST               5 ('Alice won ')
            102 LOAD_FAST                3 (total_wins)
            104 LOAD_FAST                4 (num_games)
            106 BINARY_TRUE_DIVIDE
            108 LOAD_CONST               3 (100)
            110 BINARY_MULTIPLY
            112 FORMAT_VALUE             0
            114 LOAD_CONST               6 ('% of her games')
            116 BUILD_STRING             3
            118 CALL_FUNCTION            1
            120 POP_TOP
            122 LOAD_CONST               0 (None)
            124 RETURN_VALUE
>>> 
>>> 
>>> dis.show_code(main)
Name:              main
Filename:          <stdin>
Argument count:    0
Kw-only arguments: 0
Number of locals:  6
Stack size:        4
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: None
   1: 0
   2: 1
   3: 100
   4: 10000
   5: 'Alice won '
   6: '% of her games'
Names:
   0: ArrayQueue
   1: enqueue
   2: range
   3: play_game
   4: print
Variable names:
   0: Q
   1: R
   2: i
   3: total_wins
   4: num_games
   5: game
>>> 
