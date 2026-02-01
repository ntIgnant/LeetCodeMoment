deep_graph = {
    'A': ['B', 'X'],
    'B': ['C'],
    'C': ['D', 'Y'],
    'D': ['E'],
    'E': ['F'],
    'F': ['G'],
    'G': ['H'],
    'H': ['I', 'Z'],
    'I': ['J'],
    'J': ['K'],
    'K': ['L'],
    'L': ['M'],
    'M': [],
    'X': [],
    'Y': [],
    'Z': []
}

# Create a depth limited search (DLS) implementation to find the path from node A to node X with different levels of depth (e.g 4, 5, 8)


# utility Functions
def get_last_node(a_path): return a_path[-1]

def get_succesors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []

def dls(graph, source_node, goal_node, max_depth):
    paths = [source_node] # frontier (explored but not visited paths)

    while paths != []:
        current_path, paths = paths[0], paths[1:]

        path_last_node = get_last_node(current_path)

        if path_last_node == goal_node:
            return current_path
        
        # else increase the depth level

        current_depth_level = len(current_path) - 1
        if current_depth_level == max_depth:
            continue # stop exploring new levels

        # explore new level, so get the succesors of the current last node
        last_node_succ = get_succesors(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            new_path = current_path + nd
            paths = paths + [new_path]

    return f"No path found from {source_node} to {goal_node}"


print('dls (limit 3):', dls(deep_graph, 'A', 'F', 3))
print('dls (limit 5):', dls(deep_graph, 'A', 'F', 5))
print('dls (limit 5):', dls(deep_graph, 'A', 'Z', 8)) # :o