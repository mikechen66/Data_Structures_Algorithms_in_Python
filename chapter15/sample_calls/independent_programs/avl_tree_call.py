

# avl_tree_call.py


# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the Insert operation
class AvlTree(object):
    # Insert key in subtree rooted with node and returns new root of subtree.
    def insert(self, root, key):
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left),
                        self.get_height(root.right))
        # Step 3 - Get the balance factor
        balance = self.get_balance(root)
        # Step 4 - If the node is unbalanced, then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))
        # Return the new root
        return y
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))
        # Return the new root
        return y
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def pre_order(self, root):
        if not root:
            return None
        print("{0} ".format(root.val), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)



if __name__ == '__main__':
    at = AvlTree()
    root = None
    root = at.insert(root, 10)
    root = at.insert(root, 20)
    root = at.insert(root, 30)
    root = at.insert(root, 40)
    root = at.insert(root, 50)
    root = at.insert(root, 25)
    """
    The constructed AVL Tree would be
             30
            / \
          20   40
         / \    \
        10 25    50
    """
    # pre_order Traversal
    print("pre_order traversal of the",
        "constructed AVL tree is")
    at.pre_order(root)
    print()


# Output:

"""
pre_order traversal of the constructed AVL tree is
30 20 10 25 40 50 
"""
