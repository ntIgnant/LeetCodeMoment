my_graph = {'A': ['B', 'C', 'D'], 'B': ['E'], 'C': ['E'], 'D': ['E'], 'E': ['F'], 'F': ['G', 'H'], 'G': ['I', 'K'], 'H': ['j'], 'I': [], 'K': [], 'J': []}


# Create a Depth First Search implementation to look for node K from node A

# Utility Functions
def get_last_node(a_path): return a_path[-1] # return the last value of the path | path is a str here

def get_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node] # return the values of the key in the dictionary 'graph' | those are the successors of the specific node
    else:
        return [] # else return empty list

def depth_first_search(graph, source_node, goal_node):
    paths = [source_node] # initialize the frontier (list of paths) with the source node

    while paths != []:

        current_path, paths = paths[0], paths[1:] # from path list, assign a current exploration path and update the frontier (demove the exporation path)

        # get the last node of current path
        current_last_node = get_last_node(current_path)

        # Check if the goal node was reached
        if current_last_node == goal_node:
            return current_path
        

        # If goal node was't reached yet, keep expanding, so get the succesor nodes
        last_node_succ = get_successors(graph, current_last_node)

        for nd in last_node_succ:
            new_path = current_path + nd # create a current path with the new nodes discovered
            paths = [new_path] + paths # add the new path at 0 index to have STACK BEHAVIOUR

    return f"No path found from {source_node} to {goal_node}"


test_01 = depth_first_search(my_graph, 'A', 'H')
test_02 = depth_first_search(my_graph, 'B', 'Z')
print(test_01)
print(test_02)