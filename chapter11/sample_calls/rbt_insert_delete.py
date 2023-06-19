

# rbt_insert_delete.py


"""
Red-Black Tree, invented as symmetric binary B-trees by Rudolf Bayer, modified as Red Black Tree by Leo Guibas and 
Robert Sedgewick. The following script is implemented almost completely based on Introduction to Algorithms 3rd and 
4th edition, Chap 13 and 14 by Cormen et. al in Introduction to Algorithms. However, users can't call the Cormen's
classical code with inserting or deleting number explicitly, so the script has the features as follows. 

-- To set RED as 1 and BLACK with the original Cormen's 'RED' and 'BLACK';
-- Add Node() into the rb_insert() and modify the code in rb_insert_fixup() accordingly;
-- Add node parameter into rb_delete() in order to directly write an related argument for calling. In addoition,
   add delete_node() to call rb_delete();

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
    if y.color == 1:       # case 1;
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
    if w.color == 1:                                    # case 1;
    elif w.left.color == 0 and w.right.color == 0:      # case 2;
    elif w.right.color == 0:                            # case 3;
    else: (omited in the original book)                 # case 4; 
else(same as above with "right" and "left" exchanged):
    ...
    (repeated as above)

Please note the above pseducode is a little different with the Python code snippet.

4.Reference :

# https://walkccc.me/CLRS/Chap13/13.2/?continueFlag=f08c6cbaddd3864d16b2bcb5bc1bf11f
# https://sites.math.rutgers.edu/~ajl213/CLRS/CLRS.html
"""


# Define Node
class Node():
    def __init__(self, val):
        self.val = val                                   # Value of Node
        self.p = None                                    # p of Node
        self.left = None                                 # Left Child of Node
        self.right = None                                # Right Child of Node
        self.color = 1                                   # Red Node as new node is always inserted as Red Node


# Define the red black Ttree
class RBTree():
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = 0
        # self.nil.left = None
        self.nil.left = self.nil
        # self.nil.right = None
        self.nil.right = self.nil
        self.root = self.nil
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
    # Insert New Node
    def rb_insert(self, key):
        node = Node(key)
        node.p = self.nil 
        node.val = key
        y = self.nil                                    # y will be parent of z
        x = self.root                                   # node being compared with z(?)
        while x != self.nil:                            # descend until reaching the sentinel(self.nil)
            y = x                                       # y records the p node related z node
            if node.val < x.val:                        # if stmt (judge to insert into left or right by comparing key)
                x = x.left                              # ...then x's left child becomes x 
            else:                                       # otherwise
                x = x.right                             # ...then x's right child becomes x
        node.p = y                                      # y is z's parent now 
        if y == self.nil:                               # if y is root 
            self.root = node                            # ...then z is root 
        elif node.val < y.val:                          # if...(judge whether to insert left or right subtree)
            y.left = node                               # ...then z is y's left child 
        else:                                           # otherwise
            y.right = node                              # ...then z becomes y's child
        node.left = self.nil                            # z's left child is a sentinel 
        node.right = self.nil                           # z's right child is a sentinel too
        node.color = 1                                  # the new node starts out red that may violate its properties
        self.rb_insert_fixup(node)                      # so correct any violations of red-black properties
    # Fix Up Insertion
    def rb_insert_fixup(self, z):                       # keep the rb tree's features
        while z.p.color == 1:                           # While p is red
            if z.p == z.p.p.right:                      # if z's parent is a right child?                      
                y = z.p.p.left                          # ...then y is z's uncle node 
                if y.color == 1:                        # case 1: if y's color is RED
                    y.color = 0                         # ...y's color is BLACK
                    z.p.color = 0                       # ...then z's parent is BLACK
                    z.p.p.color = 1                     # ...z's grandparent is RED
                    z = z.p.p                           # ...z's grandparent is z now 
                elif z == z.p.left:                     # case 2: if z is a left child  
                    z = z.p                             # ...then z's parent is z                
                    self.right_rotate(z)                # ...perform z's right rotation
                else:                                   # case 3: else 
                    z.p.color = 0                       # ...color z's parent as BLACK
                    z.p.p.color = 1                     # ...color z's grandparent as RED
                    self.left_rotate(z.p.p)             #  ...perform z.p.p's left rotation
            else:                                       # else (correspond to the above first-level if):
                y = z.p.p.right                         # ...z's grandparent is y 
                if y.color == 1:                        # case 1
                    y.color = 0
                    z.p.color = 0
                    z.p.p.color = 1
                    z = z.p.p                   
                elif z == z.p.right:                    # case 2
                    z = z.p
                    self.left_rotate(z)
                else:                                   # case 3 
                    z.p.color = 0
                    z.p.p.color = 1
                    self.right_rotate(z.p.p)
            if z == self.root:
                break
        self.root.color = 0                             # After ending the while loop, root is set as BLACK
    # Function to transplant nodes
    def rb_transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else :
            u.p.right = v
        v.p = u.p
    def tree_minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node
    # Function to handle deletion
    def rb_delete(self, node, key):
        z = self.nil
        while node != self.nil:                         # Search for the node having that value/ key and store it in 'z'
            if node.val == key:
                z = node
            if node.val <= key:
                node = node.right
            else:
                node = node.left
        if z == self.nil:                               # If Key is not present then deletion not possible so return
            print("Value not present in Tree!!")
            return None
        y = z
        y_original_color = y.color                      # Store the color of z- node
        if z.left == self.nil:                          # If left child of z is nil
            x = z.right                                 # Assign right child of z to x
            self.rb_transplant(z, z.right)              # Transplant Node to be deleted with x
        elif (z.right == self.nil):                     # If right child of z is nil
            x = z.left                                  # Assign left child of z to x
            self.rb_transplant(z, z.left)               # Transplant Node to be deleted with x
        else:                                           # If z has both the child nodes
            y = self.tree_minimum(z.right)              # Find tree_minimum of the right sub tree
            y_original_color = y.color                  # Store color of y
            x = y.right
            if y.p == z:                                # If y is child of z
                x.p = y                                 # Set p of x as y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 0:                       # If color is black then fixing is needed
            self.rb_delete_fixup(x)
    # Deletion of node
    def delete_node(self, val):
        self.rb_delete(self.root, val)                  # Call for deletion
    # Function to fix issues after deletion
    def rb_delete_fixup(self, x):
        while x != self.root and x.color == 0:          # Repeat until x reaches nodes and color of x is black
            if x == x.p.left:                           # If x is left child of its p
                w = x.p.right                           # Sibling of x
                if w.color == 1:                        # case1: if sibling is red
                    w.color = 0                         # ...Set its color to black
                    x.p.color = 1                       # ...Make its p red
                    self.left_rotate(x.p)               # ...Call for left rotate on p of x
                    w = x.p.right
                # If both the children are black
                elif w.left.color == 0 and \
                        w.right.color == 0:             # case 2: 
                    w.color = 1                         # ...Set color of s as red
                    x = x.p
                elif w.right.color == 0:                # case 3: If right child of s is black
                        w.left.color = 0                # ...set left child of s as black
                        w.color = 1                     # ...set color of s as red
                        self.right_rotate(w)            # ...call right rotation on x
                        w = x.p.right
                else:                                   # case 3: 
                    w.color = x.p.color
                    x.p.color = 0                       # ...Set p of x as black
                    w.right.color = 0
                    self.left_rotate(x.p)               # ...call left rotation on p of x
                    x = self.root
            else:                                       # If x is right child of its p
                w = x.p.left                            # Sibling of x
                if w.color == 1:                        # if sibling is red
                    w.color = 0                         # Set its color to black
                    x.p.color = 1                       # Make its p red
                    self.right_rotate(x.p)              # Call for right rotate on p of x
                    w = x.p.left
                elif w.right.color == 0 and \
                        w.right.color == 0:
                    w.color = 1
                    x = x.p
                elif w.left.color == 0:                 # If left child of s is black
                        w.right.color = 0               # set right child of s as black
                        w.color = 1
                        self.left_rotate(w)             # call left rotation on x
                        w = x.p.left
                else: 
                    w.color = x.p.color
                    x.p.color = 0
                    w.left.color = 0
                    self.right_rotate(x.p)
                    x = self.root
        x.color = 0
    # Function to print
    def show_call(self, node, indent, last):
        if node != self.nil:
            print(indent, end=' ')
            if last :
                print("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += " |    "
            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.val) + "(" + s_color + ")")
            self.show_call(node.left, indent, False)
            self.show_call(node.right, indent, True)
    # Function to call print
    def show_tree(self) :
        self.show_call(self.root , "" , True)


if __name__ == "__main__":
    rbt = RBTree()
    rbt.rb_insert(10)
    rbt.rb_insert(20)
    rbt.rb_insert(30)
    rbt.rb_insert(5)
    rbt.rb_insert(4)
    rbt.rb_insert(2)
    rbt.show_tree()
    print("\nAfter deleting an element")
    rbt.delete_node(2)
    rbt.show_tree()


# Output:


"""
 R---- 20(BLACK)
      L---- 5(RED)
      |     L---- 4(BLACK)
      |     |     L---- 2(RED)
      |     R---- 10(BLACK)
      R---- 30(BLACK)

After deleting an element
 R---- 20(BLACK)
      L---- 5(RED)
      |     L---- 4(BLACK)
      |     R---- 10(BLACK)
      R---- 30(BLACK)
"""