

# kruskal_mst.py


# Python program for Kruskal's algorithm to find Minimum Spanning Tree of a giverticesen connected,
# undirected and weighted graph

"""
Kruskal's algorithm is a minimum spanning tree algorithm that takes a graph as input 
and finds the subset of the edges of that graph which 

form a tree that includes everticesery verticesertex;
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
Keep adding edges until we reach all verticesertices.
"""


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
    # It has u and v as vertices and w as weight
    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])
    # A utility function to find set of an element i with path compression
    def find_subtree(self, parent, i):
        if parent[i] != i:
            # Reassign a parent to a root node as path compression requires
            parent[i] = self.find_subtree(parent, parent[i])
        return parent[i]
    # Merge two sets of x and y by rank(subtree depth)
    def union(self, parent, rank, x, y):
        # Attach smaller rank tree under root of high rank tree
        # x and y are defined in the while loop of kruskal_mst() funtion body
        if rank[x] < rank[y]:  
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        # If ranks are same, then make one as root and increment its rank by 1
        else:
            parent[y] = x
            rank[x] += 1
    # kruskal adopts the while loop
    def kruskal_mst(self):
        # This will store the resultant MST
        mst = []
        # An iterator used for sorted edges
        i = 0
        # Number of edges in the MST
        e = 0
        # Sort all the edges in the increasing order of weight
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = []
        rank = []
        # Create vertices subsets with single elements
        for vertice in range(self.vertices):
            parent.append(vertice)
            rank.append(0)
        # Number of edges to be taken is less than vertices-1
        while e < self.vertices - 1:
            # Pick the smallest edge and increment the index for next iteration
            u, v, w = self.edges[i]
            i += 1
            # x and y are relocated in the untion() function body
            x = self.find_subtree(parent, u)
            y = self.find_subtree(parent, v)
            # If two vertices are not in the same subtree, we merge the two subtrees
            # and increment the index of result for next edge
            if x != y:
                e += 1
                mst.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
        min_cost = 0
        print("Edges in the constructed MST")
        for u, v, w in mst:
            min_cost += w
            print("%d -- %d == %d" % (u, v, w))
        print("Minimum Spanning Tree", min_cost)


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    g.kruskal_mst()

# Output:

"""
Edges in the constructed MST
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
Minimum Spanning Tree 19
"""