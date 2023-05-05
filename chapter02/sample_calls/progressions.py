

# progressions.py


class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression): 
    """Iterator produces an arithmetic progression."""
    def __init__(self, increment=1, start=0):
        """
        Create a new arithmetic progression.
        increment  the fixed constant to add to each term (default 1)
        start      the first term of the progression (default 0)
        """
        super().__init__(start)       # initialize base class
        self._increment = increment
    def _advance(self):               # override inherited version
        # Update current value by adding the fixed increment.
        self._current += self._increment


# inherit from Progression    
class GeometricProgression(Progression):  
    """Iterator produces a geometric progression."""
    def __init__(self, base=2, start=1):
        """
        Create a new geometric progression.
        base: the fixed constant multiplied to each term (default 2)
        start: the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base
    def _advance(self):  # override inherited version
        # Update current value by multiplying it by the base value.
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    def __init__(self, first=0, second=1):
        """
        Create a new fibonacci progression.
        first      the first term of the progression (default 0)
        second     the second term of the progression (default 1)
        """
        super().__init__(first)      # start progression at first
        self._prev = second - first  # fictitious value preceding the first
    def _advance(self):
        # Update current value by taking sum of previous two.
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)
    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5, 0).print_progression(10)
    print('Arithmetic progression with increment 5 and start 2:')
    ArithmeticProgression(5, 2).print_progression(10)
    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)
    print('Geometric progression with base 3:')
    GeometricProgression(3).print_progression(10)
    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)
    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4, 6).print_progression(10)


# Output:

"""
Default progression:
0 1 2 3 4 5 6 7 8 9
Arithmetic progression with increment 5:
0 5 10 15 20 25 30 35 40 45
Arithmetic progression with increment 5 and start 2:
2 7 12 17 22 27 32 37 42 47
Geometric progression with default base:
1 2 4 8 16 32 64 128 256 512
Geometric progression with base 3:
1 3 9 27 81 243 729 2187 6561 19683
Fibonacci progression with default start values:
0 1 1 2 3 5 8 13 21 34
Fibonacci progression with start values 4 and 6:
4 6 10 16 26 42 68 110 178 288
"""

#---------------------------------------------------------------------------------------------


class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression): 
    """Iterator produces an arithmetic progression."""
    def __init__(self, increment=1, start=0):
        """
        Create a new arithmetic progression.
        increment  the fixed constant to add to each term (default 1)
        start      the first term of the progression (default 0)
        """
        super().__init__(start)       # initialize base class
        self._increment = increment
    def _advance(self):               # override inherited version
        # Update current value by adding the fixed increment.
        self._current += self._increment


if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)
    print('Arithmetic progression with increment 1:')
    ArithmeticProgression(1, 0).print_progression(10)


# Output:

"""
Default progression:
0 1 2 3 4 5 6 7 8 9
Arithmetic progression with increment 5:
0 1 2 3 4 5 6 7 8 9
"""

#---------------------------------------------------------------------------------------------


# ArithmeticProgression(等差数列)


class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression): 
    """Iterator produces an arithmetic progression."""
    def __init__(self, increment=1, start=0):
        """
        Create a new arithmetic progression.
        increment  the fixed constant to add to each term (default 1)
        start      the first term of the progression (default 0)
        """
        super().__init__(start)       # initialize base class
        self._increment = increment
    def _advance(self):               # override inherited version
        # Update current value by adding the fixed increment.
        self._current += self._increment


if __name__ == '__main__':
    print('Default progression:')
    Progression(2).print_progression(10)
    print('Arithmetic progression with increment 2:')
    ArithmeticProgression(2, 2).print_progression(10)


# Output:

"""
Default progression:
2 3 4 5 6 7 8 9 10 11
Arithmetic progression with increment 2:
2 4 6 8 10 12 14 16 18 20
"""


#----------------------------------------------------------------------------------------------------


# GeometricProgression

class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


# inherit from Progression    
class GeometricProgression(Progression):  
    """Iterator produces a geometric progression."""
    def __init__(self, base=2, start=1):
        """
        Create a new geometric progression.
        base: the fixed constant multiplied to each term (default 2)
        start: the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base
    def _advance(self):  # override inherited version
        # Update current value by multiplying it by the base value.
        self._current *= self._base


if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)
    print('Geometric progression with default base:')
    GeometricProgression(2,1).print_progression(10)
    print('Geometric progression with base 3:')
    GeometricProgression(3,1).print_progression(10)
    print('Geometric progression with base 3 and start 2:')
    GeometricProgression(3,2).print_progression(10)


# Output:

"""
Default progression:
0 1 2 3 4 5 6 7 8 9
Geometric progression with default base:
1 2 4 8 16 32 64 128 256 512
Geometric progression with base 3:
1 3 9 27 81 243 729 2187 6561 19683
Geometric progression with base 3 and start 2:
2 6 18 54 162 486 1458 4374 13122 39366
"""

#--------------------------------------------------------------------------------------------


# PowerProgression

# https://encyclopediaofmath.org/wiki/Power_function

class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


# inherit from Progression    
class PowerProgression(Progression):  
    """Iterator produces a geometric progression."""
    def __init__(self, index=2, start=1):
        """
        Create a new geometric progression.
        base: the fixed constant multiplied to each term (default 2)
        start: the first term of the progression (default 1)
        """
        super().__init__(start)
        self._index = index
    def _advance(self):  # override inherited version
        # Update current value by multiplying it by the base value.
        self._current **= self._index


if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)
    print('Power progression with default base:')
    PowerProgression(2,1).print_progression(10)
    print('Power progression with base 3 and start 2:')
    PowerProgression(3,2).print_progression(10)
    print('Power progression with base 3 and start 3:')
    PowerProgression(3,3).print_progression(10)


# Output:

"""
Default progression:
0 1 2 3 4 5 6 7 8 9
Power progression with default base:
1 1 1 1 1 1 1 1 1 1
Power progression with base 3 and start 2:
2 8 512 134217728 2417851639229258349412352 14134776518227074636666380005943348126619871175004951664972849610340958208 2824013958708217496949108842204627863351353911851577524683401930862693830361198499905873920995229996970897865498283996578123296865878390947626553088486946106430796091482716120572632072492703527723757359478834530365734912 22521666186739810716017129863546474247925813985186306383480395759255528226899398031271474259176472311138130302909797370563984143657840869015723623128208458564711932390036470899999940399003451938771468124775412134017692556582989981820657376622292117781429636251681663364133246565240603802421309871873386179061056683850002592550658912005406539073633368208169912295100765107813056035892005304712416817301893705332191267615274619407764899319819287315641053762034009508858938727147166108668063720886082155921552955435591503022900749768195878181491707144967461286550140023171580051111358071521188926359524314904062599527129957121490685127011258936786658012354838528
"""

#--------------------------------------------------------------------------------------------


# Fibanacci progression

class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    def __init__(self, first=0, second=1):
        """
        Create a new fibonacci progression.
        first      the first term of the progression (default 0)
        second     the second term of the progression (default 1)
        """
        super().__init__(first)      # start progression at first
        self._prev = second - first  # fictitious value preceding the first
    def _advance(self):
        # Update current value by taking sum of previous two.
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(100)
    print('Fibonacci progression with default start values:')
    FibonacciProgression(0, 1).print_progression(100)
    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4, 6).print_progression(100)


# Output:

"""
Default progression:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
Fibonacci progression with default start values:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903 2971215073 4807526976 7778742049 12586269025 20365011074 32951280099 53316291173 86267571272 139583862445 225851433717 365435296162 591286729879 956722026041 1548008755920 2504730781961 4052739537881 6557470319842 10610209857723 17167680177565 27777890035288 44945570212853 72723460248141 117669030460994 190392490709135 308061521170129 498454011879264 806515533049393 1304969544928657 2111485077978050 3416454622906707 5527939700884757 8944394323791464 14472334024676221 23416728348467685 37889062373143906 61305790721611591 99194853094755497 160500643816367088 259695496911122585 420196140727489673 679891637638612258 1100087778366101931 1779979416004714189 2880067194370816120 4660046610375530309 7540113804746346429 12200160415121876738 19740274219868223167 31940434634990099905 51680708854858323072 83621143489848422977 135301852344706746049 218922995834555169026
Fibonacci progression with start values 4 and 6:
4 6 10 16 26 42 68 110 178 288 466 754 1220 1974 3194 5168 8362 13530 21892 35422 57314 92736 150050 242786 392836 635622 1028458 1664080 2692538 4356618 7049156 11405774 18454930 29860704 48315634 78176338 126491972 204668310 331160282 535828592 866988874 1402817466 2269806340 3672623806 5942430146 9615053952 15557484098 25172538050 40730022148 65902560198 106632582346 172535142544 279167724890 451702867434 730870592324 1182573459758 1913444052082 3096017511840 5009461563922 8105479075762 13114940639684 21220419715446 34335360355130 55555780070576 89891140425706 145446920496282 235338060921988 380784981418270 616123042340258 996908023758528 1613031066098786 2609939089857314 4222970155956100 6832909245813414 11055879401769514 17888788647582928 28944668049352442 46833456696935370 75778124746287812 122611581443223182 198389706189510994 321001287632734176 519390993822245170 840392281454979346 1359783275277224516 2200175556732203862 3559958832009428378 5760134388741632240 9320093220751060618 15080227609492692858 24400320830243753476 39480548439736446334 63880869269980199810 103361417709716646144 167242286979696845954 270603704689413492098 437845991669110338052 708449696358523830150 1146295688027634168202 1854745384386157998352
"""