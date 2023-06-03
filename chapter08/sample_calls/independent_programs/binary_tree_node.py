

# binary_tree_node.py

"""

A binary search tree is a binary tree data structure with the following properties.

There are no duplicate elements in a binary search tree.
The element at the left child of a node is always less than the element at the current node.  
The left subtree of a node has all elements less than the current node.
The element at the right child of a node is always greater than the element at the current node.
The right subtree of a node has all elements greater than the current node. 
"""


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insert(root, newvalue):
    # If binary search tree is empty, create a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newvalue)
        return root
    # If newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newvalue < root.data:
        root.leftchild = insert(root.leftchild, newvalue)
    else:
        # If newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightchild = insert(root.rightchild, newvalue)
    return root


if __name__ == '__main__':
    root = insert(None, 50)
    insert(root, 20)
    insert(root, 53)
    insert(root, 11)
    insert(root, 22)
    insert(root, 52)
    insert(root, 78)
    node1 = root
    node2 = node1.leftchild
    node3 = node1.rightchild
    node4 = node2.leftchild
    node5 = node2.rightchild
    node6 = node3.leftchild
    node7 = node3.rightchild
    print("Root Node is:")
    print(node1.data)
    print("left child of the node is:")
    print(node1.leftchild.data)
    print("right child of the node is:")
    print(node1.rightchild.data)
    print("Node is:")
    print(node2.data)
    print("left child of the node is:")
    print(node2.leftchild.data)
    print("right child of the node is:")
    print(node2.rightchild.data)
    print("Node is:")
    print(node3.data)
    print("left child of the node is:")
    print(node3.leftchild.data)
    print("right child of the node is:")
    print(node3.rightchild.data)
    print("Node is:")
    print(node4.data)
    print("left child of the node is:")
    print(node4.leftchild)
    print("right child of the node is:")
    print(node4.rightchild)
    print("Node is:")
    print(node5.data)
    print("left child of the node is:")
    print(node5.leftchild)
    print("right child of the node is:")
    print(node5.rightchild)
    print("Node is:")
    print(node6.data)
    print("left child of the node is:")
    print(node6.leftchild)
    print("right child of the node is:")
    print(node6.rightchild)
    print("Node is:")
    print(node7.data)
    print("left child of the node is:")
    print(node7.leftchild)
    print("right child of the node is:")
    print(node7.rightchild)


# Output:

"""
<__main__.BinaryTreeNode object at 0x7f69915dc450>
<__main__.BinaryTreeNode object at 0x7f69915dc450>
<__main__.BinaryTreeNode object at 0x7f69915dc450>
<__main__.BinaryTreeNode object at 0x7f69915dc450>
<__main__.BinaryTreeNode object at 0x7f69915dc450>
<__main__.BinaryTreeNode object at 0x7f69915dc450>
Root Node is:
50
left child of the node is:
20
right child of the node is:
53
Node is:
20
left child of the node is:
11
right child of the node is:
22
Node is:
53
left child of the node is:
52
right child of the node is:
78
Node is:
11
left child of the node is:
None
right child of the node is:
None
Node is:
22
left child of the node is:
None
right child of the node is:
None
Node is:
52
left child of the node is:
None
right child of the node is:
None
Node is:
78
left child of the node is:
None
right child of the node is:
None
"""