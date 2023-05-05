
# disjoint.py

# Algo complexity: O(n^3)

def disjoint1(A, B, C):
    # Return True if there is no element common to all three lists.
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False       # we found a common value
    return True                        # if we reach this, sets are disjoint


# Algo complexity: O(n^2)

def disjoint2(A, B, C):
    # Return True if there is no element common to all three lists.
    for a in A:  # O(n)
        for b in B: # O(n^2)
            if a == b:   # only check C if we found match from A and B
                for c in C: # O(n^2)
                    if a == c:         # (and thus a == b == c)
                        return False   # we found a common value
    return True                        # if we reach this, sets are disjoint


# Set use {} to represent
if __name__ == '__main__': 
    A = {0,1,2,3,4,5,6,7,8,9}
    B = {10,11,12,13,14,15,16,17,18,19,20}
    C = {21,22,23,24,25,26,27,28,29,30}
    print(disjoint1(A,B,C))
    print(disjoint2(A,B,C))

# Output:

"""
True
True
"""

##########################################################################################################################


# disjoint sets


class DisjointSet:
    def __init__(self, vertices, parent):
        self.vertices = vertices
        self.parent = parent
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2


if __name__ == '__main__':
    vertices = ['a', 'b', 'c', 'd', 'e', 'h', 'i']
    parent = {}
    for v in vertices:
        parent[v] = v
    ds = DisjointSet(vertices, parent)
    print("Print all vertices in genesis: ")
    ds.union('b', 'd')
    ds.union('h', 'b')
    print(ds.find('h')) # prints d (OK)
    ds.union('h', 'i')
    print(ds.find('i')) # prints i (expecting d)

# Output:

"""
Print all vertices in genesis: 
d
i
>>> 
"""