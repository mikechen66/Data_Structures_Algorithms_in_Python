

# binary_tree_node.py


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


def search(root, value):
    # Node is empty
    if root is None:
        return False
    # If element is equal to the element to be searched
    elif root.data == value:
        return True
    # Element to be searched is less than the current node
    elif root.data > value:
        return search(root.leftchild, value)
    # Element to be searched is greater than the current node
    else:
        return search(root.rightchild, value)


if __name__ == '__main__':
    root = insert(None, 50)
    insert(root, 20)
    insert(root, 53)
    insert(root, 11)
    insert(root, 22)
    insert(root, 52)
    insert(root, 78)
    print("53 is present in the binary tree:", search(root, 53))
    print("100 is present in the binary tree:", search(root, 100))


# Output:

"""
<__main__.BinaryTreeNode object at 0x7f57b3800190>
<__main__.BinaryTreeNode object at 0x7f57b3800190>
<__main__.BinaryTreeNode object at 0x7f57b3800190>
<__main__.BinaryTreeNode object at 0x7f57b3800190>
<__main__.BinaryTreeNode object at 0x7f57b3800190>
<__main__.BinaryTreeNode object at 0x7f57b3800190>
53 is present in the binary tree: True
100 is present in the binary tree: False
"""