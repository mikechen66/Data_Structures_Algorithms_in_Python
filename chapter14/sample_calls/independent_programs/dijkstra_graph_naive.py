
# dijkstra_graph_naive.py


from math import inf
from graphviz import Graph


def undirected_graph(wmat, name="weighted_undirected_graph"):
    """
    Creates a pdf file with a weigthted graph's visualization
    Args:
    wmat: weigthted graph's adjacency matrix
    name: (optional) graph's filename
    """
    n = len(wmat)
    f = Graph(name, filename=name+'.gv')
    f.attr('node', shape='circle')
    for i in range(n):
        f.node(str(i))
    for i in range(n):
        for j in range(n):
            if wmat[i][j] != 0 and i < j:
                f.edge(str(i), str(j), label=str(wmat[i][j]))
    return f.view()


def find_all(wmat, start, end=-1):
    """
    distances[x] are the shortest distances from x vertex which 
    shortest path is paths[x]. x is an element of {0, 1, ..., n-1} 
    where n is the number of vertices
    Args:
    wmat:  weighted graph's adjacency matrix
    start: paths' first vertex
    end:  (optional) path's end vertex. 
    Return: a tuple with a distances' list and paths' list of
            all remaining vertices with the same indexing
            (distances, paths)
    Exceptions:
    Index out of range, Be careful with start and end vertices
    """
    n = len(wmat)
    dist = [inf]*n
    dist[start] = wmat[start][start]  
    spVertex = [False]*n
    parent = [-1]*n
    path = [{}]*n
    for count in range(n-1):
        minix = inf
        u = 0
        for v in range(len(spVertex)):
            if spVertex[v] == False and dist[v] <= minix:
                minix = dist[v]
                u = v
        spVertex[u] = True
        for v in range(n):
            if not(spVertex[v]) and wmat[u][v] != 0 and dist[u] + wmat[u][v] < dist[v]:
                parent[v] = u
                dist[v] = dist[u] + wmat[u][v]
    for i in range(n):
        j = i
        s = []
        while parent[j] != -1:
            s.append(j)
            j = parent[j]
        s.append(start)
        path[i] = s[::-1]
    return (dist[end], path[end]) if end >= 0 else (dist, path)


def find_shortest_path(wmat, start, end=-1):
    """
    Args:
    wmat    weigthted graph's adjacency matrix
    start   paths' first vertex
    end     (optional) path's end vertex. Return just
                the path
    Return: paths' list of all remaining vertices.
    Exceptions:
    Index out of range, Be careful with start and end vertices.
    """
    return find_all(wmat, start, end)[1]


def find_shortest_distance(wmat, start, end=-1):
    """
    Args:
    wmat: weigthted graph's adjacency matrix
    start:paths' first vertex
    end:  (optional) path's end vertex. 
    Return: distances' list of all remaining vertices.
    Exceptions:
    Index out of range, Be careful with start and end vertices.
    """
    return find_all(wmat, start, end)[0]


if __name__ == '__main__':
    wmat = [[0, 2, 0, 0, 0, 1, 0, 0],
        [2, 0, 2, 2, 4, 0, 0, 0],
        [0, 2, 0, 0, 3, 0, 0, 1],
        [0, 2, 0, 0, 4, 3, 0, 0],
        [0, 4, 3, 4, 0, 0, 7, 0],
        [1, 0, 0, 3, 0, 0, 5, 0],
        [0, 0, 0, 0, 7, 5, 0, 6],
        [0, 0, 1, 0, 0, 0, 6, 0]]
    print(find_all(wmat, 0))
    undirected_graph(wmat,"dijkstra_example")


# Output:

"""
([0, 2, 4, 4, 6, 1, 6, 5], [[0], [0, 1], [0, 1, 2], [0, 5, 3], [0, 1, 4], [0, 5], [0, 5, 6], [0, 1, 2, 7]])
'dijkstra_example.gv.pdf'
"""