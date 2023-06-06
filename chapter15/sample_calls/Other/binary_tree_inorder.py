

# binary_tree_inorder.py


"""
# inorder traversal for binary tree

1) Initialize list of Binary Trees as empty.  
2) For every element in[i] where i varies from 0 to n-1,
    do following
    a) Create a new node with key as 'arr[i]', let this node be 'node'
    b) Recursively construct list of all left subtrees.
    c) Recursively construct list of all right subtrees.
3) Iterate for all left subtrees
   a) For current leftsubtree, iterate for all right subtrees
      Add current left and right subtrees to 'node' and add 'node' to 
      list.
"""


# Node Structure
class Node:
    # Utility to create a new node
    def __init__(self , item):
        self.key = item
        self.left = None
        self.right = None


# A utility function to do preorder traversal of BST
def preorder(root):
    if root is not None:
        print (root.key,end=" ")
        preorder(root.left)
        preorder(root.right)


# Function for constructing all possible trees with
# given inorder traversal stored in an array from
# arr[start] to arr[end]. This function returns a
# vector of trees.
def get_trees(arr , start , end):
    # List to store all possible trees
    trees = []
    """ 
    if start > end then subtree will be empty so
    returning NULL in the list 
    """
    if start > end :
        trees.append(None)
        return trees
        """ 
        Iterating through all values from start to end
        for constructing left and right subtree
        recursively 
        """
    for i in range(start , end+1):
        # Constructing left subtree
        ltrees = get_trees(arr , start , i-1)
        # Constructing right subtree
        rtrees = get_trees(arr , i+1 , end)
        """ 
        Looping through all left and right subtrees
        and connecting to ith root below
        """
        for j in ltrees :
            for k in rtrees :
                # Make arr[i] as root
                node = Node(arr[i])
                # Connect left subtree
                node.left = j
                # Connect right subtree
                node.right = k
                # Add this tree to list
                trees.append(node)
    return trees


if __name__ == '__main__':
    inp = [4 , 5, 7]
    n = len(inp)
    trees = get_trees(inp , 0 , n-1)
    print("Preorder traversals of different possible\
           binary Trees are ")
    for i in trees :
        preorder(i);
        print ("")

# Output:

"""

Preorder traversals of different possible binary Trees are 
4 5 7 
4 7 5 
5 4 7 
7 4 5 
7 5 4 
"""