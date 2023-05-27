

# floyd_warshall.py


"""
Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the 
pairs of vertices in a weighted graph. Please see the simple idea for the algorithm
as follows. 

Let k be the intermediate vertex in the shortest path from source to destination. In this 
step, k is the first vertex. 

if 
(A[i][j] > A[i][k] + A[k][j]).

do
A[i][j] = (A[i][k] + A[k][j]) 

This algorithm works for both the directed and undirected weighted graphs. But, it does 
not work for the graphs with negative cycles (where the sum of the edges in a cycle is 
negative).

The origianl "from graph_direct import Graph" can be worked only in the condition of 
adding remove_edge() method that is shown in the script of graph_direct.py


Due to the chained call on Graph and HeapPriorityQueue classes, the realization of the
algorithm in the textbook is more complex than a stand-alone Floyd-Warshall algorithm. 
"""


from copy import deepcopy
from graph_direct import Graph


def floyd_warshall(g):
    closure = deepcopy(g)                      # imported from copy module
    verts = list(closure.vertices())           # make indexable list
    n = len(verts)
    for k in range(n):
        for i in range(n):
            trans_one = closure.get_edge(verts[i], verts[k])
            if k != i and trans_one is not None:
                for j in range(n):
                    trans_two = closure.get_edge(verts[k], verts[j])
                    if i != j != k and trans_two is not None:
                        trans_three = closure.get_edge(verts[i], verts[j])
                        trans_weight = trans_one.element() + trans_two.element()
                        if trans_three is None:
                            closure.insert_edge(verts[i], verts[j], trans_weight)
                        elif trans_three.element() > trans_weight:  # replace it with a shorter way
                            closure.remove_edge(trans_three)
                            closure.insert_edge(verts[i], verts[j], trans_weight)
    # Return a new graph and vertices.
    return closure, verts


if __name__ == "__main__":
    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    v6 = g.insert_vertex('v6')
    v7 = g.insert_vertex('v7')
    v8 = g.insert_vertex('v8')
    e1 = g.insert_edge(v1, v2, 10)
    e2 = g.insert_edge(v1, v5, 10)
    e3 = g.insert_edge(v4, v5, 15)
    e4 = g.insert_edge(v4, v6, 15)
    e5 = g.insert_edge(v2, v5, 10)
    e6 = g.insert_edge(v5, v6, 10)
    e7 = g.insert_edge(v2, v3, 5)
    e8 = g.insert_edge(v3, v7, 5)
    e9 = g.insert_edge(v6, v7, 13)
    e10 = g.insert_edge(v7, v8, 7)
    e11 = g.insert_edge(v6, v8, 15)
    e12 = g.insert_edge(v2, v8, 20)
    e13 = g.insert_edge(v5, v7, 2)
    closure, vertices = floyd_warshall(g)
    print(closure)
    print(vertices)
    vertices.sort(key=lambda x: x.element())
    assert closure.get_edge(vertices[1], vertices[7]).element() == 17 # v2 -> v8
    assert closure.get_edge(vertices[0], vertices[7]).element() == 19 # v1 -> v8


# Output:

"""
<graph_direct.Graph object at 0x7f2e0e0ca710>
[Vertex[v4], Vertex[v3], Vertex[v8], Vertex[v5], Vertex[v6], Vertex[v7], Vertex[v1], Vertex[v2]]
"""