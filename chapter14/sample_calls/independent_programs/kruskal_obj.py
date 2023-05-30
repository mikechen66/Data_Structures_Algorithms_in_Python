

# kruskal_obj.py

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


# Kruskal's algorithm in Python


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    # Search function
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])
    def apply_union(self, parent, rank, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    #  Apply Kruskal algorithm
    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_subtree(parent, u)
            y = self.find_subtree(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 0, 4)
    g.add_edge(2, 0, 4)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 2, 3)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 2, 4)
    g.add_edge(4, 3, 3)
    g.add_edge(5, 2, 2)
    g.add_edge(5, 4, 3)
    g.kruskal_mst()


# Output:

"""
1 - 2: 2
2 - 5: 2
2 - 3: 3
3 - 4: 3
0 - 1: 4
"""