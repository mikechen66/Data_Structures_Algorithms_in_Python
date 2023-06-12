

# splay_tree_call.py


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        # x is root
        if x.parent == None:
            self.root = y
        # x is left child
        elif x == x.parent.left:
            x.parent.left = y
        # x is right child
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        # x is root
        if x.parent == None:
            self.root = y
        # x is right child
        elif x == x.parent.right:
            x.parent.right = y
        # x is left child
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    def splay(self, n):
        # node is not root
        while n.parent != None:
            # node is child of root, one rotation
            if n.parent == self.root:
                if n == n.parent.left:
                    self.rightRotate(n.parent)
                else:
                    self.leftRotate(n.parent)
            else:
                p = n.parent
                g = p.parent  # grandparent
                if n.parent.left == n and p.parent.left == p:  # both are left children
                    self.rightRotate(g)
                    self.rightRotate(p)
                elif n.parent.right == n and p.parent.right == p:  # both are right children
                    self.leftRotate(g)
                    self.leftRotate(p)
                elif n.parent.right == n and p.parent.left == p:
                    self.leftRotate(p)
                    self.rightRotate(g)
                elif n.parent.left == n and p.parent.right == p:
                    self.rightRotate(p)
                    self.leftRotate(g)
    def insert(self, n):
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        n.parent = y
        if y == None:  # newly added node is root
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n
        self.splay(n)
    def bstSearch(self, n, x):
        if x == n.data:
            self.splay(n)
            return n
        elif x < n.data:
            return self.bstSearch(n.left, x)
        elif x > n.data:
            return self.bstSearch(n.right, x)
        else:
            return None
    def inOrder(self, n):
        if n != None:
            self.inOrder(n.left)
            print(n.data, end=' ')
            self.inOrder(n.right)


if __name__ == '__main__':
    tree = SplayTree()
    a = TreeNode(10)
    b = TreeNode(20)
    c = TreeNode(30)
    d = TreeNode(100)
    e = TreeNode(90)
    f = TreeNode(40)
    g = TreeNode(50)
    tree.insert(a)
    tree.insert(b)
    tree.insert(c)
    tree.insert(d)
    tree.insert(e)
    tree.insert(f)
    tree.insert(g)
    tree.bstSearch(tree.root, 90)
    tree.inOrder(tree.root)
    print()


# Output:

"""
<__main__.TreeNode object at 0x7f342e099810>
10 20 30 40 50 90 100 
"""