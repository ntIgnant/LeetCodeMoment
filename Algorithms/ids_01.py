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

# Implement a Iterative deepening search (IDS) searching algorithm to search a path from A to Z
# Iterative-deepening-search is just a Depth limited search but with a depth controller

# Utility functions
def get_last_node(a_path): return a_path[-1]

def get_succesors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    return []


def dls(graph, source_node, goal_node, limit):
    paths = [source_node]

    while paths != []:
        current_path, paths = paths[0], paths[1:]

        # get the last node of current path
        path_last_node = get_last_node(current_path)

        if path_last_node == goal_node:
            return current_path
        
        # else keep expanding, so check for the lepth limit reach
        curr_depth = len(current_path) - 1

        if curr_depth == limit:
            continue

        # otherwise, keep expaning the graph, exploring more paths
        last_node_succ = get_succesors(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            new_path = current_path + nd
            paths = [new_path] + paths # use Stack Behaviour

    return None # if there was no path found at the depth limit


# Now, create the actuall Iterative deepening search controller

def iterative_deepening_search(graph, soruce_node, goal_node, max_depth):
    for lim in range(max_depth + 1):

        # test different depths (and progresively increase it) till a path is found
        tmp_res = dls(graph,  soruce_node, goal_node, lim) # pass the args to dls but increase the depth limit progressively

        if tmp_res is not None:
            return tmp_res, lim # if a path was found, return the obtained dls path with its limit (assigned in ids)
        
    return None, None


print(iterative_deepening_search(deep_graph, 'A', 'Z', 7))  # should be (None, None)
print(iterative_deepening_search(deep_graph, 'A', 'Z', 8))  # should succeed
