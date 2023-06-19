

# red_black_tree.py


"""
Red-Black Tree, invented as symmetric binary B-trees by Rudolf Bayer, modified as Red Black Tree by Leo Guibas and 
Robert Sedgewick. The following script is implemented almost completely based on Introduction to Algorithms 3rd and 
4th edition, Chap 13 and 14 by Cormen et. al in Introduction to Algorithms. However, users can't call the Cormen's
classical code with inserting or deleting number explicitly, so the script has the features as follows. 

-- # 1(red) for True and 0(black) for False with self.colored;
-- Add Node() into the rb_insert() and modify the code in rb_insert_fixup() accordingly;
-- Add node parameter into rb_delete() in order to directly write an related argument for calling. In addoition,
   add delete_node() to call rb_delete();
-- Add get_root(), search(), iter_search() for richer effects. 
-- Add some utility methods such as is_bst(), is_pretty_print() and __str__() for judgement and printing

0. Conception:

A red-black tree is a weak-balanced binary search tree that has five attributes including color, key, left, right 
and p (parent). It basically has the functions including search(), predecesor(),successor(), minimum(), maximum(), 
insert() and insert(). It satisfies the following red-black properties:

1). Every node is either red or black.
2). The root is black.
3). Every leaf (nil) is black.
4). If a node is red, then both its children are black.
5). For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.


1.Rotation

1).left_rotate: 

The following three links is marked by double lines are altered. This check is not in the book but needed to avoid. 
With regard to code, swaping between x and y is equivalent to swaping between left and right (for left and right 
rotation). Please see the weblink as follows. 

2).right_rotate: 

The following three links marked by double lines are altered. It is the reverse process of the following left 
rotation. With regard to code(not pseducode), swaping between x and y is equivalent to swaping between left and 
right(for right and left rotation). 

The other Left-Right and Right-Left Rotation is the combination of the above two basic rotations. 

2.Insertion

1).Insertion and Coloring

Insert a node z into the tree T as if it were an ordinary binary search tree, and then color z red.

2).rb_insert_fixup

To enable the tree's properties are preserved, we call an auxiliary procedure rb_insert_FIXUP to re-color nodes 
and perform rotations. It has three cases(or scenarios) whitin its if..esle stmt of while loop pseducode:

if z.p == z.p.p.left       # BLACK as 0 and RED as 1 
    ...
    if y.colored:          # case 1;
    elif z == z.p.left:    # case 2;
    else:                  # case 3;
else(same as then clause with "right" and "left" exchanged):
    ...                    

Please note many red-black tree implementations do not strickly apply with the above rule in the else clause("right" 
and "left" exchanged). Also applied code has a varation on the if..else stmt. 

3.Deletion

The procedure for deleting a node from a red-black tree is based on the TREE_DELETE procedure (Section 12.3). 

1).rb_transplant

Because deleting a node need a process of transplanting, we customize the RB_Transplant subroutine in assisting 
TREE_DELETE implementation. 

2).tree_delete 

While deleting a node z, there are three scenarios including z has no child node, one child node or two children 
nodes. Each scenarios need different treatments that rely on a auxiliary procedure rb_delete_FIXUP. 

3).rb_delete_fixup

rb_delete_FIXUP restore the red-black properties with changing colors and performing rotations. It restores No.1, 
No.2 and No.4 properties mentioned in the above conception. It has 4 cases (or scenarios) within its while loop 
pseducode as follows.

if x == x.p.left:
    ...
    if w.colored:                                       # case 1;
    elif not w.left.colored and not w.right.colored:    # case 2;
    elif not w.right.colored:                           # case 3;
    else: (omited in the original book)                 # case 4; 
else(same as above with "right" and "left" exchanged):
    ...
    (repeated as above)

Please note the above pseducode is a little different with the Python code snippet.

4.Reference :

# https://walkccc.me/CLRS/Chap13/13.2/?continueFlag=f08c6cbaddd3864d16b2bcb5bc1bf11f
# https://sites.math.rutgers.edu/~ajl213/CLRS/CLRS.html
"""


import numpy as np


class KeyObject:
    """Used for testing anything that requires a key."""
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


class Node:
    def __init__(self, data):
        # Initialize the Node and add a color attribute.
        self.left = None
        self.right = None
        self.p = None
        self.data = data
        self.colored = True                            # 1(red) as colored and 0(black) for False
    def __str__(self):
        # Return <data>: <color>.
        return str(self.data) + ": " + ("red" if self.colored else "black")


class RBTree:
    """contain the same number of black nodes."""
    def __init__(self, key_func=None, nil=None):
        """
        Initialize this RBTree with asentinel that is a Node.
        Arguments: 
        key_func: an optional function that returns the key for the objects stored.  
                  If omitted, then identity function is used.
        nil: sentinel for the p of the root and children of the leaves of tree. 
        """
        if key_func is None:
            self.get_key = lambda x: x
        else:
            self.get_key = key_func
        if nil is None:
            self.nil = Node(None)
        else:
            self.nil = nil 
        self.root = self.nil
        self.nil.colored = False                         # the root must be black
    def get_root(self):
        return self.root
    # Return a node with a given key k in the subtree rooted at x, or self.nil if no node with key k exists.
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
    # Return a node in subtree rooted at x with the smallest key.
    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node                                      # leftmost key
    # Return a node in subtree rooted at x with the largest key.
    def maximum(self, node):
        while node.left != self.nil:
            node = node.left
        return node                                      # rightmost key
    # Code for left rotate
    def left_rotate(self, x):
        y = x.right                                      # y = Right child of x
        x.right = y.left                                 # Change right child of x to left child of y
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p                                        # Change p of y as p of x
        if x.p == self.nil:                              # If p of x == None ie. root node
            self.root = y                                # Set y as root
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
    # Code for right rotate
    def right_rotate(self, x):
        y = x.left                                       # Y = Left child of x
        x.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p                                        # Change p of y as p of x
        if x.p == self.nil:                              # If x is root node
            self.root = y                                # Set y as root
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
    def tree_insert(self, data):
        self.insert_node(Node(data))                     # defaults to red
    def insert_node(self, z):
        x = self.root                                    # node being compared with z
        y = self.nil                                     # y will be the p of z
        while x != self.nil:                             # descend until reaching a leaf
            y = x
            if self.get_key(z.data) < self.get_key(x.data): 
                x = x.left
            else:
                x = x.right
        z.p = y                                          # found the location -- insert z with p y
        if y == self.nil:
            self.root = z                                # tree was empty
        elif self.get_key(z.data) < self.get_key(y.data):
            y.left = z                                   # assign z as y's left child
        else:
            y.right = z                                  # assign z as y's right child
        z.right = self.nil
        z.left = self.nil
        self.rb_insert_fixup(z)                          # correct any violations of red-black properties
    # Fix up the insertion features
    def rb_insert_fixup(self, z):
        while z.p.colored:                               # two reds in a row
            if z.p == z.p.p.left:                        # is z's p a left child?
                y = z.p.p.right                          # y is z's uncle
                if y.colored:                            # Case 1: z's uncle y is red.
                    z.p.colored = False                  # ...color z's p black
                    y.colored = False                    # ...color z's uncle black
                    z.p.p.colored = True                 # ....color z's grandparent red
                    z = z.p.p                            # ...continue from z's grandp
                elif z == z.p.right:                     # Case 2: z's uncle y is black
                        z = z.p
                        self.left_rotate(z)              # ...z is now a left child
                else:                                    # Case 3: z is a left child
                    z.p.colored = False
                    z.p.p.colored = True 
                    self.right_rotate(z.p.p)             # ...right rotation(no consecutive red node)
            else:                                        # z's p is a right child
                y = z.p.p.left                           # y is z's uncle
                if y.colored:                            # Case 1: z's uncle y is red.
                    z.p.colored = False                  # ...color z's p black
                    y.colored = False                    # ...color z's uncle black
                    z.p.p.colored = True                 # ...color z's grandparent red
                    z = z.p.p                            # continue from z's grandp
                elif z == z.p.left:                      # Case 2: z is a left child
                        z = z.p
                        self.right_rotate(z)             # ...z is now a right child
                else:                                    # Case 3: z is a right child
                    z.p.colored = False
                    z.p.p.colored = True
                    self.left_rotate(z.p.p)              # ...no consecutive red node
        self.root.colored = False                        # restore the root as black
    # Replace the subtree rooted at node u with the subtree rooted at node v
    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v                                # replacing the root
        elif u == u.p.left:                              # is u a left child?
            u.p.left = v                                 # update left child to v
        else:                                            # u is a right child
            u.p.right = v                                # update right child to v
        v.p = u.p                                        # update v's parent
    # Delete z and maintain the red-black tree, assume node z exists in the tree.
    def tree_delete(self, z):
        if z is None or z == self.nil:
            raise RuntimeError("Cannot delete sentinel or None node.")
        y = z                                            # y is the node either removed from the tree or moved within the tree.
        y_original_color = y.colored
        if z.left == self.nil:                           # z has no left child
            x = z.right                                  # ...x will move into y's position
            self.transplant(z, z.right)                  # ...replace z by its right child
        elif z.right == self.nil:                        # z has a left child, but no right child
            x = z.left                                   # ...x will move into y's position.
            self.transplant(z, z.left)                   # ...replace z by its left child
        else:                                            # if two children
            y = self.minimum(z.right)                    # ...y is z's successor
            y_original_color = y.colored
            x = y.right
            if y != z.right:                             # is y farther down the tree?
                self.transplant(y, y.right)              # ...replace y by its right child
                y.right = z.right                        # ...z's right child becomes y's right child
                y.right.p = y
            else:
                x.p = y                                  # in case x is self.nil
            self.transplant(z, y)                        # replace z by its successor y
            y.left = z.left                              # give z's left child to y, which had no left child
            y.left.p = y
            y.colored = z.colored                        # give y same color as z
        if not y_original_color:
            self.rb_delete_fixup(x)                      # If any red-black violations occurred, correct them.
    # Maintain the red-black properties after deletion. 
    def rb_delete_fixup(self, x):
        # Argument: x is the node that moved into the deleted position
        while x != self.root and not x.colored:          # x is "doubly black."
            if x == x.p.left:                            # is x a left child?
                w = x.p.right                            # w is x's sibling
                if w.colored:                            # Case 1: x's sibling w is red.
                    w.colored = False
                    x.p.colored = True
                    self.left_rotate(x.p)
                    w = x.p.right                        # transform to case 2, 3, or 4
                elif not w.left.colored and not w.right.colored: # Case 2: x's sibling w is black, and both of w's children are black.
                    w.colored = True
                    x = x.p                              # the extra black moves up one level
                elif not w.right.colored:                # Case 3: x's sibling w is black 
                        w.left.colored = False
                        w.colored = True
                        self.right_rotate(w)
                        w = x.p.right                    # ...transform to case 4
                else:                                    # Case 4: x's sibling w is black, and w's right child is red.
                    w.colored = x.p.colored
                    x.p.colored = False
                    w.right.colored = False
                    self.left_rotate(x.p)
                    x = self.root                        # ...the loop terminates upon the next condition test
            else:                                        # x is a right child
                w = x.p.left                             # w is x's sibling
                if w.colored:                            # Case 1: x's sibling w is red.
                    w.colored = False
                    x.p.colored = True
                    self.right_rotate(x.p)
                    w = x.p.left                         # ...transform to case 2, 3, or 4
                elif not w.right.colored and not w.left.colored: # Case 2: x's sibling w is black
                    w.colored = True
                    x = x.p                              # ...the extra black moves up one level
                elif not w.left.colored:                 # Case 3: x's sibling w is black, w's left child is red, 
                        w.right.colored = False
                        w.colored = True
                        self.left_rotate(w)
                        w = x.p.left                     # ...transform to case 4
                else:                                    # Case 4: x's sibling w is black, and w's right child is red.
                    w.colored = x.p.colored
                    x.p.colored = False
                    w.left.colored = False
                    self.right_rotate(x.p)
                    x = self.root                        # the loop terminates upon the next condition test
        x.colored = False                                # ensure that the root is black
    # Return a boolean indicating whether this tree obeys the binary search tree properties.
    def is_bst(self, x=None):
        # x: root of a subtree.  None indicates root of the entire RBTree.
        if x is None:
            x = self.root
        if x == self.nil:
            return True                                  # for an empty RBTree
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
    # Return a boolean indicating whether the tree is a legal red-black tree.
    def is_rb_tree(self):
        if not RBTree.is_bst(self):
            return False
        if self.root.colored or self.nil.colored:        # The root and sentinel should be black.
            return False
        return self.is_rb_subtree(self.root) != -1
    # Determines whether a subtree of a red-black tree has valid black-heights and no two red nodes in a row.
    def is_rb_subtree(self, x):
        """
        Argument:
        x: root of the subtree
        Returns:
          -1 for invalid red black tree
          black height for valid red black tree
        """
        if x == self.nil:
            return 0
        if x.colored and x.p.colored:
            return -1  # two red nodes in a row
        left_black_height = self.is_rb_subtree(x.left)
        right_black_height = self.is_rb_subtree(x.right)
        if left_black_height == -1 or right_black_height == -1 or left_black_height != right_black_height:
            return -1
        else:
            return left_black_height + int(not x.colored) # Increase the black-height if x is black.
    def inorder_tree_walk(self, x, func=print):
        """
        Argument:
        x: root of the subtree
        func: function to run on each node in the subtree.  If omitted, print.
        Return: None
        """
        if x != self.nil:
            self.inorder_tree_walk(x.left, func)
            func(x)
            self.inorder_tree_walk(x.right, func)
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
        result += ('  ' * depth) + str(node) + '\n'        # print this node
        if node.left != self.nil:
            result += self.pretty_print(node.left, depth + 1)
        return result
    # Return pretty_print
    def __str__(self):
        return self.pretty_print(self.root)


# Testing
if __name__ == "__main__":
    # Insert. 
    rb_tree1 = RBTree()
    array1 = np.arange(0, 100, 13)
    np.random.shuffle(array1)
    for value in array1:
        rb_tree1.tree_insert(value)
    print(rb_tree1.is_rb_tree())
    print(rb_tree1)
    rb_tree1.inorder_tree_walk(rb_tree1.get_root())
    # Search.
    node39 = rb_tree1.search(rb_tree1.get_root(), 39)
    print("Found: " + str(node39))
    # Unsuccessful search. 
    print("Found: " + str(rb_tree1.search(rb_tree1.get_root(), 55)))
    # Iterative. 
    print("Found: " 
        + str(rb_tree1.iter_search(rb_tree1.get_root(), 39)))
    print("Found: " 
        + str(rb_tree1.iter_search(rb_tree1.get_root(), 55)))
    # Minimum and maximum. 
    print("Max: " + str(rb_tree1.maximum(rb_tree1.get_root()))) 
    print("Min: " + str(rb_tree1.minimum(rb_tree1.get_root()))) 
    # Delete. 
    rb_tree1.tree_delete(node39)
    print("After deleting 39: ")
    print(rb_tree1.is_rb_tree())
    print(rb_tree1)
    node52 = rb_tree1.search(rb_tree1.get_root(), 52)
    rb_tree1.tree_delete(node52)
    print("After deleting 52: ")
    print(rb_tree1.is_rb_tree())
    print(rb_tree1)
    rb_tree1.inorder_tree_walk(rb_tree1.get_root())
    # Delete a node that does not exist.
    node99 = rb_tree1.search(rb_tree1.get_root(), 99)
    try:
        rb_tree1.tree_delete(node99)
    except RuntimeError as e:
        print(e)
    print(rb_tree1.is_rb_tree())
    print(rb_tree1)
    # Tree with objects. 
    rb_tree2 = RBTree(KeyObject.get_key)
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "HI", "NH", "NY"]
    list2 = []
    for i in range(len(states)):
        list2.append(KeyObject(states[i], i))
    array2 = np.array(list2)
    np.random.shuffle(array2)
    for x in array2:
        rb_tree2.tree_insert(x)
    print(rb_tree2.is_rb_tree())
    print(rb_tree2)
    nodeCO = rb_tree2.search(rb_tree2.get_root(), 5)
    rb_tree2.tree_delete(nodeCO)
    print("After deleting CO:")
    print(rb_tree2.is_rb_tree())
    print(rb_tree2)
    # Check that is_rb_tree works correctly by making a black node turn red.
    for x in array2:
        # Find a non-root black node.
        node = rb_tree2.search(rb_tree2.get_root(), KeyObject.get_key(x))
        if not node.colored and node != rb_tree2.get_root():
            break
    node.colored = True
    print(rb_tree2.is_rb_tree())
    # Restore blackness to that node, but make two reds in a row.
    node.colored = False
    for x in array2:
        node = rb_tree2.search(rb_tree2.get_root(), KeyObject.get_key(x))
        if node.colored:
            break
    node.p.colored = True
    print(rb_tree2.is_rb_tree())
    # Restore blackness, but make the root red.
    node.p.colored = False
    rb_tree2.get_root().colored = True
    print(rb_tree2.is_rb_tree())
    # Make the root black but the sentinel red.
    rb_tree2.get_root().colored = False
    rb_tree2.nil.colored = True
    print(rb_tree2.is_rb_tree())
    # Exhaustive testing.
    rb_tree3 = RBTree()
    array2 = np.arange(-100, 1000)
    np.random.shuffle(array2)
    for value in array2:
        rb_tree3.tree_insert(value)  # Covers every insert fixup case.
        if not rb_tree3.is_rb_tree():
            print(rb_tree3)
            break
    print(rb_tree3.is_rb_tree())
    np.random.shuffle(array2)
    for value in array2:
        to_delete = rb_tree3.search(rb_tree3.get_root(), value)
        rb_tree3.tree_delete(to_delete)
        if not rb_tree3.is_rb_tree():
            print(rb_tree3)
            break
    print(rb_tree3.is_rb_tree())




# Output:

"""
True
  91: black
78: black
      65: red
    52: black
      39: red
  26: red
    13: black
      0: red

0: red
13: black
26: red
39: red
52: black
65: red
78: black
91: black
Found: 39: red
Found: None: black
Found: 39: red
Found: None: black
Max: 0: red
Min: 0: red
After deleting 39: 
True
  91: black
78: black
      65: red
    52: black
  26: red
    13: black
      0: red

After deleting 52: 
True
  91: black
78: black
    65: black
  26: red
    13: black
      0: red

0: red
13: black
26: red
65: black
78: black
91: black
Cannot delete sentinel or None node.
True
  91: black
78: black
    65: black
  26: red
    13: black
      0: red

True
      NY: red
    NH: black
      HI: red
  CT: red
    CO: black
CA: black
    AR: black
      AZ: red
  AK: red
    AL: black

After deleting CO:
True
    NY: black
  NH: red
      HI: red
    CT: black
CA: black
    AR: black
      AZ: red
  AK: red
    AL: black

False
False
False
False

True
True
"""