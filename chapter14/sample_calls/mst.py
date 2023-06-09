

# mst.pt


"""
The mst functions can not call the methods related to the orginal methods under the orginal 
Graph class in graph.py. 

TypeError: '<' not supported between instances of 'str' and 'float'

However, there is modified Graph class under the scruipt of graph_direct.py. Users can adopt
mst_direct and mst_simple to call the methods of the modified Graph with the environment of 
either HeapPriorityQueue or directly simple environment. 

"""


from heap_priority_queue import HeapPriorityQueue
from adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from partition import Partition
from graph import Graph


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


if __name__ == '__main__':
    g = Graph(directed=True)
    v1 = g.insert_vertex(x='v1')
    v2 = g.insert_vertex(x='v2')
    v3 = g.insert_vertex(x='v3')
    v4 = g.insert_vertex(x='v4')
    v5 = g.insert_vertex(x='v5')
    e1 = g.insert_edge(v1, v2, x='e1')
    e2 = g.insert_edge(v1, v3, x='e2')
    e3 = g.insert_edge(v2, v3, x='e3')
    e4 = g.insert_edge(v3, v4, x='e4')
    e5 = g.insert_edge(v3, v5, x='e5')
    print(g)


# Output:

"""
<graph.Graph object at 0x7f8e1c667550>
"""