

# dfs.py

"""
A graph is a way of representing relationships that exist between pairs of objects. A graph 
is a set of objects, called vertices, together with a collection of pairwise connections 
between them, called edges. 

Edges in a graph are either directed or undirected. An edge (u, v) is said tobe directed 
from u to v if the pair (u, v) is ordered, with u preceding v. An edge (u, v) is said to be 
undirected if the pair (u, v) is not ordered. The two vertices joined by an edge are called 
the end vertices (or endpoints) of the edge.

If an edge is directed, its first endpoint is its origin and the other is the destination of 
the edge. Two vertices u and v are said to be adjacent if there is an edge whose end vertices 
are u and v.

The outgoing edges of a vertex are the directed edges whose origin is the vertex. The incoming 
edges of a vertex are the directed edges whose destination is the vertex. The degree of a 
vertex v, denoted deg(v), is the number of incident edges of v. The in-degree and out-degree 
of a vertex v are the number of the incoming and outgoing edges of v, and are denoted indeg(v) 
and outdeg(v), respectively.

The definition of a graph refers to the group of edges as a collection, not a set, thus allowing 
two undirected edges to have the same end vertices, and for two directed edges to have the same 
origin and the same destination. 

With few exceptions, graphs do not have parallel edges or self-loops. Such graphs are said to 
be simple. Thus, we can usually say that the edges of a simple graph are a set of vertex pairs 
(and not just a collection). Representation of a simple graph uses an adjacency map.
"""


from graph import Graph


def dfs(g, u, discovered):
    """
    Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in g.incident_edges(u):       # for every outgoing edge from u
        v = e.opposite(u)               # v is the opposite of u along the edge 
        if v not in discovered:         # v is an unvisited vertex
            discovered[v] = e           # e is the tree edge that discovered v
            dfs(g, v, discovered)       # recursively explore from v
    return g


def construct_path(u, v, discovered):
    """
    Return a list of vertices comprising the directed path from u to v,
    or an empty list if v is not reachable from u.
    discovered is a dictionary resulting from a previous call to DFS started at u.
    """
    path = []                        # empty path by default
    if v in discovered:
        # we build list from v to u and then reverse it at the end
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]        # find edge leading to walk
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()                  # reorient path from u to v
    return path


def dfs_complete(g):
    """
    Perform DFS for entire graph and return forest as a dictionary.
    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None            # u will be the root of a tree
            dfs(g, u, forest)
    return forest


if __name__ == "__main__":
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
    discovered = {v1: None}
    dfs(g, v1, discovered)
    assert len(discovered) == 5
    cp = construct_path(v1, v5, discovered)
    print(cp)
    dc = dfs_complete(g)
    print(dc)


# Output:

"""
# dfs(g, v1, discovered)
<graph.Graph object at 0x7fd288862e10>

# print(cp)
[<graph.Graph.Vertex object at 0x7fd288862e50>, <graph.Graph.Vertex object at 0x7fd288862e90>, 
<graph.Graph.Vertex object at 0x7fd288862ed0>, <graph.Graph.Vertex object at 0x7fd288862f50>]

# print(dc)
{<graph.Graph.Vertex object at 0x7fd288862e50>: None, 
 <graph.Graph.Vertex object at 0x7fd288862e90>: <graph.Graph.Edge object at 0x7fd288869eb0>,
 <graph.Graph.Vertex object at 0x7fd288862ed0>: <graph.Graph.Edge object at 0x7fd28886b870>, 
 <graph.Graph.Vertex object at 0x7fd288862f10>: <graph.Graph.Edge object at 0x7fd28886b8c0>, 
 <graph.Graph.Vertex object at 0x7fd288862f50>: <graph.Graph.Edge object at 0x7fd28886b910>}
"""
