

# bellman_ford.py


"""
How does this work? 
Like other Dynamic Programming Problems, the algorithm calculates the shortest paths 
in a bottom-up manner. It first calculates the shortest distances which have at most 
one edge in the path. Then, it calculates the shortest paths with at-most 2 edges, 
and so on. After the i-th iteration of the outer loop, the shortest paths with at most 
i edges are calculated. There can be maximum |V| – 1 edges in any simple path, that is 
why the outer loop runs |v| – 1 times. The idea is, assuming that there is no negative 
weight cycle if we have calculated shortest paths with at most i edges, then an iter-
ation over all edges guarantees to give the shortest path with at-most (i+1) edges.
"""


# Class to represent a graph

class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []
    # function to add an edge to graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    # utility function used to print the solution
    def print_arr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
    # The main function that finds shortest distances from src to all 
    # other vertices using Bellman-Ford algorithm. The function also 
    # detects negative weight cycle
    def bellman_ford(self, src):
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0
        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V|-1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices
            # of the picked vertex. Consider only those vertices which are 
            # still in queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        # print all distance
        self.printArr(dist)


if __name__ == '__main__':
    g = Graph(5)
    g.add_Edge(0, 1, -1)
    g.add_Edge(0, 2, 4)
    g.add_Edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_Edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)
    g.bellman_ford(0)


# Output:

"""
Vertex Distance from Source
0       0
1       -1
2       2
3       -2
4       1
"""
