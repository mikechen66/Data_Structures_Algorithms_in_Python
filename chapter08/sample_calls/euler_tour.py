

# euler_tour.py 


# Option 1:


# Python program to print Euler tour of a tree.
from collections import defaultdict


# Adjacency list representation of tree
adj = defaultdict(list)
# Visited dictionary to keep track of visited nodes on our tour
vis = defaultdict(bool)


# defaultdict to store Euler Tour
MAX = 1001
Euler = [0]*(2*MAX)


# Function to add edges to tree
def add_edge(u, v):
    adj[u].append(v)
    adj[v].append(u)


# Function to store Euler Tour of Tree
def eulerTree(u, index):
    vis[u] = True
    Euler[index] = u
    index += 1
    for nbr in adj[u]:
        if not vis[nbr]:
            index = eulerTree(nbr, index)
            Euler[index] = u
            index += 1
    return index


# Function to print Euler Tour of Tree
def printEulerTour(root, N):
    index = 0
    eulerTree(root, index)
    for i in range(2*N-1):
        print(Euler[i], end=" ")


if __name__ == '__main__': 
    # Driver Code
    N = 4
    add_edge(1, 2)
    add_edge(2, 3)
    add_edge(2, 4)
    printEulerTour(1, N)
    print()


# Output:

"""
1 2 3 2 4 2 1
"""

######################################################################################################


# Option 2:


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Find Euler Tree
def euler_tree(root, euler):
    # store current node's data
    euler.append(root.data)
    # If left node exists
    if root.left:
        # traverse left subtree
        euler = euler_tree(root.left, euler)
        # store parent node's data
        euler.append(root.data)
    # If right node exists
    if root.right:
        # traverse right subtree
        euler = euler_tree(root.right, euler)
        # store parent node's data
        euler.append(root.data)
    return euler


# Function to print Euler Tour of tree
def euler_tour(root):
    # Stores Euler Tour
    euler = []
    euler = euler_tree(root, euler)
    for i in range(len(euler)):
        print(euler[i], end=" ")


if __name__ == '__main__':
    # Driver function to test above functions */
    # Constructing tree given in the above figure
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    # print Euler Tour
    euler_tour(root)
    print()


# Output:

"""
1 2 4 2 5 2 1 3 6 8 6 3 7 3 1 
"""

######################################################################################################


# Option 3: Euler Tree with recursion 


#  Binary Tree Node
class TreeNode :
    def __init__(self, data) :
        #  Set node value
        self.data = data
        self.left = None
        self.right = None
    

class BinaryTree :
    def __init__(self) :
        self.root = None
    #  Recursively Printing the elements of euler path
    def euler_path(self, node, parent) :
        if (node == None) :
            #  When tree node empty
            return None
        #  Display node value
        print("", node.data, end = " ")
        #  Recursively visit the left and right subtree
        self.euler_path(node.left, node)
        self.euler_path(node.right, node)
        if (parent != None) :
            #  When parent not null
            print("", parent.data, end = " ")
        

def main() :
    #  Create new tree
    tree = BinaryTree()
    #        9
    #       / \
    #      5   7
    #     / \   \
    #    1   6   11
    #   /   / \   \
    #  10  4   8   20
    #         / \
    #        2   3
    #  -----------------------
    #    Binary Tree
    tree.root = TreeNode(9)
    tree.root.left = TreeNode(5)
    tree.root.right = TreeNode(7)
    tree.root.left.left = TreeNode(1)
    tree.root.left.left.left = TreeNode(10)
    tree.root.left.right = TreeNode(6)
    tree.root.left.right.left = TreeNode(4)
    tree.root.left.right.right = TreeNode(8)
    tree.root.left.right.right.left = TreeNode(2)
    tree.root.left.right.right.right = TreeNode(3)
    tree.root.right.right = TreeNode(11)
    tree.root.right.right.right = TreeNode(20)
    tree.eulerPath(tree.root, None)
    print()


if __name__ == "__main__": 
    main()


# Output:

"""
 9  5  1  10  1  5  6  4  6  8  2  8  3  8  6  5  9  7  11  20  11  7  9 
"""

######################################################################################################


# Option 4: Euler path


def euler_path(graph):
    # counting the number of vertices with odd degree
    alist = list(graph.keys())
    odd = [x for x in alist if len(graph[x])&1]
    odd.append(alist[0])
    if len(odd) > 3:
        return None
    stack = [odd[0]]
    path = []
    # major algorithm
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v][0]
            stack.append(u)
            # deleting edge u-v
            del graph[u][ graph[u].index(v) ]
            del graph[v][0]
        else:
            path.append(stack.pop())
    return path


if __name__ == '__main__':
    euler_path({1: [2, 3, 4],
                2: [1, 3],
                3: [1, 2],
                4: [1, 5],
                5: [4]})


# Output:

"""
[5, 4, 1, 3, 2, 1]
"""

######################################################################################################


# Option 5: Use DFS to realize the Euler tree


def dfs(u, graph, visited_edge, path=[]):
    path = path + [u]
    for v in graph[u]:
        if visited_edge[u][v] == False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    return path


# for checking in graph has euler path or circuit
def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph.keys():
            continue
        if len(graph[i]) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node


def check_euler(graph, max_node):
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("graph is not Eulerian")
        print("no path")
        return
    start_node = 1
    if check == 2:
        start_node = odd_node
        print("graph has a Euler path")
    if check == 1:
        print("graph has a Euler cycle")
    path = dfs(start_node, graph, visited_edge)
    print(path)


def main():
    G1 = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2],
        4: [1, 5],
        5: [4]
    }
    G2 = {
        1: [2, 3, 4, 5],
        2: [1, 3],
        3: [1, 2],
        4: [1, 5],
        5: [1, 4]
    }
    G3 = {
        1: [2, 3, 4],
        2: [1, 3, 4],
        3: [1, 2],
        4: [1, 2, 5],
        5: [4]
    }
    G4 = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
    }
    G5 = {
        1: [],
        2: []
        # all degree is zero
    }
    max_node = 10
    check_euler(G1, max_node)
    check_euler(G2, max_node)
    check_euler(G3, max_node)
    check_euler(G4, max_node)
    check_euler(G5, max_node)


if __name__ == "__main__":
    main()


# Output:

"""
graph has a Euler path
[5, 4, 1, 2, 3, 1]
graph has a Euler cycle
[1, 2, 3, 1, 4, 5, 1]
graph is not Eulerian
no path
graph has a Euler cycle
[1, 2, 3, 1]
graph has a Euler cycle
[1]
"""

#######################################################################################################


# Option 6: Gregor Ulm


def find_eulerian_tour(graph):
    def freqencies():
        # save all nodes of edges to my_list
        # e.g. [3,4,5,1,2,2,3,5]
        my_list = [x for (x, y) in graph]
        # get the max num of nodes-->create a list
        # set all to 0
        # for i in range(5) = 0 1 2 3 4
        # so range("5" +1) means
        # len=6, result=[0,0,0,0,0,0]
        # so that the index = the number itself
        result = [0 for i in range(max(my_list) + 1)]
        # nodes in my_list, increment
        # e.g. [0,1,2,2,1,2] 
        # 3appears 2times.
        for i in my_list:
            result[i] += 1
        return result
        # this is Frequencies of each nodes.
    def find_node(tour):
        for i in tour:
            if freq[i] != 0:
                return i
        return -1
    def helper(tour, next):
        find_path(tour, next)
        u = find_node(tour)
        while sum(freq) != 0:     
            sub = find_path([], u)
            # get the sub_path
            # add them together
            # when draw to u, turn to sub, and then come back to go on the original tour path
            # [:a], start to a; [a+1:] a+1 to end
            tour = tour[:tour.index(u)] + sub + tour[tour.index(u) + 1:]  
            u = find_node(tour)
        return tour
    def find_path(tour, next):
        for (x, y) in graph:
            if x == next:
                # from "double-graph"
                # pop out the current one and its respondent one
                # actually it means we delete this edge
                current = graph.pop(graph.index((x,y)))
                graph.pop(graph.index((current[1], current[0])))
                # now add this "next" node into the tour
                tour.append(current[0])
                # decrement in frequency
                freq[current[0]] -= 1
                freq[current[1]] -= 1
                return find_path(tour, current[1])
        # if this "next" node is not connected to any other nodes
        # single one
        tour.append(next)
        return tour             
    # in graph, all edges get reversed one and be added to graph
    # can call it "double-graph"  
    # it helps to calculate the frequency in find_path
    # actually we can regard frequency as degrees for each node       
    graph += [(y, x) for (x, y) in graph]
    freq = freqencies()   
    # set graph[0][0] as starting point
    return helper([], graph[0][0])


if __name__ == '__main__':
    graph1 = [(1, 2), (2, 3), (3, 1)]
    graph2 = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 3)]
    graph3 = [(2, 6), (4, 2), (5, 4), (6, 5), (6, 8), (7, 9), (8, 7), (9, 6)]
    print(find_eulerian_tour(graph1))
    print(find_eulerian_tour(graph2))
    print(find_eulerian_tour(graph3))



# Output:

"""
[1, 2, 3, 1]
[1, 2, 3, 4, 3, 1]
[2, 6, 8, 7, 9, 6, 5, 4, 2]
"""