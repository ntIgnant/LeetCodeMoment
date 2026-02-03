my_graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
path = ['a', 'b', 'c', 'd', 'e']

def get_successors(graph, node):
    return graph[node]

node_successors = get_successors(my_graph, 'B')

# print(node_successors)

# print(path[-1]) # so last index

paths = ["ab", "ac"]   # existing alternative paths
new_path = "ad"        # path we just generated

# DFS-style insertion (front)
paths = [new_path] + paths # This is what makes DFS have stack behaviour
# print(paths)

numArr = [1, 3, 2]

num = 123

print(num[0])
