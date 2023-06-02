

# union_by_rank.py


# Implementation of Disjoint Set Union-By-Rank and Path Compression.


class Set :
    def __init__(self, arg_data, arg_rank) :
        self.rank = arg_rank
        self.data = arg_data
        self.parent = self
        print("Created set : " + str(arg_data) + " Rank : " + str(arg_rank))


# FindParent applies path compression to all the nodes in the search path of the parent
# without changing their ranks.
def FindParent(s):
    if (s.data != s.parent.data) :
        s.parent = FindParent((s.parent))
    return s.parent


# Merge operation makes use of heuristic union-by-rank.
def Merge(a, b):
    parent_of_a = FindParent(a)
    parent_of_b = FindParent(b)
    if (parent_of_a.data != parent_of_b.data):
        if (a.rank < b.rank):
            a.parent = parent_of_b
            b.rank += 1
        else:
            b.parent = parent_of_a
            a.rank += 1
    print("\nMerging " + str(a.data) + " & " + str(b.data))
    print("Rank of : " + str(a.data) + " = " + str(a.rank))
    print("Parent of : " + str(a.data) + " = " + str(a.parent.data))
    print("Rank of : " + str(b.data) + " = " + str(b.rank))
    print("Parent of : " + str(b.data) + " = " + str(b.parent.data))


def main() :
    # Initially every node in a set has a rank 0 and is a parent of itself
    s1 = Set(1, 0) # Data : 1, Rank : 0, Parent : 1
    s2 = Set(2, 0)
    s3 = Set(3, 0)
    s4 = Set(4, 0)
    s5 = Set(5, 0)
    s6 = Set(6, 0)
    s7 = Set(7, 0)
    s8 = Set(8, 0)
    s9 = Set(9, 0)
    s10 = Set(10, 0)
    Merge (s1, s3)
    Merge (s2, s4)
    # 
    #   1      2
    #   ^      ^
    #   |      |
    #   3      4
    # 
    # After merging (s1, s3), merge (s3, s5), s1 is parent 
    Merge (s3, s5)
    # After merging (s2, s4), merge (s4, s6), s2 is parent 
    Merge (s4, s6)
    # 
    #   1        2
    #   ^        ^
    #   | \      | \
    #   3  5     4  6 
    # 
    Merge(s7, s8)
    Merge(s9, s10)
    Merge(s5, s7)
    Merge(s6, s9)
    Merge(s8, s10)


if __name__ == "__main__" :
    main()


# Output:

"""
Created set : 1 Rank : 0
Created set : 2 Rank : 0
Created set : 3 Rank : 0
Created set : 4 Rank : 0
Created set : 5 Rank : 0
Created set : 6 Rank : 0
Created set : 7 Rank : 0
Created set : 8 Rank : 0
Created set : 9 Rank : 0
Created set : 10 Rank : 0

Merging 1 & 3
Rank of : 1 = 1
Parent of : 1 = 1
Rank of : 3 = 0
Parent of : 3 = 1

Merging 2 & 4
Rank of : 2 = 1
Parent of : 2 = 2
Rank of : 4 = 0
Parent of : 4 = 2

Merging 3 & 5
Rank of : 3 = 1
Parent of : 3 = 1
Rank of : 5 = 0
Parent of : 5 = 1

Merging 4 & 6
Rank of : 4 = 1
Parent of : 4 = 2
Rank of : 6 = 0
Parent of : 6 = 2

Merging 7 & 8
Rank of : 7 = 1
Parent of : 7 = 7
Rank of : 8 = 0
Parent of : 8 = 7

Merging 9 & 10
Rank of : 9 = 1
Parent of : 9 = 9
Rank of : 10 = 0
Parent of : 10 = 9

Merging 5 & 7
Rank of : 5 = 0
Parent of : 5 = 7
Rank of : 7 = 2
Parent of : 7 = 7

Merging 6 & 9
Rank of : 6 = 0
Parent of : 6 = 9
Rank of : 9 = 2
Parent of : 9 = 9

Merging 8 & 10
Rank of : 8 = 1
Parent of : 8 = 7
Rank of : 10 = 0
Parent of : 10 = 7
"""