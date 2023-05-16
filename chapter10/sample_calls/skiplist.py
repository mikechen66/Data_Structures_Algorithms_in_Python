

import random


class SkipTable:
    """key is class int"""
    #----------------------------------------------------_Chain--------------------------------------------
    class _Chain:
        #------------------------------------------------_Item---------------------------------------------        
        class _Item:
            """The construction method of _Item"""
            def __init__(self,k,v,after,below):
                # input (key, value, after, below)
                self._key = k
                self._value = v
                self._after = after
                self._below = below
            def __eq__(self, other):
                if isinstance(other,int):            # if other is int
                    return self._key == other
                return self._key == other._key       # compare items based on their keys
            def __ne__(self, other):
                return not (self == other)           # opposite of __eq__
            def __lt__(self, other):
                if isinstance(other, int):           # if other is int
                    # print(self._key,other)
                    return self._key < other
                return self._key < other._key        # compare items based on their keys
            def __gt__(self,other):
                if isinstance(other, int):           # if other is int
                    return self._key > other                
                return self._key > other._key    
            def __le__(self,other):
                # print(self._key,self._value)
                if isinstance(other, int):           # if other is int
                    return self._key <= other                
                return self._key <= other._key    
        #--------------------------------------------------------------------------------------------------
        def __init__(self):
            # The construction method of _Chain
            # create a chain with head and tail
            self._head = self._Item('k_min', 'v_min', None, None)      # the min item
            self._tail = self._Item('k_max', 'v_max', None, None)      # the max item
            self._head._after = self._tail           # conbine the head and tail
            self._size = 0
        def tail(self):
            return self._tail
        def __len__(self):
            return self._size
        def key(self, item):
            return item._key
        def first(self):
            return self._head
        def after(self, item):
            return item._after
        def below(self, item):
            return item._below
        def add_after(self, item, new):
            # add (new) after the item,only horizontal
            new._after = item._after  
            item._after = new
            self._size += 1
            return new
        def del_after(self, item):
            # delete after the node, only horizontal
            temp = item._after
            item._after = temp._after
            temp._after = None
            self._size -= 1
            return temp
    #--------------------------------------------------------------------------------------------------
    # Construction method of SkipTable
    def __init__(self):
        self._table = [self._Chain()]                # store the skipchain
        self._size = 0                               # len of the skipTable
    def __setitem__(self, k, v):
        self.insert(k, v)
    def __getitem__(self, k):
        # get the item or raise error
        index, temp = self.search_before(k)
        chain = self._table[index]
        ras = chain.after(temp)
        if ras._key != k:
            raise ValueError('no item')
        return ras._value
    def __delitem__(self, k):
        self.delete(k)
    def __len__(self):
        return self._size
    def _coin(self):
        # return a num of the level the item should be
        times = 0
        while random.randint(0, 1) == 1:
            times += 1                    # if the random is 1 ,times +=1
        return times
    def search_before(self, k, high=None):
        """
        find the node before item that key is k or like k;
        return (index,temp)
        if k in this chain, return the index of chain and item before k;
        if k not in the chain, returnn high  
        """
        # print(k,high,len(self._table))
        chain = self._table[-1]                      # the top chain
        temp = chain.first()                         # the min node
        if high == None:                             # vague search for insert
            high = 0
        for i in range(len(self._table)-1, high-1, -1):  # inverse order traver the table
            # print(chain.tail() is chain.after(temp),temp,temp._value) 
            # if next node isn't tail or bigger than item           
            while chain.after(temp) is not chain.tail() and chain.after(temp) <= k:                   
                if chain.after(temp) == k:
                    return (i, temp)                 # return index of chain and temp at not buttom level
                temp = chain.after(temp)
            if i == high:                            # end of the table
                return (i, temp)
            temp = chain.below(temp)                 # change the chain    
            chain = self._table[i-1]
    def append_chain(self):
        # append a new chain and conbine the head and tail
        self._table.append(self._Chain())
        self._table[-1]._head._below = self._table[-2]._head    
        self._table[-1]._tail._below = self._table[-2]._tail
    def insert(self, k, v):
        """
        caculate the times of coin;
        add item at position where it should be;
        conbine the below
        """
        h = self._coin()
        while h >= len(self._table):
            self.append_chain()                      # if the level is lower than h ,append it
        index, temp = self.search_before(k, h)       # (chain index , positions)         
        chain = self._table[index]
        if chain.after(temp)._key == k:              # if k in the table,change it
            return self.change(k, v)
        c_temp = self._Chain._Item(k, v, None, None) # current item
        b_temp = self._Chain._Item(k, v, None, None) # below item        
        self._size += 1                              # size +1        
        for i in range(index, -1, -1):               # trave the level from level index to 0
            chain.add_after(temp, c_temp) 
            c_temp._below = b_temp                   # conbine the below
            c_temp = b_temp                          # exchange item
            b_temp = self._Chain._Item(k, v, None, None)
            if i == 0:                               # end of the chain
                return None
            temp = chain.below(temp)                 # change the below chain
            chain = self._table[i-1]
            # print(chain.after(temp) is chain.tail(),chain.after(temp)._key, chain.tail()._key)
            while chain.after(temp) is not chain.tail() and chain.after(temp) < k:
                temp = chain.after(temp)             # chagne the temp
    def change(self, k, v):
        # delete and insert
        self.delete(k)
        self[k] = v
    def delete(self, k):
        # delete k or raise error
        index,temp = self.search_before(k)           # find the item front k
        if self._table[index].after(temp)._key != k:
            raise ValueError('none item')
        chain = self._table[index]
        for i in range(index, -1, -1):               # trave the level from level index to 0
             del_item = chain.del_after(temp)        # cut the after link
             del_item._below = None                  # cut the below link
             if i == 0:                              # end of the chain
                 return None
             temp = chain.below(temp)
             chain = self._table[i-1]
             while chain.after(temp) != k:           # fand the new temp
                 temp = chain.after(temp)


def getlist(n=1000):
    import random
    """
    n is the num of list
    return list1, in order sequence
    return list2, disorder sequence
    """
    list1=[i for i in range(n)]
    list2=random.sample(range(n*5),n)
    return list1,list2


def ftime(l=None, T=None):
    import time
    """
    l is the input sequence
    T is the data structure's instance
    return the time
    """
    if l == None or T == None:
        raise KeyError('invalid parameter.')
    time1 = time.time()
    for i in l:                                      # perform set method
        T[i] = i
    for i in l:                                      # perform get method
        T[i]
    for i in l:
        del T[i]                                     # perform del method
    return time.time() - time1


if __name__ == '__main__':              
    n = 10000
    l1, l2 = getlist(n)                              # if too many node,  python will break
    t1 = ftime(l1, SkipTable())
    print('skiptable:',t1)
    t2 = ftime(l2, SkipTable())
    print('skiptable:', t2)


# Output:

"""
skiptable: 0.6429965496063232
skiptable: 0.8079638481140137
"""