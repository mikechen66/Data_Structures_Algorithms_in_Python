

# topological_sort_print.py


"""
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices 
such that for every directed edge u v, vertex u comes before v in the ordering.
"""


from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)   # dictionary containing adjacency List
        self.V = vertices                # Numberof vertices
    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
    # A recursive function used by topologicalSort
    def util(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.util(i, visited, stack)
        # Push current vertex to stack which stores result
        stack.append(v)
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topological_sort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.util(i, visited, stack)
        # Print contents of the stack
        print(stack[::-1]) # return list in reverse order


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    print("Here give a Topological Sort of the given graph")
    g.topological_sort()


# Output:

"""
Here give a Topological Sort of the given graph
[5, 4, 2, 3, 1, 0]

"""