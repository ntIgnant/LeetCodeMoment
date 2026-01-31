my_graph = {'A': ['B', 'C', 'D'], 'B': ['E'], 'C': ['E'], 'D': ['E'], 'E': ['F'], 'F': []}

# Utility functions
def get_last_node(path): return path[-1] # so this will return the last element of the list (so last node in the path)
def get_successors(a_graph, node):
    if node in a_graph.keys():
        return a_graph[node]
    return [] # case where the node was not found in the graph (as dictionary key)

def breadth_search(graph, source_node, goal_node):
    paths = [source_node] # this list will store all the paths as they appear | frontier | so each element is a PATH

    while paths != []:
        # While list 'paths' not empty
        current_path, paths = paths[0], paths[1:] # first assign the current path, and then use list slicing to 'cut' the path list from index 1 to last (without 0)

        path_last_node = get_last_node(current_path)

        # Check if the goal node was reached, and return the full path
        if path_last_node == goal_node:
            return current_path
        
        last_node_succ = get_successors(my_graph, path_last_node) # get the successors of the current last node of the path

        for nd in last_node_succ:
            new_path = current_path + nd # so the paths are actually strings here
            paths.append(new_path)

    return f"No paths found from {source_node} to {goal_node}" # case wheere no path was found

test_01 = breadth_search(my_graph, 'A', 'F')
print(test_01)