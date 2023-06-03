

# binary_tree_update.py


class BinaryTreeUpdate:
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


if __name__ == '__main__':
    t = BinaryTreeUpdate()
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