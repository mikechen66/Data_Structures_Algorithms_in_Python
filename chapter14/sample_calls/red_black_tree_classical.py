

# red_black_tree_classical.py

"""

A red-black tree is a binary search tree with one extra bit of storage per node: its color, which can 
be either RED or BLACK . By constraining the node colors on anysimple path from the root to a leaf, 
red-black trees ensure that no such path is more than twice as long as any other, so that the tree is 
approximately balanced.

Each node of the tree now contains the attributes color, key, left, right, and p. If a child or the 
parent of a node does not exist, the corresponding pointer attribute of the node contains the value NIL. 
We shall regard these NIL s as being pointers to leaves (external nodes) of the binary search tree and 
the normal, key-bearing nodes as being internal nodes of the tree.


A red-black tree is a binary tree that satisfies the following red-black properties:

1. Every node is either red or black.
2. The root is black.
3. Every leaf ( NIL ) is black.
4. If a node is red, then both its children are black.
5. For each node, all simple paths from the node to descendant leaves contain the same number of black 
   nodes.

The code is provided according to the pseudocode of Cormen's Introduction to Algorithm
"""


import sys


# Construct Node class
class Node(object):
    def __init__(self, key, color='', parent=None, lchild=None, rchild=None):
        self.key = key
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
        self.color  = color


# Define a RBTree that is a binary seach tree with red and black nodes 
class RBTree(object):
    def __init__(self, root=None):
        self.nil = Node(key=-1, color='BLACK')
        self.root = self.nil
    def left_rotate(self, x):
        y = x.rchild               # set y 
        x.rchild = y.lchild        # turn y's left subtree into x's right subtree
        if y.lchild != self.nil:
            y.lchild.parent = x
        y.parent = x.parent        # link x's parent to y
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.lchild:
            x.parent.lchild = y
        else:
            x.parent.rchild = y
        y.lchild = x               # put x on y's left
        x.parent = y
    def right_rotate(self, y):
        x = y.lchild               # set x
        y.lchild = x.rchild        # turn x's right subtree into y's left subtree
        if x.rchild != self.nil:
            x.rchild.parent = y
        x.parent = y.parent        # link y's parent to x
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.rchild:
            y.parent.rchild = x
        else:
            y.parent.lchild = x
        x.rchild = y               # put y on x's right
        y.parent = x
    def rb_insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x                  # y records the parent node related z node
            if z.key < x.key:      # judge to insert into left or right by comparing key
                x = x.lchild
            else:
                x = x.rchild
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:        # judge whether to insert left or right subtree
            y.lchild = z
        else:
            y.rchild = z
        z.lchild = self.nil
        z.rchild = self.nil
        z.color = 'RED'
    # keep the rb tree's features
    def rb_insert_fixup(self, z):
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.lchild:
                y = z.parent.parent.rchild
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                elif z == z.parent.rchild:
                    z = z.parent
                    self.left_rotate(z)
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                self.right_rotate(z.parent.parent)
            # elif z.parent == z.parent.parent.rchild:
            else: 
                y = z.parent.parent.rchild
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                elif z == z.parent.lchild:
                    z = z.parent
                    self.right_rotate(z)
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                self.left_rotate(z.parent.parent)
            self.root.color = 'BLACK'
    def inorder_walk(self, tree):
        if tree !=self.nil:
            self.inorder_walk(tree.lchild)
            print(tree.key, end=" ")
            self.inorder_walk(tree.rchild)


if __name__=='__main__':
    tree = RBTree()
    for x in [15,6,18,3,7,17,20,2,4,13,9]:
        x = Node(x)
        tree.rb_insert(x)
    tree.inorder_walk(tree.root)
    print()


# Output:

"""
2 3 4 6 7 9 13 15 17 18 20 
"""