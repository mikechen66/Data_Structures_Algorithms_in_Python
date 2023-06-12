

# binary_tree_height.py


"""
How to find the Height of a Binary Tree?

As we studied before. the height of the binary tree is considered to be the longest path 
starting from the root node to any leaf node in the binary tree.  If the target node for 
which we have to calculate the height, doesn’t have any other nodes connected to it, 
conclusively the height of that node would be 0.

Therefore, we can say that the height of a binary tree is the elevation from the root node 
in the entire binary tree. In layman's terms, the height of a binary tree is equivalent to 
the largest quantity of edges starting from the root to the most sparse leaf node in the 
binary tree.

A related concept in the binary tree data structure is the depth of the tree. According to 
the definition of depth of a node in the binary tree is the total amount of edges starting 
from the root node to the destination node.
"""


import collections


# define a Class Tree, to intiate the binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root):
    # Set result variable to 0
    ans = 0
    # Initialise the queue
    queue = collections.deque()
    # Check if the tree has no nodes
    if root is None:
        return ans
    # Append the nodes to queue and process it in while loop until its empty
    queue.append(root)
    # Process in while loop until there are elements in queue
    while queue:
        currSize = len(queue)
        # Unless the queue is empty
        while currSize > 0:
            # Pop elements one-by-one
            currNode = queue.popleft()
            currSize -= 1
            # Check if the node has left/right child
            if currNode.left is not None:
                queue.append(currNode.left)
            if currNode.right is not None:
                queue.append(currNode.right)
        # Increment ans when currSize = 0
        ans += 1
    return ans
 

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print("Height of the binary tree is: " + str(height(root)))


# Output:

"""
Height of the binary tree is: 3
"""