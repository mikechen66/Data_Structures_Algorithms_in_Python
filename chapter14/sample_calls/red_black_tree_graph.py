

# red_black_tree_graph.py

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

               xP               xP
               ||               ||
                x                y
               / \\     =>     // \
              xL  y            x   yRR
                // \          / \\
               yRL yRR       xL yRL


2).right_rotate: 

The following three links marked by double lines are altered. It is the reverse process of 
the following left rotation. With regard to code(not pseducode), swaping between x and y is 
equivalent to swaping between left and right(for right and left rotation). 

                xP              xP
                ||              ||
                 x               y
               // \             / \\
               y   xR   =>    yLL  x
              / \\               // \
            yLL yLR             yLR xR

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


Please note the above pseducode is a little different with the Python code snippet

4.Graph Presentatoin 

It gives a vivid Graph of Red Black Tree while running the script with graphviz module embedded 
in the unittest module code snippet. For presenting quality effect, set 'pdf' that is much better 
than 'png' within the snippet of code related to graphiz

1).Install graphiz

$ pip install graphviz

2).Use Digraph (Directed Graph)

from graphviz import Digraph


5.@total_ordering

Functools module in python helps in implementing higher-order functions. Higher-order functions 
are dependent functions that call other functions. Total_ordering provides rich class comparison 
methods that help in comparing classes without explicitly defining a function for it. It helps in 
the redundancy of code.

6.Reference :

# https://walkccc.me/CLRS/Chap13/13.2/?continueFlag=f08c6cbaddd3864d16b2bcb5bc1bf11f
# https://github.com/ShoYamanishi/RedBlackTree/blob/master/rbtree.py
# https://graphviz.readthedocs.io/en/stable/examples.html
# https://pypi.org/project/graphviz/
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
# https://docs.python.org/3/library/functools.html
"""


from graphviz import Digraph
from functools import total_ordering


@total_ordering
class RedBlackNode(object):
    def __init__(self, key):
        self.key = key
        self.colored = 1                     # -1:nil, 0:Black, 1:Red
        self.left  = None
        self.right = None
        self.p = None
    def __eq__(self, other):
        return self.key == other.key
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        return self.key < other.key
    def __repr__(self):
        if self.is_nil():
            return f"[N]: {self.key}"
        if self.is_black():
            return f"[B]: {self.key}"
        else:
            return f"[R]: {self.key}"
    def is_red(self):
        return self.colored == 1
    def is_black(self):
        return self.colored < 1                # nil or Black
    def is_nil(self):
        return self.colored == -1
    def set_nil(self):
        self.colored = -1
    def set_black(self):
        if self.colored != -1:
            self.colored = 0
    def set_red(self):
        if self.colored != -1:
            self.colored = 1
    def color(self):
        return self.colored
    def set_color(self, rbtype):
        self.colored = rbtype
    def __iter__(self):
        if not self.left.is_nil():
            yield from self.left.__iter__()
        yield self.key
        if not self.right.is_nil():
            yield from self.right.__iter__()
    def val(self):
        return self.key
    def draw(self, dot, node_id):
        if self.is_nil():
            dot.node(str(node_id), label='', shape='box', style='filled', 
                     color='grey', height='0.1', width='0.1', fixedsize='true')
        elif self.is_red(): 
            dot.node(str(node_id), label='%.2f' % self.key, shape='circle', style='filled', 
                     color='red', height='0.5', width='0.5', fixedsize='true')
        else:
            dot.node(str(node_id), label='%.2f' % self.key, shape='circle', style='filled', 
                     color='black', height='0.5', width='0.5', fixedsize='true')


class RedBlackTree(object):
    def __init__(self):
        self.tnill  = RedBlackNode(0)
        self.tnill.set_nil()
        self.troot = self.tnill
        self._size  = 0
    def left_rotate(self, x):
        if x == self.tnill:
            return None
        y = x.right                      # set y
        x.right = y.left                 # turn y's left subtree into x's right subtree
        if y.left != self.tnill:
            y.left.p = x
        y.p = x.p                        # link x's parent to y's parent
        if x.p == self.tnill:
            self.troot = y
        elif x == x.p.left: 
            x.p.left = y
        else:
            x.p.right = y
        y.left = x                       # put x on y's left (child)
        x.p = y
    def right_rotate(self, x):           # swap between left and right based on left_rotate()
        if x == self.tnill:              # x has already been the root.
            return None
        y = x.left
        x.left = y.right
        if y.right != self.tnill:
            y.right.p = x
        y.p = x.p
        if x.p == self.tnill:
            self.troot = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
    def rb_insert(self, z):
        y = self.tnill
        x = self.troot
        while x != self.tnill:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.tnill:
            self.troot = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left  = self.tnill
        z.right = self.tnill
        z.set_red()                      # originally z.color = 'RED'
        self.rb_insert_fixup(z)
        self._size += 1
    def rb_insert_fixup(self, z):
        while z.p.is_red():              # originally z.p.color == 'RED'
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.is_red():                                  # case 1       
                    z.p.set_black()      
                    y.set_black()
                    z.p.p.set_red()
                    z = z.p.p
                elif z == z.p.right:                            # case 2: 
                    z = z.p
                    self.left_rotate(z)
                else:                                           # case 3
                    z.p.set_black()
                    z.p.p.set_red()
                    self.right_rotate(z.p.p)
            else:                       # same as "if" clause with "right" and "left" exchanged
                y = z.p.p.left
                if y.is_red():
                    z.p.set_black()
                    y.set_black()
                    z.p.p.set_red()
                    z = z.p.p
                elif z == z.p.left:                             
                    z = z.p
                    self.right_rotate(z)
                else: 
                    z.p.set_black()
                    z.p.p.set_red()
                    self.left_rotate(z.p.p)
        self.troot.set_black()
    def rb_transplant(self, u, v):
        if u.p == self.tnill:
            self.troot = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p
    def is_black(self, color):
        # nil or Black
        return color < 1
    def tree_maximum(self, x):
        while x.right != self.tnill:
            x = x.right
        return x
    def tree_minimum(self, x):
        while x.left != self.tnill:
            x = x.left
        return x
    def root(self):
        return self.troot
    def nil(self):
        return self.tnill
    def size(self):
        return self._size
    def tree_successor(self, x):
        if x.right != self.tnill:
            return self.tree_minimum(x.right)
        y = x.p
        while (y != self.tnill) and (x == y.right):
            x = y
            y = y.p
        return y
    def tree_predecessor(self, x):
        if x.left != self.tnill:
            return self.tree_maximum(x.left)
        y = x.p
        while (y != self.tnill) and (x == y.left):
            x = y
            y = y.p
        return y
    def rb_delete(self, z):
        self._size -= 1
        y = z
        y_original_color = y.color()
        if z.left == self.tnill:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.tnill:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color()
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
            y.set_color(z.color())
        if self.is_black(y_original_color):
            self.rb_delete_fixup(x)
    def rb_delete_fixup(self, x):
        while (x != self.troot) and x.is_black():
            if x == x.p.left:
                w = x.p.right
                if w.is_red():                                  # Case 1
                    w.set_black()
                    x.p.set_red()
                    self.left_rotate(x.p)
                    w = x.p.right
                elif w.left.is_black() and w.right.is_black():  # Case 2
                    w.set_red()
                    x = x.p
                elif w.right.is_black():                        # Case 3
                        w.left.set_black()
                        w.set_red()
                        self.right_rotate(w)
                        w = x.p.right
                else:                                           # case 4
                    w.set_color(x.p.color())
                    x.p.set_black()
                    w.right.set_black()
                    self.left_rotate(x.p)
                    x = self.troot
            else:                                               
                w = x.p.left
                if w.is_red():
                    w.set_black()
                    x.p.set_red()
                    self.right_rotate(x.p)
                    w = x.p.left
                elif w.left.is_black() and w.right.is_black():
                    w.set_red()
                    x = x.p
                elif w.left.is_black():
                    w.right.set_black()
                    w.set_red()
                    self.left_rotate(w)
                    w = x.p.left
                else: 
                    w.set_color(x.p.color())
                    x.p.set_black()
                    w.left.set_black()
                    self.right_rotate(x.p)
                    x = self.troot
        x.set_black()
    def __iter__(self):
        if self.nil() is self.root():
            return []
        yield from self.troot.__iter__()
    def draw(self, tree_name, view_now=True, out_format="svg", orientation="vertical"):
        g_dot = Digraph(comment=tree_name)
        if orientation == 'horizontal':
            g_dot.graph_attr['rankdir'] = 'LR'
        self._node_id = 0
        if not self.troot is self.tnill:        
            node_id = self._node_id
            self._node_id += 1
            self.tnill.draw(g_dot, node_id)
            self.visit_draw(self.troot, g_dot, node_id)
        g_dot.render(tree_name.strip('<>'), view=view_now, format=out_format)
    def visit_draw(self, n, dot, parent_id):
        node_id = self._node_id
        self._node_id += 1
        n.draw(dot, node_id)
        if parent_id != -1:
            dot.edge(str(parent_id), str(node_id))
        if not n is self.tnill:
            n._node_id = node_id
            node_id_left  = self.visit_draw(n.left,  dot, n._node_id)
            node_id_right = self.visit_draw(n.right, dot, n._node_id)
            # Add horizontal edges to force ordering among children.
            dot.edge(str(node_id_left), str(node_id_right), style='invis')
            with dot.subgraph() as s:
                s.attr(rank='same')
                s.node(str(node_id_left),  fontcolor='white', style="filled")
                s.node(str(node_id_right), fontcolor='white', style="filled")
        return node_id

#-------------------------------------------------------------------------------------------------


# Unit Test and Graph Presentation


import unittest
import random


class test_rbtree(unittest.TestCase):
    def test_random(self):
        NUM_OPERATIONS = 10000
        RATIO_INSERTS_OVER_DELETES = 0.5
        # rbt = rbtree.RedBlackTree()
        rbt = RedBlackTree()
        node_list = []
        num_set = set()
        for i in range(0, NUM_OPERATIONS):
            r_ops = random.uniform(0.0, 1.0)
            if r_ops <= RATIO_INSERTS_OVER_DELETES:
                while True:
                    num = random.uniform(-100, 100)
                    if num not in num_set:
                        num_set.add(num)
                        break;
                # node = rbtree.RedBlackNode(num)
                node = RedBlackNode(num)
                rbt.rb_insert(node)
                node_list.append(node)
            else:
                if len(node_list) > 0:
                    r_index = random.randint(0, len(node_list)-1)
                    n = node_list[r_index]
                    node_list.remove(n)
                    num_set.remove(n.key)
                    rbt.rb_delete(n)
        num_list_from_min = []
        n_cur = rbt.tree_minimum(rbt.root())
        while not n_cur is rbt.nil():
            num_list_from_min.append(n_cur.key)
            n_cur = rbt.tree_successor(n_cur)
        num_list_from_iter = [n for n in rbt]
        num_list_from_max = []
        n_cur = rbt.tree_maximum(rbt.root())
        while not n_cur is rbt.nil():
            num_list_from_max.append(n_cur.key)
            n_cur = rbt.tree_predecessor(n_cur)
        num_list = list(num_set)
        for i, n in enumerate(sorted(num_list)):
            self.assertEqual(n, num_list_from_min[i])
            self.assertEqual(n, num_list_from_iter[i])
        for i, n in enumerate(sorted(num_list, reverse=True)):
            self.assertEqual(n, num_list_from_max[i])
        self.assertEqual(rbt.size(), len(num_list) )
        rbt.draw('test_random_10000_operations', True, 'pdf', 'vertical')


if __name__ == '__main__':
    unittest.main()


# Output:

"""
/home/user/miniconda3/lib/python3.7/subprocess.py:883: ResourceWarning: subprocess 2345 is still running
  ResourceWarning, source=self)
ResourceWarning: Enable tracemalloc to get the object allocation traceback
.
----------------------------------------------------------------------
Ran 1 test in 0.208s
"""