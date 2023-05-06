
# linked_deque_call.py


class Empty(Exception):
    pass


# Non-nested _Node class
class _Node:
    """The calss is used to encapsulate deque nodes"""
    def __init__(self, element=None, prev=None, next=None):
        self.element = element  # object element
        self.prev = prev        # previous node reference
        self.next = next        # next node reference


class _DoublyLinkedBase:
    """It is the base class of deque"""
    #------------------------------ list constructor ------------------------------
    def __init__(self):
        """Initialize an empty deque"""
        self._header = _Node(element=None, prev=None, next=None)
        self._trailer = _Node(element=None, prev=None, next=None)
        self._header.next = self._trailer    # Trailer placed after head sentinel
        self._trailer.prev = self._header    # Head placed before trailer sentinel
        self._size = 0                       # number of elements
     #------------------------------ public accessors ------------------------------   
    def __len__(self):
        # Return number of elements of deque
        return self._size
    def is_empty(self):
        # Return True if empty"""
        return self._size == 0
    #------------------------------ non-public utilities ------------------------------
    def _insert_between(self, element, predecessor, successor):
        """
        Insert element node between two nodes and return the node
        :param element: element (of new nodes)
        :param predecessor: predecessingt node
        :param successor: successing node
        :return: new node encapsulated element
        """
        new_node = _Node(element, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self._size += 1
        return new_node
    def _delete_node(self, node):
        # Delete non-sentinel node and return it
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element


class LinkedDeque(_DoublyLinkedBase):
    """Realize the double queue with deque"""
    def __iter__(self):
        # Generate elements with the forward iteration in the queue
        cursor = self._header.next
        while cursor.element is not None:
            yield cursor.element
            cursor = cursor.next
    @property
    def first(self):
        # Return the head element and don't delete it
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header.next.element
    @property
    def last(self):
        # Return trailing element and don't delete it
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer.prev.element
    def insert_first(self, element):
        # Insert an element in the head of queue
        self._insert_between(element, self._header, self._header.next)
    def insert_last(self, element):
        # Insert an element in the trailer of queue
        self._insert_between(element, self._trailer.prev, self._trailer)
    def delete_first(self):
        # Delete a heading node and return nodes
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header.next)
    def delete_last(self):
        # Delete a heading node and return nodes
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer.prev)


if __name__ == '__main__':
    ld = LinkedDeque()
    ld.insert_first(9)
    ld.insert_last(5)
    print(len(ld))            # 2
    ld.insert_first(3)
    ld.insert_last(8)
    print(list(ld))           # [3, 9, 5, 8]
    print(ld.delete_first())  # 3
    print(list(ld))           # [9, 5, 8]
    print(ld.delete_last())   # 8
    print(len(ld))            # 2
    print(list(ld))           # [9, 5]


# Output:

"""
2
[3, 9, 5, 8]
3
[9, 5, 8]
8
2
[9, 5]
"""