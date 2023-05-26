

# topological_sort_graph.py

"""
Say that an n-vertex directed acyclic graph G is compact if there is some way of 
numbering the vertices of G with the integers from 0 to n−1 such that G contains 
the edge (i, j) if and only if i < j, for all i, j in [0,n− 1]. Give an O(n2)-time 
algorithm for detecting if G is compact
"""


from graph_direct import Graph


def topological_sort(g):
    """
    Return a list of verticies of directed acyclic graph g in topological order.
    If graph g has a cycle, the result will be incomplete.
    """
    topo = []             # a list of vertices placed in topological order
    ready = []            # list of vertices that have no remaining constraints
    incount = {}          # keep track of in-degree for each vertex
    for u in g.vertices():
        incount[u] = g.degree(u, False)  # parameter requests incoming degree
        if incount[u] == 0:              # if u has no incoming edges,
            ready.append(u)              # it is free of constraints
    while len(ready) > 0:
        u = ready.pop()                  # u is free of constraints
        topo.append(u)                   # add u to the topological order
        for e in g.incident_edges(u):    # consider all outgoing neighbors of u
            v = e.opposite(u)
            incount[v] -= 1              # v has one less constraint without u
            if incount[v] == 0:
                ready.append(v)
    return topo


def is_compact(g):
    # if graph `g` has a cycle, result of the topological sort will be incomplete
    return g.vertex_count() == len(topological_sort(g))


if __name__ == "__main__":
    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    e1 = g.insert_edge(v1, v2, 'e1')
    e2 = g.insert_edge(v2, v3, 'e2')
    e3 = g.insert_edge(v3, v1, 'e3')
    assert not is_compact(g)
    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    e1 = g.insert_edge(v2, v1, 'e1')
    e2 = g.insert_edge(v2, v3, 'e2')
    assert is_compact(g)
    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    v6 = g.insert_vertex('v6')
    v7 = g.insert_vertex('v7')
    v8 = g.insert_vertex('v8')
    e1 = g.insert_edge(v1, v2, 'e1')
    e2 = g.insert_edge(v1, v5, 'e2')
    e3 = g.insert_edge(v4, v5, 'e3')
    e4 = g.insert_edge(v4, v6, 'e4')
    e5 = g.insert_edge(v2, v5, 'e5')
    e6 = g.insert_edge(v5, v6, 'e6')
    e7 = g.insert_edge(v2, v3, 'e7')
    e8 = g.insert_edge(v3, v7, 'e8')
    e9 = g.insert_edge(v6, v7, 'e9')
    e10 = g.insert_edge(v7, v8, 'e10')
    e11 = g.insert_edge(v6, v8, 'e11')
    e12 = g.insert_edge(v2, v8, 'e12')
    assert is_compact(g)