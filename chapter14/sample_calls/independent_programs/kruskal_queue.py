

# kruskal_queue.py


"""
Kruskal's algorithm is often used in network design problems, such as designing a 
communication network or an electrical power grid. The algorithm can also be 
implemented using a priority queue in python.


The algorithm works by sorting the edges of the graph by weight and then adding the 
edges to the minimum spanning tree one by one, starting with the smallest weight.

As each edge is added to the minimum spanning tree, it is checked to ensure that it 
does not create a cycle. If the edge connects two vertices that are already in the 
same connected component, then adding the edge would create a cycle, and the edge 
is discarded.

As long as the graph is connected and the edge weights are distinct, Kruskal will 
always identify the graph's minimum spanning tree.
"""


import queue  


class Graph:  
    def __init__(self, vertices):  
        self.vertices = vertices  
        self.edges = []  
        self.parent = {}  
        self.rank = {}  
        for v in self.vertices:  
            self.make_set(v)  
    def add_edge(self, u, v, w):  
        self.edges.append((w, u, v))  
    def make_set(self, v):  
        self.parent[v] = v  
        self.rank[v] = 0  
    def find_subtree(self, v):  
        if self.parent[v] != v:  
            self.parent[v] = self.find_subtree(self.parent[v])  
        return self.parent[v]  
    def union(self, u, v):  
        root1 = self.find_subtree(u)  
        root2 = self.find_subtree(v)  
        if root1 != root2:  
            if self.rank[root1] > self.rank[root2]:  
                self.parent[root2] = root1  
            else:  
                self.parent[root1] = root2  
                if self.rank[root1] == self.rank[root2]:  
                    self.rank[root2] += 1  
    def kruskal(self):  
        mst = set()  # minimum spanning tree
        # Sort edges by weight using priority queue  
        edge_queue = queue.PriorityQueue()  
        for edge in self.edges:  
            edge_queue.put(edge)  
        # Iterate through edges in priority queue and add to MST  
        while not edge_queue.empty():  
            weight, u, v = edge_queue.get()  
            if self.find_subtree(u) != self.find_subtree(v):  
                self.union(u, v)  
                mst.add((u, v, weight))  
        return mst  


if __name__ == "__main__": 
    # Create a graph with 5 vertices  
    g = Graph([0, 1, 2, 3, 4])  
    # Add edges to the graph  
    g.add_edge(0, 1, 2)  
    g.add_edge(0, 2, 3)  
    g.add_edge(0, 3, 6)  
    g.add_edge(1, 2, 5)  
    g.add_edge(1, 4, 3)  
    g.add_edge(2, 3, 1)  
    g.add_edge(2, 4, 4)  
    g.add_edge(3, 4, 5)  
    # Find the minimum spanning tree  
    mst = g.kruskal()  
    # Print the edges in the minimum spanning tree  
    for edge in mst:  
        print(edge)  


# Outpout:


"""
(0, 1, 2)
(0, 2, 3)
(1, 4, 3)
(2, 3, 1)
"""