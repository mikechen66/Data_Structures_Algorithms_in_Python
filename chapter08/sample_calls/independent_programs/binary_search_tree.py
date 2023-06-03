

# bst_call.py

# It is the class of SearchBianryTree that is called by a caller. 


class Node(object):
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.parent = None
        self.left_child = left_child
        self.right_child = right_child


class SearchBinaryTree(object):
    def __init__(self):
        self.__root = None
        self.prefix_branch = '├'
        self.prefix_trunk  = '|'
        self.prefix_leaf   = '└'
        self.prefix_empty  = ''
        self.prefix_left   = '─L─'
        self.prefix_right  = '─R─'
    def is_empty(self):
        return not self.__root
    @property
    def root(self):
        return self.__root
    @root.setter
    def root(self, value):
        self.__root = value if isinstance(value, Node) else Node(value)
    def show_tree(self):
        if self.is_empty():
            print('Empty binary tree')
            return
        print('-' * 20)
        print(self.__root.data)
        self.__print_tree(self.__root)
        print('-' * 20)
    def levelorder_traversal(self):
        if self.is_empty():
            return
        queue = list()
        queue.insert(0, self.__root)
        while len(queue):
            cur = queue.pop()
            print(cur.data, end=' ')
            if cur.left_child is not None:
                queue.insert(0, cur.left_child)
            if cur.right_child is not None:
                queue.insert(0, cur.right_child)
        print()
    def preorder_traversal(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder_traversal(node.left_child)
        self.preorder_traversal(node.right_child)
    def inorder_traversal(self, node):
        if node is None:
            return
        self.inorder_traversal(node.left_child)
        print(node.data, end=' ')
        self.inorder_traversal(node.right_child)
    def postorder_traversal(self, node):
        if node is None:
            return
        self.postorder_traversal(node.left_child)
        self.postorder_traversal(node.right_child)
        print(node.data, end=' ')
    def __print_tree(self, node, prefix=None):
        if prefix is None:
            prefix, prefix_left_child = '', ''
        else:
            prefix = prefix.replace(self.prefix_branch, self.prefix_trunk)
            prefix = prefix.replace(self.prefix_leaf, self.prefix_empty)
            prefix_left_child = prefix.replace(self.prefix_leaf, self.prefix_empty)
        if self.has_child(node):
            if node.right_child is not None:
                print(prefix + self.prefix_branch + self.prefix_right + str(node.right_child.data))
                if self.has_child(node.right_child):
                    self.__print_tree(node.right_child, prefix + self.prefix_branch + ' ')
            else:
                print(prefix + self.prefix_branch + self.prefix_right)
            if node.left_child is not None:
                print(prefix + self.prefix_leaf + self.prefix_left + str(node.left_child.data))
                if self.has_child(node.left_child):
                    prefix_left_child += '  '
                    self.__print_tree(node.left_child, self.prefix_leaf + prefix_left_child)
            else:
                print(prefix + self.prefix_leaf + self.prefix_left)
    def has_child(self, node):
        return node.left_child is not None or node.right_child is not None
    def __str__(self):
        return str(self.__class__)
    def insert(self, root, value):
            # Insert nodes recursively
            node = value if isinstance(value, Node) else Node(value)
            if self.is_empty():
                self.root = node
                return
            if root is None:
                root = node
            elif node.data < root.data:
                root.left_child = self.insert(root.left_child, value)
                root.left_child.parent = root
            elif node.data > root.data:
                root.right_child = self.insert(root.right_child, value)
                root.right_child.parent = root
            return root
    def insert_normal(self, value):
            # Insert nodes without recursion
            node = value if isinstance(value, Node) else Node(value)
            if self.is_empty():
                self.root = node
                return
            else:
                current_node = self.root
                while True:
                    if node.data < current_node.data:
                        if current_node.left_child:
                            current_node = current_node.left_child
                        else:
                            current_node.left_child = node
                            node.parent = current_node
                            break
                    elif node.data > current_node.data:
                        if current_node.right_child:
                            current_node = current_node.right_child
                        else:
                            current_node.right_child = node
                            node.parent = current_node
                            break
                    else:
                        break


if __name__ == '__main__':
    tree = SearchBinaryTree()
    data = [50, 77, 55, 29, 10, 50, 30, 66, 18, 80, 51, 18, 90]
    for i in data:
        # tree.insert_normal(i)
        tree.insert(tree.root, i)
    tree.show_tree()


# Output:

"""
--------------------
50
├─R─77
| ├─R─80
| | ├─R─90
| | └─L─
| └─L─55
|   ├─R─66
|   └─L─51
└─L─29
  ├─R─30
  └─L─10
    ├─R─18
    └─L─
--------------------
"""


################################################################################################



# binary_search_tree1.py
# https://blog.csdn.net/ca___0/article/details/111385872


from collections import Iterable
import networkx as nx
import matplotlib.pyplot as plt


class TreeNode:
    '''二叉搜索树节点的定义'''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class OperationTree:
    '''二叉搜索树操作'''
    def insert(self, root, val):
        '''二叉搜索树插入操作'''
        if root == None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root
    def query(self, root, val):
        '''二叉搜索树查询操作'''
        if root == None:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.query(root.left, val)
        elif val > root.val:
            return self.query(root.right, val)
    def findMin(self, root):
        '''查找二叉搜索树中最小值点'''
        if root.left:
            return self.findMin(root.left)
        else:
            return root
    def findMax(self, root):
        '''查找二叉搜索树中最大值点'''
        if root.right:
            return self.findMax(root.right)
        else:
            return root
    def delNode(self, root, val):
        '''删除二叉搜索树中值为val的点'''
        if root == None:
            return
        if val < root.val:
            root.left = self.delNode(root.left, val)
        elif val > root.val:
            root.right = self.delNode(root.right, val)
        # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
        else:
            if root.left and root.right:
                # 既有左子树又有右子树，则需找到右子树中最小值节点
                temp = self.findMin(root.right)
                root.val = temp.val
                # 再把右子树中最小值节点删除
                root.right = self.delNode(root.right, temp.val)
            elif root.right == None and root.left == None:
                # 左右子树都为空
                root = None
            elif root.right == None:
                # 只有左子树
                root = root.left
            elif root.left == None:
                # 只有右子树
                root = root.right
        return root
    def printTree(self, root):
        # 打印二叉搜索树(中序打印，有序数列)
        if root == None:
            return
        self.printTree(root.left)
        print(root.val, end = ' ')
        self.printTree(root.right)


if __name__ == '__main__':
    List = [17,5,35,2,11,29,38,9,16,8]
    root = None
    op = OperationTree()
    for val in List:
        root = op.insert(root,val)
    print('中序打印二叉搜索树：', end = ' ')
    op.printTree(root)
    print('')
    print('根节点的值为：', root.val)
    print('树中最大值为:', op.findMax(root).val)
    print('树中最小值为:', op.findMin(root).val)
    print('查询树中值为5的节点:', op.query(root, 5))
    print('查询树中值为100的节点:', op.query(root, 100))
    print('删除树中值为16的节点:', end = ' ')
    root = op.delNode(root, 16)
    op.printTree(root)
    print('')
    print('删除树中值为5的节点:', end = ' ')
    root = op.delNode(root, 5)
    op.printTree(root)
    print('')


# Output:

"""
中序打印二叉搜索树： 2 5 8 9 11 16 17 29 35 38 
根节点的值为： 17
树中最大值为: 38
树中最小值为: 2
查询树中值为5的节点: True
查询树中值为100的节点: False
删除树中值为16的节点: 2 5 8 9 11 17 29 35 38 
删除树中值为5的节点: 2 8 9 11 17 29 35 38 
"""

#####################################################################################################


# 树的可视化


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点


from collections import Iterable


class BinaryTree:
    def __init__(self, seq=()):
        assert isinstance(seq, Iterable)  # 确保输入的参数为可迭代对象
        self.root = None
        self.insert(*seq)
    def insert(self, *args):
        if not args:
            return
        if not self.root:
            self.root = Node(args[0])
            args = args[1:]
        for i in args:
            seed = self.root
            while True:
                if i > seed.value:
                    if not seed.right:
                        node = Node(i)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = Node(i)
                        seed.left = node
                        break
                    else:
                        seed = seed.left
    def minNode(self):
        node = self.root
        while node.left:
            node = node.left
        return node
    def maxNode(self):
        node = self.root
        while node.right:
            node = node.right
        return node


import networkx as nx
import matplotlib.pyplot as plt


def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.value] = (x, y)
    if node.left:
        G.add_edge(node.value, node.left.value)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.value, node.right.value)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)

def draw(node):   # 以某个节点为根画图
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()


if __name__ == '__main__':
    List = [17,5,35,2,11,29,38,9,16,8]
    tree = BinaryTree()
    tree.insert(*List)
    draw(tree.root)


#####################################################################################################


# BST
# https://www.cnblogs.com/lilip/p/9937697.html
# https://www.cnblogs.com/lilip/p/9937697.html

# encoding=utf-8
import queue
 
class TreeNode(object):
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
        self.father = None

 
class BST(object):
    def __init__(self,nodeList):
        self.root = None
        for node in nodeList:
            self.bfs_insert(node)
    def bfs_insert(self,node):
        father = None
        cur = self.root
        while cur != None:
            if cur.value == node.value:
                return -1
            father = cur
            if node.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        node.father = father
        if father == None:
            self.root = node
        elif node.value < father.value:
            father.left = node
        else:
            father.right = node
    def bfs(self):
        if self.root == None:
            return None
        retList = []
        q = queue.Queue()
        q.put(self.root)
        while q.empty() is not True:
            node = q.get()
            retList.append(node.value)
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)
        return retList
    def bfs_search(self,value):
        cur = self.root
        while cur != None:
            if cur.value == value:
                return cur
            elif cur.value < value:
                cur = cur.right
            else:
                cur = cur.left
        return None
    def bfs_delete(self,node):
        father = node.father
        if node.left == None:
            if father == None:
                self.root = node.right
                if node.right != None:
                    node.right.father = None
            elif father.left == node:
                father.left = node.right
                if node.right != None:
                    node.right.father = father
            else:
                father.right = node.right
                if node.right != None:
                    node.right.father = father
            return 'delete successfully'
        tmpNode = node.left
        while tmpNode.right != None:
            tmpNode = tmpNode.right
        tmpNode.right = node.right
        if node.right != None:
            node.right.father = tmpNode
        if father == None:
            self.root = node.left
            node.left.father = None
        elif father.left == node:
            father.left = node.left
            node.left.father = father
        else:
            father.right = node.left
            node.left.father = father
        node = None
        return 'delete successfully'


if __name__ == '__main__':
    varList = [24,34,5,4,8,23,45,35,28,6,29]
    nodeList = [TreeNode(var) for var in varList]
    bst = BST(nodeList)
    print (bst.bfs())
    node = bst.bfs_search(34)
    bst.bfs_delete(node)
    print (bst.bfs())