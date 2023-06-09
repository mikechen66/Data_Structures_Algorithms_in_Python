

# btree.py

"""

Searching for an element in a B-tree is the generalized form of searching an element 
in a Binary Search Tree. The following steps are followed.

1. Definition:

Root node: 
The topmost node of a tree or the node which does not have any parent node is called the 
root node. 

Internal node: 
A node with at least one child is called Internal Node.

Leaf node: 
Leaf node is also called External node: The nodes which do not have any child nodes are 

Degree of a Node: 
The total count of subtrees attached to that node is called the degree of the node. The 
degree of a leaf node must be 0. The degree of a tree is the maximum degree of a node 
among all the nodes in the tree.

2. Algorithm:

Starting from the root node, compare k with the first key of the node.

If k = the first key of the node, return the node and the index.

If k.leaf = true, return NULL (i.e. not found).

If k < the first key of the root node, search the left child of this key recursively.

If there is more than one key in the current node and k > the first key, compare k with 
the next key in the node.

If k < next key, search the left child of this key (ie. k lies in between the first and 
the second keys).

Else, search the right child of the key.

Repeat steps 1 to 4 until the leaf is reached.

"""


# Create a node
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


# Tree
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t
    # Insert node
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)
    # Insert nonfull
    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)
    # Split the child
    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t-1]
        if not y.leaf:
            z.child = y.child[t: 2*t]
            y.child = y.child[0: t-1]
    # Print the tree
    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)
    # Search key in the tree
    def search_key(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.child[i])
        else:
            return self.search_key(k, self.root)


def main():
    B = BTree(3)
    for i in range(10):
        B.insert((i, 2 * i))
    B.print_tree(B.root)
    if B.search_key(8) is not None:
        print("\nFound")
    else:
        print("\nNot Found")


if __name__ == '__main__':
    main()


# Output:

"""
Level  0   2:(2, 4) (5, 10) 
Level  1   2:(0, 0) (1, 2) 
Level  1   2:(3, 6) (4, 8) 
Level  1   4:(6, 12) (7, 14) (8, 16) (9, 18) 

Found
"""