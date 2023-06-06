

# tree_operate.py


"""
Binary Tree: 
A Binary tree is represented by a pointer to the topmost node (commonly known as the “root”) 
of the tree. If the tree is empty, then the value of the root is NULL. Each node of a Binary 
Tree contains the following parts:

1. Data
2. Pointer to left child
3. Pointer to right child


Nodes: 
Node 1 is the root node
1 is the parent of 2 and 3
2 and 3 are the siblings
4, 5, 6 and 7 are the leaf nodes
1 and 2 are the ancestors of 5
"""


# Function to add an edge between vertices x and y


# Function to print the parent of each node

def show_parents(node, adj, parent):
    # current node is Root, thus, has no parent
    if (parent == 0):
        print(node, "-> Root")
    else:
        print(node, "->", parent)
    # Using DFS
    for cur in adj[node]:
        if (cur != parent):
            show_parents(cur, adj, node)


# Function to print the children of each node
def show_children(Root, adj):
    # Queue for the BFS
    q = []
    # pushing the root
    q.append(Root)
    # visit array to keep track of nodes that have been visited
    vis = [0]*len(adj)
    # BFS
    while (len(q) > 0):
        node = q[0]
        q.pop(0)
        vis[node] = 1
        print(node, "-> ", end=" ")
        for cur in adj[node]:
            if (vis[cur] == 0):
                print(cur, " ", end=" ")
                q.append(cur)
        print("\n")


# Function to print the leaf nodes

def show_leafnodes(Root, adj):
    # Leaf nodes have only one edge and are not the root
    for i in range(0, len(adj)):
        if (len(adj[i]) == 1 and i != Root):
            print(i, end=" ")
        print("\n")


# Function to print the degrees of each node
def show_degrees(Root, adj):
    for i in range(1, len(adj)):
        print(i, ": ", end=" ")
        # Root has no parent, thus, its degree is equal to
        # the edges it is connected to
        if (i == Root):
            print(len(adj[i]))
        else:
            print(len(adj[i])-1)


if __name__ == '__main__':
    # Number of nodes
    N = 7
    Root = 1
    # Adjacency list to store the tree
    adj = []
    for i in range(0, N+1):
     adj.append([])
    # Creating the tree
    adj[1].append(2)
    adj[2].append(1)
    adj[1].append(3)
    adj[3].append(1)
    adj[1].append(4)
    adj[4].append(1)
    adj[2].append(5)
    adj[5].append(2)
    adj[2].append(6)
    adj[6].append(2)
    adj[4].append(7)
    adj[7].append(4)
    # Printing the parents of each node
    print("The parents of each node are:")
    show_parents(Root, adj, 0)
    # Printing the children of each node
    print("The children of each node are:")
    show_children(Root, adj)
    # Printing the leaf nodes in the tree
    print("The leaf nodes of the tree are:")
    show_leafnodes(Root, adj)
    # Printing the degrees of each node
    print("The degrees of each node are:")
    show_degrees(Root, adj)


# Output:

"""
The parents of each node are:
1 -> Root
2 -> 1
5 -> 2
6 -> 2
3 -> 1
4 -> 1
7 -> 4
The children of each node are:
1 ->  2   3   4   

2 ->  5   6   

3 ->  

4 ->  7   

5 ->  

6 ->  

7 ->  

The leaf nodes of the tree are:






3 



5 

6 

7 

The degrees of each node are:
1 :  3
2 :  2
3 :  0
4 :  1
5 :  0
6 :  0
7 :  0
"""