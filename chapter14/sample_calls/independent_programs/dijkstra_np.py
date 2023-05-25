
# dijkstra_np.py

"""

1.graph dict: 

We will use the adjacency list representation for the graph and pathing from node A to node B
that use graph dict for representation. 

2.costs dict:

Keep track of the cost of pathing from our source node to all other nodes in our graph  with 
costs dictionary.

3. parents dicts:

Store node info in parents dict 
"""

from numpy import inf


def search(source, target, graph, costs, parents):
    """
    source: staring node 
    target: ending node
    costs: costs dict
    parents: parenting nodes 
    """
    nextNode = source
    while nextNode != target:
        # Iterate: once a node has been explored it is no longer a candidate 
        # for stepping, 
        for neighbor in graph[nextNode]:
            # Add the cost of pathing to the neighbor and the cost of the path 
            # to the next node
            if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                parents[neighbor] = nextNode
            # Remove the explored nodes from adjacency dicts of neighbors. 
            del graph[neighbor][nextNode]
        # Remove it from the cost dict
        del costs[nextNode]
        # Determine the shortest path by searcing the min element of cost dict
        nextNode = min(costs, key=costs.get)
    return parents


def back_pedal(source, target, searchResult):
    node = target
    backpath = [target]
    path = []
    while node != source:
        backpath.append(searchResult[node])
        node = searchResult[node]
    for i in range(len(backpath)):
        path.append(backpath[-i - 1])
    return path


if __name__ == '__main__':
    # Use the adjacency list representation for the graph  between nodes 
    graph = {'A': {'C': 5, 'D': 1, 'E': 2}, 
             'B': {'H': 1, 'G': 3}, 
             'C': {'I': 2, 'D': 3, 'A': 5},
             'D': {'C': 3, 'A': 1, 'H': 2}, 
             'E': {'A': 2, 'F': 3},
             'F': {'E': 3, 'G': 1}, 
             'G': {'F': 1, 'B': 3, 'H': 2}, 
             'H': {'I': 2, 'D': 2, 'B': 1, 'G': 2},
             'I': {'C': 2, 'H': 2}}
    # Assume the src node to any other node is infinite 
    costs = {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf, 'I': inf}
    # Store node info in parents dict 
    parents = {}
    result = search('A', 'B', graph, costs, parents)
    print('parent dictionary={}'.format(result))
    print('longest path={}'.format(back_pedal('A', 'B', result)))


# Output:

"""
parent dictionary={'C': 'D', 'D': 'A', 'E': 'A', 'H': 'D', 'F': 'E', 'I': 'H', 'B': 'H', 'G': 'H'}
longest path=['A', 'D', 'H', 'B']
"""