

# mst_simple.py

"""

# Modification

1. Delete PriorityQueue-like classes

PriorityQueue class such as replace PriorityQueue and AdaptableHeapPriorityQueueincludes chained 
reference from super classes that incurs many faults. Instead, here adopt insertion counter bc of 
Python. 

2. Add heap module to reaplce above class functionalities 

Useheapify, heanpop and heappush to replace the previous HeapPriorityQueue

"""


from heapq import heapify, heappop, heappush
from graph_direct import Graph
from partition import Partition


def mst_prim_jarnik(g):
    d = {}
    tree = []
    h = []
    # insertion counter bc without PriorityQueue-like class
    dummy = 0
    for v in g.vertices():
        if len(d) == 0:
            d[v] = 0
        else:
            d[v] = float('inf')
        dummy += 1
        heappush(h, (d[v], dummy, (v, None))) # dummy autoincr will make last tuple out of comparison
    while len(h) > 0:
        key, _, value = heappop(h)
        u, edge = value
        if edge is not None:
            tree.append(edge)
        for link in g.incident_edges(u):
            v = link.opposite(u)
            e = next((e for e in h if e[0] == d[v] and e[2][0] == v), None)
            if e is not None:
                wgt = link.element()
                if wgt < d[v]:
                    d[v] = wgt
                    del h[h.index(e)]
                    heappush(h, (d[v], e[1], (v, link)))
    return tree


def mst_kruskal(g):
    tree = []
    h = []
    forest = Partition()
    position = {}
    dummy = 0
    for v in g.vertices():
        position[v] = forest.make_group(v)
    for e in g.edges():
        heappush(h, (e.element(), dummy, e))
        dummy += 1 # bc of heap radix sort
    size = g.vertex_count()
    while len(tree) != size -1 and len(h) > 0:
        wgt, _, edge = heappop(h)
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a is not b:
            forest.union(a, b)
            tree.append(edge)
    return tree



if __name__ == "__main__":
    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    v6 = g.insert_vertex('v6')
    v7 = g.insert_vertex('v7')
    v8 = g.insert_vertex('v8')
    e1 = g.insert_edge(v1, v2, 4)
    e2 = g.insert_edge(v1, v5, 5)
    e3 = g.insert_edge(v4, v5, 7)
    e4 = g.insert_edge(v4, v6, 6)
    e5 = g.insert_edge(v2, v5, 5)
    e6 = g.insert_edge(v5, v6, 4)
    e7 = g.insert_edge(v2, v3, 2)
    e8 = g.insert_edge(v3, v7, 2)
    e9 = g.insert_edge(v6, v7, 6)
    e10 = g.insert_edge(v7, v8, 3)
    e11 = g.insert_edge(v6, v8, 7)
    e12 = g.insert_edge(v2, v8, 8)
    e13 = g.insert_edge(v5, v7, 1)
    """
    tree = mst_prim_jarnik(g)
    print(tree)
    """
    tree = mst_kruskal(g)
    print(tree)
    assert set(tree) == {e13, e8, e7, e10, e6, e1, e4}


# Output:

"""
[Edge[Vertex[v5] ->[1] Vertex[v7]], Edge[Vertex[v2] ->[2] Vertex[v3]], Edge[Vertex[v3] ->[2] Vertex[v7]], 
 Edge[Vertex[v7] ->[3] Vertex[v8]], Edge[Vertex[v1] ->[4] Vertex[v2]], Edge[Vertex[v5] ->[4] Vertex[v6]], 
 Edge[Vertex[v4] ->[6] Vertex[v6]]]
"""
