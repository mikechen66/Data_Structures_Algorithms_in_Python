

# graph_build.py


"""
# Add the methods as follows 

1.get_vertex(self, el)
2.adjacent_vertices(self, v, outgoing=True):
3.delete_edge(self, u, v)
4.delete_vertex(self, x)

# Add graph_build() funcion

It is the caller that use Graph as the medium 

"""

class Graph:
    """Representation of a simple graph using an adjacency map."""
    #----------------------------------- nested Vertex class --------------------------------
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
    #----------------------------------- nested Edge class ----------------------------------
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
            # return self._destination if v is self._origin else self._origin
            if v is self._origin:
                return self._destination
            else: 
                return self._origin
            raise ValueError('v not incident to edge')
        def element(self):
            # Return element associated with this edge.
            return self._element
        def __hash__(self):                     # will allow edge to be a map/set key
            return hash((self._origin, self._destination))
        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)
    #----------------------------------- Graph methods -------------------------------------
    def __init__(self, directed=False):
        """
        Create an empty graph (undirected, by default).
        Graph is directed if optional paramter is set to True.
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing
        """
        if directed:
            self._incoming = {}
        else:
            self._outgoing
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
    # Add get_vertex() method
    def get_vertex(self, el):
        """
        Return the graph's vertex with corresponding element
        equal to el. Return None on failure
        """
        for vertex in self.vertices():
            if vertex.element() == el:
                return vertex
        return None
    def edge_count(self):
        # Return the number of edges in the graph.
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges 
        # return total if self.is_directed() else total // 2
        if self.is_directed():
            return total
        else:
            return total // 2
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
        # adj = self._outgoing if outgoing else self._incoming
        if outgoing:
            adj = self._outgoing
        else: 
            adj = self._incoming
        return len(adj[v])
    def incident_edges(self, v, outgoing=True):   
        """
        Return all (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to request incoming edges.
        """
        self._validate_vertex(v)
        # adj = self._outgoing if outgoing else self._incoming
        if outgoing:
            adj = self._outgoing
        else:
            adj = self._incoming
        for edge in adj[v].values():
            yield edge
    # Add adjacent_vertices() method
    def adjacent_vertices(self, v, outgoing=True):
        # Return adjacent vertices to a given vertex
        if outgoing:
            if v in self._outgoing:
                return self._outgoing[v].keys()
            else:
                return None
        else:
            if v in self._incoming:
                return self._incoming[v].keys()
            else:
                return None
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
    # Add delete_edge() method
    def delete_edge(self, u, v):
        if not self.get_edge(u, v):
            # exception for trying to delete non-existent edge
            # can be handled from class user
            raise Exception('Edge is already non-existent.')
            return None
        u_neighbours = self._outgoing[u]
        del u_neighbours[v]
        v_neighbours = self._incoming[v]
        del v_neighbours[u]
        return None
    # Add delete_vertex() method
    def delete_vertex(self, x):
        # Delete vertex and all its adjacent edges from graph
        if (x not in self._outgoing) and (x not in self._incoming):
            raise Exception('Vertex already non-existent')
            return None
        secondary_map = self._outgoing[x]
        for vertex in secondary_map:
            # delete reference to incident edges
            if self.is_directed():
                del self._incoming[vertex][x]
            else:
                del self._outgoing[vertex][x]
        # delete reference to the vertex itself
        del self._outgoing[x]
        return None


def build_graph(sequence, is_directed=False):
    G = Graph(directed=is_directed)
    weight_mapping = {}
    if len(sequence[0]) == 3:
        weighted = True
    else:
        weighted = False
    for edge in sequence:
        source, destination = edge[0:2]
        try:
            source_vertex = G.insert_vertex(source)
        except Exception:
            source_vertex = G.get_vertex(source)
        try:
            destination_vertex = G.insert_vertex(destination)
        except Exception:
            destination_vertex = G.get_vertex(destination)
        new_edge = G.insert_edge(source_vertex,
                                 destination_vertex,
                                 str(source) + str(destination))
        if weighted:
            weight_mapping[new_edge] = edge[2]
        else:
            weight_mapping[new_edge] = 1
    return G, weight_mapping


if __name__ == '__main__':
    # Undirected graph example
    E = [('a', 'b'), ('b', 'c'), ('a', 'c')]
    G, _ = build_graph(E)
    print('Undirected G=(V,E) with V=(a,b,c) and E={(a,b),(b,c),(a,c)}.')
    print('Is the graph directed?: ' + str(G.is_directed()))
    a = G.get_vertex('a')
    print('Incident edges to: ' + a.element())
    for edge in G.incident_edges(a):
        print(edge.element())
    print('Adjacent vertices to: ' + a.element())
    x = G.adjacent_vertices(a, outgoing=True)
    for vertex in x:
        print(vertex.element())
    print('Deleting vertex a.')
    G.delete_vertex(a)
    print('Vertices count of G: ' + str(G.vertex_count()))
    for vertex in G.vertices():
        print(vertex.element())
    # print('Edges count of G: ' + str(G.edges_count()))
    print('Edges count of G: ' + str(G.edge_count()))
    for edge in G.edges():
        print(edge.element())
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # directed example
    E = [('a', 'b'), ('b', 'c'), ('a', 'c')]
    G, _ = build_graph(E)
    print('Undirected G=(V,E) with V=(a,b,c) and E={(a,b),(b,c),(a,c)}.')
    print('Is the graph directed?: ' + str(G.is_directed()))
    a = G.get_vertex('a')
    print('Is the graph directed?: ' + str(G.is_directed()))
    print('Incident edges to: ' + a.element())
    for edge in G.incident_edges(a):
        print(edge.element())
    print('Adjacent vertices to: ' + a.element())
    x = G.adjacent_vertices(a, outgoing=True)
    for vertex in x:
        print(vertex.element())
    print('Deleting vertex a.')
    G.delete_vertex(a)
    print('Vertices count of G: ' + str(G.vertex_count()))
    for vertex in G.vertices():
        print(vertex.element())
    # print('Edges count of G: ' + str(G.edges_count()))
    print('Edges count of G: ' + str(G.edge_count()))
    for edge in G.edges():
        print(edge.element())


# Output:

"""
Undirected G=(V,E) with V=(a,b,c) and E={(a,b),(b,c),(a,c)}.
Is the graph directed?: False
Incident edges to: a
ab
Adjacent vertices to: a
b
Deleting vertex a.
Vertices count of G: 5
b
b
c
a
c
Edges count of G: 2
bc
ac
Undirected G=(V,E) with V=(a,b,c) and E={(a,b),(b,c),(a,c)}.
Is the graph directed?: False
Is the graph directed?: False
Incident edges to: a
ab
Adjacent vertices to: a
b
Deleting vertex a.
Vertices count of G: 5
b
b
c
a
c
Edges count of G: 2
ac
bc
"""