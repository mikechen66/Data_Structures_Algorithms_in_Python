
# Algorithm for BTree


class Node:
    def __init__(self):
        self.n = 0
        self.key = [0] * MAX_KEYS
        self.child = [None] * MAX_CHILDREN
        self.leaf = True


def BtreeSearch(x, k):
    i = 0
    while i < x.n and k >= x.key[i]:
        i += 1
    if i < x.n and k == x.key[i]:
        return x
    if x.leaf:
        return None
    return BtreeSearch(x.child[i], k)