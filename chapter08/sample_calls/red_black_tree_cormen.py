

# red_black_tree_cormen.py


"""
Red-Black Tree, invented as symmetric binary B-trees by Rudolf Bayer, modified as Red Black Tree
by Leo Guibas and Robert Sedgewick. The following script is implemented almost completely based 
on Introduction to Algorithms 3rd Ed., Chap 12, 13 and 14 by Cormen et. al in Introduction to 
Algorithms. 

0. Conception:

A red-black tree is a weak-balanced binary search tree that has five attributes including color, 
key, left, right and p (parent). It basically has the functions including search(), predecesor(),
successor(), minimum(), maximum(), insert() and insert(). It satisfies the following red-black 
properties:

1). Every node is either red or black.
2). The root is black.
3). Every leaf (nil) is black.
4). If a node is red, then both its children are black.
5). For each node, all simple paths from the node to descendant leaves contain the same number of 
    black nodes.

1.Rotation

1).left_rotate: 

The following three links is marked by double lines are altered. This check is not in the book 
but needed to avoid. With regard to code, swaping between x and y is equivalent to swaping 
between left and right (for left and right rotation). Please see the weblink as follows. 

2).right_rotate: 

The following three links marked by double lines are altered. It is the reverse process of 
the following left rotation. With regard to code(not pseducode), swaping between x and y is 
equivalent to swaping between left and right(for right and left rotation). 

The other Left-Right and Right-Left Rotation is the combination of the above two basic rotations. 

2.Insertion

1).Insertion and Coloring

Insert a node z into the tree T as if it were an ordinary binary search tree, and then color z 
red.

2).rb_insert_fixup

To enable the tree's properties are preserved, we call an auxiliary procedure rb_insert_FIXUP 
to re-color nodes and perform rotations. It has three cases(or scenarios) whitin its if..esle
stmt of while loop pseducode:

if z.p == z.p.p.left
    ...
    if y.color == RED:     # case 1;
    elif z == z.p.right:   # case 2;
    else:                  # case 3;
else(same as then clause with "right" and "left" exchanged):
    ...                    

Please note many red-black tree implementations do not strickly apply with the above rule in
the else clause("right" and "left" exchanged). Also applied code has a varation on the 
if..else stmt. 

3.Deletion

The procedure for deleting a node from a red-black tree is based on the TREE_DELETE procedure 
(Section 12.3). 

1).rb_transplant

Because deleting a node need a process of transplanting, we customize the RB_Transplant subroutine 
in assisting TREE_DELETE implementation. 

2).tree_delete 

While deleting a node z, there are three scenarios including z has no child node, one child node 
or two children nodes. Each scenarios need different treatments that rely on a auxiliary procedure 
rb_delete_FIXUP. 

3).rb_delete_fixup

rb_delete_FIXUP restore the red-black properties with changing colors and performing rotations. 
It restores No.1, No.2 and No.4 properties mentioned in the above conception. It has 4 cases
(or scenarios) within its while loop pseducode as follows.

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
    def rb_transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p
    def rb_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 'black':
            self.rb_delete_fixup(x)
    def rb_delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.p.left:
                w = x.p.right
                if w.color == 'red':                    # case 1
                    w.color = 'black'
                    x.p.color = 'red'
                    self.left_rotate(x.p)
                    w = x.p.right
                elif w.left.color == 'black' and \
                        w.right.color == 'black':       # case 2
                    w.color = 'red'
                    x = x.p
                elif w.right.color == 'black':          # case 3
                    w.left.color = 'black'
                    w.color = 'red'
                    self.right_rotate(w)
                    w = x.p.right
                else:                                   # case 4 
                    w.color = x.p.color
                    x.p.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == 'red':
                    w.color = 'black'
                    x.p.color = 'red'
                    self.right_rotate(x.p)
                    w = x.p.left
                elif w.left.color == 'black' and \
                        w.right.color == 'black':
                    w.color = 'red'
                    x = x.p
                elif w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.p.left
                else: 
                    w.color = x.p.color
                    x.p.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.p)
                    x = self.root
        x.color = 'black'
    def tree_minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x
    def inorder(self, x):
        if x != None:
            self.inorder(x.left)
            if x.key != 0:
                print('key:', x.key, 'x.p', x.p.key)
            self.inorder(x.right)


if __name__=='__main__':
    nodes = [11,2,14,1,7,15,5,8,4]
    rbt = RBTree()
    for node in nodes:
        print('Insert data', rbt.rb_insert(Node(node)))
    print('inorder traversal')
    rbt.inorder(rbt.root)
    rbt.rb_delete(rbt.root)
    print('inorder traversal')
    rbt.inorder(rbt.root)
    rbt.rb_delete(rbt.root)
    print('inorder traversal')
    rbt.inorder(rbt.root)


# Output:


"""
Insert data (11, 'black')
Insert data (2, 'red')
Insert data (14, 'red')
Insert data (1, 'red')
Insert data (7, 'red')
Insert data (15, 'red')
Insert data (5, 'red')
Insert data (8, 'red')
Insert data (4, 'red')
inorder traversal
key: 1 x.p 2
key: 2 x.p 7
key: 4 x.p 5
key: 5 x.p 2
key: 7 x.p 0
key: 8 x.p 11
key: 11 x.p 7
key: 14 x.p 11
key: 15 x.p 14
inorder traversal
key: 1 x.p 2
key: 2 x.p 8
key: 4 x.p 5
key: 5 x.p 2
key: 8 x.p 0
key: 11 x.p 14
key: 14 x.p 8
key: 15 x.p 14
inorder traversal
key: 1 x.p 2
key: 2 x.p 11
key: 4 x.p 5
key: 5 x.p 2
key: 11 x.p 0
key: 14 x.p 11
key: 15 x.p 14

"""
#--------------------------------------------------------------------------------------------


# Reuse the above RBTree class 


if __name__=='__main__':
    rbt = RBTree()
    for x in [15,6,18,3,7,17,20,2,4,13,9]:
        x = Node(x)
        rbt.rb_insert(x)
    rbt.inorder(rbt.root)
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
key: 2 x.p 3
key: 3 x.p 6
key: 4 x.p 3
key: 6 x.p 15
key: 7 x.p 9
key: 9 x.p 6
key: 13 x.p 9
key: 15 x.p 0
key: 17 x.p 18
key: 18 x.p 15
key: 20 x.p 18


"""