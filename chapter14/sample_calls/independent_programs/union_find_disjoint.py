

# union_find_disjoint.py


"""
A union-find disjoint set data structure.

"""

# 2to3 sanity
from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)


# Third-party libraries
import numpy as np


class UnionFind(object):
    """
    Union-find disjoint sets datastructure.
    Union-find is a data structure that maintains disjoint set
    (called connected components or components in short) membership,
    and makes it easier to merge (union) two components, and to find
    if two elements are connected (i.e., belong to the same
    component).
    This implements the "weighted-quick-union-with-path-compression"
    union-find algorithm.  Only works if elements are immutable
    objects.
    Worst case for union and find: :math:`(N + M \log^* N)`, with
    :math:`N` elements and :math:`M` unions. The function
    :math:`\log^*` is the number of times needed to take :math:`\log`
    of a number until reaching 1. In practice, the amortized cost of
    each operation is nearly linear [1]_.
    Terms
    -----
    Component
        Elements belonging to the same disjoint set
    Connected
        Two elements are connected if they belong to the same component.
    Union
        The operation where two components are merged into one.
    Root
        An internal representative of a disjoint set.
    Find
        The operation to find the root of a disjoint set.
    Parameters
    ----------
    elements : NoneType or container, optional, default: None
        The initial list of elements.
    Attributes
    ----------
    n_elts : int
        Number of elements.
    n_comps : int
        Number of distjoint sets or components.
    Implements
    ----------
    __len__
        Calling ``len(uf)`` (where ``uf`` is an instance of ``UnionFind``)
        returns the number of elements.
    __contains__
        For ``uf`` an instance of ``UnionFind`` and ``x`` an immutable object,
        ``x in uf`` returns ``True`` if ``x`` is an element in ``uf``.
    __getitem__
        For ``uf`` an instance of ``UnionFind`` and ``i`` an integer,
        ``res = uf[i]`` returns the element stored in the ``i``-th index.
        If ``i`` is not a valid index an ``IndexError`` is raised.
    __setitem__
        For ``uf`` and instance of ``UnionFind``, ``i`` an integer and ``x``
        an immutable object, ``uf[i] = x`` changes the element stored at the
        ``i``-th index. If ``i`` is not a valid index an ``IndexError`` is
        raised.
    .. [1] http://algs4.cs.princeton.edu/lectures/
    """
    def __init__(self, elements=None):
        self.n_elts = 0  # current num of elements
        self.n_comps = 0  # the number of disjoint sets or components
        self._next = 0  # next available id
        self._elts = []  # the elements
        self._indx = {}  #  dict mapping elt -> index in _elts
        self._par = []  # parent: for the internal tree structure
        self._siz = []  # size of the component - correct only for roots
        if elements is None:
            elements = []
        for elt in elements:
            self.add(elt)
    def __repr__(self):
        return  (
            '<UnionFind:\n\telts={},\n\tsiz={},\n\tpar={},\nn_elts={},n_comps={}>'
            .format(
                self._elts,
                self._siz,
                self._par,
                self.n_elts,
                self.n_comps,
            ))
    def __len__(self):
        return self.n_elts
    def __contains__(self, x):
        return x in self._indx
    def __getitem__(self, index):
        if index < 0 or index >= self._next:
            raise IndexError('index {} is out of bound'.format(index))
        return self._elts[index]
    def __setitem__(self, index, x):
        if index < 0 or index >= self._next:
            raise IndexError('index {} is out of bound'.format(index))
        self._elts[index] = x
    def add(self, x):
        """
        Add a single disjoint element.
        Parameters
        ----------
        x : immutable object
        Returns
        -------
        None
        """
        if x in self:
            return
        self._elts.append(x)
        self._indx[x] = self._next
        self._par.append(self._next)
        self._siz.append(1)
        self._next += 1
        self.n_elts += 1
        self.n_comps += 1
    def find(self, x):
        """
        Find the root of the disjoint set containing the given element.
        Parameters
        ----------
        x : immutable object
        Returns
        -------
        int
            The (index of the) root.
        Raises
        ------
        ValueError
            If the given element is not found.
        """
        if x not in self._indx:
            raise ValueError('{} is not an element'.format(x))
        p = self._indx[x]
        while p != self._par[p]:
            # path compression
            q = self._par[p]
            self._par[p] = self._par[q]
            p = q
        return p
    def connected(self, x, y):
        """
        Return whether the two given elements belong to the same component.
        Parameters
        ----------
        x : immutable object
        y : immutable object
        Returns
        -------
        bool
            True if x and y are connected, false otherwise.
        """
        return self.find(x) == self.find(y)
    def union(self, x, y):
        """
        Merge the components of the two given elements into one.
        Parameters
        ----------
        x : immutable object
        y : immutable object
        Returns
        -------
        None
        """
        # Initialize if they are not already in the collection
        for elt in [x, y]:
            if elt not in self:
                self.add(elt)
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self._siz[xroot] < self._siz[yroot]:
            self._par[xroot] = yroot
            self._siz[yroot] += self._siz[xroot]
        else:
            self._par[yroot] = xroot
            self._siz[xroot] += self._siz[yroot]
        self.n_comps -= 1
    def component(self, x):
        """
        Find the connected component containing the given element.
        Parameters
        ----------
        x : immutable object
        Returns
        -------
        set
        Raises
        ------
        ValueError
            If the given element is not found.
        """
        if x not in self:
            raise ValueError('{} is not an element'.format(x))
        elts = np.array(self._elts)
        vfind = np.vectorize(self.find)
        roots = vfind(elts)
        return set(elts[roots == self.find(x)])
    def components(self):
        """
        Return the list of connected components.
        Returns
        -------
        list
            A list of sets.
        """
        elts = np.array(self._elts)
        vfind = np.vectorize(self.find)
        roots = vfind(elts)
        distinct_roots = set(roots)
        return [set(elts[roots == root]) for root in distinct_roots]
        # comps = []
        # for root in distinct_roots:
        #     mask = (roots == root)
        #     comp = set(elts[mask])
        #     comps.append(comp)
        # return comps
    def component_mapping(self):
        """
        Return a dict mapping elements to their components.
        The returned dict has the following semantics:
            `elt -> component containing elt`
        If x, y belong to the same component, the comp(x) and comp(y)
        are the same objects (i.e., share the same reference). Changing
        comp(x) will reflect in comp(y).  This is done to reduce
        memory.
        But this behaviour should not be relied on.  There may be
        inconsitency arising from such assumptions or lack thereof.
        If you want to do any operation on these sets, use caution.
        For example, instead of
        ::
            s = uf.component_mapping()[item]
            s.add(stuff)
            # This will have side effect in other sets
        do
        ::
            s = set(uf.component_mapping()[item]) # or
            s = uf.component_mapping()[item].copy()
            s.add(stuff)
        or
        ::
            s = uf.component_mapping()[item]
            s = s | {stuff}  # Now s is different
        Returns
        -------
        dict
            A dict with the semantics: `elt -> component contianing elt`.
        """
        elts = np.array(self._elts)
        vfind = np.vectorize(self.find)
        roots = vfind(elts)
        distinct_roots = set(roots)
        comps = {}
        for root in distinct_roots:
            mask = (roots == root)
            comp = set(elts[mask])
            comps.update({x: comp for x in comp})
            # Change ^this^, if you want a different behaviour:
            # If you don't want to share the same set to different keys:
            # comps.update({x: set(comp) for x in comp})
        return comps


if __name__ == '__main__':
    uf = UnionFind(list('abcdefghij'))
    print(uf)
    uf.union('e', 'd')
    print(uf)
    uf.union('d', 'i')
    print(uf)
    uf.union('g', 'f')
    print(uf)
    uf.union('j', 'e')
    print(uf)
    uf.union('c', 'b')
    print(uf)
    uf.union('i', 'j')
    print(uf)
    uf.union('f', 'a')
    print(uf)
    uf.union('h', 'c')
    print(uf)
    uf.union('g', 'b')
    print(uf)
    uf.union('a', 'b')
    print(uf)
    uf.union('g', 'h')
    print(uf)
    uf.connected('a', 'g')
    uf.component('a')
    uf.components()
    uf.component_mapping()


# Output:

"""
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    par=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
n_elts=10,n_comps=10>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    par=[0, 1, 2, 4, 4, 5, 6, 7, 8, 9],
n_elts=10,n_comps=9>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
    par=[0, 1, 2, 4, 4, 5, 6, 7, 4, 9],
n_elts=10,n_comps=8>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 1, 1, 3, 1, 2, 1, 1, 1],
    par=[0, 1, 2, 4, 4, 6, 6, 7, 4, 9],
n_elts=10,n_comps=7>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 1, 1, 4, 1, 2, 1, 1, 1],
    par=[0, 1, 2, 4, 4, 6, 6, 7, 4, 4],
n_elts=10,n_comps=6>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 2, 1, 4, 1, 2, 1, 1, 1],
    par=[0, 2, 2, 4, 4, 6, 6, 7, 4, 4],
n_elts=10,n_comps=5>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 2, 1, 4, 1, 2, 1, 1, 1],
    par=[0, 2, 2, 4, 4, 6, 6, 7, 4, 4],
n_elts=10,n_comps=5>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 2, 1, 4, 1, 3, 1, 1, 1],
    par=[6, 2, 2, 4, 4, 6, 6, 7, 4, 4],
n_elts=10,n_comps=4>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 3, 1, 4, 1, 3, 1, 1, 1],
    par=[6, 2, 2, 4, 4, 6, 6, 2, 4, 4],
n_elts=10,n_comps=3>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 3, 1, 4, 1, 6, 1, 1, 1],
    par=[6, 2, 6, 4, 4, 6, 6, 2, 4, 4],
n_elts=10,n_comps=2>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 3, 1, 4, 1, 6, 1, 1, 1],
    par=[6, 6, 6, 4, 4, 6, 6, 2, 4, 4],
n_elts=10,n_comps=2>
<UnionFind:
    elts=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    siz=[1, 1, 3, 1, 4, 1, 6, 1, 1, 1],
    par=[6, 6, 6, 4, 4, 6, 6, 6, 4, 4],
n_elts=10,n_comps=2>
True
{'c', 'f', 'h', 'g', 'b', 'a'}
[{'d', 'e', 'i', 'j'}, {'c', 'f', 'h', 'g', 'b', 'a'}]
{'d': {'d', 'e', 'i', 'j'}, 'e': {'d', 'e', 'i', 'j'}, 'i': {'d', 'e', 'i', 'j'}, 'j': {'d', 'e', 'i', 'j'}, 'c': {'c', 'f', 'h', 'g', 'b', 'a'}, 'f': {'c', 'f', 'h', 'g', 'b', 'a'}, 'h': {'c', 'f', 'h', 'g', 'b', 'a'}, 'g': {'c', 'f', 'h', 'g', 'b', 'a'}, 'b': {'c', 'f', 'h', 'g', 'b', 'a'}, 'a': {'c', 'f', 'h', 'g', 'b', 'a'}}
"""