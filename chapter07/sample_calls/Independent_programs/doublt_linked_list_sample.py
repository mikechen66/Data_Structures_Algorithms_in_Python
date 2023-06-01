

# doublt_linked_list_sample.py

"""
A doubly linked list has more efficient iteration, particularly if you need to ever iterate 
in reverse and more efficient deletion of particular nodes.

We conclude that a doubly linked list is a complex type of linked list where a node contains 
a pointer to the previous as well as the next node in the sequence. Therefore, in a doubly 
linked list, a node consists of three components: node data, pointer to the next node in node
(next pointer), pointer to the former node (previous pointer).
"""


class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


# Class for doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
    # Insert Element to Empty list
    def insert_to_empty_list(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")
    # Insert element at the end
    def insert_to_end(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    # Delete the elements from the start
    def delete_at_start(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None;
    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    # Traversing and Displaying each element of the list
    def display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_to_empty_list(10)
    dll.insert_to_end(20)
    dll.insert_to_end(30)
    dll.insert_to_end(40)
    dll.insert_to_end(50)
    dll.insert_to_end(60)
    dll.display()
    dll.delete_at_start()
    dll.delete_at_start()
    dll.display()


# Output:


"""
Element is:  10
Element is:  20
Element is:  30
Element is:  40
Element is:  50
Element is:  60


Element is:  30
Element is:  40
Element is:  50
Element is:  60
"""