

from sequence_abc import Sequence


class CompareSequence(Sequence):
    def __init__(self, arm):
        self._arm = arm
    def __len__(self):
        len(self._arm)
    def __getitem__(self,val):
        return arm[val-1]
    def __eq__(self,other):
        if self._arm == other._arm:
            return True
        else:
            return False
    def __lt__(self,other):
        if len(self) > len(other):
            return True
        else:
            return False

       
if __name__=="__main__":
    cs1 = CompareSequence('1,2,3')
    cs2 = CompareSequence('1,3,3')
    print("Compare the length of the two dicts")
    print(cs1==cs2)
