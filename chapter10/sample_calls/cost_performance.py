# cost_performance.py

"""

1.All of the arguments are integers 

2.Add the method of __len() to address the length

"""


from sorted_table_map import SortedTableMap


class CostPerformanceDatabase:
    # A database with maximal (cost, performance) pairs
    def __init__(self):
        self._M = SortedTableMap()
    def __len__(self):
        return len(self._M)
    def best(self, c):
        # return (c, p) pairs with largest cost not exceeding c.
        return self._M.find_le(c)
    def add(self, c, p):
        other = self._M.find_le(c)
        if other is not None and other[1] >= p:
            return
        self._M[c] = p
        # remove any pairs that are dominated by (c, p)
        other = self._M.find_gt(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)


if __name__ == '__main__':
    cpd = CostPerformanceDatabase()
    cpd.add(2000000, 200)
    cpd.add(1600000, 160)
    cpd.add(1400000, 140)
    cpd.add(1200000, 120)
    cpd.add(800000, 80)
    print(cpd.best(1000000))
    print(cpd.__len__())


# Output:

"""
(800000, 80)
5
"""

