

# Check all three given traversals are of the same tree


"""
The basic approach to solve this problem will be to first construct a tree using two 
of the three given traversals and then do the third traversal on this constructed 
tree and compare it with the given traversal. If both of the traversals are same then 
print Yes otherwise print No. Here, we use Inorder and Preorder traversals to construct 
the tree. We may also use Inorder and Postorder traversal instead of Preorder traversal 
for tree construction. You may refer to this post on how to construct a tree from given 
Inorder and Preorder traversal. After constructing the tree, we will obtain the Postorder 
traversal of this tree and compare it with the given Postorder traversal.

search()

Function to find index of value in arr[start...end]. The function assumes that value 
is present

build_tree():

Recursive function to construct binary tree of size lenn from Inorder traversal in and 
Preorder traversal pre[]. Initial values of inStrt and inEnd should be 0 and lenn -1. 
The function doesn't do any error checking for cases where inorder and preorder do not
form a tree

check_postorder()

function to compare Postorder traversal on constructed tree and given Postorder
"""


class node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


PreIndex = 0


def search(arr, strt, end, value):
    for i in range(strt, end+1):
        if(arr[i] == value):
            return i


def build_tree(inn, pre, instrt, inend):
    global PreIndex
    if(instrt > inend):
        return None
    # Pick current node from Preorder traversal using 
    # PreIndex and increment PreIndex
    tnode = node(pre[PreIndex])
    PreIndex += 1
    # If this node has no children then return
    if (instrt == inend):
        return tnode
    # Else find the index of this node in Inorder traversal
    inindex = search(inn, instrt, inend, tnode.data)
    # Using index in Inorder traversal, construct left and 
    # right subtress
    tnode.left = build_tree(inn, pre, instrt, inindex - 1)
    tnode.right = build_tree(inn, pre, inindex+1, inend)
    return tnode


def check_postorder(node, postorder, index):
    if (node == None):
        return index
    # first recur on left child
    index = check_postorder(node.left, postorder, index)
    # now recur on right child
    index = check_postorder(node.right, postorder, index)
    # Compare if data at current index in both Postorder 
    # traversals are same
    if (node.data == postorder[index]):
        index += 1
    else:
        return - 1
    return index


if __name__ == '__main__':
    inorder = [4, 2, 5, 1, 3]
    preorder = [1, 2, 4, 5, 3]
    postorder = [4, 5, 2, 3, 1]
    lenn = len(inorder)
    # build tree from given
    # Inorder and Preorder traversals
    root = build_tree(inorder, preorder, 0, lenn-1)
    # compare postorder traversal on constructed 
    # tree with given Postorder traversal
    index = check_postorder(root, postorder, 0)
    # If both postorder traversals are same
    if (index == lenn):
        print("Yes")
    else:
        print("No")

# Output:

"""
Yes
"""