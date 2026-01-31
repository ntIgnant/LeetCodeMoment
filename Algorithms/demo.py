my_graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
path = ['a', 'b', 'c', 'd', 'e']

def get_successors(graph, node):
    return graph[node]

node_successors = get_successors(my_graph, 'B')

print(node_successors)

print(path[-1]) # so last index