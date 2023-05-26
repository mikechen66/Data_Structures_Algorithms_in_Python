

# dijkstra_graph_show.py


from math import inf, isinf
from heapq import heappush, heappop
from typing import Any, Mapping, Tuple, List


Node = Any
Edges = Mapping[Node, float]
Graph = Mapping[Node, Edges]


def dijkstra(graph: Graph, start: Node, goal: Node) -> Tuple[float, List]:
    """
    Find the shortest distance between two nodes in a graph, and
    the path that produces that distance.
    The graph is defined as a mapping from Nodes to a Map of nodes which
    can be directly reached from that node, and the corresponding distance.
    Returns:
        A tuple containing
            - the distance between the start and goal nodes
            - the path as a list of nodes from the start to goal.
    If no path can be found, the distance is returned as infinite, and the
    path is an empty list.
    """
    shortest_distance = {}
    predecessor = {}
    heap = []
    heappush(heap, (0, start, None))
    while heap:
        distance, node, previous = heappop(heap)
        if node in shortest_distance:
            continue
        shortest_distance[node] = distance
        predecessor[node] = previous
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = predecessor[node]
            return distance, path[::-1]
        else:
            for successor, dist in graph[node].items():
                heappush(heap, (distance + dist, successor, node))
    else:
        return inf, []


if __name__ == '__main__':
    graph = {
        'a' : {'b':3, 'c':4, 'd':7},
        'b' : {'c':1, 'f':5},
        'c' : {'f':6, 'd':2},
        'd' : {'e':3, 'g':6},
        'e' : {'g':3, 'h':4},
        'f' : {'e':1, 'h':8},
        'g' : {'h':2},
        'h' : {'g':2}
    }
    distance, path = dijkstra(graph, 'a', 'e')
    if isinf(distance):
        print("No path")
    else:
        print(f"Distance = {distance}, path={path}")


# Output:

"""
Distance = 9, path=['a', 'c', 'd', 'e']
"""