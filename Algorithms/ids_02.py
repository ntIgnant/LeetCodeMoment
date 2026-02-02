ids_graph = {
    "a": ["b", "c", "d"],
    "b": ["e", "f"],
    "e": ["i"],
    "i": ["m"],
    "f": ["j"],
    "c": ["g"],
    "g": ["k"],
    "k": ["n"],
    "d": ["h"],
    "h": ["l"],
    "l": ["o"],
    "j": [],
    "m": [],
    "n": [],
    "o": []
}


# Implement a Iterative-Deepening-Search (IDS) algorithm to find the path from node a -> o with max_deptth of 5

# So IDS is basically DLS but with a progresive depth controller

# Utility Functions
def get_last_node(a_path): return a_path[-1]

def get_succesors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []

def dls(graph, source_node, goal_node, limit):
    paths = [source_node] # frontier

    while paths != []:
        current_path, paths = paths[0], paths[1:]

        path_last_node = get_last_node(current_path)

        if path_last_node == goal_node:
            return current_path
        
        # else, increase the depth to continue expanding
        curr_depth = len(current_path) - 1
        if curr_depth == limit:
            continue

        last_node_succ = get_succesors(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            new_path = current_path + nd
            paths = [new_path] + paths

    return None # in case no path was found | return none to IDS to increase the max level

def ids(graph, source_node, goal_node, max_depth):
    for d in range(max_depth):
        result = dls(graph, source_node, goal_node, d)
        if result != None:
            return result, d # return the path with the depth where it was found
        
    return None, None


for i in range(1, 6):
    test = ids(ids_graph, 'a', 'o', i)
    print(test)