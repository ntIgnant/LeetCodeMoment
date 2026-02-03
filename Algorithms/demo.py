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

# print(num[0])

node1 = (1, 2, 3)
node2 = (1, 2, 3)
node3 = {1, 2, 3}
node4 = {2, 3, 1}

# print(node1 == node2)
# print(node2 == node3)
# print(node2 == node4)

# transformation frrom tuple to list Ooo oOO
pepe = (1, 2, 3, 4)
listed_pepe = list(pepe)

# print(listed_pepe)

for x in range(len(listed_pepe) - 1):
    print(f"{x} Hola")