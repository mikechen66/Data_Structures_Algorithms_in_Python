

# dag_shortest.py


"""
Constructor of the DFS class
[time]: counter to record [arrival] and
        [departure] times of the algorithm in each node.
[state]: mapping from vertices to a state that can be 'unexplored',
         'exploring' and 'explored'.
[has_cycle]: boolean to indicate if the algorithm discovered that
             the graph has a cycle
[depth_traversal]: a list that we manipulate as a stack
                   that holds the edges of the resulting
                   depth first traversal (DFS tree)
[top_ordering]: list with vertices of G sorted topologicaly
                If has_cycle == true it is deemed meaningless
"""


import math
import graph_added


class DFS:
    """Callable class that is instantiated on a graph."""
    def __init__(self, G):
        self.time = 0
        self.state = {vertex: 'unexplored' for vertex in G.vertices()}
        self.depth_traversal = []
        self.arrival = {vertex: None for vertex in G.vertices()}
        self.departure = {vertex: None for vertex in G.vertices()}
        # edge_added can avoid identifying false back edges
        self.edge_added = {edge: False for edge in G.edges()}
        self.has_cycle = False
        if G.is_directed:
            self._top_ordering = []
        else:
            self._top_ordering = None
    def dfs_compute(self, G, start):
        """
        Put the unexplored neighbors of start vertex in a list
        and recursively do the same for each one of them.
        """
        self.state[start] = 'exploring'
        self.time = self.time + 1
        self.arrival[start] = self.time
        for edge in G.incident_edges(start, outgoing=True):
            neighbor = edge.opposite(start)
            if self.state[neighbor] == 'unexplored':
                self.depth_traversal.append(edge)
                self.edge_added[edge] = True
                self.dfs_compute(G, neighbor)
            else:
                if self.edge_added[edge]:
                    continue
                if self.state[neighbor] == 'exploring':
                    self.has_cycle = True
        self.time = self.time + 1
        self.departure[start] = self.time
        self.state[start] = 'explored'
        self._top_ordering.insert(0, start)
    def get_topological_order(self, G, start):
        if not G.is_directed:
            raise Exception('G is undirected')
        self.dfs_compute(G, start)
        if self.has_cycle:
            return None
        else:
            return self._top_ordering


def dag_shortest_paths(G, w, start_vertex):
    traversal = DFS(G)
    ordering = traversal.get_topological_order(G, start_vertex)
    distance_est = {vertex: math.inf for vertex in G.vertices()}
    distance_est[start_vertex] = 0
    spt_predecessor = {vertex: None for vertex in G.vertices()}
    n = len(ordering)
    for i in range(n):
        source = ordering[i]
        for edge in G.incident_edges(source):
            destination = edge.opposite(source)
            if distance_est[destination] > distance_est[source] + w[edge]:
                distance_est[destination] = distance_est[source] + w[edge]
                spt_predecessor[destination] = source
    return distance_est, spt_predecessor


if __name__ == '__main__':
    E = [('a', 'b', 4), ('b', 'd', 10),
         ('d', 'f', 11), ('b', 'c', 5),
         ('a', 'c', 2), ('c', 'e', 3),
         ('e', 'd', 4)]
    print('Shortest paths from a for graph')
    print(E)
    G, weight_mapping = graph_added.create_graph(E, is_directed=True)
    start_vertex = G.get_vertex('a')
    d, p = dag_shortest_paths(G, weight_mapping, start_vertex)
    for key in p:
        if p[key] is None:
            print(key.element() + ' is the start vertex')
        else:
            path = [key]
            vertex = p[key]
            while not (vertex is None):
                path.insert(0, vertex)
                vertex = p[vertex]
            elements = [vertex.element() for vertex in path]
            print('Shortest path to ' + key.element() + ' with value: ' + str(d[key]))
            x = '->'.join(elements)
            print(x)


# Output:

"""
Shortest paths from a for graph
[('a', 'b', 4), ('b', 'd', 10), ('d', 'f', 11), ('b', 'c', 5), ('a', 'c', 2), ('c', 'e', 3), ('e', 'd', 4)]
a is the start vertex
Shortest path to b with value: 4
a->b
Shortest path to d with value: 9
a->c->e->d
Shortest path to f with value: 20
a->c->e->d->f
Shortest path to c with value: 2
a->c
Shortest path to e with value: 5
a->c->e
"""