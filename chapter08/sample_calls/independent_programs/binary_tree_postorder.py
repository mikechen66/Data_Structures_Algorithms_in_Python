

# binary_tree_postporder.py


# Python program for postorder traversals


# Structure of a Binary Tree Node

class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


# Function to print postorder traversal

def show_postorder(node):
    if node == None:
        return
    # First recur on left subtree
    show_postorder(node.left)
    # Then recur on right subtree
    show_postorder(node.right)
    # Now deal with the node
    print(node.data, end=' ')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    # Function call
    print("Postorder traversal of binary tree is:")
    show_postorder(root)
    print()


# Output:


"""
Postorder traversal of binary tree is:
4 5 2 6 3 1
"""