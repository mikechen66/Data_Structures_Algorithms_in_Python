

# LinkedLists

##################################################################################################

# Part One. Reinforcement

##################################################################################################


# R.7.2 Describe a good algorithm for concatenating two singly linked lists L and M, 
# given only reference to the first node of each list, into a single list that contains 
# all the nodes of followed by all nodes of M. 

"""

The caller also can use the list() to concatenate the two independent list.

if __name__ == '__main__':
    L = LinkedStack()
    L.push(5)
    L.push(4)
    L.push(3)
    [i for i in L]
    M = LinkedStack()
    M.push(3)
    M.push(2)
    M.push(1)
    [i for i in M]
    N = list(L) + list(M)
    print(N)
"""


import copy


class Empty(Exception):
    """Definition for an Empty exception class."""
    pass


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""
    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage
        def __init__(self, element, next):      # initialize node's fields
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node
    #------------------------------- stack methods -------------------------------
    def __init__(self):
        # Create an empty stack.
        self._head = None                       # reference to the head node
        self._size = 0                          # number of stack elements
    def __len__(self):
        # Return the number of elements in the stack.
        return self._size
    def __iter__(self):
        cur = self._head
        while cur is not None:
            yield cur._element
            cur = cur._next
    def is_empty(self):
        # Return True if the stack is empty.
        return self._size == 0
    def push(self, e):
        # Add element e to the top of the stack.
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element              # top of stack is at head of list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next           # bypass the former top node
        self._size -= 1
        return answer


def concat_linked_stack(base, append):
    base = copy.deepcopy(base)
    append = copy.deepcopy(append)
    base_last = None
    cur = base._head
    while True:  # Need to traverse whole list since LinkedStack does not keep its last node.
        if cur._next is None:
            base_last = cur
            break
        cur = cur._next
    base_last._next = append._head
    base._size += append._size
    return base


if __name__ == '__main__':
    L = LinkedStack()
    L.push(5)
    L.push(4)
    L.push(3)
    [i for i in L]
    M = LinkedStack()
    M.push(3)
    M.push(2)
    M.push(1)
    [i for i in M]
    concat_list = concat_linked_stack(L, M)
    [i for i in concat_list]


# Output:

"""
[3, 4, 5]
[1, 2, 3]
[3, 4, 5, 1, 2, 3]
"""

##################################################################################################


# R7.3 Describe a recursive algorithm that counts the number of nodes in a singly linked list.


import copy


class Empty(Exception):
    """Definition for an Empty exception class."""
    pass


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""
    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage
        def __init__(self, element, next):      # initialize node's fields
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node
    #------------------------------- stack methods -------------------------------
    def __init__(self):
        # Create an empty stack.
        self._head = None                       # reference to the head node
        self._size = 0                          # number of stack elements
    def __len__(self):
        # Return the number of elements in the stack.
        return self._size
    def __iter__(self):
        cur = self._head
        while cur is not None:
            yield cur._element
            cur = cur._next
    def is_empty(self):
        # Return True if the stack is empty.
        return self._size == 0
    def push(self, e):
        # Add element e to the top of the stack.
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element              # top of stack is at head of list
    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next           # bypass the former top node
        self._size -= 1
        return answer


def concat_linked_stack(base, append):
    base = copy.deepcopy(base)
    append = copy.deepcopy(append)
    base_last = None
    cur = base._head
    while True:  # Need to traverse whole list since LinkedStack does not keep its last node.
        if cur._next is None:
            base_last = cur
            break
        cur = cur._next
    base_last._next = append._head
    base._size += append._size
    return base


def recur_count(list_head):
    """
    list_head: head reference to a list
    """
    if list_head._next is None:
        return 1
    else:
        return 1 + recur_count(list_head._next)


if __name__ == '__main__':
    L = LinkedStack()
    L.push(5)
    L.push(4)
    L.push(3)
    [i for i in L]
    M = LinkedStack()
    M.push(3)
    M.push(2)
    M.push(1)
    [i for i in M]
    concat_list = concat_linked_stack(L, M)
    [i for i in concat_list]
    recur_count(concat_list._head)


# Output:

"""
[3, 4, 5]
[1, 2, 3]
[3, 4, 5, 1, 2, 3]
6
"""
##################################################################################################


# R7.7 Our CircularQueue class provides a rotate() method that has semantics equivalent 
# to Q.enqueue(Q.dequeue()), for a nonempty queue. Implement such a method for the 
# LinkedQueue class without the creation of any new nodes.


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


def rotate(self):
    if self._size > 0:
        old_head = self._head
        self._head = old_head._next
        self._tail._next = old_head
        old_head._next = None


if __name__ == '__main__':
    LinkedQueue.rotate = rotate  # monkey patching
    q = LinkedQueue()
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    q.rotate()
    [i for i in q]


# Output:

"""
[4, 3, 2, 1, 5]
"""

##################################################################################################


# R7.13 Update the PositionalList class to support an additional method find(e), which 
# returns the position of the (first occurrence of )element e in the list (or None if 
# not found).


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""
    #-------------------------- nested _Node class --------------------------
    # nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'            # streamline memory
        def __init__(self, element, prev, next):            # initialize node's fields
            self._element = element                         # user's element
            self._prev = prev                               # previous node reference
            self._next = next                               # next node reference
    #-------------------------- list constructor --------------------------
    def __init__(self):
        # Create an empty list.
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                  # trailer is after header
        self._trailer._prev = self._header                  # header is before trailer
        self._size = 0                                      # number of elements
    #-------------------------- public accessors --------------------------
    def __len__(self):
        # Return the number of elements in the list.
        return self._size
    def is_empty(self):
        # Return True if list is empty.
        return self._size == 0
    #-------------------------- nonpublic utilities --------------------------
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
    #-------------------------- nested Position class --------------------------
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
    #------------------------------- utility methods -------------------------------
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
            return None                              # boundary violation
        else:
            return self.Position(self, node)         # legitimate position
    #------------------------------- accessors -------------------------------
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
    #------------------------------- mutators -------------------------------
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
        return self._delete_node(original)  # inherited method returns element
    def replace(self, p, e):
        """
        Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element       # temporarily store old element
        original._element = e               # replace with new element
        return old_value                    # return the old element value


def find(self, e):
    cur = self.first()
    while True:
        if cur is None:
            return None
        if cur.element() == e:
            return cur
        cur = self.after(cur)


if __name__ == '__main__':
    PositionalList.find = find  # Monkey patching
    p = PositionalList()
    for i in [2, 8 ,1, 10, 9, 8, 4, 3]:
        p.add_first(i)
    p.first().element()
    [i for i in p]
    p.before(p.find(10)).element()
    p.before(p.find(10)).element()


# Output:

"""
<__main__.PositionalList.Position object at 0x7f864e50add0>
<__main__.PositionalList.Position object at 0x7f864e50ae10>
<__main__.PositionalList.Position object at 0x7f864e50add0>
<__main__.PositionalList.Position object at 0x7f864e50ae10>
<__main__.PositionalList.Position object at 0x7f864e50add0>
<__main__.PositionalList.Position object at 0x7f864e50ae10>
<__main__.PositionalList.Position object at 0x7f864e50add0>
<__main__.PositionalList.Position object at 0x7f864e50ae10>
3
[3, 4, 8, 9, 10, 1, 8, 2]
9
9
"""

##################################################################################################
##################################################################################################


# Part Two. Creativity

# C-7.24 Give a complete implementation of the stack ADT using a singly linked list 
# that includes a header sentinel.


class LinkedStackSentinel:
    """LIFO Stack implementatino using a singly linked list for storage"""
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt
    def __init__(self):
        self._header = self._Node(None, None)
        self._header._next = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def push(self, e):
        new = self._Node(e, self._header._next)
        self._header._next = new
        self._size += 1
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._header._next._element
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        pop_node = self._header._next
        self._header._next = pop_node._next
        answer = pop_node._element
        pop_node = None
        self._size -= 1
        return answer


if __name__ == '__main__':
    x = LinkedStackSentinel()
    x.push(5)
    x.push(3)
    x.push(1)
    x.top()
    print(x.pop())
    print(x.pop())
    print(x.pop())


# Output:

"""
1
1
3
"""

##################################################################################################


# C7.25 Give a complete implementation of the queue ADT using a singly linked list that 
# includes a header sentinel.


class LinkedQueueSentinel:
    class _Node:
        __slots__ = '_element', '_next' 
        def __init__(self, element, next):
            self._element = element
            self._next = next
    def __init__(self):
        self._header = self._Node(None, None)
        self._header._next = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._header._next._element
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        dequeue_node = self._header._next
        self._header._next = dequeue_node._next
        answer = dequeue_node._element
        dequeue_node = None
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._header._next = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


if __name__ == '__main__':
    x = LinkedQueueSentinel()
    x.enqueue(5)
    x.enqueue(4)
    x.enqueue(3)
    x.first()
    x.dequeue()
    x.dequeue()
    x.first()


# Output:

"""
5
5
4
3
"""