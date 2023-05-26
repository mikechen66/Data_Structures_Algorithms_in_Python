

# shotest_path_length.py


"""

Implements Dijkstra's algorithm for finding a shortest path between two nodes in a 
directed graph.

Input:
   length_by_edge: A dict with every directed graph edge's length keyed by its 
                   corresponding ordered pair of nodes
   startnode: A start node
   goalnode: A target node

Precondition:
    all(length > 0 for length in length_by_edge.values())

Output:
    The length of the shortest path from startnode to goalnode in the input graph
"""


from heapq import heappush, heappop


class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], 
                 incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor = successor
        self.successors = successors
        self.predecessors = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes
    def successor(self):
        return self.successor
    def successors(self):
        return self.successors
    def predecessors(self):
        return self.predecessors


def shortest_path_length(length_by_edge, startnode, goalnode):
    unvisited_nodes = []  # FibHeap containing (node, distance) pairs
    heappush(unvisited_nodes, (0, startnode))
    visited_nodes = set()
    while len(unvisited_nodes) > 0:
        distance, node = heappop(unvisited_nodes)
        if node is goalnode:
            return distance
        visited_nodes.add(node)
        for nextnode in node.successors:
            if nextnode in visited_nodes:
                continue
            insert_or_update(unvisited_nodes,
                (min(
                    get(unvisited_nodes, nextnode) or float('inf'),
                    get(unvisited_nodes, nextnode) + length_by_edge[node, nextnode]
                ),
                nextnode)
            )
    return float('inf')


def get(node_heap, wanted_node):
    for dist, node in node_heap:
        if node == wanted_node:
            return dist
    return 0


def insert_or_update(node_heap, dist_node):
    dist, node = dist_node
    for i, tpl in enumerate(node_heap):
        a, b = tpl
        if b == node:
            node_heap[i] = dist_node #heapq retains sorted property
            return None
    heappush(node_heap, dist_node)
    return None


if __name__ == '__main__':
    node1 = Node("1")
    node5 = Node("5")
    node4 = Node("4", None, [node5])
    node3 = Node("3", None, [node4])
    node2 = Node("2", None, [node1, node3, node4])
    node0 = Node("0", None, [node2, node5])
    length_by_edge = {
        (node0, node2): 3,
        (node0, node5): 10,
        (node2, node1): 1,
        (node2, node3): 2,
        (node2, node4): 4,
        (node3, node4): 1,
        (node4, node5): 1
    }
    # Case 1: One path
    result =  shortest_path_length(length_by_edge, node0, node1)
    print(result)
    # Case 2: Multiple path
    result = shortest_path_length(length_by_edge, node0, node5)
    print(result)
    # Case 3: Start point is same as end point
    result = shortest_path_length(length_by_edge, node2, node2)
    print(result)
    # Case 4: Unreachable path
    result = shortest_path_length(length_by_edge, node1, node5)
    print(result)


# Output:

"""
1
10
0
inf
"""