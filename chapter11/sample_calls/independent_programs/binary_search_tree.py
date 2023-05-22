

# binary_search_tree

# from linked_binary_tree import LinkedBinaryTree
# from map_base import MapBase

# binary_tree_update

class BinaryTree:
# class BinaryTreeUpdate:
    '''base of the array list'''
    class Position:
        ''' seal the size of tree's node'''
        def __init__(self, e, container, data):
            self._container=container
            self._node = e       # the index
            self._data = data    # the array list
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._nod
        def element(self):
            '''return the value'''
            return self._data[self._node]
    def __init__(self):
        '''creat a array'''
        self._data = [None] * 60     # size of the array is 60
        self._size = 0            #  len of the tree
    def _make_position(self, p, container, data):
        """
        p : the index;
            container : the container;
            data : the array list
        """
        return self.Position(p, container, data) if p != None else None
    def _validate(self, p):
        if not isinstance(p, self.Position):    # if is not the same type
            raise TypeError('p must be proper Position type')
        if p._container != self:
            raise Exception('it is\'t the tree\'s node')
        if p == None:
            raise Exception('it is\'s None')
        return p._node
    def add_root(self, e):
        # add the root node, if root not None
        if self._data[0] == None:
            self._data[0] = e
            self._size += 1
        else:
            raise Exception('There is a node already')
        return self._make_position(0, self, self._data)
    def add_left(self, p, e):
        # add the left node of p
        p = self._validate(p)
        q = 2*p + 1                          # the left node's index
        self._data[q]=e
        return self._make_position(q, self, self._data)
    def add_right(self, p, e):
        # add the right node of p
        p = self._validate(p)
        q = 2*p + 2                          # the right node's index
        self._data[q]=e
        return self._make_position(q, self, self._data)
    def left(self,p):
        p=self._validate(p)
        return self._make_position(2*p+1, self, self._data)
    def right(self, p):
        p = self._validate(p)  
        return self._make_position(2*p+2, self, self._data)
    def parent(self, p):
        p = self._validate(p)
        if p == 0:
            return None
        p = int(p/2) if p%2 == 1 else p/2-1  # get the new index
        return self._make_position(p, self, self._data)


# linked_binary_tree

# from binary_tree import BinaryTree

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


# map_base


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
        
  
if __name__ == '__main__':
    t = TreeMap()
    root = t._add_root('a')
    b = t._add_left(root,'b')
    c = t._add_right(root,'c')
    print(list(map(t.Position.element,[root,b,c])),root==t.parent(b))


# Output:

"""
['a', 'b', 'c'] True
"""
