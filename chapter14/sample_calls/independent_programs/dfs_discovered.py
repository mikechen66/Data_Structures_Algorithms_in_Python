

# dfs_discovered.py


"""
The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

Please note that the definition of graph, node and discovered is different from the 
Goodrich Python textbook. Graph is dict, discovered is list and node is a list. 
However, in the textbook g (or Graph) is an abstract class, node is string, discovered 
is dict. 

The DFS algorithm works as follows:

Start by putting any one of the graph's vertices on top of a stack.
Take the top item of the stack and add it to the discovered list.
Create a list of that vertex's adjacent nodes. Add the ones which aren't in the discovered
list to the top of the stack.
Keep repeating steps 2 and 3 until the stack is empty.

"""


def dfs(graph, start, discovered):
    if discovered is None:
        discovered = set()
    discovered.add(start)
    print(start)
    for next in graph[start] - discovered:
        dfs(graph, next, discovered)
    return discovered


if __name__ == '__main__':
    graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0']),
             '3': set(['1']),
             '4': set(['2', '3'])}
    start  = '0'
    discovered = None
    dfs(graph, '0', discovered)


# Output:

"""
0
1
4
3
2
3
2
{'1', '3', '0', '4', '2'}
"""