

# Exercises


###############################################################################################################
###############################################################################################################


# 1. Reinforcement 

# Omit 

#-------------------------------------------------------------------------------------------------------------

# Ohter supporint code for excises and solitions


# linked_queue 


class Empty(Exception):
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    #-------------------------- nested _Node class -------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage
        def __init__(self, element, next):
            self._element = element
            self._next = next
    #------------------------------- queue methods -------------------------------
    def __init__(self):
        # Create an empty queue.
        self._head = None
        self._tail = None
        self._size = 0                          # number of queue elements
    def __len__(self):
        # Return the number of elements in the queue.
        return self._size
    # For the rotate() function 
    def __iter__(self):
        cur = self._head
        while cur is not None:
            yield cur._element
            cur = cur._next
    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0
    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element              # front aligned with head of list
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                     # special case as queue is empty
            self._tail = None                   # removed head had been the tail
        return answer
    def enqueue(self, e):
        # Add an element to the back of queue.
        newest = self._Node(e, None)            # node will be new tail node
        if self.is_empty():
            self._head = newest                 # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                     # update reference to tail node
        self._size += 1


# For the call from the main function
def rotate(self):
    if self._size > 0:
        old_head = self._head
        self._head = old_head._next
        self._tail._next = old_head
        old_head._next = None


###############################################################################################################  


# Tree

import collections


class Tree:
    """Abstract base class representing a tree structure."""
    #------------------------------- nested Position class -------------------------------
    class Position:
        """
        An abstraction representing the location of a single element within a tree.
        Note that two position instaces may represent the same inherent location in a tree.
        Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when 
        testing equivalence of positions.
        """
        def element(self):
            # Return the element stored at this Position.
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self, other):
            # Return True if other Position represents the same location.
            raise NotImplementedError('must be implemented by subclass')
        def __ne__(self, other):
            # Return True if other does not represent the same location.
            return not (self == other)            # opposite of __eq__
    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        # Return Position representing the tree's root (or None if empty).
        raise NotImplementedError('must be implemented by subclass')
    def parent(self, p):
        # Return Position representing p's parent (or None if p is root).
        raise NotImplementedError('must be implemented by subclass')
    def num_children(self, p):
        # Return the number of children that Position p has.
        raise NotImplementedError('must be implemented by subclass')
    def children(self, p):
        # Generate an iteration of Positions representing p's children.
        raise NotImplementedError('must be implemented by subclass')
    def __len__(self):
        # Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')
    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        # Return True if Position p represents the root of the tree.
        return self.root() == p
    def is_leaf(self, p):
        # Return True if Position p does not have any children.
        return self.num_children(p) == 0
    def is_empty(self):
        # Return True if the tree is empty.
        return len(self) == 0
    def depth(self, p):
        # Return the number of levels separating Position p from the root.
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    def _height1(self):                   # works, but O(n^2) worst-case time
        # Return the height of the tree.
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    def _height2(self, p):                # time is linear in size of subtree
        # Return the height of the subtree rooted at Position p.
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    def height(self, p=None):
        """
        Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)                           # start _height2 recursion
    def __iter__(self):
        # Generate an iteration of the tree's elements.
        for p in self.positions():                        # use same order as positions()
            yield p.element()                             # but yield each element
    def positions(self):
        # Generate an iteration of the tree's positions.
        return self.preorder()                            # return entire preorder iteration
    def preorder(self):
        # Generate a preorder iteration of positions in the tree.
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()): # start recursion
                yield p
    def _subtree_preorder(self, p):
        # Generate a preorder iteration of positions in subtree rooted at p.
        yield p                                           # visit p before its subtrees
        for c in self.children(p):                        # for each child c
            for other in self._subtree_preorder(c):       # do preorder of c's subtree
                yield other                               # yield each to our caller
    def postorder(self):
        # Generate a postorder iteration of positions in the tree.
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):# start recursion
                yield p
    def _subtree_postorder(self, p):
        # Generate a postorder iteration of positions in subtree rooted at p.
        for c in self.children(p):                        # for each child c
            for other in self._subtree_postorder(c):      # do postorder of c's subtree
                yield other                               # yielding each to our caller
        yield p                                           # visit p after its subtrees
    def breadthfirst(self):
        # Generate a breadth-first iteration of the positions of the tree.
        if not self.is_empty():
            fringe = LinkedQueue()                        # known positions not yet yielded
            fringe.enqueue(self.root())                   # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue()                      # remove from front of the queue
                yield p                                   # report this position
                for c in self.children(p):
                    fringe.enqueue(c)                     # add children to back of queue


###############################################################################################################  


# BinaryTree


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""
    # --------------------- additional abstract methods ---------------------
    def left(self, p):
        """
        Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')
    def right(self, p):
        """
        Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')
    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        # Return a Position representing p's sibling (or None if no sibling).
        parent = self.parent(p)
        if parent is None:                 # p must be the root
            return None                    # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)  # possibly None
            else:
                return self.left(parent)   # possibly None
    def children(self, p):
        # Generate an iteration of Positions representing p's children.
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    def inorder(self):
        # Generate an inorder iteration of positions in the tree.
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    def _subtree_inorder(self, p):
        # Generate an inorder iteration of positions in subtree rooted at p.
        if self.left(p) is not None:       # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                            # visit p between its subtrees
        if self.right(p) is not None:      # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other
    # Override inherited version to make inorder the default
    def positions(self):
        # Generate an iteration of the tree's positions.
        return self.inorder()              # make inorder the default

###############################################################################################################  


# linked_binary_tree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""
    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right' # streamline memory usage
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    #-------------------------- nested Position class --------------------------
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""
        def __init__(self, container, node):
            # Constructor should not be invoked by user.
            self._container = container
            self._node = node
        def element(self):
            # Return the element stored at this Position.
            return self._node._element
        def __eq__(self, other):
            # Return True if other is a Position representing the same location.
            return type(other) is type(self) and other._node is self._node
    #------------------------------- utility methods -------------------------------
    def _validate(self, p):
        # Return associated node, if position is valid.
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self, node):
        # Return Position instance for given node (or None if no node).
        return self.Position(self, node) if node is not None else None
    #-------------------------- binary tree constructor --------------------------
    def __init__(self):
        # Create an initially empty binary tree.
        self._root = None
        self._size = 0
    #-------------------------- public accessors --------------------------
    def __len__(self):
        # Return the total number of elements in the tree.
        return self._size
    def root(self):
        # Return the root Position of the tree (or None if tree is empty).
        return self._make_position(self._root)
    def parent(self, p):
        # Return the Position of p's parent (or None if p is root).
        node = self._validate(p)
        return self._make_position(node._parent)
    def left(self, p):
        # Return the Position of p's left child (or None if no left child).
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self, p):
        # Return the Position of p's right child (or None if no right child).
        node = self._validate(p)
        return self._make_position(node._right)
    def num_children(self, p):
        # Return the number of children of Position p.
        node = self._validate(p)
        count = 0
        if node._left is not None:     # left child exists
            count += 1
        if node._right is not None:    # right child exists
            count += 1
        return count
    #-------------------------- nonpublic mutators --------------------------
    def _add_root(self, e):
        """
        Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    def _add_left(self, p, e):
        """
        Create a new left child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)                  # node is its parent
        return self._make_position(node._left)
    def _add_right(self, p, e):
        """
        Create a new right child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)                 # node is its parent
        return self._make_position(node._right)
    def _replace(self, p, e):
        # Replace the element at position p with e, and return old element.
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    def _delete(self, p):
        """
        Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent   # child's grandparent becomes parent
        if node is self._root:
            self._root = child             # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node                # convention for deprecated node
        return node._element
    def _attach(self, p, t1, t2):
        """
        Attach trees t1 and t2, respectively, as the left and right subtrees of the 
        external Position p. As a side effect, set t1 and t2 to be empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():              # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None                # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():              # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None                # set t2 instance to empty
            t2._size = 0

###############################################################################################################        


# MapBase


from collections import MutableMapping


class MapBase(MutableMapping):
  """Our own abstract base class that includes a nonpublic _Item class."""
  #------------------------------- nested _Item class -------------------------------
  class _Item:
    """Lightweight composite to store key-value pairs as map items."""
    __slots__ = '_key', '_value'
    def __init__(self, k, v):
        self._key = k
        self._value = v
    def __eq__(self, other):               
        return self._key == other._key   # compare items based on their keys
    def __ne__(self, other):
        return not (self == other)       # opposite of __eq__
    def __lt__(self, other):               
        return self._key < other._key    # compare items based on their keys


###############################################################################################################


# TreeMap of Binary Search Tree


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""
    #---------------------------- override Position class ----------------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            # Return key of map's key-value pair.
            return self.element()._key
        def value(self):
            # Return value of map's key-value pair.
            return self.element()._value
    #------------------------------- nonpublic utilities -------------------------------
    def _subtree_search(self, p, k):
        # Return Position of p's subtree having key k, or last node searched.
        if k == p.key():                             # found match
            return p                                         
        elif k < p.key():                            # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)   
        else:                                        # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p                                     # unsucessful search
    def _subtree_first_position(self, p):
        # Return Position of first item in subtree rooted at p.
        walk = p
        while self.left(walk) is not None:           # keep walking left
            walk = self.left(walk)
        return walk
    def _subtree_last_position(self, p):
        # Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None:          # keep walking right
            walk = self.right(walk)
        return walk
    #--------------------- public methods providing "positional" support ---------------------
    def first(self):
        # Return the first Position in the tree (or None if empty).
        return self._subtree_first_position(self.root()) if len(self) > 0 else None
    def last(self):
        # Return the last Position in the tree (or None if empty).
        return self._subtree_last_position(self.root()) if len(self) > 0 else None
    def before(self, p):
        """
        Return the Position just before p in the natural order.
        Return None if p is the first position.
        """
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above
    def after(self, p):
        """
        Return the Position just after p in the natural order.
        Return None if p is the last position.
        """
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above
    def find_position(self, k):
        # Return position with key k, or else neighbor (or None if empty).
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)                  # hook for balanced tree subclasses
            return p
    def delete(self, p):
        # Remove the item at given Position.
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.left(p) and self.right(p):           # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())    # from LinkedBinaryTree
            p =  replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)                              # inherited from LinkedBinaryTree
        self._rebalance_delete(parent)               # if root deleted, parent is None
    #--------------------- public methods for (standard) map interface ---------------------
    def __getitem__(self, k):
        # Return value associated with key k (raise KeyError if not found).
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)                  # hook for balanced tree subclasses
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()
    def __setitem__(self, k, v):
        # Assign value v to key k, overwriting existing value if present.
        if self.is_empty():
            leaf = self._add_root(self._Item(k,v))     # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v                   # replace existing item's value
                self._rebalance_access(p)                # hook for balanced tree subclasses
                return
            else:
                item = self._Item(k,v)
                if p.key() < k:
                    leaf = self._add_right(p, item)        # inherited from LinkedBinaryTree
                else:
                    leaf = self._add_left(p, item)         # inherited from LinkedBinaryTree
        self._rebalance_insert(leaf)                 # hook for balanced tree subclasses
    def __delitem__(self, k):
        # Remove item associated with key k (raise KeyError if not found).
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)                           # rely on positional version
                return                                   # successful deletion complete
            self._rebalance_access(p)                  # hook for balanced tree subclasses
        raise KeyError('Key Error: ' + repr(k))
    def __iter__(self):
        # Generate an iteration of all keys in the map in order.
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)
    #--------------------- public methods for sorted map interface ---------------------
    def __reversed__(self):
        # Generate an iteration of all keys in the map in reverse order.
        p = self.last()
        while p is not None:
            yield p.key()
            p = self.before(p)
    def find_min(self):
        # Return (key,value) pair with minimum key (or None if empty).
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())
    def find_max(self):
        # Return (key,value) pair with maximum key (or None if empty).
        if self.is_empty():
            return None
        else:
            p = self.last()
            return (p.key(), p.value())
    def find_le(self, k):
        """
        Return (key,value) pair with greatest key less than or equal to k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if k < p.key():
                p = self.before(p)
            return (p.key(), p.value()) if p is not None else None
    def find_lt(self, k):
        """
        Return (key,value) pair with greatest key strictly less than k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if not p.key() < k:
                p = self.before(p)
            return (p.key(), p.value()) if p is not None else None
    def find_ge(self, k):
        """
        Return (key,value) pair with least key greater than or equal to k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)                   # may not find exact match
            if p.key() < k:                             # p's key is too small
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None
    def find_gt(self, k):
        """
        Return (key,value) pair with least key strictly greater than k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if not k < p.key():                   
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None
    def find_range(self, start, stop):
        """
        Iterate all (key,value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # we initialize p with logic similar to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)
    #--------------------- hooks used by subclasses to balance a tree ---------------------
    def _rebalance_insert(self, p):
        # Call to indicate that position p is newly added.
        pass
    def _rebalance_delete(self, p):
        # Call to indicate that a child of p has been removed.
        pass
    def _rebalance_access(self, p):
        # Call to indicate that position p was recently accessed.
        pass
    #--------------------- nonpublic methods to support tree balancing ---------------------
    def _relink(self, parent, child, make_left_child):
        # Relink parent node with child node (we allow child to be None)."""
        if make_left_child:                           # make it a left child
            parent._left = child
        else:                                         # make it a right child
            parent._right = child
        if child is not None:                         # make child point to parent
            child._parent = parent
    def _rotate(self, p):
        """
        Rotate Position p above its parent.
        Switches between these configurations, depending on whether p==a or p==b.

              b                  a
             / \                /  \
            a  t2             t0   b
           / \                     / \
          t0  t1                  t1  t2

        Caller should ensure that p is not the root.
        """
        # Rotate Position p above its parent.
        x = p._node
        y = x._parent                                   # we assume this exists
        z = y._parent                                   # grandparent (possibly None)
        if z is None:            
            self._root = x                              # x becomes root
            x._parent = None        
        else:
            self._relink(z, x, y == z._left)            # x becomes a direct child of z
        # Now rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True)             # x._right becomes left child of y
            self._relink(x, y, False)                   # y becomes right child of x
        else:
            self._relink(y, x._left, False)             # x._left becomes right child of y
            self._relink(x, y, True)                    # y becomes left child of x
    def _restructure(self, x):
        """
        Perform a trinode restructure among Position x, its parent, and its grandparent.
        Return the Position that becomes root of the restructured subtree.
        Assumes the nodes are in one of the following configurations:

            z=a                 z=c           z=a               z=c  
           /  \                /  \          /  \              /  \  
          t0  y=b             y=b  t3       t0   y=c          y=a  t3 
             /  \            /  \               /  \         /  \     
            t1  x=c         x=a  t2            x=b  t3      t0   x=b    
               /  \        /  \               /  \              /  \    
              t2  t3      t0  t1             t1  t2            t1  t2   

        The subtree will be restructured so that the node with key b becomes its root.

                  b
                /   \
              a       c
             / \     / \
            t0  t1  t2  t3

        Caller should ensure that x has a grandparent.
        """
        # Perform trinode restructure of Position x with parent/grandparent.
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):  # matching alignments
            self._rotate(y)                               # single rotation (of y)
            return y                                      # y is new subtree root
        else:                                             # opposite alignments
            self._rotate(x)                               # double rotation (of x)     
            self._rotate(x)
            return x                                      # x is new subtree root

###############################################################################################################


# AVLTreeMap


class AVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL tree."""
    #-------------------------- nested _Node class --------------------------
    class _Node(TreeMap._Node):
        """
        Node class for AVL maintains height value for balancing.
        We use convention that a "None" child has height 0, thus a leaf has height 1.
        """
        __slots__ = '_height'         # additional data member to store height
        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0          # will be recomputed during balancing
        def left_height(self):
            return self._left._height if self._left is not None else 0
        def right_height(self):
            return self._right._height if self._right is not None else 0
    #------------------------- positional-based utility methods -------------------------
    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())
    def _isbalanced(self, p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1
    def _tall_child(self, p, favorleft=False): # parameter controls tiebreaker
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)
    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # if child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)
    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height                      # trivially 0 if new node
        if not self._isbalanced(p):                           # imbalance detected!
            # perform trinode restructuring, setting p to resulting root,
            # and recompute new local heights after the restructuring
            p = self._restructure(self._tall_grandchild(p))
            self._recompute_height(self.left(p))                
            self._recompute_height(self.right(p))                           
        self._recompute_height(p)                             # adjust for recent changes
        if p._node._height == old_height:                     # has height changed?
            p = None                                          # no further changes needed
        else:
            p = self.parent(p)                                # repeat with parent
    #---------------------------- override balancing hooks ----------------------------
    def _rebalance_insert(self, p):
        self._rebalance(p)
    def _rebalance_delete(self, p):
        self._rebalance(p)

###############################################################################################################


class LeftAVL(AVLTreeMap):
    """
    add a filed to store the minium node,it's a position class;
    control the minimum node when add node or delete node
    """
    #-----------------------------add a filed----------------------------------
    def __init__(self):
        super().__init__()
        self._mininum=None               # a Position class
    #-----------------------------control the mininum----------------------------------
    def _add_root(self,k,v):
        temp=super()._add_root(k,v)
        if k==None or k<self._mininum.element()._key:
            self._mininum=temp
        return temp 
    def _add_left(self,k,v):
        temp=super()._add_left(k,v)
        if k==None or k<self._mininum.element()._key:
            self._mininum=temp
        return temp
    def _add_right(self,k,v):
        temp=super()._add_right(k,v)
        if k==None or k<self._mininum.element()._key:
            self._mininum=temp
        return temp
    """
    def _rebalance_insert(self,p):
        if self._mininum==None or p.element()._key<self._mininum.element()._key:
            self._mininum=p
        super()._rebalance_insert(p)
    """
    def __delitem__(self,k):
        # remove the node which values equal k
        if k==self._mininum.element()._key:
            self._muninum=self.after(self._mininum)
        super().__delitem__(k)
    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        return self._mininum



###############################################################################################################


# avl_tree_call.py


# Option 1


# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the Insert operation
class AvlTree(object):
    # Insert key in subtree rooted with node and returns new root of subtree.
    def insert(self, root, key):
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left),
                        self.get_height(root.right))
        # Step 3 - Get the balance factor
        balance = self.get_balance(root)
        # Step 4 - If the node is unbalanced, then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))
        # Return the new root
        return y
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))
        # Return the new root
        return y
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def pre_order(self, root):
        if not root:
            return None
        print("{0} ".format(root.val), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)



if __name__ == '__main__':
    at = AvlTree()
    root = None
    root = at.insert(root, 10)
    root = at.insert(root, 20)
    root = at.insert(root, 30)
    root = at.insert(root, 40)
    root = at.insert(root, 50)
    root = at.insert(root, 25)
    """
    The constructed AVL Tree would be
             30
            / \
          20   40
         / \    \
        10 25    50
    """
    # pre_order Traversal
    print("pre_order traversal of the",
        "constructed AVL tree is")
    at.pre_order(root)
    print()


# Output:

"""
pre_order traversal of the constructed AVL tree is
30 20 10 25 40 50 
"""

######################################################################################################


# Option 2


class avl_Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

      
class AVLTree(object):
    def insert_node(self, root, value):
        if not root:
            return avl_Node(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.avl_Height(root.left),
                              self.avl_Height(root.right))
        # Update the balance factor and balance the tree
        balanceFactor = self.avl_BalanceFactor(root)
        if balanceFactor > 1:
            if value < root.left.value:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if value > root.right.value:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    def avl_Height(self, root):
        if not root:
            return 0
        return root.height
    # Get balance factore of the node
    def avl_BalanceFactor(self, root):
        if not root:
            return 0
        return self.avl_Height(root.left) - self.avl_Height(root.right)
    def avl_MinValue(self, root):
        if root is None or root.left is None:
            return root
        return self.avl_MinValue(root.left)
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.value), end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
    def leftRotate(self, b):
        a = b.right
        T2 = a.left
        a.left = b
        b.right = T2
        b.height = 1 + max(self.avl_Height(b.left),
                           self.avl_Height(b.right))
        a.height = 1 + max(self.avl_Height(a.left),
                           self.avl_Height(a.right))
        return a
    def rightRotate(self, b):
        a = b.left
        T3 = a.right
        a.right = b
        b.left = T3
        b.height = 1 + max(self.avl_Height(b.left),
                           self.avl_Height(b.right))
        a.height = 1 + max(self.avl_Height(a.left),
                           self.avl_Height(a.right))
        return a
    def delete_node(self, root, value):
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.avl_MinValue(root.right)
            root.value = temp.key
            root.right = self.delete_node(root.right, temp.value)
        if root is None:
            return root
        # Update the balance factor of nodes
        root.height = 1 + max(self.avl_Height(root.left), self.avl_Height(root.right))
        balanceFactor = self.avl_BalanceFactor(root)
        # Balance the tree
        if balanceFactor > 1:
            if self.avl_BalanceFactor(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.avl_BalanceFactor(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root


if __name__ == '__main__':            
    Tree = AVLTree()       
    root = None
    root = Tree.insert_node(root,40)
    root = Tree.insert_node(root,60)
    root = Tree.insert_node(root,50)
    root = Tree.insert_node(root,70)
    print("PREORDER")
    Tree.preOrder(root)

######################################################################################################


# Option 3

# AVL tree implementation in Python


import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    # Function to insert a node
    def insert_node(self, root, key):
        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    # Function to delete a node
    def delete_node(self, root, key):
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root
        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        balanceFactor = self.getBalance(root)
        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


if __name__ == '__main__':
    myTree = AVLTree()
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in nums:
        root = myTree.insert_node(root, num)
    myTree.printHelper(root, "", True)
    key = 13
    root = myTree.delete_node(root, key)
    print("After Deletion: ")
    myTree.printHelper(root, "", True)


# Output:

"""
R----33
     L----13
     |    L----9
     |    |    L----8
     |    |    R----11
     |    R----21
     R----52
          R----61
After Deletion: 
R----33
     L----9
     |    L----8
     |    R----21
     |         L----11
     R----52
          R----61
"""

###############################################################################################################
###############################################################################################################

# 2. Creativity


# C11.31 Repeat Exercise C-10.28 for the TreeMap class.
#  Modify the method __setitem__()


from binary_search_tree import TreeMap


class NewTreeMap(TreeMap):
    def setdefaut(self,k,v):
        # return k's value if k exist in the tree,else add (k,d)
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))     # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                return p.element()._value
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    # inherited from LinkedBinaryTree
                    leaf = self._add_right(p, item)
                else:
                    # inherited from LinkedBinaryTree
                    leaf = self._add_left(p, item)
        # hook for balanced tree subclasses
        try:     # add try grammar for text the ADT
            self._rebalance_insert(leaf)
        except e:
            pass


if __name__ == '__main__':
    t = NewTreeMap()
    for i in range(5):
        t.setdefaut(i,i)
    print(t.setdefaut(i,i+10))


# Output:

"""
4
"""
###############################################################################################################  


# C11.40 In our AVL implementation, each node stores the height of its subtree, which is an arbitrarily 
# large integer. The space usage for an AVL tree can be reduced by instead storing the balance factor 
# of a node, which is defined as the height of its left subtree minus the height of its right subtree.
# Thus, the balance factor of a node is always equal to −1, 0, or 1, except during an insertion or removal, 
# when it may become temporarily equal to −2 or +2. Reimplement the AVLTreeMap class storing balance factors
# rather than subtree heights.


from avl_tree import AVLTreeMap


class FactorAVL(AVLTreeMap):
    """
    alter variable:
        _height
    alter method:
        left_height
        right_height
        _recompute_height
        _isbalanced
        _tall_child
        _rebalance
        _rotate
    """
    class _Node(AVLTreeMap._Node):
        __slots__ = '_factor'         # additional data member to store height
        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._factor = 0            # will be recomputed during balancing
        def left_factor(self):
            return self._left._factor if self._left is not None else 0
        def right_factor(self):
            return self._right._factor if self._right is not None else 0
    #------------------------- positional-based utility methods --------------
    def _recompute_factor(self, p,orient):
        # have aid of the orient parameter
        if orient == None:
            return 
        p._node._factor =p._node._factor+1 if orient=='l' else p._node._factor-1
    def _isbalanced(self, p):
        return p._node._factor != 2 or p._node._factor != -2    # return False when factor== 2 or -2
    def _tall_child(self, p, favorleft=False):  # parameter controls tiebreaker
        if p._node.left_factor() + (1 if favorleft else 0) > p._node.right_factor():
            return self.left(p)
        else:
            return self.right(p)
    def _tall_grandchild(self, p):
        child = self._tall_child(p)            
        # if child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)
    def _rebalance(self, p):
        orient = None                             # definition the orient of child,'l' if leftchild else 'r'
        while p is not None:
            old_height = p._node._height          # trivially 0 if new node        
            self._recompute_factor(p,orient)
            # imbalance detected!
            if not self._isbalanced(p):
                # perform trinode restructuring, setting p to resulting root,
                # and recompute new local heights after the restructuring
                p = self._restructure(self._tall_grandchild(p))
            # adjust for recent changes            
            if p._node._height == old_height and orient==None:    # has height changed?
                p = None                                          # no further changes needed
            else:
                # cheak the orients
                if p is self.parent(p).left():
                    orient = 'l'
                else:
                    orient = 'r'
                # repeat with parent
                p = self.parent(p)
    def _rotate(self, p):
        """
        Rotate Position p above its parent.
        Switches between these configurations, depending on whether p==a or p==b.
              y                  y
             / \                /  \
            x  t2             t0   x
           / \                     / \
          t0  t1                  t1  t2
        Caller should ensure that p is not the root.
        """
        # Rotate Position p above its parent.
        x = p._node
        y = x._parent                                             # we assume this exists
        # grandparent (possibly None)
        z = y._parent
        if z is None:
            self._root = x                                        # x becomes root
            x._parent = None
        else:
            # x becomes a direct child of z
            self._relink(z, x, y == z._left)
        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            # x._right becomes left child of y
            self._relink(y, x._right, True)
            # y becomes right child of x
            self._relink(x, y, False)
            #calculate the factor
            y._factor = y._factor+min(-x._factor,0)+1
            x._factor = x._factor+min(0,y._factor)-1
        else:
            # x._left becomes right child of y
            self._relink(y, x._left, False)
            # y becomes left child of x
            self._relink(x, y, True)
            #calculate the factor
            y._factor = y._factor+max(-y._factor,0)+1
            x._factor = x._factor+max(0,y._factor)+1

            
if __name__ == '__main__':
    t = FactorAVL()
    for i in range(20):
        t[i] = i
    for i in range(20):
        print(t[i])


# Output:

"""
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
"""

###############################################################################################################  


# C11.42 If the approach described in the previous problem were implemented as part of the TreeMap 
# class, what additional modifications (if any) would be necessary to a subclass such as AVLTreeMap 
# in order to accurately maintain the reference to the leftmost position?


# Omit


###############################################################################################################  


# C11.43 Describe a modification to the binary search tree implementation having worst-case O(1)-time 
# performance for methods after(p) and before(p) without adversely affecting the asymptotics of any 
# other methods.


from avl_tree import AVLTreeMap


class NewAVL(AVLTreeMap):
    """add a field to make after and before method worst-cost O(1)-time"""
    #-------------------------------------add a filed----------------------------------------------
    class _Node(AVLTreeMap._Node):
        __slots__ = '_before','_after'         # additional data member to store height
        def __init__(self, element, parent=None, left=None, right=None, before=None, after=None):
            super().__init__(element, parent, left, right)
            self._before=before
            self._after=after
    #-------------------------------------alter add method-----------------------------------------    
    def _add_left(self,p,e):
        # inherit from linked_binary_tree
        temp=super()._add_left(p,e)
        node = self._validate(temp)
        p=node._parent                        # get the parent node
        node._after=p                         # tie the node
        node._before=p._before
        if p._before !=None:                  # if p is the mininum value node
            node._before._after=node
        node._after._before=node
        return temp
    def _add_right(self,p,e):
        # inherit from linked_binary_tree
        temp = super()._add_right(p,e)
        node = self._validate(temp)
        p = node._parent                      # get the parent node
        node._before = p                      # tie the node
        node._after = p._after
        if p._after != None:                  # if p is the maxnum value node
            node._after._before = node
        node._before._after = node
        return temp
    #-------------------------------------alter delete method--------------------------------------    
    def _delete(self,p):
        # inherit from linked_binary_tree
        temp=super()._delete(p)
        temp._after._before=temp._before    # tie the node
        temp._before._after=temp._after
    def after(self,p):
        node=self._validate(p)                   # inherited from LinkedBinaryTree
        return self._make_position(node._after)
    def before(self,p):
        node = self._validate(p)
        return self._make_position(node._before)
    

if __name__ == '__main__':
    t = NewAVL()
    for i in range(20):
        t[i]=i
        print(i)
    temp = t.first()
    for i in range(19):
        temp=t.after(temp)
        print(temp)
    print('######')
    for i in range(20):
        temp = t.before(temp)
        print(temp)

###############################################################################################################  


# C11.46 and C11.59
# The script is ased For both C11.46 and C11.59 

# binary_search_tree


# from binary_search_tree import TreeMap


from linked_binary_tree import LinkedBinaryTree
from map_base import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""
    #---------------------------- override Position class ----------------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            # Return key of map's key-value pair.
            return self.element()._key
        def value(self):
            # Return value of map's key-value pair.
            return self.element()._value
    #------------------------------- nonpublic utilities -------------------------------
    def _subtree_search(self, p, k):
        # Return Position of p's subtree having key k, or last node searched.
        if k == p.key():                             # found match
            return p                                         
        elif k < p.key():                            # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)   
        else:                                        # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p                                     # unsucessful search
    def _subtree_first_position(self, p):
        # Return Position of first item in subtree rooted at p.
        walk = p
        while self.left(walk) is not None:           # keep walking left
            walk = self.left(walk)
        return walk
    def _subtree_last_position(self, p):
        # Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None:          # keep walking right
            walk = self.right(walk)
        return walk
    #--------------------- public methods providing "positional" support ---------------------
    def first(self):
        # Return the first Position in the tree (or None if empty).
        return self._subtree_first_position(self.root()) if len(self) > 0 else None
    def last(self):
        # Return the last Position in the tree (or None if empty).
        return self._subtree_last_position(self.root()) if len(self) > 0 else None
    def before(self, p):
        """
        Return the Position just before p in the natural order.
        Return None if p is the first position.
        """
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above
    def after(self, p):
        """
        Return the Position just after p in the natural order.
        Return None if p is the last position.
        """
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above
    def find_position(self, k):
        # Return position with key k, or else neighbor (or None if empty).
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)                  # hook for balanced tree subclasses
            return p
    def delete(self, p):
        # Remove the item at given Position.
        self._validate(p)                            # inherited from LinkedBinaryTree
        if self.left(p) and self.right(p):           # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())    # from LinkedBinaryTree
            p =  replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)                              # inherited from LinkedBinaryTree
        self._rebalance_delete(parent)               # if root deleted, parent is None
    #--------------------- public methods for (standard) map interface ---------------------
    def __getitem__(self, k):
        # Return value associated with key k (raise KeyError if not found).
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)                  # hook for balanced tree subclasses
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()
    def __setitem__(self, k, v):
        # Assign value v to key k, overwriting existing value if present.
        if self.is_empty():
            leaf = self._add_root(self._Item(k,v))     # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v                   # replace existing item's value
                self._rebalance_access(p)                # hook for balanced tree subclasses
                return
            else:
                item = self._Item(k,v)
                if p.key() < k:
                    leaf = self._add_right(p, item)        # inherited from LinkedBinaryTree
                else:
                    leaf = self._add_left(p, item)         # inherited from LinkedBinaryTree
        self._rebalance_insert(leaf)                 # hook for balanced tree subclasses
    def __delitem__(self, k):
        # Remove item associated with key k (raise KeyError if not found).
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)                           # rely on positional version
                return                                   # successful deletion complete
            self._rebalance_access(p)                  # hook for balanced tree subclasses
        raise KeyError('Key Error: ' + repr(k))
    def __iter__(self):
        # Generate an iteration of all keys in the map in order.
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)
    #--------------------- public methods for sorted map interface ---------------------
    def __reversed__(self):
        # Generate an iteration of all keys in the map in reverse order.
        p = self.last()
        while p is not None:
            yield p.key()
            p = self.before(p)
    def find_min(self):
        # Return (key,value) pair with minimum key (or None if empty).
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())
    def find_max(self):
        # Return (key,value) pair with maximum key (or None if empty).
        if self.is_empty():
            return None
        else:
            p = self.last()
            return (p.key(), p.value())
    def find_le(self, k):
        """
        Return (key,value) pair with greatest key less than or equal to k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if k < p.key():
                p = self.before(p)
            return (p.key(), p.value()) if p is not None else None
    def find_lt(self, k):
        """
        Return (key,value) pair with greatest key strictly less than k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if not p.key() < k:
                p = self.before(p)
            return (p.key(), p.value()) if p is not None else None
    def find_ge(self, k):
        """
        Return (key,value) pair with least key greater than or equal to k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)                   # may not find exact match
            if p.key() < k:                             # p's key is too small
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None
    def find_gt(self, k):
        """
        Return (key,value) pair with least key strictly greater than k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if not k < p.key():                   
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None
    def find_range(self, start, stop):
        """
        Iterate all (key,value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # we initialize p with logic similar to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)
    #--------------------- hooks used by subclasses to balance a tree ---------------------
    def _rebalance_insert(self, p):
        # Call to indicate that position p is newly added.
        pass
    def _rebalance_delete(self, p):
        # Call to indicate that a child of p has been removed.
        pass
    def _rebalance_access(self, p):
        # Call to indicate that position p was recently accessed.
        pass
    #--------------------- nonpublic methods to support tree balancing ---------------------
    def _relink(self, parent, child, make_left_child):
        # Relink parent node with child node (we allow child to be None)."""
        if make_left_child:                           # make it a left child
            parent._left = child
        else:                                         # make it a right child
            parent._right = child
        if child is not None:                         # make child point to parent
            child._parent = parent
    def _rotate(self, p):
        """
        Rotate Position p above its parent.
        Switches between these configurations, depending on whether p==a or p==b.

              b                  a
             / \                /  \
            a  t2             t0   b
           / \                     / \
          t0  t1                  t1  t2

        Caller should ensure that p is not the root.
        """
        # Rotate Position p above its parent.
        x = p._node
        y = x._parent                                   # we assume this exists
        z = y._parent                                   # grandparent (possibly None)
        if z is None:            
            self._root = x                              # x becomes root
            x._parent = None        
        else:
            self._relink(z, x, y == z._left)            # x becomes a direct child of z
        # Now rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True)             # x._right becomes left child of y
            self._relink(x, y, False)                   # y becomes right child of x
        else:
            self._relink(y, x._left, False)             # x._left becomes right child of y
            self._relink(x, y, True)                    # y becomes left child of x
    def _restructure(self, x):
        """
        Perform a trinode restructure among Position x, its parent, and its grandparent.
        Return the Position that becomes root of the restructured subtree.
        Assumes the nodes are in one of the following configurations:

            z=a                 z=c           z=a               z=c  
           /  \                /  \          /  \              /  \  
          t0  y=b             y=b  t3       t0   y=c          y=a  t3 
             /  \            /  \               /  \         /  \     
            t1  x=c         x=a  t2            x=b  t3      t0   x=b    
               /  \        /  \               /  \              /  \    
              t2  t3      t0  t1             t1  t2            t1  t2   

        The subtree will be restructured so that the node with key b becomes its root.

                  b
                /   \
              a       c
             / \     / \
            t0  t1  t2  t3

        Caller should ensure that x has a grandparent.
        """
        # Perform trinode restructure of Position x with parent/grandparent.
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):  # matching alignments
            self._rotate(y)                               # single rotation (of y)
            return y                                      # y is new subtree root
        else:                                             # opposite alignments
            self._rotate(x)                               # double rotation (of x)     
            self._rotate(x)
            return x                                      # x is new subtree root

#----------------------------------------------------------------------------------------------------------


# C11.46 Modify binary_search_tree or create a subclass for BinarySearchTree. Here choose a subclass 


"""

Describe a modification to the binary search tree data structure that would support the following two 
index-based operations for a sorted map in O(h) time, where h is the height of the tree.

at index(i): Return the position p of the item at index i of a sorted map.
index of(p): Return the index i of the item at position p of a sorted map.

"""

# from binary_search_tree import TreeMap


class SubTreeMap(TreeMap):
    """add two field"""
    #-----------------------------------------alter two field-------------------------------------------   
    class _Node(TreeMap._Node):
        """inherit from linked_binary_tree"""
        __slots__='_left_num','_right_num'
        def __init__(self, element, parent=None, left=None, right=None, _left_num=0, _right_num=0):
            super().__init__(element, parent, left, right)
            self._right_num=_right_num          # add field for sum of right child num
            self._left_num=_left_num            # add field for sum of left child num
    class Position(TreeMap.Position):
        """inherit from linked_binary_tree, add two methods for coding conveniently"""
        def left_num(self):
            return self._node._left_num        
        def right_num(self): 
            return self._node._right_num
    def _change_num(self, temp, num):
        """
        temp is the beginning node which is a Position class,
        num is the int where need to change;
        node's num  on the route which from node p to root add num
        """
        p = self.parent(temp)
        while p is not None:    # cycle to add the child num
            if temp is self.left(p):            # if p is left child ,parent._left_num+=1
                p._node._left_num += num
            else:                               # else p is right child, parent._right_num+=1
                p._node._right_num += num
            temp = p
            p = self.parent(p)
    #----------------------------------------alter add method----------------------------------------------    
    def _add_left(self,p,e):
        temp = super()._add_left(p,e)
        self._change_num(temp,1)                # node's num  on the route which from node p to root add 1 
    def _add_right(self,p,e):
        temp = super()._add_right(p,e)
        self._change_num(temp,1)                # node's num  on the route which from node p to root add 1 
    #-----------------------------alter delete method----------------------------------    
    def _delete(self,p):
        self._change_num(p,-1)                  # node's num  on the route which from node p to root add -1
        super()._delete(p)
    #----------------------------------------add method-----------------------------------------------------
    def at_index(self,i,p=None):
        # recursion compare the child's num with i to get the Position index range begin at 0
        if i >= self._size or i < 0:
            raise KeyError('invalid key')
        if p == None:             
            p = self._root                       # recur from the root node
        if i < p._left_num:                      # if index i in p's left subtree
            return self.at_index(i,p._left)
        elif i == p._left_num:
            return self._make_position(p)       # if index i is p
        else:
            return self.at_index(i-p._left_num-1,p._right)    # if index i in p's right subtree
    def index_of(self,p):
        # cycle compare the child parent with itself's position to get the index p is a Position class
        num = p.left_num()
        if p is self.root():                    # if p is root
            return num
        temp = self.parent(p)                   # record the parent node
        while temp !=None:
            if p == self.right(temp):           # if p is it's parent's right node
                num += temp.left_num()+1        # num += left subtree node and 1
            p = temp
            temp = self.parent(temp)
        return num


if __name__ == '__main__':
    t = SubTreeMap()
    for i in range(10,30):
        t[i]=i
    temp = t.root()
    for i in range(10,30):
        print(temp.left_num(), temp.right_num())
        temp = t.after(temp)
    for i in range(20):
        temp = t.at_index(i)
        print(temp.element()._key)
        print(t.index_of(temp))


# Output:

"""
0 19
0 18
0 17
0 16
0 15
0 14
0 13
0 12
0 11
0 10
0 9
0 8
0 7
0 6
0 5
0 4
0 3
0 2
0 1
0 0
10
0
11
1
12
2
13
3
14
4
...
"""
###############################################################################################################  


# C11.59 Call BinaryTreeMap

"""
As a positional structure, our TreeMap implementation has a subtle flaw. A position instance p associated 
with an key-value pair (k, v) should remain valid as long as that item remains in the map. In particular, 
that position should be unaffected by calls to insert or delete other items in the collection. Our algorithm
for deleting an item from a binary search tree may fail to provide such a guarantee, in particular because 
of our rule for using the inorder predecessor of a key as a replacement when deleting a key that is located 
in a node with two children. Given an explicit series of Python commands that demonstrates such a flaw.
"""


from binary_search_tree import TreeMap 


class NewTreeMap(TreeMap):
    def delete(self,p):
        # Remove the item at given Position.
        node = self._validate(p)                     
        if self.left(p) and self.right(p):       
            replacement = self._subtree_last_position(self.left(p))._node
            # change section
            # combine replacement's parent with his child
            if replacement is replacement._parent._left:    
                replacement._parent._left=replacement._left if replacement._left is not None else replacement._right
            else:
                replacement._parent._right=replacement._left if replacement._left is not None else replacement._right            
            if node is self._root: # if p is root            
                self._root=replacement
            # combine the new node            
            replacement._parent = node._parent
            replacement._left = node._left    
            replacement._right = node._right
            # convention for deprecated node                        
            node._parent = node           
            node._left = node._right = None
        else:
            # now p has at most one child
            parent = self.parent(p)
            # inherited from LinkedBinaryTree
            self._delete(p)                          
            # if root deleted, parent is None


if __name__ == '__main__':
    t = NewTreeMap()
    t[2] = 2
    t[1] = 1
    t[3] = 3
    print('in order input [2,1,3] to the tree')
    root = t.root()
    left = t.left(root)
    right = t.right(root)
    print('delete the root node which value is 2')
    t.delete(root)
    print('delete have done')
    print('original left:\n\t',left.element()._value,'\n\tcurrent position:\n\t',t.root().element()._value)
    print('original left == new root:\n\t',left == t.root())    
    print('current root\'s next node:\n\t',t.after(t.root()))
    print('original\'s after:\n\t',t.after(left)) 


# Output:

"""
in order input [2,1,3] to the tree
delete the root node which value is 2
delete have done
original left:
     1 
    current position:
     1
original left == new root:
     True
current root's next node:
     <binary_search_tree.TreeMap.Position object at 0x7fafbe9fca50>
original's after:
     <binary_search_tree.TreeMap.Position object at 0x7fafbe9fca50>
"""

###############################################################################################################  


# C11.60 Rewrite delete() metod

# How might the TreeMap implementation be changed to avoid the flaw described in the previous problem?


from binary_search_tree import TreeMap


class NewTreeMap(TreeMap):
    def delete(self,p):
        # Remove the item at given Position.
        node = self._validate(p)                     
        if self.left(p) and self.right(p):       
            replacement = self._subtree_last_position(self.left(p))._node
            # change section
            # combine replacement's parent with his child
            if replacement is replacement._parent._left:    
                replacement._parent._left=replacement._left if replacement._left is not None else replacement._right
            else:
                replacement._parent._right=replacement._left if replacement._left is not None else replacement._right            
            if node is self._root: # if p is root            
                self._root=replacement
            # combine the new node            
            replacement._parent=node._parent
            replacement._left=node._left    
            replacement._right=node._right
            # convention for deprecated node                        
            node._parent=node           
            node._left=node._right=None
        else:
            # now p has at most one child
            parent = self.parent(p)
            # inherited from LinkedBinaryTree
            self._delete(p)                          
            # if root deleted, parent is None


if __name__ == '__main__':
    t = NewTreeMap()
    root = t._add_root('a')
    b = t._add_left(root,'b')
    c = t._add_right(root,'c')
    print(list(map(t.Position.element,[root,b,c])),root==t.parent(b))


# Output:

"""
['a', 'b', 'c'] True
"""

###############################################################################################################  
###############################################################################################################  


# Projects

###############################################################################################################


# P11.61 Perform an experimental study to compare the speed of our AVL tree, splay tree, and 
# red-black tree implementations for various sequences of operations.


from splay_tree import SplayTreeMap as STM
from avl_tree import AVLTreeMap as AVLTM
from red_black_tree import RedBlackTreeMap as RBTM
import sys
sys.setrecursionlimit(100000) #set the maxinum recursion


def getlist(n=1000):
    import random
    """
    n is the num of list
    return list1, in order sequence
    return list2, disorder sequence
    """
    list1=[i for i in range(n)]
    list2=random.sample(range(n*5),n)
    return list1,list2


def ftime(l=None,T=None):
    import time
    """
    l is the input sequence
    T is the data structure's instance
    return the time
    """
    if l==None or T==None:
        raise KeyError('invalid parameter.')
    time1=time.time()
    for i in l:                              # perform set method
        T[i]=i
    for i in l:                              # perform get method
        T[i]
    for i in l:
        del T[i]                             # perform del method
    return time.time() - time1


def text(n=10000):
    l1, l2 = getlist(n)                      # if there are too many node,  python will break
    splay1 = ftime(l1,STM())
    splay2 = ftime(l2,STM())
    avl1 = ftime(l1,AVLTM())
    avl2 = ftime(l2,AVLTM())
    rbt1 = ftime(l1,RBTM())
    rbt2 = ftime(l2,RBTM())
    print('Ordered:')
    print('splay:', splay1)
    print('avl:', avl1)
    print('rbt:', rbt1)
    print('out-of-order:')
    print('splay:', splay2)
    print('avl:', avl2)
    print('rbt:', rbt2)

###############################################################################################################  


# 11.62 Make a SkipTale class


# Redo the previous exercise, including an implementation of skip lists(See Exercise P-10.53.)


import random


class SkipTable:
    """key is class int"""
    #----------------------------------------------------_Chain--------------------------------------------
    class _Chain:
        #------------------------------------------------_Item---------------------------------------------        
        class _Item:
            """The construction method of _Item"""
            def __init__(self,k,v,after,below):
                # input (key, value, after, below)
                self._key = k
                self._value = v
                self._after = after
                self._below = below
            def __eq__(self, other):
                if isinstance(other,int):            # if other is int
                    return self._key == other
                return self._key == other._key       # compare items based on their keys
            def __ne__(self, other):
                return not (self == other)           # opposite of __eq__
            def __lt__(self, other):
                if isinstance(other, int):           # if other is int
                    # print(self._key,other)
                    return self._key < other
                return self._key < other._key        # compare items based on their keys
            def __gt__(self,other):
                if isinstance(other, int):           # if other is int
                    return self._key > other                
                return self._key > other._key    
            def __le__(self,other):
                # print(self._key,self._value)
                if isinstance(other, int):           # if other is int
                    return self._key <= other                
                return self._key <= other._key    
        #--------------------------------------------------------------------------------------------------
        def __init__(self):
            # The construction method of _Chain
            # create a chain with head and tail
            self._head = self._Item('k_min', 'v_min', None, None)      # the min item
            self._tail = self._Item('k_max', 'v_max', None, None)      # the max item
            self._head._after = self._tail           # conbine the head and tail
            self._size = 0
        def tail(self):
            return self._tail
        def __len__(self):
            return self._size
        def key(self, item):
            return item._key
        def first(self):
            return self._head
        def after(self, item):
            return item._after
        def below(self, item):
            return item._below
        def add_after(self, item, new):
            # add (new) after the item,only horizontal
            new._after = item._after  
            item._after = new
            self._size += 1
            return new
        def del_after(self, item):
            # delete after the node, only horizontal
            temp = item._after
            item._after = temp._after
            temp._after = None
            self._size -= 1
            return temp
    #--------------------------------------------------------------------------------------------------
    # Construction method of SkipTable
    def __init__(self):
        self._table = [self._Chain()]                # store the skipchain
        self._size = 0                               # len of the skipTable
    def __setitem__(self, k, v):
        self.insert(k, v)
    def __getitem__(self, k):
        # get the item or raise error
        index, temp = self.search_before(k)
        chain = self._table[index]
        ras = chain.after(temp)
        if ras._key != k:
            raise ValueError('no item')
        return ras._value
    def __delitem__(self, k):
        self.delete(k)
    def __len__(self):
        return self._size
    def _coin(self):
        # return a num of the level the item should be
        times = 0
        while random.randint(0, 1) == 1:
            times += 1                    # if the random is 1 ,times +=1
        return times
    def search_before(self, k, high=None):
        """
        find the node before item that key is k or like k;
        return (index,temp)
        if k in this chain, return the index of chain and item before k;
        if k not in the chain, returnn high  
        """
        # print(k,high,len(self._table))
        chain = self._table[-1]                      # the top chain
        temp = chain.first()                         # the min node
        if high == None:                             # vague search for insert
            high = 0
        for i in range(len(self._table)-1, high-1, -1):  # inverse order traver the table
            # print(chain.tail() is chain.after(temp),temp,temp._value) 
            # if next node isn't tail or bigger than item           
            while chain.after(temp) is not chain.tail() and chain.after(temp) <= k:                   
                if chain.after(temp) == k:
                    return (i, temp)                 # return index of chain and temp at not buttom level
                temp = chain.after(temp)
            if i == high:                            # end of the table
                return (i, temp)
            temp = chain.below(temp)                 # change the chain    
            chain = self._table[i-1]
    def append_chain(self):
        # append a new chain and conbine the head and tail
        self._table.append(self._Chain())
        self._table[-1]._head._below = self._table[-2]._head    
        self._table[-1]._tail._below = self._table[-2]._tail
    def insert(self, k, v):
        """
        caculate the times of coin;
        add item at position where it should be;
        conbine the below
        """
        h = self._coin()
        while h >= len(self._table):
            self.append_chain()                      # if the level is lower than h ,append it
        index, temp = self.search_before(k, h)       # (chain index , positions)         
        chain = self._table[index]
        if chain.after(temp)._key == k:              # if k in the table,change it
            return self.change(k, v)
        c_temp = self._Chain._Item(k, v, None, None) # current item
        b_temp = self._Chain._Item(k, v, None, None) # below item        
        self._size += 1                              # size +1        
        for i in range(index, -1, -1):               # trave the level from level index to 0
            chain.add_after(temp, c_temp) 
            c_temp._below = b_temp                   # conbine the below
            c_temp = b_temp                          # exchange item
            b_temp = self._Chain._Item(k, v, None, None)
            if i == 0:                               # end of the chain
                return None
            temp = chain.below(temp)                 # change the below chain
            chain = self._table[i-1]
            # print(chain.after(temp) is chain.tail(),chain.after(temp)._key, chain.tail()._key)
            while chain.after(temp) is not chain.tail() and chain.after(temp) < k:
                temp = chain.after(temp)             # chagne the temp
    def change(self, k, v):
        # delete and insert
        self.delete(k)
        self[k] = v
    def delete(self, k):
        # delete k or raise error
        index,temp = self.search_before(k)           # find the item front k
        if self._table[index].after(temp)._key != k:
            raise ValueError('none item')
        chain = self._table[index]
        for i in range(index, -1, -1):               # trave the level from level index to 0
             del_item = chain.del_after(temp)        # cut the after link
             del_item._below = None                  # cut the below link
             if i == 0:                              # end of the chain
                 return None
             temp = chain.below(temp)
             chain = self._table[i-1]
             while chain.after(temp) != k:           # fand the new temp
                 temp = chain.after(temp)


def getlist(n=1000):
    import random
    """
    n is the num of list
    return list1, in order sequence
    return list2, disorder sequence
    """
    list1=[i for i in range(n)]
    list2=random.sample(range(n*5),n)
    return list1,list2


def ftime(l=None, T=None):
    import time
    """
    l is the input sequence
    T is the data structure's instance
    return the time
    """
    if l == None or T == None:
        raise KeyError('invalid parameter.')
    time1 = time.time()
    for i in l:                                      # perform set method
        T[i] = i
    for i in l:                                      # perform get method
        T[i]
    for i in l:
        del T[i]                                     # perform del method
    return time.time() - time1


if __name__ == '__main__':              
    n = 10000
    l1, l2 = getlist(n)                              # if too many node,  python will break
    t1 = ftime(l1, SkipTable())
    print('skiptable:',t1)
    t2 = ftime(l2, SkipTable())
    print('skiptable:', t2)


# Output:

"""
skiptable: 0.6429965496063232
skiptable: 0.8079638481140137
"""

###############################################################################################################  


# P-11.63 Implement the Map ADT using a (2,4) tree. (See Section 10.1.1.)

# tree24.py


class TreeMap24:
    BLANK = object()                         # in down_split method, substitute other node
    class Position:
        """position class"""
        def __init__(self,node,container):
            self._node = node
            self._container = container
        def element(self):
            # return value of position
            return self._node._value
        def key(self):
            return self._node._key
        def __eq__(self,other):
            return type(self) == type(other) and self._node is other._node
    class _Node:
        """creat the link node"""
        def __init__(self, k, v, before=None, after=None, parent=None, child=None):
            self._key    = k
            self._value  = v
            self._before = before
            self._after  = after
            self._parent = parent
            self._child  = child
        #-------------------------------------------------------Utility Methods----------------------------------------------------        
        def __eq__(self, k):
            # return true, if k==self._key
            if type(k) ==int:
                return self._key == k
            elif isinstance(k,type(self)):
                return self._key == k._key
        def __nq__(self, k):
            return not self == k
        def __lt__(self, k):
            # return true if k < self._key
            if type(k) ==int:
                return self._key < k
            elif isinstance(k, type(self)):
                return self._key < k._key
        def __gt__(self, k):
            return not self < k and self != k
        def __le__(self, k):
            return self < k or self == k
        def __ge__(self, k):
            return self > k or self == k
    #--------------------------------------------------------------------------------------------------------------------------------
    # Construction method of Tree24
    def __init__(self):
        # root return the first node
        self._root = None
        self._size = 0
    def _validate(self, p):
        # Return associated node, if position is valid.
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:               # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self, node):
        # return position of node
        return self.Position(node, self) if node != None else None
    def _add_after(self, p, temp, head_node=None):
        # add a node after p,p is Position class; reconect node's after,before parent,without child.
        node = self._validate(p)
        # temp's before is node,after is node's after parent is node's parent
        temp._before = node
        temp._after  = node._after
        temp._parent = node._parent
        node._after  = temp
        if temp._after is not None:
            temp._after._before = temp
        if head_node is not None:
            while temp is not None:      # repoint child's parent，_add_beofre method can't repoint
                subnode = temp._child
                while subnode is not None:
                    subnode._parent = head_node
                    subnode = subnode._after
                temp = temp._after
        return self._make_position(temp)
    def _add_before(self, p, temp, head_node=None):
        """
        this method can only be used for p which before node is none;
        add a node before p,p is Position and head node;
        temp is a _Node;
        head_node is _Node class;
        reconnect node's child, parent'before and after.
        """
        node = self._validate(p)
        # temp's before is node._before,after is node, parent is node._parent
        if temp._before is not None and temp._child is None:  # in case 2.1 of down_split method
            temp._child = node._before
        else:
            temp._before = node._before
        temp._after = node
        temp._parent = node._parent
        node._before = temp
        parent = self.parent(p)
        if parent is None:
            self._root = temp
        else:
            parent = self._validate(parent)
            if parent._before is node:
                parent._before = temp
            if parent._child is node:
                parent._child = temp
        tempnode = temp
        if head_node is not None:
            while tempnode is not None:           # repoint child's parent，
                subnode = tempnode._child
                while subnode is not None:
                    subnode._parent = head_node
                    subnode = subnode._after
                tempnode = tempnode._after
        return self._make_position(temp)          # now temp is the head
    def _add(self, p, k, v, head):
        # add a node in a proper posiiton
        node = self._validate(p)
        temp = self._Node(k, v)
        self._size += 1
        if node < k:
            self._add_after(p,temp)
            self._up_split(head)
        else:
            self._up_split(self._add_before(p, temp, temp))
    def _search(self, k, head=None, node=None):
        """
        return the proper Position and head if chain's child is None; find begin of root if node is None
        head and node are _Node class
        """
        if node is None:
            node = self._root
            head = node
        # print(node, k, self._root)
        if node > k:                              # recursion to node's before
            if node._before is None:              # break the cursion if there is none child
                return self._make_position(node),self._make_position(head)
            return self._search(k, node._before, node._before)
        if node == k:                             # break the cursion
            return self._make_position(node),self._make_position(head)
        if node < k:                              # recursion to node's after
            if node._after is not None:           # if there is item after node
                if k < node._after:               # node<k<node._after
                    if node._child is None:       # node is the last node
                        return self._make_position(node), self._make_position(head)
                    return self._search(k, node._child, node._child)
                else:                             # noke._after <k
                    return self._search(k, head, node._after)
            else:
                if node._child is None:           # if node is last Position
                    return self._make_position(node), self._make_position(head)
                return self._search(k, node._child, node._child)
    def _up_split(self, head):
        # head is a Position class      
        if self.is_filled(head):
            node = self._validate(head)
            mid = node._after._after              # split in to tree parts, (node,mid,p2)
            p2 = mid._after                       # p2 is the mid's child            
            parent = node._parent
            # combine the tree parts
            node._after._after = None
            p2._before = mid._child
            mid._child = p2
            p2._parent = parent                   # if parent is None , p2._parent is mid
            temp = p2._before
            while temp is not None:               # p2 became a head node ,repoint child and child._after
                temp._parent = p2
                temp = temp._after
            temp = p2._child
            while temp is not None:
                temp._parent = p2
                temp = temp._after
            # find the proper position for mid
            if parent is not None:  # if node isn't root
                parent = self._validate(self.parent(self._make_position(node))) # get the parent node
                if parent > mid:
                    if parent._before is node:    # if mid add to the head ,the node and p2's parent should be mid
                        self._add_before(self._make_position(parent),mid,mid)
                        node._parent = mid
                        node._after._parent = mid
                        return self._up_split(self._make_position(mid))
                    mid._before = parent._before
                    mid._before._after = mid
                    mid._after = parent
                    parent._before = mid
                    mid._parent = parent._parent                                                
                if parent < mid:
                    self._add_after(self._make_position(parent),mid)
                return self._up_split(self._make_position(node._parent))# Prevent overflow from passing upwards
            else:                                 # if node is root
                self._root  = mid                 # make mid is the root
                mid._before = node
                mid._after  = None
                mid._parent = None
                node._parent = mid                # the node and p2 's parent should be mid
                node._after._parent = mid
                p2._parent = mid
    def _pop(self, p, head):
        # warrring pop need to be devided in to situations
        """
        cut all links related p;
        p is the Position;
        p._before will be p._after._before and the p._child need to be None
        """
        node = self._validate(p)
        after = node._after
        if after is not None:     
            before = node._before
            self._pointer_repoint(self._make_position(node._after),p,head)
            after._before = before               # repoint node's after node, node._after._before node
        else:
            self._pointer_repoint(None, p, head)
        return self._make_position(node)
    def _replace(self, p, position, head):
        # substitue position for p and return position
        node = self._validate(p)
        p_node = self._validate(position)
        if p_node._parent is not node:
            node._parent = p_node._parent
        node._child = p_node._child
        node._before = p_node._before
        node._after = p_node._after
        self._pointer_repoint(p, position, head)
        return position
    def _pointer_repoint(self, p, position, head):
        # the pointer to position repoints p； when p is root and p.after is not empty,let p.after be root
        if p is not None:                          # in case p is None,when _pop() method
            node = self._validate(p)
        else:
            node = None
        p_node = self._validate(position)
        if p_node is self._root:                   # if position is root node
            self._root = node
        if position == head:                       # repoint node's child and parent
            parent = self._validate(self.parent(position)) if p_node._parent is not None else None
            # all of child repoint to node
            temp = p_node._before                  # before fraction
            while temp is not None:
                temp._parent = node
                temp = temp._after
            temp_node = p_node                     # child fraction
            while temp_node is not None:
                temp = temp_node._child
                while temp is not None:
                    temp._parent = node
                    temp = temp._after
                temp_node = temp_node._after
            if parent is not None:                 # repoint parent's child
                if parent._before is p_node:
                    parent._before = node
                else:
                    parent._child = node
        else:                                      # if node is not head
            p_node._before._after=node
        if p_node._after is not None:              # repoint node's after node, node._after._before node
            p_node._after._before = node
        p_node._parent = None
        p_node._after  = None
        p_node._before = None
        p_node._child  = None
    def _brother(self, p, r=True):
        # return p's brother node; if r is Flase,denote the method working for recursion；
        node = self._validate(p)
        parent = self._validate(self.parent(p))
        parent_h = node._parent
        if parent._before is node:                 # get brother
            brother = parent._child
            brother_head = brother
        else:
            brother1 = parent._before if parent is parent_h else parent._before._child
            brother_head = brother1
            while brother1._after is not None:
                brother1 = brother1._after
            if r:
                brother2 = parent._after._child if parent._after is not None else None
                if not self.is_singular(self._make_position(brother2)) and self.is_singular(self._make_position(brother_head)):
                    brother = brother2
                    brother_head = brother2
                else:
                    brother = brother1
            else:
                brother = brother1
        return self._make_position(brother), self._make_position(brother_head)
    def _down_split(self, position, r=True):
        """
        cut chain of position ;
        case 1 :
            position's brother is not singular
        case 2 :
            position's brother is singular
            case 2.1 :
                position's parent is singular  (this way need recursion)
            case 2.2 :
                position's parnet is not singual
        """
        node = self._validate(position)
        parent = self._validate(self.parent(position))
        parent_h = node._parent           # parent_h is parent's head
        brother, brother_head = self._brother(position, r)
        brother = self._validate(brother)
        if not self.is_singular(brother_head) and r:        # case 1
            brother_parent = self.parent(brother_head)
            temp1 = self._pop(self._make_position(brother),brother_head)
                # replace temp1 with parent
            if node > brother:        # there are different parents when different size relationship of brother and node
                temp2 = self._replace(temp1, self._make_position(parent), self._make_position(parent_h))
            else:
                temp2 = self._replace(temp1, brother_parent, self._make_position(parent_h))
            # replace temp2 with position
            temp3 = self._replace(temp2, position, position)
            return temp3
        else:                                                # if brother is singular,case 2
            if self.is_singular(self._make_position(parent_h)):        # case 2.1
                blank_node = self._Node(parent._key, TreeMap24.BLANK)
                blank = self._make_position(blank_node)
                temp1 = self._replace(blank, self._make_position(parent), self._make_position(parent))   # replace parent Position
                self._replace(temp1, position, position)     # replace position with parent
                if brother > parent:
                    blank_node._before = None
                    self._add_before(self._make_position(brother), parent,parent)
                    brother_head = self._make_position(parent)
                    if blank_node < blank_node._parent:      # Deal with the before and child value issues of blank nodes
                        blank_node._before, blank_node._child = blank_node._child, blank_node._before
                else:
                    blank_node._child = None
                    self._add_after(self._make_position(brother), parent, self._validate(brother_head))
                    if blank_node > blank_node._parent:      # Deal with the before and child value issues of blank nodes
                        blank_node._before, blank_node._child = blank_node._child, blank_node._before
                if blank_node._parent is None:               # if blank is root
                    blank_node._before = blank_node._child if blank_node._child is not None else blank_node._before   # incase pop the node
                    blank_node._child = None
                    self._pop(blank, blank)
                    self._root = self._validate(brother_head) if self._validate(brother_head) < parent else parent
                    return self.root()
                # in case node is filled
                if self.is_filled(brother_head):
                    blank_node._before, blank_node._child = blank_node._child, blank_node._before
                    self._up_split(brother_head)
                    if parent < brother and blank_node._before is None:      # let new node be the _before of blank_node
                        blank_node._before = blank_node._child
                    blank_head = blank if blank_node < brother else self._make_position(blank_node._before)
                    self._pop(blank, blank_head)
                    return None
                return self._down_split(blank, False)
            else:                                            # if parent is not sigular ,case 2.2
                TEMP = self._make_position(self._Node(TreeMap24.BLANK, TreeMap24.BLANK))         # TEMP  uesed to repalce parent node
                self._replace(TEMP, self._make_position(parent), self._make_position(parent_h))  # parent Position
                res = self._replace(self._make_position(parent), position, position)             # position Position
                if brother > parent:                  # add the older parent to brother
                    self._add_before(self._make_position(brother), parent, parent)
                    brother_head = self._make_position(parent)
                else:
                    self._add_after(self._make_position(brother), parent, self._validate(brother_head))
                if parent_h is parent:                # delete temp
                    if parent < brother:              # let new node be the left node of TEMP
                        TEMP._node._before = TEMP._node._child  # for _pop mtehod
                    TEMP._node._child = None          # let parent._before be parent._after._before for the pop method
                    parent_h = TEMP
                else:
                    parent_h = self._make_position(parent_h)
                self._pop(TEMP, parent_h)
                self._up_split(brother_head)
                return self._make_position(res)
    def _subnode(self, p, head):
        # find the subnode which should lt p of p
        node = self._validate(p)
        if p == head:
            temp = node._before
        else:
            temp = node._before._child
        head = temp
        if temp is not None:
            while temp._after is not None or temp._child is not None:
                while temp._after is not None:
                    temp = temp._after
                if temp._child is not None:
                    temp = temp._child
                    head = temp
            return self._make_position(temp), self._make_position(head)
        else:
            return None, None
    def _before(self,p,head):
        """ 
        p is position ,head is p's head and a position;
        return position and head,position less than p 
        """
        node = self._validate(p)                            # find a proper subtree to search
        if node._before is None:   # node is leaf node
            if node._parent is None:                        # if p is the root node
                return None,None
            head = node._parent
            temp = self._validate(self.parent(p))
            while temp._before is node: # looking up to the top, find the before the node
                node = temp
                head = temp._parent
                temp = self._validate(self.parent(self._make_position(temp)))
                if temp is None:                            # if p is the leftmost node
                    return None, None
            if temp._before is not node:
                return self._make_position(temp), self._make_position(head)
        else:
            temp = node._before                             # temp is the target node
            if p == head :                                  # if p is not head node
                return self._search(node._key, temp, temp)
            elif temp._child is not None:
                temp = temp._child
                return self._search(node._key, temp, temp)
            else:
                return self._make_position(temp), head
    def _next(self, p, head):
        """ 
        p is position ,head is p's head and head is position
        return position and head,position great than p
        """
        node = self._validate(p)
        if node._child is not None:
            return self._search(node._key, node._child, node._child)
        if node._after is not None:
            return self._make_position(node._after),head
        temp = self._validate(self.parent(head))            # parent's child or before node is head
        head = self._make_position(node._parent)            # get the parent 's head
        while temp <= node:                                 # lookup the parent's node
            if temp._after is not None:                     # if the parent has after node to return it, else travel to the top of the tree
                return self._make_position(temp._after), head
            head,temp = self._make_position(temp._parent), self._validate(self.parent(head))
        return self._make_position(temp), head
    def _generate(self, p, head):
        """
        recuisively yield _Node;
        n,head are class _Node;
        if return whole tree,p and head should convey both self._root.
        """
        if p is None:
            return
        if p is head:
            for i in self._generate(p._before, p._before):
                yield  i
        yield self._make_position(p)
        for i in self._generate(p._child, p._child):
            yield i
        for i in self._generate(p._after, head):
            yield i
    def _get_head(self, n):
        # n is a Position, returning a node that is a Position
        n = self._validate(n)
        if n._child is not None:
            return self._make_position(n._child._parent)
        else:
            while n._before is not None:
                n = n._before
            return self._make_position(n) 
    def __len__(self):
        return self._size
    def __setitem__(self, k, v):
        if len(self) == 0:
            self._root = self._Node(k,v)
            self._size += 1
            return
        node, head = self._search(k)                  # get the position and head
        if node.key() == k:
            node._node._value = v
        else:
            self._add(node, k, v, head)
    def __delitem__(self, k):
        position, head = self._search(k)              # delete node
        self._size -= 1
        if position.key() != k:
            raise KeyError('key warring')
        subs, subs_head = self._subnode(position, head)
        if subs is not None:                          # dispose the position
            if self.is_singular(subs_head):
                self._down_split(subs)
                if self._validate(position)._parent is not None:    # in case head is changed,research position
                    t, head = self._search(position.element(), self._validate(position)._parent, self._validate(position)._parent)
                else :
                    t, head = position, self.root()
            else:
                self._pop(subs, subs_head)
            return self._replace(subs, position, head)
        else:
            if self.root() == position:            # if tree only has root node
                self._pop(position, position)
                self._size = 0
                return
            else:
                if self.is_singular(head):         # if position is a leaf node , a head
                    return self._down_split(position)
                else:
                    return self._pop(position, head)
    def __getitem__(self, k):
        """
        return value of Position which key ==k,
        raise KeyError if k not find
        """
        p,head = self._search(k)
        if p.key() == k:
            return p.element()
        else:
            raise KeyError('invalid key')
    def __contains__(self, k):
        p,head = self._search(k)
        if p.key() == k:
            return True
        else:
            return False
    def __iter__(self):
        for i in self._generate(self._root, self._root):
            yield i.element()
    def get(self, k, d):
        # if k is found return k.element else return d
        p, head = self._search(k)
        return p.element() if p.key() == k else d
    def is_filled(self,head):
        # return True, If the head is connected to two nodes
        head = self._validate(head)
        n = 1
        while head._after is not None:
            head = head._after
            n += 1
        return n == 4                               # 4 is the  maxinum
    def is_singular(self,head):
        if head is None:
            return True        
        node = self._validate(head)
        return node._after is None
    def root(self):
        return self._make_position(self._root)
    def parent(self, p):
        """
        find p's parent position;
        p have to be  a head node.
        """
        node = self._validate(p)
        parent = node._parent
        if parent is None:
            return None
        while not ( parent._before is node or parent._child is node):   
            parent = parent._after            
        return self._make_position(parent)
    def items(self):
        return [(i.key(), i.element()) for i in self._generate(self._root, self._root)]
    def pop(self, k, d=None):
        if d is None:
            raise KeyError('d have be not None')
        try:
            self.__delitem__(k)
        except KeyError:
            return d
    def popitem(self):
        import random
        seed = random.randint(0,len(self))                            
        for i in self._generate(self._root, self._root):
            if seed == 0:
                break           
            seed -= 1
        self.__delitem__(i.key())
        return (i.key(), i.element())
    def setdefault(self, k, d):
        if len(self) == 0:
            self._root = self._Node(k,d)
            self._size += 1
            return None
        node, head = self._search(k)   # get the position and head
        if node.key() == k:
            return node.element()
        else:
            self._add(node, k, d, head)
    def find_min(self):
        # return first node of _generate
        temp=next(self._generate(self._root,self._root))
        return temp.key(),temp.element()
    def find_max(self):
        # find the last and rightmost node
        temp=self._root
        while temp._after is not None:
            temp=temp._after
        while temp._child is not None:
            temp=temp._child
            while temp._after is not None:
                temp=temp._after
        return temp._key,temp._value
    def find_lt(self,k):
        p,h=self._search(k)
        if p.key()==k:
            p,h=self._before(p,h)
        return p.key(),p.element()
    def find_le(self,k):
        p, h = self._search(k)
        return p.key(),p.element()
    def find_gt(self,k):
        p,h=self._search(k)
        p,h=self._next(p,h)
        return p.key(),p.element()
    def find_ge(self,k):
        p,h=self._search(k)
        if p.key()!=k:
            p,h=self._next(p,h)
        return p.key(),p.element()
    def find_range(self,start,stop=None):
        # start and stop is key
        if stop==None:
            stop=start
            start=self.first().key()    # define the initial number of start
        if stop < start or stop>len(self):
            raise IndexError('parameter is invalid')
        nex,h=self._search(start)    # find the first node
        while 1:            # get the next node in cycles
            yield nex.element()
            if nex.key()< stop-1:
                nex,h=self._next(nex,h)
            else:
                break
    def reversed(self):
        # return k all of the tree that reversed iter
        walk=self.last()
        head=self._get_head(walk)
        yield walk.element()
        for i in range(len(self)-1):
            walk,head=self._before(walk,head)
            yield walk.element()
    def first(self):
        # find the mininum node ,return it's Position
        walk=self._root
        while walk._before is not None:
            walk=walk._before
        return self._make_position(walk)
    def last(self):
        # find the maxnium node ,return it's Position
        walk=self._root
        while 1:                        # find the node which is the max k.
            while walk._after is not None:
                walk=walk._after
            if walk._child is not None:
                walk=walk._child
                head=walk
            else:
                break
        return self._make_position(walk)
    def before(self,p):
        # p is a Position,return a Position
        head = self._get_head(p)
        po, he = self._before(p,head)
        return po
    def after(self,p):
        # p is a Position, return a Position
        head = self._get_head(p)
        po, he = self._next(p, head)
        return po
    def find_position(self,k):
        # if k in the tree return a Position that belong k, else raise Error
        p,h=self._search(k)
        if p.key() == k:
            return p
        else:
            raise KeyError('invalid key')


if __name__ == '__main__':
    o = 100
    t = TreeMap24()
    # del test
    for i in range(o):
        t[i] = str(i)+'#'
    for i in range(o):
        del t[i]
    print('order done')
    for i in range(o):
        t[i] = str(i)+'#'
    for i in range(o-1, -1, -1):
         # print(i)
        del t[i]
    print('reverse order done')
    """
    # test del from the midst
    for i in range(o):
        t[i] = str(i)+'#'
    for i in range(o//2, -1, -1):
        # print(i)
        del t[i]
    print('midst previous done')
    for i in range(o//2+1,0):
        # print(i)
        del t[i]
    print('midst afterwards done')
    print(3 in t)
    print(t.get(-3,'d'))
    print(t.items())
    # del t
    # print(t)
    print(iter(t))
    print(t.pop(-3, 'test pop'))
    print(t.popitem())
    print(t.setdefault(-3,'-3#'), t[-3])
    """


# Output:

"""
order done
reverse order done
"""

###############################################################################################################  


# P11.64 Call (2,4) Tree

# Redo the previous exercise, including all methods of the Sorted Map ADT. (See Section 10.3.)


if __name__ == '__main__':
    t = TreeMap24()
    for i in range(1000):
        t[i] = str(i)+"#"
    print(t.find_min())
    print(t.find_max())
    print(t.find_lt(500))
    print(t.find_le(500))
    print(t.find_gt(500)) 
    print(t.find_ge(500))
    for i in t.find_range(1000):
        print(i)
    for i in t.reversed():
        print(i)


# Output:

"""
(0, '0#')
(999, '999#')
(499, '499#')
(500, '500#')
(501, '501#')
(500, '500#')
0#
1#
2#
3#
4#
5#
6#
7#
8#
9#
10#
...
"""

###############################################################################################################  


# P11.65 Call (2,4) Tree

"""
Redo Exercise P-11.63 providing positional support, as we did for binary search trees (Section 11.1.1), 
so as to include methods first(), last(), before(p), after(p), and find position(k). Each item should have 
a distinct position in this abstraction, even though several items may be stored at a single node of a tree.
"""

if __name__ == '__main__':
    t = TreeMap24()
    for i in range(1000):
        t[i] = str(i)+'#'
    a = t.first()
    b = t.last()
    print(a.element(), t.after(a).element())
    print(b.element(), t.before(b).element())
    print(t.find_position(999).element())
    print(t.find_position(333).element())


# Output:

"""
0# 1#
999# 998#
999#
333#
"""
###############################################################################################################  


# P11.66 Write a Python class that can take any red-black tree and convert it into its
# corresponding (2,4) tree and can take any (2,4) tree and convert it into its
# corresponding red-black tree.


# Convert between Red Black Tree and (2,4) Tree


from red_black_tree import RedBlackTreeMap as RBT
from tree24 import TreeMap24 as TM2
from queue import Queue


class Convert(RBT, TM2):
    """convert RedBlackTree to 24TreeMap or covert 24TreeMap to RedblackTree"""
    def __init__(self):
        if 'y' == input('define Tree24 pressing y else pressing others: '):
            self._tree = TM2()
            self._arm = RBT()
        else:
            self._tree = RBT()
            self._arm = TM2()
        self._rbt = Queue()
        self._tm = Queue()
    def __getitem__(self, k):
        return self._tree[k]
    def __setitem__(self,k,v):
        self._tree[k]=[v]
    def _convertRBT(self, chain):
        """
        convent 2_3_4tree's node to RedBlackTree;
        return black node
        chain is a _Node of TM2;
        there are 3 kind of case;case1 there are 3 node,;case2 there are 2 node;case 1 there is 1 node.
        """
        first = RBT._Node(RBT._Item(chain._key, chain._value))
        second = RBT._Node(RBT._Item(chain._after._key, chain._after._value)) if chain._after is not None else None
        third = RBT._Node(RBT._Item(chain._after._after._key, chain._after._after._value)) if (chain._after is not None and chain._after._after is not None)else None
        if self._rbt.empty():
            self._arm._root = second if second is not None else first
        if second is not None:                        # case there are 2 or 3 number of node
            second._red = False                       # set second black
            self._combine(second,first,False)
            self._rbt.put((first,'l'))                # case 1:input queue
            self._rbt.put((first,'r'))
            if third is not None:
                self._combine(second,third)
                self._rbt.put((third,'l'))            # case 2:input queue
                self._rbt.put((third,'r'))
                return second
            else:
                self._rbt.put((second,'r'))
                return second
        else:
            first._red = False                        # set first black
            self._rbt.put((first,'l'))                # case 3:input queue
            self._rbt.put((first,'r'))
            return first
    def _combine(self, parent, child, right=True):
        """
        combine parent and right child if right is True,else combine parent and left child ;
        parent and child is _Node of RedBlackTreeMap.
        """
        if right:
            parent._right = child
        else:
            parent._left = child
        child._parent = parent
    def _circleRBT(self):
        # control 24TreeMap converning to RBT
        if self._tm.empty():
            return
        walk = self._tm.get()
        res = self._convertRBT(walk)
        if walk._before is not None:                  # if walk is leaf node return
            self._tm.put(walk._before)                # else put child to self._tm
            while walk is not None:             
                self._tm.put(walk._child)
                walk = walk._after
        black = res
        if black==self._arm._root:
            return None                               # Don't conbine the walk when first allocate the method
        info = self._rbt.get()
        if info[1] == 'r':
            self._combine(info[0], black)
        else:
            self._combine(info[0], black, False)
    def _convertTM(self, black):
        """
        convert node of RedBlackTree to 234TM node;
        put position to _tm
        """
        second = TM2._Node(black._element._key,black._element._value)
        first = TM2._Node(black._left._element._key, black._left._element._value) if (black._left is not None and black._left._red) is True else None
        third = TM2._Node(black._right._element._key, black._right._element._value) if (black._right is not None and black._right._red)is True else None
        second._before = first
        second._after = third
        if self._tm.empty():                    # set root node
            self._arm._root = first if first is not None else second
        head = second
        if first is not None:
            head = first
            first._after = second
            self._tm.put((first, False, head))        # put (first,judge) to _tm, if the judge is Ture meaning _before node
            self._tm.put((first, True, head))
        else:
            self._tm.put((second, False, head))
        if third is not None:
            third._before = second
            self._tm.put((third, False, head))
            self._tm.put((third, True, head))
        else:
            self._tm.put((second, True, head))
        return head
    def _combineTM(self, parent, head, child, right):
        # In a 24Tree, conbine child to its parent's child,if parameter right is True.
        if right:
            parent._child = child
        else:
            if head is not parent:                    # case in 2node or 3node
                parent._before._child = child
            else:                                     # case in 1node
                parent._before = child
        while child is not None:        # repoint to parent
            child._parent = head
            child = child._after
    def _circleTM(self):
        walk = self._rbt.get()
        res = self._convertTM(walk)
        if walk._left is not None :
            if walk._left._red is True:               # if walk._left is red
                if walk._left._left is not None:            
                    self._rbt.put(walk._left._left)   # this node have to be a black
                    self._rbt.put(walk._left._right)
            else:
                self._rbt.put(walk._left)
        if walk._right is not None:
            if walk._right._red is True:
                if walk._right._left is not None:
                    self._rbt.put(walk._right._left)
                    self._rbt.put(walk._right._right)
            else:
                self._rbt.put(walk._right)
        parent = res
        if parent == self._arm._root:
            return None                               # Don't conbine the walk when first allocate the method
        info=self._tm.get()
        self._combineTM(info[0], info[2], parent, info[1])
    def changeTM(self):
        # convert RBT to 234TM
        if len(self._tree) == 0:
            raise ValueError('There is no item.')
        self._rbt.put(self._tree._root)
        while not self._rbt.empty():
            self._circleTM()
        self._arm._size = self._tree._size            # set size of arm
    def arm(self):
        return self._arm
    def changeRBT(self):
        # convert 234 tree to RBT
        if len(self._tree) == 0:
            raise ValueError('There is no item.')
        self._tm.put(self._tree._root)
        while not self._tm.empty():
            self._circleRBT()
        self._arm._size = self._tree._size            # set size of arm


if __name__ == '__main__':
    # Test Tree24 converted to RBT
    t = Convert()
    for i in range(100):
        t[i] = str(i)
    t.changeRBT()
    a = [i for i in t.arm().__iter__()]
    for i in range(100):                             # text if equal
        if i not in a:
            print(i, '*')
    # Test convertion from RBT to 24 Tree
    t = Convert()
    for i in range(100):
        t[i] = str(i)
    t.changeTM()
    a = [i for i in t.arm().__iter__()]
    print(a)


# Output:

"""
define Tree24 pressing y else pressing others: y
define Tree24 pressing y else pressing others: others
[['0'], ['1'],  ['2'],  ['3'],  ['4'],  ['5'],  ['6'],  ['7'],  ['8'],  ['9'], 
['10'], ['11'], ['12'], ['13'], ['14'], ['15'], ['16'], ['17'], ['18'], ['19'], 
['20'], ['21'], ['22'], ['23'], ['24'], ['25'], ['26'], ['27'], ['28'], ['29'], 
['30'], ['31'], ['32'], ['33'], ['34'], ['35'], ['36'], ['37'], ['38'], ['39'], 
['40'], ['41'], ['42'], ['43'], ['44'], ['45'], ['46'], ['47'], ['48'], ['49'], 
['50'], ['51'], ['52'], ['53'], ['54'], ['55'], ['56'], ['57'], ['58'], ['59'], 
['60'], ['61'], ['62'], ['63'], ['64'], ['65'], ['66'], ['67'], ['68'], ['69'], 
['70'], ['71'], ['72'], ['73'], ['74'], ['75'], ['76'], ['77'], ['78'], ['79'], 
['80'], ['81'], ['82'], ['83'], ['84'], ['85'], ['86'], ['87'], ['88'], ['89'], 
['90'], ['91'], ['92'], ['93'], ['94'], ['95'], ['96'], ['97'], ['98'], ['99']]
>>> 
"""

###############################################################################################################  



# 11.67 In describing multisets and multimaps in Section 10.5.3, we describe ageneral approach 
# for adapting a traditional map by storing all duplicates within a secondary container as a 
# value in the map. Give an alternative implementation of a multimap using a binary search tree 
# such that each entry of the map is stored at a distinct node of the tree. With the existence
# of duplicates, we redefine the search tree property so that all items in the left subtree of 
# a position p with key k have keys that are less than or equal to k, while all items in the 
# right subtree of p have keys that are greater than or equal to k. Use the public interface 
# given in Code Fragment 10.17.


# Change dict to AVlTreeMap-


from avl_tree import AVLTreeMap


class MultiMap:
    _MapType = AVLTreeMap                        # MapType refined by subclass
    def __init__(self):
        # Create a new empty multimap instance.
        self._map = self._MapType()              # create map instance for storage
        self._n = 0
    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self._map))
    def __len__(self):
        # Return number of (k,v) pairs in multimap.
        return self._n
    def __iter__(self):
        # Iterate through all (k,v) pairs in multimap.
        for k, secondary in self._map.items():
            for v in secondary:
                yield (k,v)
    def add(self, k, v):
        # Add pair (k,v) to multimap.
        container = self._map.setdefault(k, [])  # create empty list if needed
        container.append(v)
        self._n += 1
    def pop(self, k):
        # Remove and return arbitrary (k,v) pair with key k (or raise KeyError).
        secondary = self._map[k]                 # may raise KeyError
        v = secondary.pop()
        if len(secondary) == 0:
            del self._map[k]                     # no pairs left
        self._n -= 1
        return (k, v)
    def find(self, k):
        # Return arbitrary (k,v) pair with given key (or raise KeyError).
        secondary = self._map[k]                 # may raise KeyError
        return (k, secondary[0])
    def find_all(self, k):
        # Generate iteration of all (k,v) pairs with given key.
        secondary = self._map.get(k, [])         # empty list by default
        for v in secondary:
            yield (k,v)

    
if __name__ == '__main__':
    mm = MultiMap()
    for i in range(10):
        mm.add(i, str(i) + '#')
    print([i for i in mm])


if __name__ == '__main__':
    m = MultiMap()
    m.add('a', 1)
    m.add('b', 2)
    m.add('c', 3)
    m.add('c', 4)
    print(m)

###############################################################################################################  


# P11.68 Prepare an implementation of splay trees that uses top-down splaying as described in 
# Exercise C-11.56. Perform extensive experimental studies to compare its performance to the 
# standard bottom-up splaying implemented in this chapter.


from splay_tree import SplayTreeMap


class STM(SplayTreeMap):
    """rewrite _subtree_search method"""
    def _subtree_search(self, p, k):
        # find the z,y,x then rotate them 
        z = p
        while True:
            y = self.left(z) if z.element()._key > k else self.right(z)
            if y is None:               # can't find k
                return z
            if y.element()._key > k and z.element()._key > k: 
                x = self.left(y)
                if x == None:             
                    self._rotate(y)     # zig 
                else:                   # zig-zig
                    self._rotate(y)
                    self._rotate(x)     
            elif y.element()._key < k and z.element()._key < k:
                x = self.right(y)
                if x == None:
                    self._rotate(y)     # zig
                else:
                    self._rotate(y)     # zig-zig
                    self._rotate(x)
            else:                       # zig-zag
                if x == None:
                    self._rotate(y)     # zig
                else:
                    self._ratate(x)     # zig-zag
                    self._ratate(x)
            if x is not None:           # control circle         
                if x.element()._key == k:
                    return x
                z = x
            else:
                z = y         
    def _rebalance_insert(self,p):
        pass
    def _rebalance_access(self,p):
        pass


if __name__ == '__main__':
    stm = STM()
    for i in range(100):
        stm[i] = str(i) + '#'
    print([i for i in stm])


# Output:


"""
[0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 
80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
"""

###############################################################################################################  


# P11.69 The mergeable heap ADT is an extension of the priority queue ADT consisting of operations 
# add(k, v), min(), remove min() and merge(h), where the merge(h) operations performs a union of 
# the mergeable heap h with the present one, incorporating all items into the current one while
# emptying h. Describe a concrete implementation of the mergeable heap ADT that achieves O(log n) 
# performance for all its operations, where n denotes the size of the resulting heap for the merge 
# operation. 


class Heap:
    """A heap that find the min"""
    class _Node:
        class _Item:
            # The construction of the grand subclass of _Item
            def __init__(self, key, value):
                self._key = key
                self._value = value
            def __eq__(self, k):
                return self._key == k._key
            def __gt__(self, k):
                return self._key > k._key
            def __lt__(self, k):
                return self._key < k._key
        # The construction method of subclass of _Node
        def __init__(self, k, v, parent=None):
            self._parent  = parent
            self._left    = None
            self._right   = None
            self._factor  = 0              # if _factor is 1, preform left deeper than right
            self._element = self._Item(k,v)
        def __eq__(self, k):
            return self._element == k._element
        def __gt__(self, k):
            return self._element > k._element
        def __lt__(self, k):
            return self._element < k._element
    # The construction method of class Heap       
    def __init__(self):
        self._root = None
        self._size = 0
    def _min(self, n1, n2):
        # n1,n2 are self._Node
        if n1 is None:
            return n2
        if n2 is None:
            return n1
        return n1 if n1 < n2 else n2
    def _replace(self,n1,n2):
        # replace n1._element with n2._element
        n1._element,n2._element = n2._element,n1._element
    def _down(self,k):
        # After del method,be used for finding a porper position
        while True:
            child = self._min(k._left,k._right)
            if (child is not None)and k > child:
                self._replace(k,child)
                k = child
            else:
                return
    def _up(self, k):
        # After add method ,be used for find a porper position
        while True:
            if k._parent is not None and k < k._parent:
                self._replace(k, k._parent)
                k = k._parent
            else:
                return
    def _pop(self, walk):
        """
        pop a node that is the k's leaf that is smaller than brother;
        return the node and the hight;
        k is a self._Node.
        """
        h = -1
        while True:                     # find a walk that is the leaf
            h += 1
            if walk._factor > 0:
                    walk = walk._left
            else:
                if walk._right is not None:
                    walk = walk._right
                else:               # now walk._right and walk._left is None
                    break
        if walk is not self._root:
            if walk._parent._factor != 0:     # recalculate the factor if walk's height be change
                temp = walk
                while temp._parent is not None:
                    if self.is_left(temp):
                        temp._parent._factor -= 1
                    else:
                        temp._parent._factor += 1
                    if temp._parent._factor == 0:      # when parent._factor equal zero stop spreading
                        temp=temp._parent
                    else:
                        break
            else:
                if self.is_left(walk):
                    walk._parent._factor -= 1
                else:
                    walk._parent._factor += 1
            if (walk._parent._left is not None) and walk._parent._left is walk: # cut down chain
                walk._parent._left = None
            else:
                walk._parent._right = None
            walk._parent = None
        else:                                         # if there is only one node in Heap
            self._root = None
        self._size -= 1
        return walk, h
    def is_left(self,p):
        return (p is p._parent._left) if p._parent is not None else False
    def is_right(self,p):
        return (p is p._parent._right) if p._parent is not None else False    
    def remove_min(self):
        # favorite is right
        res = self._root._element
        walk = self._pop(self._root)[0]
        if self._root is not None:
            self._replace(walk, self._root)
            self._down(self._root)
        return res._key, res._value
    def min(self):
        return self._root._element._value
    def add(self,k,v):
        # favorite is left 
        self._size += 1
        if self._root is None:
            self._root=self._Node(k, v)
        else:
            walk = self._root
            while True:                 # find the leaf and contorl the factor
                if walk._factor > 0:
                    if walk._right is not None:
                        walk = walk._right
                    else:
                        walk._right = self._Node(k,v,walk)        # add a new _Node
                        walk = walk._right
                        break
                else:
                    if walk._left is not None:
                        walk = walk._left
                    else:
                        walk._left = self._Node(k,v,walk)         # add a new _Node
                        walk = walk._left
                        break
            if walk._parent._factor == 0:         # recalculate the factor if walk's height be changed
                temp = walk
                while temp._parent is not None:
                    if self.is_left(temp):
                        temp._parent._factor += 1
                    else:
                        temp._parent._factor -= 1
                    if temp._parent._factor != 0:        # when parent._factor==0 stop spreading.
                        temp = temp._parent
                    else:
                        break
            else:
                if self.is_left(walk):
                    walk._parent._factor += 1
                else:
                    walk._parent._factor -= 1
            self._up(walk)              # handle the new Node
    def root(self):
        return self._root
    def merge(self, h):
        if not type(self) == type(h):
            raise KeyError('parameter is not isinstance whit Heap')
        last, h1 = self._pop(self._root)
        walk = h.root()
        h2 = 1
        while walk._left is not None:    # caculate the hight of h
            if walk._factor < 0:
                walk = walk._right
            else:
                walk = walk._left
            h2 += 1
        last._factor = h1 - h2
        last._left = self._root           # chain these Heap
        last._right = h.root()
        self._root._parent = last
        h.root()._parent = last
        h._root = None                    # handle the field of self and h
        self._size += h._size
        h._size = 0
        self._root = last
        self._down(self._root)


if __name__ == '__main__':
    t = Heap()
    for i in range(10):
        t.add(i,i)
    print(t.min())
    for i in range(10):
        print(t.remove_min())
    for i in range(20,40):
        t.add(i,i)
    l = Heap()
    for i in range(100):
        l.add(i,i)
    t.merge(l)
    print(t.min())
    for i in range(10):
        print(t.remove_min())
    for i in range(10):
        print(t.remove_min())
    for i in range(100):
        print(t.remove_min())


# Output:

"""
0
(0, 0)
(1, 1)
(2, 2)
(3, 3)
(4, 4)
(5, 5)
(6, 6)
(7, 7)
(8, 8)
(9, 9)
0
(0, 0)
(1, 1)
(2, 2)
(3, 3)
(4, 4)
(5, 5)
(6, 6)
(7, 7)
(8, 8)
(9, 9)
(10, 10)
(11, 11)
(12, 12)
(13, 13)
(14, 14)
(15, 15)
(16, 16)
(17, 17)
(18, 18)
(19, 19)
(20, 20)
(20, 20)
(21, 21)
(21, 21)
(22, 22)
(22, 22)
(23, 23)
(23, 23)
(24, 24)
(24, 24)
(25, 25)
(25, 25)
(26, 26)
(26, 26)
(27, 27)
(27, 27)
(28, 28)
(28, 28)
(29, 29)
(29, 29)
(30, 30)
(30, 30)
(31, 31)
(31, 31)
(32, 32)
(32, 32)
(33, 33)
(33, 33)
(34, 34)
(34, 34)
(35, 35)
(35, 35)
(36, 36)
(36, 36)
(37, 37)
(37, 37)
(38, 38)
(38, 38)
(39, 39)
(39, 39)
(40, 40)
(41, 41)
(42, 42)
(43, 43)
(44, 44)
(45, 45)
(46, 46)
(47, 47)
(48, 48)
(49, 49)
(50, 50)
(51, 51)
(52, 52)
(53, 53)
(54, 54)
(55, 55)
(56, 56)
(57, 57)
(58, 58)
(59, 59)
(60, 60)
(61, 61)
(62, 62)
(63, 63)
(64, 64)
(65, 65)
(66, 66)
(67, 67)
(68, 68)
(69, 69)
(70, 70)
(71, 71)
(72, 72)
(73, 73)
(74, 74)
(75, 75)
(76, 76)
(77, 77)
(78, 78)
(79, 79)
(80, 80)
(81, 81)
(82, 82)
(83, 83)
(84, 84)
(85, 85)
(86, 86)
(87, 87)
(88, 88)
(89, 89)
(90, 90)
(91, 91)
(92, 92)
(93, 93)
(94, 94)
(95, 95)
(96, 96)
(97, 97)
(98, 98)
(99, 99)
"""

############################################################################################################### 


# P11.70 Wirte a Jumping Leprechauns which perform n-body simulation

"""
Write a program that performs a simple n-body simulation, called “Jump-ing Leprechauns.” This 
simulation involves n leprechauns, numbered 1 to n. It maintains a gold value g i for each 
leprechaun i, which begins with each leprechaun starting out with a million dollars worth of 
gold, that is, gi = 1 000 000 for each i = 1, 2, ..., n. In addition, the simulation also
maintains, for each leprechaun, i, a place on the horizon, which is represented as a double
precision floating-point number, xi . In each iteration of the simulation, the simulation 
processes the leprechauns in order. Processing a leprechaun i during this iteration begins by 
computing a new place on the horizon for i, which is determined by the assignment

xi = xi + rgi;

where r is a random floating-point number between −1 and 1. The leprechaun i then steals half 
the gold from the nearest leprechauns on either side of him and adds this gold to his gold 
value, g i . Write a program that can perform a series of iterations in this simulation for a 
given number, n, of leprechauns. You must maintain the set of horizon positions using a sorted 
map data structure described in this chapter.
"""


from avl_tree import AVLTreeMap
import random


class SkipSpirit:
    """Define a class SkipSpirit"""
    def __init__(self,n):
        self._tree = AVLTreeMap()
        self._list = []
        self._n = n
        self._store = []                                            # store empty index
        for i in range(n):
            self._list.append(self._add(i,1000))
    def _add(self,k,v):
        # Assign value v to key k, overwriting existing value if present.
        if self._tree.is_empty():
            leaf = self._tree._add_root(self._tree._Item(k, v))     # from LinkedBinaryTree
        else:
            p = self._tree._subtree_search(self._tree.root(), k)
            if p.key() == k:                
                return self._add(k+round(random.uniform(-1,1), 2),v)
            else:
                item = self._tree._Item(k, v)
                if p.key() < k:
                    # inherited from LinkedBinaryTree
                    leaf = self._tree._add_right(p, item)
                else:
                    # inherited from LinkedBinaryTree
                    leaf = self._tree._add_left(p, item)
        # hook for balanced tree subclasses
        self._tree._rebalance_insert(leaf)
        return leaf
    def after(self, p):
        # return the next node after p
        return self._tree.after(p)
    def before(self, p):
        # return the next node after p
        return self._tree.before(p)
    def delete(self, p):
        self._tree.delete(p)
    def run(self):
        for i in range(self._n):
            temp = self._list[i]
            if temp is None:
                continue
            if temp._node._parent is temp._node:                     # if temp was deleted ,add index to self._store
                self._list[i] = None
                self._store.append(i)
                continue
            aim = self.before(temp)
            aim2 = self.after(temp)
            if aim is None :
                aim = aim2
            elif aim2 is not None:
                aim = aim if temp.key()-aim.key() < aim2.key()-temp.key() else aim2     # find the closer node
            aim.element()._value /= 2
            gold = aim.element()._value + temp.element()._value      # calculate the key and node
            key = temp.key() + round(random.uniform(-1,1),2) * gold
            self.delete(temp)
            if len(self._store) == 0:
                self._list.append(self._add(key,gold))
            else:
                self._list[self._store.pop()] = self._add(key,gold)
    def print(self):
        for i in self._list:
            if i is not None:
                print('The node of key equal',i.key(),'value is',i.value())


if __name__ == '__main__':
    ss = SkipSpirit(30)
    for i in range(10):
        ss.run()
    ss.print()
