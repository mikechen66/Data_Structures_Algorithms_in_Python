

# floyd_warshall_simple.py


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


# The number of vertices
V = 4

INF = 999999


# Algorithm implementation
def floyd_warshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    # Adding vertices individually
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print_result(dist)


# Print the result
def print_result(dist):
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("INF", end=" ")
            else:
                print(dist[i][j], end="  ")
        print(" ")


if __name__ == '__main__':
    graph = [[0,     3, INF,   5],
             [2,     0, INF,   4],
             [INF,   1,   0, INF],
             [INF, INF,   2,   0]]
    floyd_warshall(G)


# Output:

"""
0  3  7  5   
2  0  6  4   
3  1  0  5   
5  3  2  0   
"""