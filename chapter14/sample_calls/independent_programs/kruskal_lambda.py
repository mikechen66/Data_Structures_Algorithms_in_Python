

# kruskal_func.py

"""
kruskal's idea is intuitive. The edges are sorted by weight from smallest to largest, 
and then the edges that don't form a loop are selected from the smallest to the 
largest to form a spanning tree. Choose two edges that are not in the same connected
component.

Construct the union lookup set and use it to determine whether a  loop is formed, i.e.,
whether it is in the same component. Two connected components if the root node is the 
same, two connected points will form a loop. 
"""


def find_subtree(parent, i):
    """
    look up the most upper lever of i
    :param parent: parent is upper level of vertice 
    :param i: the number that is looked for 
    :return: the node of root 
    """
    if parent[i] != i:
        # Reassig a parent to a root node as compression requires
        parent[i] = find_subtree(parent, parent[i])
    return parent[i]


def union(parent, rank, u, v):
    """
    Merge the two subtrees 
    :param parent: as same as above 
    :param rank: the depth of subtree
    :param u: one vertice
    :param v: another vertice
    :return: None
    """
    h1 = find_subtree(parent, u)
    h2 = find_subtree(parent, v)
    # Merge the two vertices while not are same subtree
    if h1 != h2:
        if rank[h1] < rank[h2]:
            parent[h1] = h2
        else:
            parent[h2] = h1
            if rank[h1] == rank[h2]:
                rank[h1] += 1


def kruskal(n, edges):
    """
    :param n: number of vertices 
    :param edges: edges with weights
    :return: the edge set of the MST
    """
    mst = []
    # parent as e and ranks initilized as 0
    parent = [e for e in range(n)]
    # rank initialized as 0
    rank = [0] * n
    # make the edges sorted
    edges = sorted(edges, key=lambda item: item[2])
    num = 0
    for edge in edges:
        # u, v, w = egde[i]
        h1 = find_subtree(parent, edge[0]) 
        h2 = find_subtree(parent, edge[1])
        if h1 != h2:
            mst.append(edge)
            union(parent, rank, edge[0], edge[1])
            num += 1
        else:
            continue
        if num == n:
            break
    return mst


if __name__ == '__main__':
    edges = [
        [0, 1, 6],
        [0, 2, 1],
        [0, 3, 5],
        [2, 1, 5],
        [2, 3, 5],
        [2, 4, 5],
        [2, 5, 4],
        [1, 4, 3],
        [4, 5, 6],
        [5, 3, 2]
    ]
    n = 6
    mst = kruskal(n, edges)
    print('edges:')
    for e in mst:
        print(e)
    print('Total cost of MST:', sum([e[-1] for e in mst]))
    print('Maximum cost of MST:', max([e[-1] for e in mst]))


# Output:

"""
edges:
[0, 2, 1]
[5, 3, 2]
[1, 4, 3]
[2, 5, 4]
[2, 1, 5]
Total cost of MST: 15
Maximum cost of MST: 5
"""