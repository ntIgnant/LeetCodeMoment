my_graph = {'A': ['B', 'C', 'D'], 'B': ['E'], 'C': ['E'], 'D': ['E'], 'E': ['F'], 'F': ['G', 'H'], 'G': ['I', 'K'], 'H': ['j'], 'I': [], 'K': [], 'J': []}


# Implement Breadth First Search

# Utility Functions | get_last_node and get_succesors

def get_last_node(a_path): return a_path[-1] # return the last element of the given path (index -1)

def get_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node] # if the graph containns the node (as key), then return their values
    
    # else return empty
    return []

def breadth_search(graph, source_node, goal_node):
    paths = [source_node] # this is the 'frontier' | all the paths will be stored here

    while paths != []:
        current_path, paths = paths[0], paths[1:] # the current path will be the first in the list (queue behaviour) and the resth of paths from index 1 to last index

        path_last_node = get_last_node(current_path) # get the last element (node) of the current path

        # if the last element of the current path matches the goal node, then return the path
        if path_last_node == goal_node:
            return current_path
        
        # if the node was not found yet, get the successor nodes of the current las node
        last_node_succ = get_successors(graph, path_last_node) # this will be a list containing the succesor nodes to the current node

        # create a new path and store it in paths | to keep record of the paths in case the goal node is found
        for nd in last_node_succ:
            new_path = current_path + nd # new path is actually a string (e.g 'abceg')
            paths.append(new_path)

    # Case where there was no patth found
    return f"No path found from {source_node} to {goal_node}"

test_01 = breadth_search(my_graph, 'A', 'H')
test_02 = breadth_search(my_graph, 'B', 'Z')
print(test_01)
print(test_02)
