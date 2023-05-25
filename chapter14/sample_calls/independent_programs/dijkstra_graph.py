

# dijkstra_graph.py

"""

Dijkstra’s Algorithm in Python

Let’s start with a high-level illustration of Dijkstra’s algorithm.

Part One. Initialize the algorithm as follows:

1. set Reykjavik as the starting node.
2. set the distances between Reykjavik and all other cities to infinity, except for the 
   distance between Reykjavik and itself, which we set to 0.

Part Two. Iteratively execute the following steps:

1. choose the node with the smallest value as the “current node” and visit all of its 
   neighboring nodes. As we visit each neighbor, we update their tentative distance from 
   the starting node.
2. once visit all of the current node’s neighbors and update their distances, mark the 
   current node as “visited.” Marking a node as “visited” means that we’ve arrived at its 
   final cost.
3. go back to step one: the algorithm loops until it visits all the nodes in the graph. 

"""


import sys


# 1. Build the Graph class

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
    def construct_graph(self, nodes, init_graph):
        """
        This method makes sure that the graph is symmetrical. In other words, 
        if there's a path from node A to B with a value V, there needs to be 
        a path from node B to node A with a value V.
        """
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value   
        return graph
    def get_nodes(self):
        # Returns the nodes of the graph.
        return self.nodes
    def get_outgoing_edges(self, node):
        # Returns the neighbors of a node.
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    def value(self, node1, node2):
        # Returns the value of an edge between two nodes.
        return self.graph[node1][node2]


# 2. Implement the Dijkstra algorithm

def dijkstra(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    # Use dict to save cost of node visiting and update it as move ahead   
    shortest_path = {}
    # Use dict to save the shortest known path to a node found so far
    previous_nodes = {}
    # Use max_value to initialize the "infinity" value of unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # Initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    # Execute until visit all nodes
    while unvisited_nodes:
        # Find the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:          # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        # Retrieve the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # Also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
        # Mark the node as "visited" after visiting its neighbors,
        unvisited_nodes.remove(current_min_node)
    return (previous_nodes, shortest_path)


# 3. Create a function that shows the result

def show_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    # Add the start node manually
    path.append(start_node)
    print("Find the best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


if __name__ == '__main__':
    nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
    init_graph = {}
    for node in nodes:
        init_graph[node] = {}
    init_graph["Reykjavik"]["Oslo"] = 5
    init_graph["Reykjavik"]["London"] = 4
    init_graph["Oslo"]["Berlin"] = 1
    init_graph["Oslo"]["Moscow"] = 3
    init_graph["Moscow"]["Belgrade"] = 5
    init_graph["Moscow"]["Athens"] = 4
    init_graph["Athens"]["Belgrade"] = 1
    init_graph["Rome"]["Berlin"] = 2
    init_graph["Rome"]["Athens"] = 2
    graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra(graph=graph, start_node="Reykjavik")
    show_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Belgrade")


# Output:

"""
Find the best path with a value of 11.
Reykjavik -> Oslo -> Berlin -> Rome -> Athens -> Belgrade
"""
