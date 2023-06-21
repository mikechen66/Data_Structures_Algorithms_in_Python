

# binary_search_tree_classical.py

"""

A binary search tree (BST) is a binary tree where every node in the left subtree is less than the root, 
and every node in the right subtree is of a value greater than the root. The properties of BST are 
recursive: if we consider any node as a root, these properties will remain true. It complies with the 
properties as follows. 

Let x be a node in a binary search tree. 

If y is a node in the left subtree of x, then y.key ≤ x.key. 
If y is a node in the right subtree of x , then y.key ≤ x.key

BST can support the queries MINIMUM, MAXIMUM, SUCCESSOR,and PREDECESSOR and SEARCH. It allows insertion 
and deletion of a node. We have the following descriptions on the methods according to Cormen et el. 

1.Search

The search procedure begins its search at the root and traces a simple path downward in the tree. For each 
node x it encounters, it compares the key k with x.key. If the two keys are equal, the search terminates. 
If k is smaller than x.key, the search continues in the left subtree of x, since the binary-search-tree 
property implies that k cannot reside in the right subtree. Symmetrically, if k is larger than x.key, the 
search continues in the right subtree. 

2.Successor and predecessor

We define the successor of a node as the next node visited in an inorder tree walk. The structure of BST 
allows you to determine the successor of a node without comparing keys. The procedure of processoris 
symmetric to successor. 

3.Insertion

The insert procedure inserts a new node into T as a BST. The procedure takes T and a node z for which z.key 
has already been filled in, z.left = NIL and z.right = NIL. It modifies T and some of theattributes of z so 
as to insert z into an appropriate position in the tree.

4.Deletion

The procedure for deleting a given node z from T takes as arguments' pointers to T and z. It organizes its 
cases as follows. 

1).If z has no left child, then replace z by its right child, which may or may not be NIL. When z's right 
child is NIL, the case deals with the situation in which z has no child. When z’s right child is non-NIL, 
the case handles the situation in which z has just one child, which is its right child.

2).Otherwise, if z has just one child, then the child is a left child, replace z by its left child.

3).Otherwise, z has both a left and a right child. Find z's successor y which lies in z's right subtree 
and has no left child. Splice node y out of its current location and replace z by y in the tree. How to do 
so depends on whether y is z's right child:

(1).If y is z's right child, then replace z by y with leaving y's right child alone.

(2).Otherwise, y lies within z's right subtree but is not z's right child, first replace y by its own right 
child, and then replace z by y.

5.__str__() method: 

The __str__() is a special method in Python classes that is used to define a string representation of an 
object. The method should return a string that provides a human-readable representation of the object’s 
state. This string is used when the object is printed, or when the built-in str() function is called on 
the object. If it is not defined for a class, the interpreter will use the default implementation which 
returns the name of the object’s class and its memory address in the form of hexadecimal representation.

6.Reference :

# https://walkccc.me/CLRS/Chap13/13.2/?continueFlag=f08c6cbaddd3864d16b2bcb5bc1bf11f
# https://sites.math.rutgers.edu/~ajl213/CLRS/CLRS.html
# https://web.stanford.edu/class/cs106b/lectures/23-bst/slides
# https://courses.engr.illinois.edu/cs225/sp2022/resources/bst/
"""


import numpy as np


class KeyObject:
    """Used for testing anything (of string) that requires a key."""
    def __init__(self, string, key):
        self.string = string
        self.key = key
    @staticmethod
    def get_key(x):
        return x.key
    @staticmethod
    def set_key(x, key):
        x.key = key
    def __gt__(self, obj2):
        return self.key > obj2.key
    def __str__(self):
        return self.string


class BSTNode:
    def __init__(self, data):
        # Initialize all instance variables of node to None.
        self.left = None
        self.right = None
        self.p = None
        self.data = data
    def __str__(self):
        # Print data
        return str(self.data)


class BST:
    def __init__(self, key_func=None, nil=None):
        """
        Initialize binary search tree.
        Arguments: 
        key_func: an optional function that returns the key for the objects stored. 
                  May be a static function in the object class. If omitted, then 
                  identity function is used.
        nil: sentinel value for the parent of the root and children of the leaves 
             of the tree.
        """
        if key_func is None:
            self.get_key = lambda x: x
        else:
            self.get_key = key_func
        if nil is None:
            self.nil = BSTNode(None)
        else:
            self.nil = nil   
        self.root = self.nil                             # Initially an empty tree
    def get_root(self):
        return self.root
    # Define a node with a given key k in the subtree rooted at x, or self.nil if no node with key k.
    def search(self, x, k):
        if x == self.nil or k == self.get_key(x.data):
            return x
        elif k < self.get_key(x.data):
            return self.search(x.left, k)                # if present, k must be in left subtree
        else:
            return self.search(x.right, k)               # if present, k must be in right subtree
    def iter_search(self, x, k):
        while x != self.nil and k != self.get_key(x.data):
            if k < self.get_key(x.data):
                x = x.left                               # if present, k must be in the left subtree
            else:
                x = x.right                              # if present, k must be in the right subtree
        return x
    # Define a node in subtree rooted at x with the smallest key.
    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x                                         # return leftmost key
    # Define a node in subtree rooted at x with the largest key.
    def maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x                                         # return rightmost key
    # Define the node in the subtree rooted at x with the smallest key greater than x's key.
    def successor(self, x):
        if x.right != self.nil:
            return self.minimum(x.right)                 # leftmost node in right subtree
        else:        # Find the lowest ancestor of x whose left child is also an ancestor(uncle node) of x.                                          # else (x's right subtree is empty)
            y = x.p                                 # ...y is parent of x 
            while y != self.nil and x == y.right:        # ...while y is not empty and x is y's right child (continue up the tree)
                x = y                              
                y = y.p
        return y  
    # Define the node in the subtree rooted at x with the greatest key less than x's key.  
    def predecessor(self, x):
        if x.left != self.nil:
            return self.maximum(x.left)                  # rightmost node in left subtree
        else:       # Find the lowest ancestor of x whose right child is also an ancestor of x.
            y = x.p 
            while y != self.nil and x == y.left:         # continue up the tree
                x = y
                y = y.p
        return y    
    def tree_insert(self, data):
        z = BSTNode(data)                                # Initialize the BSTNode(data)
        z.right = self.nil                               # Initialize node's left child pointers 
        z.left = self.nil
        self.insert_node(z)
    # Insert node z into this binary search tree.
    def insert_node(self, z):
        x = self.root                                    # node being compared with z
        y = self.nil                                     # y will be the parent of z
        while x != self.nil:                             # descend until reaching a leaf
            y = x
            if self.get_key(z.data) < self.get_key(x.data):
                x = x.left
            else:
                x = x.right
        z.p = y                                          # insert z with parent y
        if y == self.nil:
            self.root = z                                # the tree was empty
        elif self.get_key(z.data) < self.get_key(y.data):
            y.left = z                                   # assign z as y's left child
        else:
            y.right = z                                  # assign z as y's right child
    # Replace the subtree rooted at node u with the subtree rooted at node v
    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v                                # replace the root with v 
        elif u == u.p.left:                              # is u a left child?
            u.p.left = v                                 # update left child to v
        else:                                            # u is a right child
            u.p.right = v                                # update right child to v
        v.p = u.p                                        # update v's parent
    # Delete node z from the BST and maintain its property.
    def tree_delete(self, z):
        if z is None or z == self.nil:
            raise RuntimeError("Cannot delete sentinel or None node.")
        if z.left == self.nil:
            self.transplant(z, z.right)                  # replace z by its right child
        elif z.right == self.nil:
            self.transplant(z, z.left)                   # replace z by its left child
        else:
            y = self.minimum(z.right)                    # y is z's successor
            if y != z.right:                             # is y farther down the tree?
                self.transplant(y, y.right)              # replace y by its right child
                y.right = z.right                        # z's right child becomes y's right child
                y.right.p = y  
            self.transplant(z, y)                        # replace z by its successor y
            y.left = z.left                              # give z's left child to y which had no left child
            y.left.p = y
    # Define a boolean indicating whether this tree obeys the binary search tree properties.
    def is_bst(self, x=None):
        if x is None:                                    # x is root of a subtree with None
            x = self.root
        if x == self.nil:
            return True                                  
        if x.left is not self.nil:                       # check the left subtree
            if self.get_key(x.left.data) > self.get_key(x.data):
                return False                             # left child's key > x's key
            elif not self.is_bst(x.left):                # check the rest of the left subtree
                return False
        if x.right is not self.nil:                      # check the right subtree
            if self.get_key(x.right.data) < self.get_key(x.data):
                return False                             # right child's key < x's key
            elif not self.is_bst(x.right):
                return False                             # check the rest of the right subtree
        return True                                      # no error found in the subtree rooted at x
    def inorder_walk(self, x, func=print):
        """
        Argument: 
            x: a root node of the subtree
            func: a function to run on each node in the subtree; if omitted, print.
        Return: 
            None
        """
        if x != self.nil:
            self.inorder_walk(x.left, func)
            func(x)
            self.inorder_walk(x.right, func)
    # Print a string representing a subtree with nodes of the same depth in the same column.
    def pretty_print(self, node, depth=0):
        """
        Arguments:
            node: root of a subtree to print
            depth: depth of the node within the binary search tree
        Return:
            result for pretty print
        """
        result = ""
        if node == self.nil:
            return result
        if node.right != self.nil:
            result += self.pretty_print(node.right, depth + 1)
        result += ('  ' * depth) + str(node) + '\n'
        if node.left != self.nil:
            result += self.pretty_print(node.left, depth + 1)
        return result
    # Define the method to call pretty_print() method 
    def __str__(self):
        return self.pretty_print(self.root)


# Test case 1. Integer object
if __name__ == "__main__":
    # Insert. 
    binary_tree1 = BST()
    array1 = np.arange(0, 100, 13)
    np.random.shuffle(array1)
    for value in array1:
        binary_tree1.tree_insert(value)
    print(binary_tree1.is_bst())
    print(binary_tree1)
    binary_tree1.inorder_walk(binary_tree1.get_root())
    # Search.
    node39 = binary_tree1.search(binary_tree1.get_root(), 39)
    print("Found:", node39)
    # Unsuccessful search. 
    print("Found:", binary_tree1.search(binary_tree1.get_root(), 55))
    # Iterative. 
    print("Found:", binary_tree1.iter_search(binary_tree1.get_root(), 39))
    print("Found:", binary_tree1.iter_search(binary_tree1.get_root(), 55))
    # Minimum and maximum. 
    print("Max:", binary_tree1.maximum(binary_tree1.get_root()))
    print("Min:", binary_tree1.minimum(binary_tree1.get_root()))
    # Delete. 
    binary_tree1.tree_delete(node39)
    print("After deleting 39: ")
    print(binary_tree1.is_bst())
    print(binary_tree1)
    binary_tree1.inorder_walk(binary_tree1.get_root(), lambda x: print("Node:", x))
    # Delete node that does not exist.
    node100 = BSTNode(100)
    print()


# Output:

"""
True
  91
    78
65
    52
      39
  26
    13
      0

0
13
26
39
52
65
78
91
Found: 39
Found: None
Found: 39
Found: None
Max: 91
Min: 0
After deleting 39: 
True
  91
    78
65
    52
  26
    13
      0

Node: 0
Node: 13
Node: 26
Node: 52
Node: 65
Node: 78
Node: 91
"""

###############################################################################################################################


# Test case 2. list object

if __name__ == "__main__":
    binary_tree2 = BST()
    list1 = [15, 18, 6, 3, 2, 4, 7, 13, 9, 17, 20]
    for value in list1:
        binary_tree2.tree_insert(value)
    print(binary_tree2.is_bst())
    print(binary_tree2)
    binary_tree2.inorder_walk(binary_tree2.get_root())
    # Successor and predecessor.
    print("Successor:", binary_tree2.successor(binary_tree2.get_root()))  # should be 17
    print("Predecessor:", binary_tree2.predecessor(binary_tree2.get_root()))  # should be 13
    print("Successor: ", binary_tree2.successor(binary_tree2.search(binary_tree2.get_root(), 13)))  # should be 15
    print("Predecessor:", binary_tree2.predecessor(binary_tree2.search(binary_tree2.get_root(), 7)))  # should be 6
    # Delete the remaining nodes, one by one.
    array2 = np.array(list1)
    np.random.shuffle(array2)
    for value in array2:
        print("After deleting " + str(value) + ":")
        binary_tree2.tree_delete(binary_tree2.search(binary_tree2.get_root(), value))
        print(binary_tree2.is_bst())
        print(binary_tree2)


# Output:

"""
True
    20
  18
    17
15
      13
        9
    7
  6
      4
    3
      2

2
3
4
6
7
9
13
15
17
18
20
Successor: 17
Predecessor: 13
Successor:  15
Predecessor: 6
After deleting 2:
True
    20
  18
    17
15
      13
        9
    7
  6
      4
    3

After deleting 13:
True
    20
  18
    17
15
      9
    7
  6
      4
    3

After deleting 18:
True
  20
    17
15
      9
    7
  6
      4
    3

After deleting 9:
True
  20
    17
15
    7
  6
      4
    3

After deleting 7:
True
  20
    17
15
  6
      4
    3

After deleting 17:
True
  20
15
  6
      4
    3

After deleting 15:
True
20
  6
      4
    3

After deleting 6:
True
20
    4
  3

After deleting 3:
True
20
  4

After deleting 20:
True
4

After deleting 4:
True
"""

###############################################################################################################################


# Test case 3. String object

if __name__ == "__main__":
    binary_tree3 = BST(KeyObject.get_key)
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "HI", "NH", "NY"]
    list3 = []
    for i in range(len(states)):
        list3.append(KeyObject(states[i], i))
    array3 = np.array(list3)
    np.random.shuffle(array3)
    for x in array3:
        binary_tree3.tree_insert(x)
    print(binary_tree3.is_bst())
    print(binary_tree3)
    # If get_key not provided, must define __gt__ or __lt__ for objects in the BST.
    binary_tree4 = BST()
    for x in array3:
        binary_tree4.tree_insert(x)
    print(binary_tree4)
    print(binary_tree4.is_bst())
    # Binary tree that does not have the BST property.
    binary_tree5 = BST()
    binary_tree5.tree_insert(100)
    new_node = BSTNode(101)
    new_node.left = binary_tree5.nil
    new_node.right = binary_tree5.nil
    binary_tree5.root.left = new_node
    new_node.p = binary_tree5.get_root()
    print(binary_tree5.is_bst())
    print(binary_tree5)
    # Large tree. 
    binary_tree6 = BST()
    array2 = np.arange(-1000, 10000, 1000)
    np.random.shuffle(array2)
    for value in array2:
        binary_tree6.tree_insert(value)
    print(binary_tree6.is_bst())


# Output:

"""
True
      NY
    NH
  HI
    CT
CO
  CA
      AR
        AZ
    AK
      AL

      NY
    NH
  HI
    CT
CO
  CA
      AR
        AZ
    AK
      AL

True
False
100
  101

True
"""