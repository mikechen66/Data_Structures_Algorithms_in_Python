

# bellman_ford_print.py


"""
Function for computing shortest paths on directed graphs.
Reports detection of negative cycle if one exists.
Inputs:
[G]: graph.Graph object of graph representation
[w]: weight mapping of edges
[start_vertex]: the source to which shortest paths will be computed
                its a graph.Vertex instance of G.
Outputs:
[distance_est]: mapping of vertices to the length of the shortes path
                with start_vertex as source i.e. = d(start_vertex, v)
[spt_predecessor]: mapping of vertice to their predecessor
                   in the shortest path tree with root start_vertex
"""


import math
import graph_added


def bellman_ford(G, w, start_vertex):
    distance_est = {vertex: math.inf for vertex in G.vertices()}
    distance_est[start_vertex] = 0
    spt_predecessor = {vertex: None for vertex in G.vertices()}
    n = G.vertex_count()
    for i in range(1, n):
        for edge in G.edges():
            source, destination = edge.endpoints()
            # edge relaxation
            if distance_est[destination] > distance_est[source] + w[edge]:
                distance_est[destination] = distance_est[source] + w[edge]
                spt_predecessor[destination] = source
    for edge in G.edges():
        source, destination = edge.endpoints()
        if distance_est[destination] > distance_est[source] + w[edge]:
            return None, None
    return distance_est, spt_predecessor


def show_results(d, p):
    # A helper function to show the results
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


if __name__ == '__main__':
    E = [('s', 'b', 8), ('s', 'a', 6), ('b', 'a', 7), ('b', 'c', 2),
         ('a', 'c', -5), ('e', 'b', 1), ('a', 'd', 4), ('c', 'e', 3),
         ('c', 'd', -4), ('d', 'e', 2), ('e', 'f', 2), ('d', 'f', 5)]
    print('A Bigger Example:')
    print(E)
    G, weight_mapping = graph_added.create_graph(E)
    start_vertex = G.get_vertex('s')
    d, p = bellman_ford(G, weight_mapping, start_vertex)
    show_results(d, p)
    E = [('a', 'b', 4), ('b', 'd', 10),
         ('d', 'f', 11), ('b', 'c', 5),
         ('a', 'c', 2), ('c', 'e', 3),
         ('e', 'd', 4)]
    G, weight_mapping = graph_added.create_graph(E)
    start_vertex = G.get_vertex('a')
    d, p = bellman_ford(G, weight_mapping, start_vertex)
    print('====================')
    print('A Smaller Example:')
    print(E)
    show_results(d, p)


# Output:

"""

A Bigger Example:
[('s', 'b', 8), ('s', 'a', 6), ('b', 'a', 7), ('b', 'c', 2), ('a', 'c', -5), ('e', 'b', 1), ('a', 'd', 4), ('c', 'e', 3), ('c', 'd', -4), ('d', 'e', 2), ('e', 'f', 2), ('d', 'f', 5)]
s is the start vertex
Shortest path to b with value: 0
s->a->c->d->e->b
Shortest path to a with value: 6
s->a
Shortest path to c with value: 1
s->a->c
Shortest path to e with value: -1
s->a->c->d->e
Shortest path to d with value: -3
s->a->c->d
Shortest path to f with value: 1
s->a->c->d->e->f
====================
A Smaller Example:
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