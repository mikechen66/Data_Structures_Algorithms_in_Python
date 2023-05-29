

# kruskal_mst.py


# Python program for Kruskal's algorithm to find Minimum Spanning Tree of a given connected,
# undirected and weighted graph

"""
Kruskal's algorithm is a minimum spanning tree algorithm that takes a graph as input 
and finds the subset of the edges of that graph which 

form a tree that includes every vertex;
has the minimum sum of weights among all the trees that can be formed from the graph

How Kruskal's algorithm works

It falls under a class of algorithms called greedy algorithms that find the local 
optimum in the hopes of finding a global optimum.We start from the edges with the 
lowest weight and keep adding edges until we reach 
our goal.

The steps for implementing Kruskal's algorithm are as follows:

Sort all the edges from low weight to high;
Take the edge with the lowest weight and add it to the spanning tree. If adding the 
edge created a cycle, then reject this edge;
Keep adding edges until we reach all vertices.
"""


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    # Function to add an edge to graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find_subtree(self, parent, i):
        if parent[i] != i:
            # Reassignment of node's parent to root node as
            # path compression requires
            parent[i] = self.find_subtree(parent, parent[i])
        return parent[i]
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1
    # The main function to construct MST using Kruskal's algorithm
    def kruskal_mst(self):
        # This will store the resultant MST
        result = []
        # An index variable, used for sorted edges
        i = 0
        # An index variable, used for result[]
        e = 0
        # Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        # Number of edges to be taken is less than to V-1
        while e < self.V - 1:
            # Pick the smallest edge and increment the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_subtree(parent, u)
            y = self.find_subtree(parent, v)
            # If including this edge doesn't cause cycle, then include it in result
            # and increment the index of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    g.kruskal_mst()


# Output

"""
Edges in the constructed MST
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
Minimum Spanning Tree 19
"""