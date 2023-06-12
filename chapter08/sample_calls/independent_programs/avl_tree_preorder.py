


# avl_tree_preorder.py

"""

AVL is Adelson-Velskii and Landis also known as a height balanced binary search tree. The difference 
between the heights of the right subtree and left subtree of every node is either -1, 0, or 1. It is 
maintained by a factor named as balance factor. 

1.Rotation

When certain operations like insertion and deletion are performed on the AVL tree, the balance factor 
may get affected. If after the insertion or deletion of the element, the balance factor of any node 
is affected then this problem is overcome by using rotation. Rotation is the method of moving the nodes 
of trees either to left or to right to make the tree heightened balance tree. It is divided into two 
further parts as follows. 

1) Single Rotation 

Single rotation switches the roles of the parent and child while maintaining the search order. We rotate 
the node and its child, the child becomes a parent.

(1). Single LL(Left Left) Rotation

Every node of the tree moves toward the left from its current position. Therefore, a parent becomes the 
right child in the LL rotation,

(2). Single RR(Right Right) Rotation

Every node of the tree moves toward the right from the current position. Therefore, the parent becomes 
a left child in RR rotation. 

2) Double Rotation

Single rotation does not fix the LR rotation and RL rotation. We require double rotation involving three 
nodes. Therefore, double rotation is equivalent to the sequence of two single rotations.

(1). LR(Left-Right) Rotation

The LR rotation is the process where we perform a single left rotation followed by a single right rotation. 
Therefore, first, every node moves towards the left and then the node of this new tree moves one position 
towards the right.

(2). RL (Right-Left) Rotation

The RL rotation is the process where we perform a single right rotation followed by a single left rotation. 
Therefore, first, every node moves towards the right and then the node of this new tree moves one position 
towards the left. 


2. Insertion Operation

The new node is always added as a leaf. After the insertion of the new node, it is necessary to modify the 
balance factor of each node in the AVL tree using the rotation operations. The algorithm steps of insertion 
operation in an AVL tree are:

Find the appropriate empty subtree where the new value should be added by comparing the values in the tree;
Create a new node at the empty subtree;
The new node is a leaf and thus will have a balance factor of zero;
Return to the parent node and adjust the balance factor of each node through the rotation process and continue 
it until we are back at the root. Remember that the modification of the balance factor must happen in a bottom
up fashion.

3. Deletion Operation: 

Deletion is the same as the deletion operation in BST. The node is always deleted as a leaf node and after 
the deletion of the node, the balance factor of each node is modified accordingly. Rotation operations are used 
to modify the balance factor of each node. The algorithm steps of deletion 
operation in an AVL tree are:

Locate the node to be deleted;
If the node does not have any child, then remove the node;
If the node has one child node, replace the content of the deletion node with the child node and remove the node;
If the node has two children nodes, find the inorder successor node ‘k' which has no child node and replace the 
contents of the deletion node with the ‘k’ followed by removing the node;

Update the balance factor of the AVL tree
"""


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def insert(self, root, key):
        if not root:                                     # if not root, return TreeNode(key) as root
            return TreeNode(key)
        elif key < root.value:                           # root is explicitly represented as TreeNode(value) 
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        bal = self.get_bal(root)                         # bal is in the range(-1,0,1)
        if bal > 1 and key < root.left.value:            # Single right rotation
            return self.right_rotate(root)
        if bal < -1 and key > root.right.value:          # Single left rotation 
            return self.left_rotate(root)
        if bal > 1 and key > root.left.value:
            root.left = self.left_rotate(root.left)      # LR double rotation
            return self.right_rotate(root)
        if bal < -1 and key < root.right.value:          # RL double rotation 
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def left_rotate(self, z):                            # z is a new-added node 
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    def get_bal(self, root):                            # get balance 
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def preorder(self, root):
        if not root:
            return None
        print("{0} ".format(root.value), end="")
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    tree = AVLTree()
    root = None                                          # root is defaulted as None
    root = tree.insert(root, 1)
    print(root)
    root = tree.insert(root, 3)
    print(root)
    root = tree.insert(root, 5)
    print(root)
    root = tree.insert(root, 7)
    print(root)
    root = tree.insert(root, 9)
    print(root)
    # preorder Traversal
    print("The preorder traversal of the constructed",
          "AVL tree is listed as follows")
    tree.preorder(root)
    print()

# Output:

"""
<__main__.TreeNode object at 0x7fbf7f7b6490>
<__main__.TreeNode object at 0x7fbf7f7b6490>
<__main__.TreeNode object at 0x7fbf7f7b64d0>
<__main__.TreeNode object at 0x7fbf7f7b64d0>
<__main__.TreeNode object at 0x7fbf7f7b64d0>
The preorder traversal of the constructed AVL tree is listed as follows
3 1 7 5 9 

Since it is constructed step by step, we give the final structure as follows. 
  
                  3              
                 /  \            
                1    7
                    / \
                   5   9
"""

##################################################################################################


if __name__ == '__main__':
    tree = AVLTree()
    root = None                                          # root is defaulted as None
    root = tree.insert(root, 1)
    print(root)
    root = tree.insert(root, 3)
    print(root)
    root = tree.insert(root, 5)
    print(root)
    root = tree.insert(root, 7)
    print(root)
    root = tree.insert(root, 9)
    print(root)
    root = tree.insert(root, 6)
    print(root)
    # preorder Traversal
    print("The preorder traversal of the constructed",
          "AVL tree is listed as follows")
    tree.preorder(root)
    print()


# Output:

"""
<__main__.TreeNode object at 0x7f078833e490>
<__main__.TreeNode object at 0x7f078833e490>
<__main__.TreeNode object at 0x7f078833e4d0>
<__main__.TreeNode object at 0x7f078833e4d0>
<__main__.TreeNode object at 0x7f078833e4d0>
<__main__.TreeNode object at 0x7f078833e510>
The preorder traversal of the constructed AVL tree is listed as follows
5 3 1 7 6 9 
"""

##################################################################################################


if __name__ == '__main__':
    tree = AVLTree()
    root = None                                          # root is defaulted as None
    root = tree.insert(root, 1)
    print(root)
    root = tree.insert(root, 2)
    print(root)
    root = tree.insert(root, 3)
    print(root)
    root = tree.insert(root, 4)
    print(root)
    root = tree.insert(root, 5)
    print(root)
    root = tree.insert(root, 6)
    print(root)
    # preorder Traversal
    print("The preorder traversal of the constructed",
          "AVL tree is listed as follows")
    tree.preorder(root)
    print()


# Output:


"""
<__main__.TreeNode object at 0x7f14adf834d0>
<__main__.TreeNode object at 0x7f14adf834d0>
<__main__.TreeNode object at 0x7f14adf83510>
<__main__.TreeNode object at 0x7f14adf83510>
<__main__.TreeNode object at 0x7f14adf83510>
<__main__.TreeNode object at 0x7f14adf83590>
The preorder traversal of the constructed AVL tree is listed as follows
4 2 1 3 5 6 
"""

################################################################################################


if __name__ == '__main__':
    tree = AVLTree()
    root = None
    root = tree.insert(root, 6)
    print(root)
    root = tree.insert(root, 5)
    print(root)
    root = tree.insert(root, 4)
    print(root)
    root = tree.insert(root, 3)
    print(root)
    root = tree.insert(root, 2)
    print(root)
    root = tree.insert(root, 1)
    print(root)
    # preorder Traversal
    print("The preorder traversal of the constructed",
          "AVL tree is listed as follows")
    tree.preorder(root)
    print()


# Output:

"""
<__main__.TreeNode object at 0x7f370a5a64d0>
<__main__.TreeNode object at 0x7f370a5a64d0>
<__main__.TreeNode object at 0x7f370a5a6510>
<__main__.TreeNode object at 0x7f370a5a6510>
<__main__.TreeNode object at 0x7f370a5a6510>
<__main__.TreeNode object at 0x7f370a5a6590>
The preorder traversal of the constructed AVL tree is listed as follows
3 2 1 5 4 6 
>>> 
"""

################################################################################################


if __name__ == '__main__':
    tree = AVLTree()
    root = None
    root = tree.insert(root, 3)
    root = tree.insert(root, 1)
    root = tree.insert(root, 2)
    root = tree.insert(root, 5)
    root = tree.insert(root, 6)
    root = tree.insert(root, 4)
    # preorder Traversal
    print("The preorder traversal of the constructed",
          "AVL tree is listed as follows")
    tree.preorder(root)
    print()


# Output:

"""
The preorder traversal of the constructed AVL tree is listed as follows
3 2 1 5 4 6 
"""