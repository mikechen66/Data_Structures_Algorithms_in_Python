

# bfs_example.py


"""
Please note that the definition of graph, node and discovered is different from the 
Goodrich Python textbook. Graph is dict, discovered is list and node is a list. 
However, in the textbook g (or Graph) is an abstract class, node is string, discovered 
is dict. 
"""


graph = {}      # A dict that includes the key-value pair
discovered = [] # List for discovered nodes.
queue = []      # Initialize a queue


def bfs(graph, node, discovered): 
    discovered.append(node)
    queue.append(node)
    # Creating loop to visit each node
    while queue:         
        m = queue.pop(0) 
        print (m, end = " ") 
        for neighbour in graph[m]:
            if neighbour not in discovered:
                discovered.append(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {
      '5' : ['3','7'],
      '3' : ['2', '4'],
      '7' : ['8'],
      '2' : [],
      '4' : ['8'],
      '8' : []
    }
    print("Following is the Breadth-First Search")
    bfs(discovered, graph, '5') 
    print()


# Output:

"""
Following is the Breadth-First Search
5 3 7 2 4 8 
"""