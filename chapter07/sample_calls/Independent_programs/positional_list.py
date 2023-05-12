

# positional_list.py


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""
    #---------------------------------- nested _Node class -------------------------------------
    # nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'            # streamline memory
        def __init__(self, element, prev, next):            # initialize node's fields
            self._element = element                         # user's element
            self._prev = prev                               # previous node reference
            self._next = next                               # next node reference
    #---------------------------------- list constructor ---------------------------------------
    def __init__(self):
        # Create an empty list.
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                  # trailer is after header
        self._trailer._prev = self._header                  # header is before trailer
        self._size = 0                                      # number of elements
    #---------------------------------- public accessors ---------------------------------------
    def __len__(self):
        # Return the number of elements in the list.
        return self._size
    def is_empty(self):
        # Return True if list is empty.
        return self._size == 0
    #---------------------------------- nonpublic utilities ------------------------------------
    def _insert_between(self, e, predecessor, successor):
        # Add element e between two existing nodes and return new node.
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    def _delete_node(self, node):
        # Delete nonsentinel node from the list and return its element.
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                             # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element                                      # return deleted element


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""
    #---------------------------------- nested Position class ----------------------------------
    class Position:
        """
        An abstraction representing the location of a single element.
        Note that two position instances may represent the same inherent
        location in the list.  Therefore, users should always rely on
        syntax 'p == q' rather than 'p is q' when testing equivalence of
        positions.
        """
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
        def __ne__(self, other):
            # Return True if other does not represent the same location.
            return not (self == other)               # opposite of __eq__
    #---------------------------------- utility methods ----------------------------------------
    def _validate(self, p):
        # Return position's node, or raise appropriate error if invalid.
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:                  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self, node):
        # Return Position instance for given node (or None if sentinel).
        if node is self._header or node is self._trailer:
            return None                                    # boundary violation
        else:
            return self.Position(self, node)               # legitimate position
    #---------------------------------- accessors ----------------------------------------------
    def first(self):
        # Return the first Position in the list (or None if list is empty).
        return self._make_position(self._header._next)
    def last(self):
        # Return the last Position in the list (or None if list is empty).
        return self._make_position(self._trailer._prev)
    def before(self, p):
        # Return the Position just before Position p (or None if p is first).
        node = self._validate(p)
        return self._make_position(node._prev)
    def after(self, p):
        # Return the Position just after Position p (or None if p is last).
        node = self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        # Generate a forward iteration of the elements of the list.
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    #---------------------------------- mutators -----------------------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        # Add element between existing nodes and return new Position.
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    def add_first(self, e):
        # Insert element e at the front of the list and return new Position.
        return self._insert_between(e, self._header, self._header._next)
    def add_last(self, e):
        # Insert element e at the back of the list and return new Position.
        return self._insert_between(e, self._trailer._prev, self._trailer)
    def add_before(self, p, e):
        # Insert element e into list before Position p and return new Position.
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    def add_after(self, p, e):
        # Insert element e into list after Position p and return new Position.
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    def delete(self, p):
        # Remove and return the element at Position p.
        original = self._validate(p)
        return self._delete_node(original)                 # inherited method returns element
    def replace(self, p, e):
        """
        Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element                      # temporarily store old element
        original._element = e                              # replace with new element
        return old_value                                   # return the old element value


if __name__ == '__main__':
    L = PositionalList()
    p1 = L.add_first(8)
    print('p1 = ', p1)     
    print('L = ', list(L))  # L =  [8]
    p2 = L.first()
    print('p2 = ', p2)  
    p3 = L.add_after(p2, 5)
    print('p3 = ', p3) 
    print('L = ', list(L))  
    p4 = L.before(p3)
    print('p4 = ', p4)  
    print(p1 == p4)  
    p5 = L.add_before(p3, 3)
    print('p5 = ', p5) 
    print('L = ', list(L))
    print('p5.element() = ', p5.element())  
    p6 = L.before(p1)
    print('p6 = ', p6)
    print(L.delete(L.last()))
    print('L = ', list(L))
    print(L.replace(p1, 7))
    print('L = ', list(L))


# Output:

"""

p1 =  <__main__.PositionalList.Position object at 0x7f7ac637c0d0>
L =  [8]
p2 =  <__main__.PositionalList.Position object at 0x7f7ac637c110>
p3 =  <__main__.PositionalList.Position object at 0x7f7ac637c150>
L =  [8, 5]
p4 =  <__main__.PositionalList.Position object at 0x7f7ac637c1d0>
True
p5 =  <__main__.PositionalList.Position object at 0x7f7ac637c190>
L =  [8, 3, 5]
p5.element() =  3
p6 =  None
5
L =  [8, 3]
8
L =  [7, 3]
"""

############################################################################################################


if __name__ == '__main__':
    a = PositionalList()
    for i in range(10):
        a.add_first(i)
    for i in range(10,15):
        a.add_last(i)
    head=a.first()
    head=a.first()
    a.add_after(head,111)
    for i in range(15):
        print(head.element())
        head = a.after(head)


# Output:

"""
... 
<__main__.PositionalList.Position object at 0x7f6096c61f90>
<__main__.PositionalList.Position object at 0x7f6096c61f50>
<__main__.PositionalList.Position object at 0x7f6096c61f90>
<__main__.PositionalList.Position object at 0x7f6096c61f50>
<__main__.PositionalList.Position object at 0x7f6096c61f90>
<__main__.PositionalList.Position object at 0x7f6096c61f50>
<__main__.PositionalList.Position object at 0x7f6096c61f90>
<__main__.PositionalList.Position object at 0x7f6096c61f50>
<__main__.PositionalList.Position object at 0x7f6096c61f90>
<__main__.PositionalList.Position object at 0x7f6096c61f50>
<__main__.PositionalList.Position object at 0x7f6096c61f90>
<__main__.PositionalList.Position object at 0x7f6096c61f50>
<__main__.PositionalList.Position object at 0x7f6096c61f90>
<__main__.PositionalList.Position object at 0x7f6096c61f50>
<__main__.PositionalList.Position object at 0x7f6096c61f90>
<__main__.PositionalList.Position object at 0x7f6096c61f50>
9
111
8
7
6
5
4
3
2
1
0
10
11
12
13
"""

#################################################################################################


# positional_list.py
class Empty(Exception):
    """尝试对空队列进行删除操作时抛出的异常"""
    pass


class _Node:
    """用于封装双向链表结点的类"""
    def __init__(self, element=None, prev=None, next=None):
        self.element = element  # 对象元素
        self.prev = prev  # 前驱结点引用
        self.next = next  # 后继结点引用


class _Position:
    """代表对象元素在位置列表中位置的抽象"""
    def __init__(self, container, node: _Node):
        self.container = container
        self.node = node
    def element(self):
        """返回某一位置处的对象元素"""
        return self.node.element
    def __eq__(self, other):
        """如果两个Position实例代表了同一个位置，则返回True"""
        return type(other) is type(self) and other.node is self.node
    def __ne__(self, other):
        """如果两个Position的实例代表不同位置，则返回True"""
        return not (self == other)


class _DoublyLinkedBase:
    """双向链表的基类"""
    def __init__(self):
        """创建一个空的双向链表"""
        self._header = _Node(element=None, prev=None, next=None)
        self._trailer = _Node(element=None, prev=None, next=None)
        self._header.next = self._trailer  # 尾哨兵结点在头哨兵结点之后
        self._trailer.prev = self._header  # 头哨兵结点在尾哨兵结点之前
        self._size = 0  # 元素数量
    def __len__(self):
        """返回链表元素数量"""
        return self._size
    def is_empty(self):
        """如果链表为空则返回True"""
        return self._size == 0
    def _insert_between(self, element, predecessor, successor):
        """
        在两个已有结点之间插入封装了元素element的新结点，并将该结点返回
        :param element: 新结点中的对象元素
        :param predecessor: 前驱结点
        :param successor: 后继结点
        :return: 封装了element的新结点
        """
        new_node = _Node(element, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self._size += 1
        return new_node
    def _delete_node(self, node):
        """删除非哨兵结点并将结点返回"""
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element


class PositionalList(_DoublyLinkedBase):
    """允许通过位置实例操作其中对象元素的序列"""
    def _validate(self, p: _Position):
        """返回位置实例处的结点引用，或当位置实例非法时抛出对应异常"""
        if not isinstance(p, _Position):
            raise TypeError('位置p:', p, '必须为准确的_Position类型！')
        if p.container is not self:
            raise ValueError('位置p', p, '不属于当前位置列表！')
        if p.node.element is None:
            raise ValueError('位置p', p, '已失效！')
        return p.node
    def _node2pos(self, node: _Node):
        """返回给定结点的Position实例对象，当给定哨兵结点时返回None"""
        if node is self._header or node is self._trailer:
            return None  # node代表的结点非法
        else:
            return _Position(self, node)
    def first(self):
        """返回位置列表中的第一个位置，如列表为空则返回None"""
        return self._node2pos(self._header.next)
    def last(self):
        """返回位置列表中的最后一个位置，如列表为空则返回None"""
        return self._node2pos(self._trailer.prev)
    def before(self, p: _Position):
        """返回位置p前的一个元素，如p为第一个业务元素的位置，则返回None"""
        node = self._validate(p)
        return self._node2pos(node.prev)
    def after(self, p: _Position):
        """返回位置p后的一个元素，如p为最后一个业务元素的位置，则返回None"""
        node = self._validate(p)
        return self._node2pos(node.next)
    def __iter__(self):
        """生成一个前向迭代器，该迭代器可依次返回列表中对象元素"""
        cursor = self.first()
        while cursor is not None:  # first()方法所使用的_node2pos()方法确保了哨兵结点的位置为None
            yield cursor.element()
            cursor = self.after(cursor)
    def __str__(self):
        """返回位置列表的字符串表示形式"""
        return str(list(self))
    def _insert_between(self, e, predecessor, successor):
        """重写父类_DoublyLinkedBase中的同名方法，在两个已有结点之间插入经封装为结点后的对象元素，并返回新结点的位置"""
        node = super()._insert_between(e, predecessor, successor)
        return self._node2pos(node)
    def add_first(self, e):
        """在列表的第一个位置出插入经封装后的对象元素，并返回结点位置"""
        return self._insert_between(e, self._header, self._header.next)
    def add_last(self, e):
        """在列表的最后一个位置出插入经封装后的对象元素，并返回结点位置"""
        return self._insert_between(e, self._trailer.prev, self._trailer)
    def add_before(self, p: _Position, e):
        """在位置p之前将对象元素经封装后得到的结点插入列表中"""
        node = self._validate(p)
        return self._insert_between(e, node.prev, node)
    def add_after(self, p: _Position, e):
        """在位置p之后将对象元素经封装后得到的结点插入列表中"""
        node = self._validate(p)
        return self._insert_between(e, node, node.next)
    def delete(self, p):
        """删除并返回位置p处对应的对象元素"""
        node = self._validate(p)
        return self._delete_node(node)  # 集成自_DoublyLinkedBase类
    def replace(self, p: _Position, e):
        """将位置p处的对象元素替换为e，并返回原先位置p处的对象元素"""
        node = self._validate(p)
        original_val = node.element  # 暂存位置p处原先的对象元素
        node.element = e  # 替换
        return original_val  # 返回位置p处原先的对象元素


if __name__ == '__main__':
    L = PositionalList()
    p1 = L.add_first(8)
    print('p1 = ', p1)     
    print('L = ', list(L))  # L =  [8]
    p2 = L.first()
    print('p2 = ', p2)  
    p3 = L.add_after(p2, 5)
    print('p3 = ', p3) 
    print('L = ', list(L))  
    p4 = L.before(p3)
    print('p4 = ', p4)  
    print(p1 == p4)  
    p5 = L.add_before(p3, 3)
    print('p5 = ', p5) 
    print('L = ', list(L))
    print('p5.element() = ', p5.element())  
    p6 = L.before(p1)
    print('p6 = ', p6)
    print(L.delete(L.last()))
    print('L = ', list(L))
    print(L.replace(p1, 7))
    print('L = ', list(L))


# Output:

"""
p1 =  <__main__._Position object at 0x7f3999fb55d0>
L =  [8]
p2 =  <__main__._Position object at 0x7f3999fb5610>
p3 =  <__main__._Position object at 0x7f3999fb5690>
L =  [8, 5]
p4 =  <__main__._Position object at 0x7f3999fb5710>
True
p5 =  <__main__._Position object at 0x7f3999fb5750>
L =  [8, 3, 5]
p5.element() =  3
p6 =  None
5
L =  [8, 3]
8
L =  [7, 3]
>>> 
"""