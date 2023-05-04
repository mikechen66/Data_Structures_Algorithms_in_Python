

# Trees

#######################################################################################################################

# Part One. Reinforcement

#######################################################################################################################


# R8.4 What is the running time of a call to T._height2(p) when called on a position p distinct from 
# the root of T? (See Code Fragment 8.5)


def _height2(self, p):
     """Return the height of the subtree rooted at Position p."""
   if self.is_leaf(p):
       return 0
   else:
       return 1 + max(self._height2(c) for c in self.children(p))


#######################################################################################################################


# R8.10 Give a direct implementation of the num_children method within the class BinaryTree.


from abc import ABC, abstractmethod

class Tree(ABC):
    """Abstract base class representing a tree structure."""
    class Position(ABC):
        """An abstraction representing the location of a single element."""
        @abstractmethod
        def element(self):
            """Return the element stored at this Position."""
            pass
        @abstractmethod
        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            pass
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)
    @abstractmethod
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        pass
    @abstractmethod
    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        pass
    @abstractmethod
    def num_children(self, p):
        """Return the number of children that Position p has."""
        pass
    @abstractmethod
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        pass
    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the tree."""
        pass
    def __iter__(self):
        for p in self.positions():
            yield p.element()
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p
    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    def _height1(self):
        return max(self.depth(p) for p in self.positions if self.is_leaf(p))
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._hegiht2(c) for c in self.children(p))
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""
    @abstractmethod
    def left(self, p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        pass
    @abstractmethod
    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        pass
    @property
    def num_children(self, p):
        num_ch = 0
        if self.left(p):
            num_ch += 1
        if self.right(p):
            num_ch += 1
        return num_ch
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)  
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None
    def __init__(self):
        """Create an intially empty binary tree."""
        self._root = None
        self._size = 0
        self._positions = []
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)
    @property
    def positions(self):
        return self._positions
    def parent(self, p):
        """Return the Position of p's parent(or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)
    def left(self, p):
        """Return the Position of p's left child(or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self, p):
        """Return the Position of p's left child(or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._right)
    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        pos = self._make_position(self._root)
        self._positions.append(pos)
        return pos
    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        Return the Position of new node
        Raise ValueError if Position p is invalidor p already has a left child.
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        pos = self._make_position(node._left)
        self._positions.append(pos)
        return pos 
    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        pos = self._make_position(node._right)
        self._positions.append(pos)
        return pos
    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any..git/
        Return the element that had been stored at Position p
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._positions.remove(p)
        self._size -= 1
        node._parent = node
        return node._element
    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2.root
            t2._root = None
            t2._size = 0


if __name__ == '__main':
    balanced_tree = LinkedBinaryTree()
    balanced_tree._add_root("root")
    balanced_tree.num_children(balanced_tree.root())
    balanced_tree._add_left(balanced_tree.root(), "left")
    balanced_tree.num_children(balanced_tree.root())
    balanced_tree._add_right(balanced_tree.root(), "right")
    balanced_tree.num_children(balanced_tree.root())

#######################################################################################################################


# R8.15 The LinkedBinaryTree class provides only nonpublic versions of the update methods discussed 
# on page 319. Implement a simple subclass named MutableLinkedBinaryTree that provides public wrapper 
# functions for each of the inheirted nonpublic update methods.


class MutableLinkedBinaryTree(LinkedBinaryTree):
    """
    Provides public wrapper functions for each of the inherited nonpublic update methods.
    """
    def add_root(self, e):
        return self._add_root(e) 
    def add_left(self, p, e):
        return self._add_left(p, e)
    def add_right(self, p, e):
        return self._add_right(p, e)
    def replace(self, p, e):
        return self._replace(p, e)
    def delete(self, p):
        return self._delete(p)
    def attach(self, p, T1, T2):
        return self.attach(p, T1, T2)


if __name__ == '__main':
    balanced_tree = MutableLinkedBinaryTree()
    balanced_tree.add_root("root")
    try:
        balanced_tree._add_root("root")
    except Exception as e:
        print(e)
    balanced_tree.root().element()

#######################################################################################################################


# Part Two. Creativity

#######################################################################################################################


# C8.40 We can simplify parts of our LinkedBinaryTree implementation if we make use of a single sentinel 
# node, referenced as the _sentinel member of the tree instance, such that the sentinel is the parent 
# of the real root of the tree, and the root is referenced as the left child of the sentinel. 
# Furthermore, the sentinel will take the place of None as the value of the _left or _right member 
# for a node without such a child. Give a new implementation of the update methods _delete and _attach, 
# assuming such a representation.


class LinkedBinaryTreeSentinel(BinaryTree):
    """Linked representation of a binary tree structure."""
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    class _Sentinel(_Node):
        def __init__(self, parent=None, left=None, right=None):
            super().__init__("SENTINEL", parent, left, right)
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None
    def __init__(self):
        """Create an intially empty binary tree."""
        self._root = None
        self._sentinel = None
        self._size = 0
        self._positions = []
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)
    @property
    def positions(self):
        return self._positions
    def parent(self, p):
        """Return the Position of p's parent(or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)
    def left(self, p):
        """Return the Position of p's left child(or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self, p):
        """Return the Position of p's left child(or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._right)
    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None: raise ValueError('Root exists')
        sentinel_node = self._Sentinel()
        root_node = self._Node(e, parent=sentinel_node)
        root_node._left = self._Sentinel(root_node)
        root_node._right = self._Sentinel(root_node)
        sentinel_node._left = root_node
        self._size = 1
        self._root = root_node
        self._sentinel = self._make_position(sentinel_node)
        pos = self._make_position(self._root)
        self._positions.append(pos)
        return pos
    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        Return the Position of new node
        Raise ValueError if Position p is invalidor p already has a left child.
        """
        node = self._validate(p)
        if not isinstance(node._left, self._Sentinel): raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        node._left._left = self._Sentinel(node._left)
        node._left._right = self._Sentinel(node._left)
        pos = self._make_position(node._left)
        self._positions.append(pos)
        return pos 
    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if not isinstance(node._right, self._Sentinel): raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        node._right._left = self._Sentinel(node._right)
        node._right._right = self._Sentinel(node._right)
        pos = self._make_position(node._right)
        self._positions.append(pos)
        return pos
    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if (not isinstance(node._left, self._Sentinel)) and (not isinstance(node._right, self._Sentinel)): raise ValueError('p has two children')
        child = node._left if (not isinstance(node._left, self._Sentinel)) else node._right
        if node is self._root:
            self._root = child
            self._sentinel._left = self._root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._positions.remove(p)
        self._size -= 1
        node._parent = node
        return node._element
    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
    def is_leaf(self, p):
        if isinstance(p._node._left, self._Sentinel) and isinstance(p._node._right, self._Sentinel):
            return True
        else:
            return False


if __name__ == '__main':
    sentinel_tree = LinkedBinaryTreeSentinel()
    sentinel_tree._add_root("root")
    sentinel_tree.root().element()
    sentinel_tree._sentinel.element()
    sentinel_tree.parent(sentinel_tree.root()).element()
    sentinel_tree.left(sentinel_tree._sentinel).element()
    root_left = sentinel_tree._add_left(sentinel_tree.root(), "root_left")
    root_left.element()
    sentinel_tree.left(root_left).element()
    sentinel_tree.right(root_left).element()
    sentinel_tree.parent(root_left).element()

#######################################################################################################################


# Part Three. Projects

# 8.66 The memory usage for the LinkedBinaryTree class can be streamlined byremoving the parent 
# reference from each node, and instead having each Position instance keep a member, path, that 
# is a list of nodes representing the entire path from the root to that position. (This generally 
# saves memory because there are typically relatively few stored position instances.) Reimplement 
# the LinkedBinaryTree class using this strategy.


import collections


# Code Fragment 6.6: Definition for an Empty exception class.
class Empty(Exception):
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    #-------------------------- nested _Node class --------------------------
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
    # For the iteration effect  
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

#---------------------------------------------------------------------------------------------------------------------


class BinaryTree:
    '''base of the array list'''
    class Position:
        ''' seal the size of tree's node'''
        def __init__(self,e,container,data):
            self._container=container
            self._node=e       # the index
            self._data=data    # the array list
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._nod
        def element(self):
            '''return the value'''
            return self._data[self._node]
    def __init__(self):
        '''creat a array'''
        self._data=[None]*60     # size of the array is 60
        self._size=0            #  len of the tree
    def _make_position(self,p,container,data):
        '''p : the index;
            container : the container;
            data : the array list
        '''
        return self.Position(p,container,data) if p!=None else None
    def _validate(self,p):
        if not isinstance(p, self.Position):    # if is not the same type
            raise TypeError('p must be proper Position type')
        if p._container!=self:
            raise Exception('it is\'t the tree\'s node')
        if p==None:
            raise Exception('it is\'s None')
        return p._node
    def add_root(self,e):
        ''' add the root node, if root not None'''
        if self._data[0] ==None:
            self._data[0]=e
            self._size+=1
        else:
            raise Exception('There is a node already')
        return self._make_position(0,self,self._data)
    def add_left(self,p,e):
        '''add the left node of p'''
        p=self._validate(p)
        q=2*p+1             # the left node's index
        self._data[q]=e
        return self._make_position(q,self,self._data)
    def add_right(self,p,e):
        '''add the right node of p'''
        p=self._validate(p)
        q=2*p+2             # the right node's index
        self._data[q]=e
        return self._make_position(q,self,self._data)
    def left(self,p):
        p=self._validate(p)
        return self._make_position(2*p+1,self,self._data)
    def right(self,p):
        p=self._validate(p)  
        return self._make_position(2*p+2,self,self._data)
    def parent(self,p):
        p=self._validate(p)
        if p==0:
            return None
        p=int(p/2) if p %2==1 else p/2-1   # get the new index
        return self._make_position(p,self,self._data)


if __name__ == '__main__':
    t = BinaryTree()
    a = t.add_root(1)
    b = t.add_left(a,2)
    c = t.add_right(a,3)
    print(a.element())
    print(t.left(a).element())
    print(t.right(a).element())


# Output:

"""
1
2
3
"""