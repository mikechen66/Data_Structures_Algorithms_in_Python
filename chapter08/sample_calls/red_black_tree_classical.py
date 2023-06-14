

# red_black_tree_classical.py

"""

A red-black tree is a binary search tree with one extra bit of storage per node: its color, which can 
be either RED or BLACK. By constraining the node colors on anysimple path from the root to a leaf, 
red-black trees ensure that no such path is more than twice as long as any other, so that the tree is 
approximately balanced.

Each node of the tree now contains the attributes color, key, left, right, and p. If a child or the 
parent of a node does not exist, the corresponding pointer attribute of the node contains the value NIL. 
We shall regard these NIL s as being pointers to leaves (external nodes) of the binary search tree and 
the normal, key-bearing nodes as being internal nodes of the tree.


A red-black tree is a weak-balanced binary search tree that satisfies the following red-black 
properties:

1. Every node is either red or black.
2. The root is black.
3. Every leaf ( NIL ) is black.
4. If a node is red, then both its children are black.
5. For each node, all simple paths from the node to descendant leaves contain the same number of black 
   nodes.

The code is provided according to the pseudocode of Cormen's Introduction to Algorithm
"""


class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.color = 'black'
        self.size=None


class RBTree(object):
    def __init__(self):
        self.nil = Node(0)
        self.root = self.nil
    def left_rotate(self, x):
        y = x.right                                     # set y
        x.right = y.left                                # turn y's left subtree into x's right subtree
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p                                       # link x's p to y's p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x                                      # put x on y's left
        x.p = y
    def right_rotate(self, x):                          # swap between left and right of left_rotate()
        y = x.left                                      # set x
        x.left = y.right                                # turn y's right subtree into y's left subtree
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p                                       # link x's p to x's p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y                                # put y on x's right
        y.right = x
        x.p = y
    def rb_insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'red'
        self.rb_insert_fixup(z)
        return (z.key, z.color)
    def rb_insert_fixup(self, z):                       # keep the rb tree's features
        while z.p.color == 'red':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'red':                    # Case 1 
                    z.p.color = 'black'
                    y.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                elif z == z.p.right:                    # case 2 
                    z = z.p
                    self.left_rotate(z)
                else:                                   # case 3
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self.right_rotate(z.p.p)
            else:                                       # explicitly elif z.p == z.p.p.right:
                y = z.p.p.left
                if y.color == 'red':
                    z.p.color = 'black'
                    y.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                elif z == z.p.left:
                    z = z.p
                    self.right_rotate(z)
                else: 
                    z.p.color = 'black'
                    z.p.p.color = 'red'
                    self.left_rotate(z.p.p)
        self.root.color = 'black'
    def inorder_walk(self, tree):
        if tree !=self.nil:
            self.inorder_walk(tree.left)
            print(tree.key, end=" ")
            self.inorder_walk(tree.right)


if __name__=='__main__':
    rbt = RBTree()
    for x in [15,6,18,3,7,17,20,2,4,13,9]:
        x = Node(x)
        rbt.rb_insert(x)
    rbt.inorder_walk(rbt.root)
    print()


# Output:

"""
(15, 'black')
(6, 'red')
(18, 'red')
(3, 'red')
(7, 'red')
(17, 'red')
(20, 'red')
(2, 'red')
(4, 'red')
(13, 'red')
(9, 'black')
2 3 4 6 7 9 13 15 17 18 20 
"""