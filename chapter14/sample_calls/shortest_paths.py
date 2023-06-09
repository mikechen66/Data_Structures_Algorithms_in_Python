

# shortest_paths.py

"""
We intend to apply the greedy method to the single-source, shortest-path problem, results 
in Dijkstra algorithm. The key of the algorithm is Edge Relax as follows.  

1. Algorithm

We define a label D[v] for each vertex v in V , which is used to approximate the distance 
in grapyh G from s to v. The meaning of these labels is that D[v] will always store the 
length of the best path we have found so far from s to v. 

Initially, D[s] = 0 and D[v] = ∞ for each v = s, and we define the set C, which is our 
"cloud" dict of vertices, to initially be empty. 

At each iteration of the algorithm, we select a vertex u not in C with smallest D[u] label, 
and pull u into C. In general, we will use a heapq to select among  the vertices outside the 
Cloud dict.

In the very first iteration, we will pull s into C. Once a new vertex u is pulled into C, 
we then update the label D[v] of each vertex v that is adjacent to u  and is outside of C, 
to reflect the fact that there may be a new and better way to get to v via u. This update 
operation is known as relaxation, for it takes an old estimate and checks if it can be 
improved to get closer to its true value. The specific edge relaxation operation is described 
as follows:

Edge Relaxation:
if D[u] + w(u, v) < D[v] then
D[v] = D[u] + w(u, v)

where 
w(u,v) = w(e) = wgt 

2. Abstraction

The script is quite abstract because it has a call on the methods of Graph class and chained 
calls on the methods of the methods of PriorityQueue-like classes. Therefore, it is hard to 
present a concrete test on the script. 


Due to half instantiation of the original graph.py, user only get the Hexadecimal address as 
conducting "from graph import Graph"

{<graph.Graph.Vertex object at 0x7f62d2c6a210>: 0, <graph.Graph.Vertex object at 0x7f62d2c6a250>: 
3, <graph.Graph.Vertex object at 0x7f62d2c6a290>: 5, <graph.Graph.Vertex object at 0x7f62d2c6a310>: 
8, <graph.Graph.Vertex object at 0x7f62d2c6a2d0>: inf}

Therefore, we use the modified "from graph_direct import graph" to enable human-readable 
output such as "Vertex[v1]: 0"。

There is a related script named dijkstra_queue.py that can help readers understand what happens 
with adoption of Queue data structure. Please take the scriupt for reference in the same folder. 
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


if __name__ == "__main__":
    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    e1 = g.insert_edge(v1, v2, 3)
    e2 = g.insert_edge(v2, v3, 2)
    e3 = g.insert_edge(v4, v2, 6)
    e4 = g.insert_edge(v3, v5, 7)
    e5 = g.insert_edge(v2, v5, 5)
    e6 = g.insert_edge(v4, v5, 6)
    path = shortest_path_lengths(g, v1)
    print(path)


# Output:

"""
{Vertex[v1]: 0, Vertex[v2]: 3, Vertex[v3]: 5, Vertex[v5]: 8, Vertex[v4]: inf}
"""