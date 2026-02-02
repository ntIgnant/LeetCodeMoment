dls_graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "d": ["e"],
    "e": ["f"],
    "c": ["g"],
    "g": ["f"],
    "f": []
}


# Implement a Depth-Limited-Search (DLS) algorithm to find the path from node a -> f with depth 3 and 4

# utility functions
def get_last_node(a_path): return a_path[-1]

def get_succesors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []


def dls(graph, source_node, goal_node, limit):
    paths = [source_node]

    while paths != []:
        current_path, paths = paths[0], paths[1:]

        path_last_node = get_last_node(current_path)

        if path_last_node == goal_node:
            return current_path
        
        # else, check if the limit of depth was reached
        current_depth = len(current_path) - 1

        if current_depth == limit:
            continue

        # else, continue exploring new paths
        last_node_succ = get_succesors(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            new_path = current_path + nd # create a new discovered path (not visited yet)
            paths = [new_path] + paths # STACK BEHAVIOUR because it's Depth based

    
    return f'No path found from {source_node} to {goal_node}'


test01 = dls(dls_graph, 'a', 'f', 2)
test02 = dls(dls_graph, 'a', 'f', 3)
test03 = dls(dls_graph, 'a', 'f', 4)

print(test01)
print(test02)
print(test03)