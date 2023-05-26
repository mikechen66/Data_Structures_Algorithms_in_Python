

# shortest_path_call.py

"""
Design an efficient algorithm for finding a longest directed path from a vertex s to a 
vertex t of an acyclic weighted directed graph G . Specify the graph representation used 
and any auxiliary data structures used. Also analyze the time complexity of your algorithm.
"""


from graph_direct import Graph
from adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


def shortest_path_lengths(g, src):
    """
    It compute shortest-path distances from src(source) to reachable vertices of g.
    Graph g can be undirected or directed, but must be weighted such that e.element() 
    returns a numeric weight for each edge e.
    Return dictionary mapping each reachable vertex to its distance from src.
    """
    d = {}                                        # d[v] is upper bound from s to v
    cloud = {}                                    # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()             # vertex v will have key d[v]
    pqlocator = {}                                # map from vertex to its pq locator
    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')                   # syntax for positive infinity
        pqlocator[v] = pq.add(d[v], v)            # save locator for future updates
    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key                            # its correct d[u] value
        del pqlocator[u]                          # u is no longer in pq
        for e in g.incident_edges(u):             # outgoing edges (u,v)
            v = e.opposite(u)
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = e.element()
                if d[u] + wgt < d[v]:                   # better path to v?
                    d[v] = d[u] + wgt                   # update the distance
                    pq.update(pqlocator[v], d[v], v)    # update the pq entry
    return cloud                                  # only includes reachable vertices


def shortest_path_tree(g, s, d):
    """
    Reconstruct shortest-path tree rooted at vertex s, given distance map d.
    Return tree as a map from each reachable vertex v (other than s) to the
    edge e=(u,v) that is used to reach v from its parent u in the tree.
    """
    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident_edges(v, False):       # consider INCOMING edges
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] + wgt:
                    tree[v] = e                        # edge e is used to reach v
    return tree


def construct_path(g, s, d):
    path = []
    for v in d:
        if v is not s:
            for e in g.incident_edges(v, outgoing=False):
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] + wgt:
                    path.append(e)
    return path


def longest_path(g, s, t):
    d = shortest_path_lengths(g, s)
    return construct_path(g, s, d)


if __name__ == "__main__":
    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    e1 = g.insert_edge(v1, v2, -3)
    e2 = g.insert_edge(v2, v3, -2)
    e3 = g.insert_edge(v4, v2, -6)
    e4 = g.insert_edge(v3, v5, -7)
    e5 = g.insert_edge(v2, v5, -5)
    e6 = g.insert_edge(v4, v5, -6)
    p = longest_path(g, v1, v5)
    print(p)


# Output:

"""
[Edge[Vertex[v1] ->[-3] Vertex[v2]], Edge[Vertex[v2] ->[-5] Vertex[v5]], Edge[Vertex[v2] ->[-2] Vertex[v3]]]
"""