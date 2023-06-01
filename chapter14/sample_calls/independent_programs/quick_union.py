

# quick_union.py


class QuickFind(object):
    id = []
    count = 0
    def __init__(self,n):
        self.count = n
        i = 0
        while i < n:
            self.id.append(i)
            i += 1 
    def connected(self,p,q):
        return self.find(p) == self.find(q)
    def find(self,p):    
        return self.id[p]
    def union(self,p,q):
        idp = self.find(p)
        if not self.connected(p,q):
            for i in range(len(self.id)):
                if self.id[i]==idp: # Set all the id as q's current id withon a group
                    self.id[i] = self.id[q] 
            self.count -= 1 


if __name__ == '__main__':
    qf = QuickFind(10)
    print("initial id list is %s" % (",").join(str(x) for x in qf.id))
    list = [
            (4,3),
            (3,8),
            (6,5),
            (9,4),
            (2,1),
            (8,9),
            (5,0),
            (7,2),
            (6,1),
            (1,0),
            (6,7)
        ]
    for k in list:
        p = k[0]
        q = k[1]
        qf.union(p,q)
        print("%d and %d is connected? %s" % (p,q,str(qf.connected(p,q))))
    print("final id list is %s" % (",").join(str(x) for x in qf.id))
    print("count of components is: %d" % qf.count)


# Output:

"""
initial id list is 0,1,2,3,4,5,6,7,8,9
4 and 3 is connected? True
3 and 8 is connected? True
6 and 5 is connected? True
9 and 4 is connected? True
2 and 1 is connected? True
8 and 9 is connected? True
5 and 0 is connected? True
7 and 2 is connected? True
6 and 1 is connected? True
1 and 0 is connected? True
6 and 7 is connected? True
final id list is 1,1,1,8,8,1,1,1,8,8
count of components is: 2
"""