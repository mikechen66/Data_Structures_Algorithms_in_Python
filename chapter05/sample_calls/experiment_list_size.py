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


import sys


try:
    n = int(sys.argv[1])
except:
    n = 100

import sys                                # provides getsizeof function


data = []
for k in range(n):                        # NOTE: must fix choice of n
    a = len(data)                         # number of elements
    b = sys.getsizeof(data)               # actual size in bytes
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)                     # increase length by one


# Output:

"""
Length:   0; Size in bytes:   72
Length:   1; Size in bytes:  104
Length:   2; Size in bytes:  104
Length:   3; Size in bytes:  104
Length:   4; Size in bytes:  104
Length:   5; Size in bytes:  136
Length:   6; Size in bytes:  136
Length:   7; Size in bytes:  136
Length:   8; Size in bytes:  136
Length:   9; Size in bytes:  200
Length:  10; Size in bytes:  200
Length:  11; Size in bytes:  200
Length:  12; Size in bytes:  200
...
Length:  91; Size in bytes:  920
Length:  92; Size in bytes:  920
Length:  93; Size in bytes:  920
Length:  94; Size in bytes:  920
Length:  95; Size in bytes:  920
Length:  96; Size in bytes:  920
Length:  97; Size in bytes:  920
Length:  98; Size in bytes:  920
Length:  99; Size in bytes:  920

"""
############################################################################


import sys


try:
    n = int(sys.argv[1])
except:
    n = 100

import sys                                # provides getsizeof function


data = []
for k in range(n):                        # NOTE: must fix choice of n
    a = len(data)                         # number of elements
    b = sys.getsizeof(data)               # actual size in bytes
    # {0:4d}: {}: 字典字符串映射; 0:第0个元素; <: 左对齐； 4:空格宽度；d: 十进制；
    print('Length: {0:4d}; Size in bytes: {1:5d}'.format(a, b))
    data.append(None)                     # increase length by one


# Output:

"""
Length:    0; Size in bytes:    72
Length:    1; Size in bytes:   104
Length:    2; Size in bytes:   104
Length:    3; Size in bytes:   104
Length:    4; Size in bytes:   104
Length:    5; Size in bytes:   136
Length:    6; Size in bytes:   136
Length:    7; Size in bytes:   136
Length:    8; Size in bytes:   136
Length:    9; Size in bytes:   200
Length:   10; Size in bytes:   200
Length:   11; Size in bytes:   200
Length:   12; Size in bytes:   200
Length:   13; Size in bytes:   200
Length:   14; Size in bytes:   200
Length:   15; Size in bytes:   200
Length:   16; Size in bytes:   200
Length:   17; Size in bytes:   272
Length:   18; Size in bytes:   272
Length:   19; Size in bytes:   272
Length:   20; Size in bytes:   272
Length:   21; Size in bytes:   272
Length:   22; Size in bytes:   272
Length:   23; Size in bytes:   272
Length:   24; Size in bytes:   272
Length:   25; Size in bytes:   272
Length:   26; Size in bytes:   352
Length:   27; Size in bytes:   352
Length:   28; Size in bytes:   352
Length:   29; Size in bytes:   352
Length:   30; Size in bytes:   352
Length:   31; Size in bytes:   352
Length:   32; Size in bytes:   352
Length:   33; Size in bytes:   352
Length:   34; Size in bytes:   352
Length:   35; Size in bytes:   352
Length:   36; Size in bytes:   440
Length:   37; Size in bytes:   440
Length:   38; Size in bytes:   440
Length:   39; Size in bytes:   440
Length:   40; Size in bytes:   440
Length:   41; Size in bytes:   440
Length:   42; Size in bytes:   440
Length:   43; Size in bytes:   440
Length:   44; Size in bytes:   440
Length:   45; Size in bytes:   440
Length:   46; Size in bytes:   440
Length:   47; Size in bytes:   536
Length:   48; Size in bytes:   536
Length:   49; Size in bytes:   536
Length:   50; Size in bytes:   536
Length:   51; Size in bytes:   536
Length:   52; Size in bytes:   536
Length:   53; Size in bytes:   536
Length:   54; Size in bytes:   536
Length:   55; Size in bytes:   536
Length:   56; Size in bytes:   536
Length:   57; Size in bytes:   536
Length:   58; Size in bytes:   536
Length:   59; Size in bytes:   648
Length:   60; Size in bytes:   648
Length:   61; Size in bytes:   648
Length:   62; Size in bytes:   648
Length:   63; Size in bytes:   648
Length:   64; Size in bytes:   648
Length:   65; Size in bytes:   648
Length:   66; Size in bytes:   648
Length:   67; Size in bytes:   648
Length:   68; Size in bytes:   648
Length:   69; Size in bytes:   648
Length:   70; Size in bytes:   648
Length:   71; Size in bytes:   648
Length:   72; Size in bytes:   648
Length:   73; Size in bytes:   776
Length:   74; Size in bytes:   776
Length:   75; Size in bytes:   776
Length:   76; Size in bytes:   776
Length:   77; Size in bytes:   776
Length:   78; Size in bytes:   776
Length:   79; Size in bytes:   776
Length:   80; Size in bytes:   776
Length:   81; Size in bytes:   776
Length:   82; Size in bytes:   776
Length:   83; Size in bytes:   776
Length:   84; Size in bytes:   776
Length:   85; Size in bytes:   776
Length:   86; Size in bytes:   776
Length:   87; Size in bytes:   776
Length:   88; Size in bytes:   776
Length:   89; Size in bytes:   920
Length:   90; Size in bytes:   920
Length:   91; Size in bytes:   920
Length:   92; Size in bytes:   920
Length:   93; Size in bytes:   920
Length:   94; Size in bytes:   920
Length:   95; Size in bytes:   920
Length:   96; Size in bytes:   920
Length:   97; Size in bytes:   920
Length:   98; Size in bytes:   920
Length:   99; Size in bytes:   920
"""