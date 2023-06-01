

# doubly_linked_list_simple.py


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_head(self, value):
        n = Node(value)
        n.next = self.head
        if(self.head != None):
            self.head.prev = n
        self.head = n
    def insert_at_tail(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = n
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_tail(1)
    dll.insert_at_tail(2)
    dll.insert_at_tail(3)
    dll.insert_at_tail(4)
    dll.insert_at_tail(5)
    print("After insertion at tail: ")
    dll.display()
    dll.insert_at_head(0)
    print("\nAfter insertion at head: ")
    dll.display()
    print()


# Output:

"""
After insertion at tail: 
1 2 3 4 5 
After insertion at head: 
0 1 2 3 4 5 
"""