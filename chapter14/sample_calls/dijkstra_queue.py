

# dijkstra_queue.py

"""
Dijkstra's algorithm works on undirected, connected, weighted graphs.

for the constructor of Graph: 
    v:       Represent the number of vertices in the graph.
    edges:   Represent the list of edges in the form of a matrix. For nodes u and v, 
             self.edges[u][v] = weight of the edge.
    visited: A set which will contain the visited vertices.

"""

from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0
    pq = PriorityQueue()
    pq.put((0, start_vertex))
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


if __name__ == '__main__':
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3) 
    D = dijkstra(g, 0)
    print(D)
    for vertex in range(len(D)):
        print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])


# Output:

"""

{0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11}

Distance from vertex 0 to vertex 0 is 0
Distance from vertex 0 to vertex 1 is 4
Distance from vertex 0 to vertex 2 is 11
Distance from vertex 0 to vertex 3 is 17
Distance from vertex 0 to vertex 4 is 9
Distance from vertex 0 to vertex 5 is 22
Distance from vertex 0 to vertex 6 is 7
Distance from vertex 0 to vertex 7 is 8
Distance from vertex 0 to vertex 8 is 11
"""