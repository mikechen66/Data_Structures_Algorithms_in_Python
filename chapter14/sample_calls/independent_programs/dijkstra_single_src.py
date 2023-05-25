

# dijkstra_single_src.py


"""

The program for Dijkstra's single source shortest path algorithm is listed for adjacency 
matrix representation of the graph

Dijkstra’s algorithm is similar to Prim’s algorithm for minimum spanning tree. Like Prim’s 
MST, we generate an spt(shortest path tree) with a given source as root; maintain two 
sets, one set contains vertices included in the shortest-path tree, another set includes 
vertices not yet included in the shortest-path tree; at every step of the algorithm, we 
find a vertex that is in the other set (set of not yet included) and has a minimum distance 
from the source. Below are the simple steps to find the shortest path from a single source 
vertex to all other vertices in the given graph. 

1) Create a set sptset (spt set) that keeps track of vertices included in shortest path 
tree, i.e., whose minimum distance from source is calculated and finalized. Initially, 
this set is empty. 

2) Assign a distance value to all vertices in the input graph; Initialize all distance 
values as INFINITE; Assign distance value as 0 for the source vertex so that it is picked 
first. 

3) While sptSet doesn’t include all vertices: 

Pick a vertex u which is not there in sptSet and has minimum distance value;
Include u to sptset;
Update distance value of all adjacent vertices of u, to update the distance values, iterate 
through all adjacent vertices; for every adjacent vertex v, if the sum of a distance value 
of u (from source) and weight of edge u-v, is less than the distance value of v, then update 
the distance value of v.

"""


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        # Present an adjacency matrix presentation 
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
    def print_result(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
    # Find the vertex with minimum distance value, from the set of vertices 
    # not yet included in shortest path tree
    def min_distance(self, dist, sptset):
        # Initialize minimum distance for next node
        min = 1e7
        # Search not nearest vertex not in the shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptset[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    # Implements Dijkstra's single source shortest path algorithm for a 
    # graph represented using adjacency matrix representation
    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptset = [False] * self.V
        for cout in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not 
            # yet processed. u is always equal to src in first iteration
            u = self.min_distance(dist, sptset)
            # Put the minimum distance vertex in the shortest path tree
            sptset[u] = True
            # Update dist value of the adjacent vertices of the picked vertex 
            # only if the current distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                sptset[v] == False and
                dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        self.print_result(dist)


if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]
    g.dijkstra(0)


# Output:

"""
Vertex   Distance from Source
0        0
1        4
2        12
3        19
4        21
5        11
6        9
7        8
8        14
"""