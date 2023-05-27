

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
"""


from copy import deepcopy
from graph_examples import figure_14_11 as example


def floyd_warshall(g):
    """Return a new graph that is the transitive closure of g."""
    closure = deepcopy(g)                      # imported from copy module
    verts = list(closure.vertices())           # make indexable list
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # verify that edge (i,k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # verify that edge (k,j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        # if (i,j) not yet included, add it to the closure
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure


if __name__ == '__main__':
        # from graph_examples import figure_14_11 as example
        g = example()
        print("Number of vertices is", g.vertex_count())
        print("Number of edges is", g.edge_count())
        closure = floyd_warshall(g)
        print("Number of edges in closure is", closure.edge_count())


# Output:


"""
Number of vertices is 7
Number of edges is 13
Number of edges in closure is 25
"""