

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;
    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    # Inserting Item at Specific Index
    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False
    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)
    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        self.start_node = self.start_node.ref
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        # Deleting first node 
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref
    

if __name__ == '__main__':
    new_linked_list = LinkedList()
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(15)
    new_linked_list.traverse_list()
    new_linked_list.insert_at_start(20)
    new_linked_list.insert_after_item(10, 17)
    new_linked_list.traverse_list()
    new_linked_list.insert_before_item(17, 25)
    new_linked_list.insert_at_index(3,8)
    new_linked_list.traverse_list()
    new_linked_list.search_item(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(20)
    new_linked_list.insert_at_end(30)
    new_linked_list.insert_at_end(40)
    new_linked_list.insert_at_end(50)
    new_linked_list.delete_at_start()
    new_linked_list.delete_at_end()


# Output:

"""
5  
10  
15  
<__main__.Node object at 0x7f9b43ac7950>
20  
5  
10  
17  
15  
<__main__.Node object at 0x7f9b43ac7950>
20  
5  
8  
10  
25  
17  
15  
Item found
True
"""