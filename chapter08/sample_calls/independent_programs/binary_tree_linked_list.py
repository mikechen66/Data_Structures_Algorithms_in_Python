

# binary_tree_linked_list.py


"""
# Python program to create a Complete Binary Tree from its linked list representation

1. Create an empty queue. 
2. Make the first node of the list as root, and enqueue it to the queue. 
3. Until we reach the end of the list, do the following. 
   a. Dequeue one node from the queue. This is the current parent. 
   b. Traverse two nodes in the list, add them as children of the current parent. 
   c. Enqueue the two nodes into the queue.
"""

# Linked List node
class ListNode:
        # Constructor to create a new node
        def __init__(self, data):
            self.data = data
            self.next = None


# Binary Tree Node structure
class BinaryTreeNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Class to convert the linked list to Binary Tree
class Conversion:
    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self, data = None):
        self.head = None
        self.root = None
    def push(self, new_data):
        # Creating a new linked list node and storing data
        new_node = ListNode(new_data)
        # Make next of new node as head
        new_node.next = self.head
        # Move the head to point to new node
        self.head = new_node
    def convertlist2binary(self):
        # Queue to store the parent nodes
        q = []
        # Base Case
        if self.head is None:
            self.root = None
            return
        # 1.) The first node is always the root node,
        # and add it to the queue
        self.root = BinaryTreeNode(self.head.data)
        q.append(self.root)
        # Advance the pointer to the next node
        self.head = self.head.next
        # Until the end of linked list is reached, do:
        while(self.head):
            # 2.a) Take the parent node from the q and
            # and remove it from q
            parent = q.pop(0) # Front of queue
            # 2.c) Take next two nodes from the linked list.
            # We will add them as children of the current
            # parent node in step 2.b.
            # Push them into the queue so that they will be
            # parent to the future node
            leftChild= None
            rightChild = None
            leftChild = BinaryTreeNode(self.head.data)
            q.append(leftChild)
            self.head = self.head.next
            if(self.head):
                rightChild = BinaryTreeNode(self.head.data)
                q.append(rightChild)
                self.head = self.head.next
            #2.b) Assign the left and right children of parent
            parent.left = leftChild
            parent.right = rightChild
    def inorder_traversal(self, root):
        if(root):
            self.inorder_traversal(root.left)
            print(root.data,end=" ")
            self.inorder_traversal(root.right)


if __name__ == '__main__':
    # Object of conversion class
    conv = Conversion()
    conv.push(36)
    conv.push(30)
    conv.push(25)
    conv.push(15)
    conv.push(12)
    conv.push(10)
    conv.convertlist2binary()
    print("Inorder Traversal of the constructed Binary Tree is:")
    conv.inorder_traversal(conv.root)
    print()


# Output:

"""
Inorder Traversal of the constructed Binary Tree is:
25 12 30 10 36 15 
"""