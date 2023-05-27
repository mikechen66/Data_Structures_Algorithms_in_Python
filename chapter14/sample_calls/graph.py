

# graph.py


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


class Graph:
    """Representation of a simple graph using an adjacency map."""
    #----------------------------------- nested Vertex class ------------------------------
    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'
        def __init__(self, x):
            # Do not call constructor directly. Use Graph's insert_vertex(x).
            self._element = x
        def element(self):
            # Return element associated with this vertex.
            return self._element
        def __hash__(self):                     # will allow vertex to be a map/set key
            return hash(id(self))
        def __str__(self):
            return str(self._element)
    #----------------------------------- nested Edge class --------------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'
        def __init__(self, u, v, x):
            # Do not call constructor directly; use Graph's insert_edge(u,v,x).
            self._origin = u
            self._destination = v
            self._element = x
        def endpoints(self):
            # Return (u,v) tuple for vertices u and v.
            return (self._origin, self._destination)
        def opposite(self, v):
            # Return the vertex that is opposite v on this edge.
            if not isinstance(v, Graph.Vertex):
                raise TypeError('v must be a Vertex')
            return self._destination if v is self._origin else self._origin
            """
            if v is self._origin:
                return self._destination
            else: 
                return self._origin
            """
            # raise ValueError('v not incident to edge')
        def element(self):
            # Return element associated with this edge.
            return self._element
        def __hash__(self):                     # will allow edge to be a map/set key
            return hash((self._origin, self._destination))
        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)
    #----------------------------------- Graph methods -----------------------------------
    def __init__(self, directed=False):
        """
        Create an empty graph (undirected by default or directed if set to True).
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing
        """
        if directed:
            self._incoming = {}
        else:
            self.incoming = self._outgoing
        """
    def _validate_vertex(self, v):
        # Verify that v is a Vertex of this graph.
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')
    def is_directed(self):
        """
        Return True if this is a directed graph; False if undirected.
        Property is based on the original declaration of the graph, not its contents.
        """
        return self._incoming is not self._outgoing # directed if maps are distinct
    def vertex_count(self):
        # Return the number of vertices in the graph.
        return len(self._outgoing)
    def vertices(self):
        # Return an iteration of all vertices of the graph.
        return self._outgoing.keys()
    def edge_count(self):
        # Return the number of edges in the graph.
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges 
        return total if self.is_directed() else total // 2
        """
        if self.is_directed():
            return total
        else:
            return total // 2
        """
    def edges(self):
        # Return a set of all edges of the graph.
        result = set()                      # avoid double-reporting edges of UG
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result
    def get_edge(self, u, v):
        # Return the edge from u to v, or None if not adjacent.
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)     # returns None if v not adjacent
    def degree(self, v, outgoing=True):   
        """
        Return number of (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to count incoming edges.
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        """
        if outgoing:
            adj = self._outgoing
        else: 
            adj = self._incoming
        """
        return len(adj[v])
    def incident_edges(self, v, outgoing=True):   
        """
        Return all (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to request incoming edges.
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        """
        if outgoing:
            adj = self._outgoing
        else:
            adj = self._incoming
        """
        for edge in adj[v].values():
            yield edge
    def insert_vertex(self, x=None):
        # Insert and return a new Vertex with element x.
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}          # need distinct map for incoming edges
        return v
    def insert_edge(self, u, v, x=None):
        """
        Insert and return a new Edge from u to v with auxiliary element x.
        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        if self.get_edge(u, v) is not None: # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
