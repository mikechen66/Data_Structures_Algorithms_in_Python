
 
 # favorites_list1.py


from favorites_list import FavoritesList
from positional_list import PositionalList


class FavoritesList1(FavoritesList):
    def clear(self):
        # clear all of item
        temp = PositionalList()    # creat a new data to dele the older data
        self._data = temp
    def reset_counts(self, num=0):
        # Reset counts of FavoritesList1
        temp = self._data.first()
        while temp != None:
            temp.element()._count = num
            temp = self._data.after(temp)


if __name__ == '__main__':
    a = FavoritesList1()
    for i in range(10):
        a.access(i)
    print(len(a))
    a.clear()
    print(len(a))
    for i in range(3):
        for j in range(10):
            a.access(j)
    a.reset_counts()
    for i in range(10, 11):
        a.access(i)
        print(a)
    for i in a.top(11):
        print(i)


# Output:

"""
>>> # the first print()
10
>>> # the second print()
0
>>> # the third print()
(10:1), (0:0), (1:0), (2:0), (3:0), (4:0), (5:0), (6:0), (7:0), (8:0), (9:0)
>>> # the fourtu print()
10
0
1
2
3
4
5
6
7
8
9
"""