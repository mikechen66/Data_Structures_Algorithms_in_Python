

# topological_sort_dfs.py


"""

A Topological sort or Topological ordering of a directed graph is a linear ordering 
of its vertices such that for every directed edge uv from vertex u to vertex v, u 
comes before v in the ordering. A topological ordering is possible if and only if 
the graph has no directed cycles, i.e. if the graph is DAG.

We can use Depth–first search (DFS) to implement topological sort algorithm. The idea 
is to order the vertices in order of their decreasing departure time of vertices in 
DFS, and we will get our desired topological sort.

Following is the relationship we have seen between the departure time for different 
types of edges involved in a DFS of the directed graph:

Tree edge (u, v):    departure[u] > departure[v]
Back edge (u, v):    departure[u] < departure[v]
Forward edge (u, v): departure[u] > departure[v]
Cross edge (u, v):   departure[u] > departure[v]

With regard to a tree edge, forward edge, or cross edge (u, v), departure[u] is more 
than departure[v]. But only for the back edge, relationship departure[u] < departure[v] 
is true. So, it is guaranteed that if an edge (u, v) has departure[u] > departure[v], 
it’s not a back-edge.

DAG, no back-edge is present. So if we order the vertices in order of their decreasing 
departure time, we will get the topological order of the graph (every edge going from 
left to right).
"""


# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adj_list = [[] for _ in range(n)]
        # add edges to the directed graph
        for (src, dest) in edges:
            # add an edge from source to destination
            self.adj_list[src].append(dest)


# Perform DFS on the graph and set the departure time of all
# vertices of the graph
def dfs(graph, v, discovered, departure, time):
    # mark the current node as discovered
    discovered[v] = True
    # set the arrival time of vertex `v`
    time = time + 1
    # do for every edge (v, u)
    for u in graph.adj_list[v]:
        # if `u` is not yet discovered
        if not discovered[u]:
            time = dfs(graph, u, discovered, departure, time)
    # ready to backtrack
    # set departure time of vertex `v`
    departure[time] = v
    time = time + 1
    return time


# Function to perform a topological sort on a given DAG
def topological_sort(graph, n):
    # departure[] stores the vertex number using departure time as an index
    departure = [-1] * 2 * n
    ''' If we had done it the other way around, i.e., fill the array
        with departure time using vertex number as an index, we would
        need to sort it later '''
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n
    time = 0
    # perform DFS on all undiscovered vertices
    for i in range(n):
        if not discovered[i]:
            time = dfs(graph, i, discovered, departure, time)
    # Print the vertices in order of their decreasing
    # departure time in DFS, i.e., in topological order
    for i in reversed(range(2*n)):
        if departure[i] != -1:
            print(departure[i], end=' ')


if __name__ == '__main__':
    # List of graph edges as per the above diagram
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
    # total number of nodes in the graph (labelled from 0 to 7)
    n = 8
    # build a graph from the given edges
    graph = Graph(edges, n)
    # perform topological sort
    topological_sort(graph, n)
    print()
 

 # Output:

"""
7 5 3 1 4 2 0 6 
"""