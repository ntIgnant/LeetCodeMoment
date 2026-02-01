my_graph = {'A': ['B', 'C', 'D'], 'B': ['E'], 'C': ['E'], 'D': ['E'], 'E': ['F'], 'F': ['G', 'H'], 'G': ['I', 'K'], 'H': ['j'], 'I': [], 'K': [], 'J': []}

# Using Depth First Search (DFS), find a path from node A to node G

# Utility Functions
def get_last_node(a_path): return a_path[-1] # return the last value of the path | in this case it's the last index of a STR!

def get_successors(a_graph, a_node):

    # check if the dictionary (graph) contains the requested node as one of iths keys
    if a_node in a_graph.keys():
        return a_graph[a_node] # return the values of the requested key
    else:
        return [] # else return an empty 'path'

def depth_fist_search(graph, source_node, goal_node):
    paths = [source_node] # this will act as the frontier | the paths will be built from here
    
    while paths != []:
        current_path, paths = paths[0], paths[1:] # assign a current path to visit (index 0) and update the paths by taking the actual path without the current taken path (without 0 index)

        # get the last node in the current path
        path_last_node = get_last_node(current_path)

        # check if the goal node was reached
        if path_last_node == goal_node:
            return current_path # if yes, then return it's path
        
        # if it was't reached, then keep exploring new paths (explore to visit later)
        last_node_succ = get_successors(graph, path_last_node)

        for nd in last_node_succ:
            new_path = current_path + nd # create a new path with the new found node (explored but not visited yet)
            paths = [new_path] + paths # 'append' the new explored node in the inxed 0 of the path list | this ends in STACK BEHAVIOR

    return f'No path found between {source_node} and {goal_node}'


test_01 = depth_fist_search(my_graph, 'A', 'G')
print(test_01)