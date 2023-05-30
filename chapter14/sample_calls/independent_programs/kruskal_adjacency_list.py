

# kruskal_adjacency_list.py


"""
A weighted undirected graph's mst(minimum spanning tree) can be found using Kruskal's 
approach. Among all possible spanning trees, The MST is one that spans every vertex on 
the graph and has the lowest overall weight.

The algorithm works by sorting all the edges of the graph in increasing order of 
their weights and then adding the edges to the MST one by one if adding the edge does 
not create a cycle. It is done until all the vertices are connected. 

We use adjacenct list to realize the script with the following steps for Kruskal's 
algorithm:

1.Sort all the edges of the graph in increasing order of their weights.

2.Create a new empty set to represent the minimum spanning tree.

3.Iterate through each edge in the sorted list of edges.

4.Check whether adding the edge to the MST would create a cycle. Add the edge to the 
MST if it doesn't. Repeat until every vertex is joined.
"""


class Graph:  
    def __init__(self, vertices):  
        self.vertices = vertices  
        self.edges = []  
        self.adjacency_list = {vertice: [] for vertice in vertices}  
    def add_edge(self, u, v, w):        # u and v are nodes and w is weight
        self.edges.append((u, v, w))  
        self.adjacency_list[u].append((v, w))  
        self.adjacency_list[v].append((u, w)) 
    # A utility function to find set of an element i with path compression
    def find_subtree(self, parent, i):
        if parent[i] != i:
            # Reassig a parent to a root node as compression requires
            parent[i] = self.find_subtree(parent, parent[i])
        return parent[i]
    # Merge two connected components in disjoint-set data
    def union(self, parent, rank, x, y):  
        root_x = self.find_subtree(parent, x)  
        root_y = self.find_subtree(parent, y)  
        if rank[root_x] < rank[root_y]:  
            parent[root_x] = root_y  
        elif rank[root_x] > rank[root_y]:  
            parent[root_y] = root_x  
        else:  
            parent[root_y] = root_x  
            rank[root_x] += 1  
    # kruskal adopts the for loop
    def kruskal(self):  
        mst = set()                      # mst: minimum_spanning_tree 
        parent = []  
        rank = []                        # depth of a subtree
        for vertice in self.vertices:  
            parent.append(vertice)  
            rank.append(0)  
        # Sorted the edges according to the 2rd component (weight)
        sorted_edges = sorted(self.edges, key=lambda item: item[2])  
        print(sorted_edges)
        for edge in sorted_edges:  
            u, v, w = edge  
            root_u = self.find_subtree(parent, u)  
            root_v = self.find_subtree(parent, v)  
            if root_u != root_v:  
                mst.add(edge)  
                self.union(parent, rank, root_u, root_v)  
        return mst


if __name__ == '__main__':
    vertices = [0, 1, 2, 3]  
    g = Graph(vertices)  
    g.add_edge(0, 1, 5)  
    g.add_edge(0, 2, 10)  
    g.add_edge(0, 3, 3)  
    g.add_edge(1, 3, 1)  
    g.add_edge(2, 3, 4)  
    mst = g.kruskal()  
    print(mst) 



# Output:

"""
# print(sorted_edges)
[(1, 3, 1), (0, 3, 3), (2, 3, 4), (0, 1, 5), (0, 2, 10)]
# print(mst)
{(0, 3, 3), (2, 3, 4), (1, 3, 1)}
""" 