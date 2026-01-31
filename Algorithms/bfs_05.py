my_graph = {'A': ['B', 'C', 'D'], 'B': ['E'], 'C': ['E'], 'D': ['E'], 'E': ['F'], 'F': ['G', 'H'], 'G': ['I', 'K'], 'H': ['j'], 'I': [], 'K': [], 'J': []}


def get_last_node(a_path): return a_path[-1] # return the last node of the path

def get_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node] # return the succesors of the node in the graph (values of key in the dictionary)
    return [] # else recuttn empty

def breadth_search(graph, source_node, goal_node):
    paths = [source_node] # initialization of paths with the source node

    while paths != []:
        current_path, paths = paths[0], paths[1:] # current path is the index 0 of paths, and new paths is everything starting from index 1
        
        path_last_node = get_last_node(current_path) # get the last node of the current path
        
        # Check if the goal node was reached
        if path_last_node == goal_node:
            return current_path
        
        last_node_succ = get_successors(graph, path_last_node) # get the succesors of the current last node

        for nd in last_node_succ:
            new_path = current_path + nd # This will create a new list based on the last string path
            paths.append(new_path) # append the new path to the list of paths

    return f'No path was found  from {source_node} to {goal_node} :()'

test_search = breadth_search(my_graph, 'A', 'K')
print(test_search)