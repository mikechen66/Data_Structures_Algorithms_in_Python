

# reverse_sequence.py


from sequence_iterator import SequenceIterator
from range import Range


class ReverseSequece(SequenceIterator):
    def __init__(self, sequence):
        super().__init__(sequence)
        self._k = -1
    def __next__(self):
        if -(self._k) >len(self._seq):
            raise StopIteration
        else:
            self._k-=1
            return self._seq[self._k+1]


class NewRange(Range):
    def __init__(self,start, stop, step):
        super().__init__(start, stop, step)
    def __contains__(self,num):
        if (num-self._start)/self._step<=len(self) and (num-self._start)%self._step==0:
            return True
        else:
            return False


if __name__=="__main__":
    rs =ReverseSequece('12345')
    print(list(rs))
    n_range = NewRange(3,100,12)
    print(15 in n_range)


# Output:

"""
['5', '4', '3', '2', '1']
True
"""