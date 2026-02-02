sample_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}


# Implement a Breadth first Search (BFS) to get from node A to node G AND from node D to node F

# Utility Functions
def get_last_node(a_path): return a_path[-1]

def get_succesors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []


# BFS
def bfs(graph, source_node, goal_node):
    paths = [source_node] # this will act as the frontier

    while paths != []:
        current_path, paths = paths[0], paths[1:]

        # get the last node of the current path for goal node verification
        path_last_node = get_last_node(current_path)

        if path_last_node == goal_node:
            return current_path
        
        # else, keep exploring new paths
        last_node_succ = get_succesors(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            new_path = current_path + nd

            # now, append the new path to paths with QUEUE BEHAVIOR | append at the end
            paths.append(new_path)

    return f"No path found from {goal_node} to {source_node}"


sampl01 = bfs(sample_graph, 'A', 'G')
sampl02 = bfs(sample_graph, 'D', 'F')

# print(sampl01)
# print(sampl02)