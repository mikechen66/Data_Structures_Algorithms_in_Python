

# kruskal_graph.py


"""
Define different classes such as Node, Graph, Edge and Kruskal to serperate
the concerns for flexible modulality.  
"""

# Define the Node class 

class Node:
    """The Node class represents each vertex of the graph"""
    def __init__(self, value, neighbors=None):
        """
        value: The attribute value represents the stored data
        neighbors: The list of neighbors represents the vertices with 
                    which exists a connection 
        """
        self.value = value
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
    # Return True if the vertex is connected with at least one vertex
    def has_neighbors(self):
        if len(self.neighbors) == 0:
            return False
        return True
    # Return the number of vertices with which has a connection
    def number_of_neighbors(self):
        return len(self.neighbors)
    # Add a new connection to the neighboor list
    def add_neighboor(self, neighboor):
        self.neighbors.append(neighboor)
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return self.value == other
    def __str__(self):
        returned_string = ""
        if self.has_neighbors():
            for neighboor in self.neighbors:
                returned_string += f"{self.value} -> {neighboor[0].value} "  
        else:
            returned_string += f"{self.value} -> None"    
        return returned_string
        

class Graph:
    """Graph class represents the graph data structure."""
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
    # Add a new node (vertex) in the grpah
    def add_node(self, node):
        self.nodes.append(node)
    # Return True if the node with the given value exists.
    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node 
        return None
    # Add a new edge between two nodes
    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)        
        node2 = self.find_node(value2)
        # Kruskal's algorithm works with undirected graphs so we just store 
        # only the one direction of the edge, the other is implied
        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor((node2, weight))
        else:
            print("Error: One or more nodes were not found")
    # Return the number of nodes of the graph
    def number_of_nodes(self):
        return f"The graph has {len(self.nodes)} nodes"
    # Return True if the given nodes are connected.
    def are_connected(self, node_one, node_two):
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)
        for neighboor in node_one.neighbors:
            if neighboor[0].value == node_two.value:
                return True
        return False
    def __str__(self):
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n" 
        return graph


class Edge():
    """Edge class represents each each of a graph."""
    def __init__(self, node1, node2, weight):
        """
        node1 : type of Node represents the first node
        node2 : type of Node represents the second node
        weight: type of int represents the wight of the edge 
        """
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
    # used to define the > between two edges based on the weight
    def __gt__(self, other):
        return self.weight > other.weight
    # used to define the < between two edges based on the weight
    def __lt__(self, other):
        return self.weight < other.weight
    # used to define the == between two edges based on the weight
    def __eq__(self, other):
        return self.weight == other.weight
    def __str__(self):
        return f"{self.node1.value} {self.node2.value} {self.weight}"



class Kruskal:
    """Represent the Kruskal's Algorithm"""
    def __init__(self, graph):
        self.graph = graph
        # create a new empty tree (in a form of graph)
        self.tree = Graph()
        # Add all the nodes to the new tree
        for node in self.graph.nodes:
            self.tree.add_node(node)
        # For each vertex of the graph we create a set and store them in a list
        self.sets = [set(node.value) for node in self.graph.nodes]
        self.edges = []
        self.number_of_vetices = len(graph.nodes)
        # Sort the edges in a ascend order based on the weight
        self.sort_edges()
        # Remove the edges from the nodes in the tree
        for node in self.tree.nodes:
            node.neighbors.clear()
    # Sort the edges of the list based in the weight of each edge.
    def sort_edges(self):
        for node in self.graph.nodes:
            for edge in node.neighbors:
                self.edges.append(Edge(node, edge[0], edge[1]))
        self.edges.sort()
    # Return the index of the set in the list of sets, in which node is contained.
    def find_set(self, node):
        for index, s in enumerate(self.sets):
            if node.value in s:
                return index
    # Merge the given sets and delete them from the list.
    def union_set(self, set1, set2):
        # Get the sets based on their index in the list
        selected_set1 = self.sets[set1]
        selected_set2 = self.sets[set2]
        # Union the two sets
        new_set = selected_set1.union(selected_set2)
        # Delete the individual sets
        self.sets.remove(selected_set1)       
        self.sets.remove(selected_set2)
        # Add the union of the set in the list of sets
        self.sets.append(new_set)   
    # The core of the algorithm. Execute the repetitive steps of the algorithm.
    def execution(self):
        # intitialize the values
        inserted_edges = 0
        total_cost = 0
        while True:
            # Select the edge with the minimum weight
            selected_edge = self.edges.pop(0)
            set1 = self.find_set(selected_edge.node1)
            set2 = self.find_set(selected_edge.node2)
            # If the vertices of the edge are not in the same set the edge 
            # does not form a cycle, so it is added to the tree
            if set1 != set2:
                # update the values
                inserted_edges += 1
                total_cost += selected_edge.weight
                self.union_set(set1, set2)
                self.tree.add_edge(selected_edge.node1.value, selected_edge.node2.value, selected_edge.weight)
            # Check if the necessary number of edges are inserted on the tree
            if inserted_edges == self.number_of_vetices - 1:
                return self.tree, total_cost
                

if __name__ == '__main__':
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node('A'))
    graph.add_node(Node('B'))
    graph.add_node(Node('C'))
    graph.add_node(Node('D'))
    graph.add_node(Node('E'))
    graph.add_node(Node('F'))
    graph.add_node(Node('G'))
    graph.add_node(Node('H'))
    graph.add_node(Node('I'))
    # Add edges
    graph.add_edge('A', 'B', 9)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('B', 'E', 7)
    graph.add_edge('C', 'D', 4)
    graph.add_edge('C', 'F', 3)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'F', 5)
    graph.add_edge('E', 'F', 6)
    graph.add_edge('E', 'G', 3)
    graph.add_edge('F', 'G', 8)
    graph.add_edge('F', 'H', 5)
    graph.add_edge('G', 'H', 1)
    graph.add_edge('G', 'I', 3)
    graph.add_edge('H', 'I', 2)
    # Execute the algorithm
    alg = Kruskal(graph)
    min_spanning_tree, cost = alg.execution()
    print("The minimum spanning tree is the following")
    print(min_spanning_tree)
    print(f"The total cost of the minimum spanning tree is {cost}")


# The minimum spanning tree is the following
# A -> C
# B -> D B -> C
# C -> F
# D -> E
# E -> G
# F -> None
# G -> H
# H -> I
# I -> None

# The total cost of the minimum spanning tree is 18