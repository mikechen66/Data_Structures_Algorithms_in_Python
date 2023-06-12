

# binary_tree_preorder.py

"""
# A program to construct Binary Tree from preorder traversal

Approach: The first element in pre[] will always be root. So we can easily figure 
out the root. If the left subtree is empty, the right subtree must also be empty, 
and the preLN[] entry for root must be ‘L’. We can simply create a node and return 
it. If the left and right subtrees are not empty, then recursively call for left 
and right subtrees and link the returned nodes to root.  
"""


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# A recursive function to create a Binary Tree from given pre[] preln[]
# arrays. The function returns root of tree. index_ptr is used to update
# index values in recursive calls. index must be initially passed as 0
def construct_tree_util(pre, preln, index_ptr, n):
    index = index_ptr[0] # store the current value
                         # of index in pre[]
    # Base Case: All nodes are constructed
    if index == n:
        return None
    # Allocate memory for this node and increment index for subsequent
    # recursive calls
    temp = newNode(pre[index])
    index_ptr[0] += 1
    # If this is an internal node, construct left and right subtrees and 
    # link the subtrees
    if preln[index] == 'N':
        temp.left = construct_tree_util(pre, preln, index_ptr, n)
        temp.right = construct_tree_util(pre, preln, index_ptr, n)
    return temp


# A wrapper over constructTreeUtil()
def construct_tree(pre, preln, n):
    # Initialize index as 0. Value of index is
    # used in recursion to maintain the current
    # index in pre[] and preLN[] arrays.
    index = [0]
    return construct_tree_util(pre, preln, index, n)


# This function is used only for testing
def show_inorder (node):
    if node == None:
        return
    # first recur on left child
    show_inorder (node.left)
    # then print the data of node
    print(node.data, end=" ")
    # now recur on right child
    show_inorder(node.right)


if __name__ == '__main__':
    root = None
    # Constructing tree given in the above figure
    #    10
    #    / \
    # 30 15
    # / \
    # 20 5
    pre = [10, 30, 20, 5, 15]
    preLN = ['N', 'N', 'L', 'L', 'L']
    n = len(pre)
    # construct the above tree
    root = construct_tree (pre, preLN, n)
    # Test the constructed tree
    print("Following is Inorder Traversal of",
        "the Constructed Binary Tree:")
    show_inorder(root)
    print()


# Output:


"""
Following is Inorder Traversal of the Constructed Binary Tree:
20 30 5 10 15 
"""