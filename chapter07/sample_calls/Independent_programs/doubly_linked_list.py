

# doubly_linked_list.py

"""
A doubly linked list has more efficient iteration, particularly if you need to ever iterate 
in reverse and more efficient deletion of particular nodes.

We conclude that a doubly linked list is a complex type of linked list where a node contains 
a pointer to the previous as well as the next node in the sequence. Therefore, in a doubly 
linked list, a node consists of three components: node data, pointer to the next node in node
(next pointer), pointer to the former node (previous pointer).

Please see the following code including the comprehensive operations on the doubly linked list. 
"""


class Node:
    def __init__(self, value):
        self.previous = None
        self.data = value
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count
    def search(self, value):
        temp = self.head
        isFound = False
        while temp is not None:
            if temp.data == value:
                isFound = True
                break
            temp = temp.next
        return isFound
    def insert_at_start(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
    def insert_to_end(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.insert_at_start(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp
    def insert_after_element(self, value, element):
        temp = self.head
        while temp is not None:
            if temp.data == element:
                break
            temp = temp.next
        if temp is None:
            print("{} is not present in the linked list. {} cannot be \
                inserted into the list.".format(element, value))
        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.previous = temp
            temp.next.previous = new_node
            temp.next = new_node
    def insert_at_position(self, value, position):
        temp = self.head
        count = 0
        while temp is not None:
            if count == position - 1:
                break
            count += 1
            temp = temp.next
        if position == 1:
            self.insert_at_start(value)
        elif temp is None:
            print("There are less than {}-1 elements in the linked list. \
                Cannot insert at {} position.".format(position, position))
        elif temp.next is None:
            self.insert_to_end(value)
        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.previous = temp
            temp.next.previous = new_node
            temp.next = new_node
    def show_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, sep=",")
            temp = temp.next
    def update_element(self, old_value, new_value):
        temp = self.head
        isUpdated = False
        while temp is not None:
            if temp.data == old_value:
                temp.data = new_value
                isUpdated = True
            temp = temp.next
        if isUpdated:
            print("Value Updated in the linked list")
        else:
            print("Value not Updated in the linked list")
    def update_at_position(self, value, position):
        temp = self.head
        count = 0
        while temp is not None:
            if count == position:
                break
            count += 1
            temp = temp.next
        if temp is None:
            print("Less than {} elements in the linked list. Cannot update.".format(position))
        else:
            temp.data = value
            print("Value updated at position {}".format(position))
    def delete_from_start(self):
        if self.is_empty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None
    def delete_from_last(self):
        if self.is_empty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.previous.next = None
            temp.previous = None
    def delete(self, value):
        if self.is_empty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            if self.head.data == value:
                self.head = None
        else:
            temp = self.head
            while temp is not None:
                if temp.data == value:
                    break
                temp = temp.next
            if temp is None:
                print("Element not present in linked list. Cannot delete element.")
            elif temp.next is None:
                self.delete_from_last()
            else:
                temp.next = temp.previous.next
                temp.next.previous = temp.previous
                temp.next = None
                temp.previous = None
    def delete_from_position(self, position):
        if self.is_empty():
            print("Linked List is empty. Cannot delete elements.")
        elif position == 1:
            self.delete_from_start()
        else:
            temp = self.head
            count = 1
            while temp is not None:
                if count == position:
                    break
                temp = temp.next
            if temp is None:
                print("There are less than {} elements in linked list. Cannot delete element.".format(position))
            elif temp.next is None:
                self.delete_from_last()
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                temp.next = None
                temp.previous = None


if __name__ == '__main__':
    dll = DoublyLinkedList()
    print(dll.is_empty())
    dll.insert_at_start(5)
    dll.show_linked_list()
    dll.insert_to_end(10)
    dll.show_linked_list()
    dll.delete_from_last()
    dll.show_linked_list()
    dll.insert_to_end(25)
    dll.show_linked_list()
    dll.delete_from_last()
    dll.delete_from_start()
    dll.insert_to_end(100)
    dll.show_linked_list()


# Output:

"""
True
5
5
10
5
5
25
100
"""