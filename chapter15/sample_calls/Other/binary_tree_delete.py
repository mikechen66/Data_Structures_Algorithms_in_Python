

# binary_tree_delete.py

"""
Algorithm:

Starting at the root, find the deepest and rightmost node in the binary tree and the node 
which we want to delete;

Replace the deepest rightmost node’s data with the node to be deleted;

Then delete the deepest rightmost node.
"""


# class to create a node with data, left child and right child.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inorder traversal of a binary tree

def inorder(temp):
    if(not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


# function to delete the given deepest node (d_node) in binary tree

def delete_deepest(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)


# function to delete element in binary tree

def delete(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        delete_deepest(root, temp)
        key_node.data = x
    return root


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion: ", end = "")
    inorder(root)
    key = 11
    root = delete(root, key)
    print();
    print("The tree after the deletion: ", end = "")
    inorder(root)
    print()


# Output:

"""
The tree before the deletion: 7 11 12 10 15 9 8 
The tree after the deletion: 7 8 12 10 15 9 
"""