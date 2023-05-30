

# kruskal_func.py

"""
To define node set A global variable Node, that is, similar {' A ':' A ', 'B', 'B', 'C', 'C', 'D' : 'D'}, 
if A and B two points connected, will be changed to {' A ', 'B', 'B', 'B ",... }, i.e., after any 
two points are connected, their values will be the same.
"""


# Set Node as a enmpty dict 
Node = dict()
# The initial value is 0, if used as the end of the connection, 
# it is increased by 1
Rank = dict()


def create_set(vertice):
    Node[vertice] = vertice
    Rank[vertice] = 0


def find_subtree(vertice):
    if Node[vertice] != vertice:
        Node[vertice] = find_subtree(Node[vertice])
    return Node[vertice]


def merge_subtree(u, v):
    # Connet two components (or nodes)
    s1 = find_subtree(u)
    s2 = find_subtree(v)
    if s1 != s2:
        if Rank[s1] > Rank[s2]:
            Node[s2] = s1
        else:
            Node[s1] = s2
            if Rank[s1] == Rank[s2]:
                Rank[s2] += 1


def kruskal(vertices, edges):
    for vertice in vertices:
        create_set(vertice)
    mst = []
    # edges = sorted(edges, key=lambda item: item[2]) 
    edges.sort(key=lambda item: item[2])
    for edge in edges:
        u, v, w = edge
        if find_subtree(u) != find_subtree(v):
            merge_subtree(u, v)
            mst.append(edge)
    return mst 


if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges  =   [('A', 'B', 7),
                ('A', 'D', 5),
                ('B', 'C', 8),
                ('B', 'D', 9),
                ('B', 'E', 7),
                ('C', 'E', 5),
                ('D', 'E',15),
                ('D', 'F', 6),
                ('E', 'F', 8),
                ('E', 'G', 9),
                ('F', 'G', 11)]
    print(kruskal(vertices, edges))


# Output:

"""
[('A', 'D', 5), ('C', 'E', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'G', 9)]
"""