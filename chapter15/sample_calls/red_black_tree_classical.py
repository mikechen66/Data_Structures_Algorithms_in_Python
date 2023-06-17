

# red_black_tree_classical.py

"""
Red-Black Tree, invented as symmetric binary B-trees by Rudolf Bayer, modified as Red Black Tree by Leo Guibas and 
Robert Sedgewick. The Cormen red-black tree is based on 2-3 tree (not 2-3-4 tree including 4-nodes) in order to 
simpleify the complexity.  The following script is implemented almost completely based on Introduction to Algorithms 
3rd and 4th edition, Chap 12, 13 and 14 by Cormen et. al in Introduction to Algorithms. 

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

if z.p == z.p.p.left
    ...
    if y.color == RED:     # case 1;
    elif z == z.p.right:   # case 2;
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
    if w.color == RED:                                      case 1;
    elif w.left.color == BLACK and w.right.color == BLACK:  case 2;
    elif w.right.color == BLACK:                            case 3;
    else: (omited in the original book)                     case 4; 
else(same as then clause with "right" and "left" exchanged):
    ...
    (repeated as above)

Please note the above pseducode is a little different with the Python code snippet.

4.Reference :

# https://walkccc.me/CLRS/Chap13/13.2/?continueFlag=f08c6cbaddd3864d16b2bcb5bc1bf11f
# https://sites.math.rutgers.edu/~ajl213/CLRS/CLRS.html
"""


import sys


# Construct Node class
class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.color  = 'BLACK'   


# Define a RBTree that is a binary seach tree
class RBTree(object):
    def __init__(self):
        self.nil = Node(0)
        self.root = self.nil
    def left_rotate(self, x):
        y = x.right                                    # set y 
        x.right = y.left                               # turn y's left subtree into x's right subtree
        if y.left != self.nil:                         # if y's left subtree is not empty...         
            y.left.p = x                               # ...then x becomes the parent of the left subtree
        y.p = x.p                                      # x's parent becomes y’s parent
        if x.p == self.nil:                            # if x was the root...
            self.root = y                              # ...then y becomes the root
        elif x == x.p.left:                            # otherwise, if x was a left child...
            x.p.left = y                               # ...then y becomes a left child
        else:                                          # otherwise
            x.p.right = y                              # ...now y becomes a right child 
        y.left = x                                     # make x become y's left child
        x.p = y                                        # y is x's parent 
    def right_rotate(self, x):                         # swap between left and right of left_rotate()
        y = x.left
        x.left = y.right                               # turn y's right subtree into x's left subtree
        if y.right != self.nil:                        # if y's right subtree is not empty...      
            y.right.p = x                              # ...then x becomes the parent of the right subtree
        y.p = x.p                                      # set y's parent to x's parent
        if x.p == self.nil:                            # if x was the root...
            self.root = y                              # ...set y as root               
        elif x == x.p.right:                           # otherwise, if x was a right child...
            x.p.right = y                              # ...then y becomes a right child
        else:                                          # otherwise, 
            x.p.left = y                               # ...now y becomes a left child 
        y.right = x                                    # make x become y's right child
        x.p = y
    def rb_insert(self, z):
        y = self.nil                                   # y will be parent of z
        x = self.root                                  # node being compared with z(?)
        while x != self.nil:                           # descend until reaching the sentinel(self.nil)
            y = x                                      # y records the p node related z node
            if z.key < x.key:                          # if stmt (judge to insert into left or right by comparing key)
                x = x.left                             # ...then x's left child becomes x 
            else:                                      # otherwise
                x = x.right                            # ...then x's right child becomes x
        z.p = y                                        # y is z's parent now 
        if y == self.nil:                              # if y is root 
            self.root = z                              # ...then z is root 
        elif z.key < y.key:                            # if...(judge whether to insert left or right subtree)
            y.left = z                                 # ...then z is y's left child 
        else:                                          # otherwise
            y.right = z                                # ...then z becomes y's child
        z.left = self.nil                              # z's left child is a sentinel 
        z.right = self.nil                             # z's right child is a sentinel too
        z.color = 'RED'                                # the new node starts out red that may violate its properties
        self.rb_insert_fixup(z)                        # so correct any violations of red-black properties
        return (z.key, z.color)                        # Add return for call 
    def rb_insert_fixup(self, z):                      # keep the rb tree's features
        while z.p.color == 'RED':
            if z.p == z.p.p.left:                      # if z's parent is a left child?
                y = z.p.p.right                        # ...then y is z's uncle node 
                if y.color == 'RED':                   # case 1: if y's color is RED
                    z.p.color = 'BLACK'                # ...then z's parent is BLACK
                    y.color = 'BLACK'                  # ...y's color is BLACK
                    z.p.p.color = 'RED'                # ...z's grandparent is RED
                    z = z.p.p                          # ...z's grandparent is z now 
                elif z == z.p.right:                   # case 2: if z is a right child 
                    z = z.p                            # ...then z's parent is z 
                    self.left_rotate(z)                # ...perform z's left rotation 
                else:                                  # case 3: else 
                    z.p.color = 'BLACK'                # ...color z's parent as BLACK
                    z.p.p.color = 'RED'                # ...color z's grandparent as RED
                    self.right_rotate(z.p.p)           # ...perform z.p.p's right rotation
            else:                                      # else (correspond to the above first-level if):
                y = z.p.p.right                        # ...z's grandparent is y 
                if y.color == 'RED':                   # case 1
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                elif z == z.p.left:                    # case 2
                    z = z.p
                    self.right_rotate(z)
                else:                                  # case 3 
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.left_rotate(z.p.p)
        self.root.color = 'BLACK'                      # After ending the while loop, root is set as BLACK
    def rb_transplant(self, u, v):
        if u.p == self.nil:                            # if u's parent is root'
            self.root = v                              # ...then set v is root
        elif u == u.p.left:                            # else if u is the left child of u's parent
            u.p.left = v                               # ...then v is the left child of u's parent
        else:                                          # else
            u.p.right = v                              # ...v is the right child of u's parent
        v.p = u.p                                      # set v and u has same parent 
    def tree_minimum(self, x):
        while x.left != self.nil:                      # while x's left child is not root
            x = x.left                                 # ... set x's left child as x 
        return x
    def rb_delete(self, z):
        y = z
        y_original_color = y.color                     # y's orginal color is y's color 
        if z.left == self.nil:                         # if z has no left child 
            x = z.right                                # ...now x is z's right child
            self.rb_transplant(z, z.right)             # ...replace z by its right child
        elif z.right == self.nil:                      # else if z has no right child
            x = z.left                                 # ... now x is z's left child
            self.rb_transplant(z, z.left)              # ...replace z by its left child
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right                                # x is y's right child now 
            if y.p == z:                               # if y's parent is z
                x.p = y                                # ...then set x's parent to y 
            else:                                      # else
                self.rb_transplant(y, y.right)         # ...replace z by its right child
                y.right = z.right                      # ...set y's right child to z's right child
                y.right.p = y                          # ...set y's right child's parent to y
            self.rb_transplant(z, y)                   # replace z by its right child y
            y.left = z.left                            # set z's left child to y's left child
            y.left.p = y                               # set y's left child's parent to y
            y.color = z.color                          # y and z has same color 
        if y_original_color == 'BLACK':                # if any red-black violations occurred
            self.rb_delete_fixup(x)                    # ...correct them to keep the red-black properties 
        return (z.key, z.color)
    def rb_delete_fixup(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.p.left:                          # if x is x's parent left child 
                w = x.p.right                          # ...then w is x's right sibling
                if w.color == 'RED':                   # Case 1: 
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.left_rotate(x.p)
                    w = x.p.right                      #...x's parent right child 
                elif w.left.color == 'BLACK' and \
                        w.right.color == 'BLACK':      # case 2
                    w.color = 'RED'
                    x = x.p
                elif w.right.color == 'BLACK':         # case 3
                    w.left.color = 'BLACK'
                    w.color = 'RED'
                    self.right_rotate(w)
                    w = x.p.right                      # ...w now becomes the right child of x's parent
                else:                                  # case 4
                    w.color = x.p.color
                    x.p.color == 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(x.p)
                    x = self.root
            else:                                      # else: same as above if stmt but with right and left exchanged                                               
                w = x.p.left                           # w now becomes the left child of x's parent
                if w.color == 'RED':                   # case 1
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.right_rotate(x.p)
                    w = x.p.left                       # ...w now becomes the left child of x's parent                       
                elif w.left.color == 'BLACK' and \
                        w.right.color == 'BLACK':      # case 2
                    w.color = 'RED'
                    x = x.p
                elif w.left.color == 'BLACK':          # case 3
                    w.right.color = 'BLACK'
                    w.color = 'RED'
                    self.left_rotate(w)
                    w = x.p.left                       # ...w now becomes the left child of x's parent 
                else:                                  # case 4  
                    w.color = x.p.color
                    x.p.color == 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(x.p)
                    x = self.root                      # x now is root 
        x.color = 'BLACK'                              # set x as BLACK 
    def inorder_walk(self, tree):
        if tree != self.nil:
            self.inorder_walk(tree.left)
            print(tree.key, end=" ")
            self.inorder_walk(tree.right)


if __name__=='__main__':
    rbt = RBTree()
    for x in [15,6,18,3,7,17,20,2,4,13,9]:
        x = Node(x)
        rbt.rb_insert(x)
    rbt.inorder_walk(rbt.root)
    # Can not input specific number such as rbt.rb_delete(7) but rbt.root
    rbt.rb_delete(rbt.root)
    rbt.inorder_walk(rbt.root)
    print()


# Output:

"""
(15, 'BLACK')
(6, 'RED')
(18, 'RED')
(3, 'RED')
(7, 'RED')
(17, 'RED')
(20, 'RED')
(2, 'RED')
(4, 'RED')
(13, 'RED')
(9, 'RED')
2 3 4 6 7 9 13 15 17 18 20 (7, 'BLACK')
2 3 4 6 9 13 15 17 18 20 
"""

##############################################################################################################################


# Call the same RBTree() as above 

if __name__=='__main__':
    nodes = [11,2,14,1,7,15,5,8,4]
    rbt = RBTree()
    for node in nodes:
        print('Insert data', rbt.rb_insert(Node(node)))
    print('inorder traversal')
    rbt.inorder_walk(rbt.root)
    rbt.rb_delete(rbt.root)
    print('inorder traversal')
    rbt.inorder_walk(rbt.root)
    rbt.rb_delete(rbt.root)
    print('inorder traversal')
    rbt.inorder_walk(rbt.root)
    print()


"""
Insert data (11, 'BLACK')
Insert data (2, 'RED')
Insert data (14, 'RED')
Insert data (1, 'RED')
Insert data (7, 'RED')
Insert data (15, 'RED')
Insert data (5, 'RED')
Insert data (8, 'RED')
Insert data (4, 'RED')
inorder traversal
1 2 4 5 7 8 11 14 15 (7, 'BLACK')
inorder traversal
1 2 4 5 8 11 14 15 (8, 'BLACK')
inorder traversal
1 2 4 5 11 14 15
"""