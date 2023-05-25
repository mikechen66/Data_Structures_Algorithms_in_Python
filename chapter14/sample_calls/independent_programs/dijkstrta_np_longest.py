
from numpy import inf


def search(source, target, graph, costs, parents):
    nextNode = source
    while nextNode != target:
        for neighbor in graph[nextNode]:
            # Delete: if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
            if graph[nextNode][neighbor] + costs[nextNode] > costs[neighbor]:    
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                parents[neighbor] = nextNode
            del graph[neighbor][nextNode]
        del costs[nextNode]
        # Delete: nextNode = min(costs, key=costs.get)
        nextNode = max(costs, key=costs.get)
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
    graph = {'A': {'C': 5, 'D': 1, 'E': 2}, 
             'B': {'H': 1, 'G': 3}, 
             'C': {'I': 2, 'D': 3, 'A': 5},
             'D': {'C': 3, 'A': 1, 'H': 2}, 
             'E': {'A': 2, 'F': 3},
             'F': {'E': 3, 'G': 1}, 
             'G': {'F': 1, 'B': 3, 'H': 2}, 
             'H': {'I': 2, 'D': 2, 'B': 1, 'G': 2},
             'I': {'C': 2, 'H': 2}}
    # Delete: costs = {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf, 'I': inf}
    costs = {'A': 0, 'B': -inf, 'C': -inf, 'D': -inf, 'E': -inf, 'F': -inf, 'G': -inf, 'H': -inf, 'I': -inf}
    parents = {}
    result = search('A', 'B', graph, costs, parents)
    print('parent dictionary={}'.format(result))
    print('longest path={}'.format(back_pedal('A', 'B', result)))


# Output:

"""
parent dictionary={'C': 'A', 'D': 'C', 'E': 'A', 'I': 'H', 'H': 'D', 'B': 'G', 'G': 'H', 'F': 'G'}
longest path=['A', 'C', 'D', 'H', 'G', 'B']
"""