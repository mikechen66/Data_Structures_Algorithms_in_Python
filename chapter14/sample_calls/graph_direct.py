

# graph_direct.py


class Graph:
    """Representation of a simple graph using an adjacency map."""
    #----------------------------------- nested Vertex class ------------------------------
    class Vertex:
        __slots__ = '_element'
        def __init__(self, element=None, *args, **kwargs):
            self._element = element
        def element(self):
            return self._element
        def __repr__(self):
            if hasattr(self, '_element') is not None:
                return f'Vertex[{self._element}]'
            else:
                return super().__repr__()
    #----------------------------------- nested Edge class --------------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'
        def __init__(self, origin, destination, element=None, *args, **kwargs):
            self._origin = origin
            self._destination = destination
            self._element = element
        def element(self):
            return self._element
        def endpoints(self):
            return (self._origin, self._destination)
        def opposite(self, v):
            if v not in (self._origin, self._destination):
                raise Exception('Vertex is not an endpoint of this edge.')
            return self._destination if v == self._origin else self._origin
        def __repr__(self):
            if self._element is not None:
                return f'Edge[{self._origin} ->[{self._element}] {self._destination}]'
            else:
                return f'Edge[{self._origin} -> {self._destination}]'
    #----------------------------------- Graph methods -----------------------------------
    def __init__(self, directed=False, *args, **kwargs):
        self._outgoing = {}
        self._incoming = self._outgoing if not directed else {}
    def is_directed(self):
        return self._outgoing is not self._incoming
    def insert_vertex(self, element=None):
        v = self.Vertex(element)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    def insert_edge(self, u, v, element=None):
        e = self.Edge(u, v, element)
        self._incoming[v][u] = e
        self._outgoing[u][v] = e
        return e
    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for e in adj[v].values():
            yield e
    def vertex_count(self):
        return len(self._outgoing)
    def vertices(self):
        return set(self._outgoing.keys())
    def edge_count(self):
        s = sum([len(self._outgoing[v]) for v in self._outgoing])
        return s if self.is_directed() else s // 2
    def edges(self):
        edges = set()
        for v in self._outgoing:
            edges.update(self._outgoing[v].values())
        return edges
    def get_edge(self, u, v):
        return self._outgoing[u].get(v, None)
    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    def remove_vertex(self, v):
        # removes vertex `v` and its related edges in O(deg(v)) amortized time.
        outgoing_edges = list(self.incident_edges(v))
        incoming_edges = []
        if self.is_directed():
            incoming_edges = list(self.incident_edges(v, outgoing=False))
            if v in self._incoming:
                del self._incoming[v]
            for e in incoming_edges:     # O(deg(v))
                u = e.opposite(v)
                del self._outgoing[u][v]
        if v in self._outgoing:
            del self._outgoing[v]
        for e in outgoing_edges:         # O(deg(v))
            u = e.opposite(v)
            del self._outgoing[u][v]
    def remove_edge(self, e):
        # removes edge `e` from graph in O(1) time.
        u, v = e.endpoints()
        del self._outgoing[u][v]
        if self.is_directed():
            del self._incoming[v][u]
        else:
            del self._outgoing[v][u]