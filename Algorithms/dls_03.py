test_graph = {
    'S': ['A', 'B'],
    'A': ['C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['H'],
    'G': [],
    'H': ['I'],
    'I': []
}


# Implement a Depth limited search (dls) algo. to find a path from node S to node I

# Utility Functions
def get_last_node(a_path): return a_path[-1]

def get_succesors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []

def dls(graph, source_node, goal_node, max_depth):
    paths = [source_node]

    while paths != []:
        current_path, paths = paths[0], paths[1:]

        # get the last node of the current path
        path_last_node = get_last_node(current_path)

        if path_last_node == goal_node:
            return current_path
        
        # else, keep exploring by increasing one depth level
        curr_depth_level = len(current_path)
        if curr_depth_level == max_depth:
            continue # stop going deeper if the max level was reached

        # keep expaning the paths
        last_node_succ = get_succesors(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            new_path = current_path + nd
            paths = paths + [new_path]

    return f'No path found from {source_node} to {goal_node}'

print('dls (limit 4):', dls(test_graph, 'S', 'I', 4))
print('dls (limit 5):', dls(test_graph, 'S', 'I', 8)) # :o