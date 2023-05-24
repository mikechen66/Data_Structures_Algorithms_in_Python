

# mst_direct.pt

"""

Call the modified Graph(within graph_show.py) with importing the PriorityQueue-like classes.

"""


from heap_priority_queue import HeapPriorityQueue
from adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from partition import Partition
from graph_direct import Graph


def mst_prim_jarnik(g):
    """
    Compute a minimum spanning tree of weighted graph g.
    Return a list of edges that comprise the MST (in arbitrary order).
    """
    d = {}                               # d[v] is bound on distance to tree
    tree = []                            # list of edges in spanning tree
    pq = AdaptableHeapPriorityQueue()    # d[v] maps to value (v,e=(u,v))
    pqlocator = {}                       # map from vertex to its pq locator
    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if len(d) == 0:                                 # this is the first node
            d[v] = 0                                    # make it the root
        else:
            d[v] = float('inf')                         # positive infinity
        pqlocator[v] = pq.add(d[v], (v,None))
    while not pq.is_empty():
        key, value = pq.remove_min()
        u, edge = value                                 # unpack tuple from pq
        del pqlocator[u]                                # u is no longer in pq
        if edge is not None:
            tree.append(edge)                           # add edge to tree
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator:                          # thus v not yet in tree
                # see if edge (u,v) better connects v to the growing tree
                wgt = link.element()
                if wgt < d[v]:                                # better edge to v?
                    d[v] = wgt                                # update the distance
                    pq.update(pqlocator[v], d[v], (v, link))  # update the pq entry
    return tree


def mst_kruskal(g):
    """
    Compute a minimum spanning tree of a graph using Kruskal's algorithm.
    Return a list of edges that comprise the MST.
    The elements of the graph's edges are assumed to be weights.
    """
    tree = []                   # list of edges in spanning tree
    pq = HeapPriorityQueue()    # entries are edges in G, with weights as key
    forest = Partition()        # keeps track of forest clusters
    position = {}               # map each node to its Partition entry
    for v in g.vertices():
        position[v] = forest.make_group(v)
    for e in g.edges():
        pq.add(e.element(), e)    # edge's element is assumed to be its weight
    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a,b)
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
    tree = mst_prim_jarnik(g)
    print(tree)
    tree = mst_kruskal(g)
    print(tree)
    assert set(tree) == {e13, e8, e7, e10, e6, e1, e4}


# Output:

"""
# mst_prim_jarnik() method

[Edge[Vertex[v2] ->[2] Vertex[v3]], Edge[Vertex[v3] ->[2] Vertex[v7]], Edge[Vertex[v5] ->[1] Vertex[v7]], 
 Edge[Vertex[v7] ->[3] Vertex[v8]], Edge[Vertex[v5] ->[4] Vertex[v6]], Edge[Vertex[v1] ->[4] Vertex[v2]], 
 Edge[Vertex[v4] ->[6] Vertex[v6]]]


# mst_kruskal() method 
[Edge[Vertex[v5] ->[1] Vertex[v7]], Edge[Vertex[v3] ->[2] Vertex[v7]], Edge[Vertex[v2] ->[2] Vertex[v3]], 
 Edge[Vertex[v7] ->[3] Vertex[v8]], Edge[Vertex[v5] ->[4] Vertex[v6]], Edge[Vertex[v1] ->[4] Vertex[v2]], 
 Edge[Vertex[v4] ->[6] Vertex[v6]]]

"""
