

# sequence_abc.py


# collections.abc is deprecated 
# from collections.abc import ABCMeta, abstractmethod 
from abc import ABCMeta, abstractmethod            


class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""
    @abstractmethod
    def __len__(self):
        # Return the length of the sequence.
        pass
    @abstractmethod
    def __getitem__(self, j):
        # Return the element at index j of the sequence.
        pass
    def __contains__(self, val):
        # Return True if val found in the sequence; False otherwise.
        for j in range(len(self)):
            if self[j] == val:                        # found match
                return True
        return False
    def index(self, val):
        # Return leftmost index at which val is found (or raise ValueError).
        for j in range(len(self)):
            if self[j] == val:                        # leftmost match
                return j
        raise ValueError('value not in sequence')     # never found a match
    def count(self, val):
        # Return the number of elements equal to given value.
        k = 0
        for j in range(len(self)):
            if self[j] == val:                        # found a match
                k += 1
        return k