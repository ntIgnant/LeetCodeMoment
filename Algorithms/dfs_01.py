my_graph = {'A': ['B', 'C', 'D'], 'B': ['E'], 'C': ['E'], 'D': ['E'], 'E': ['F'], 'F': ['G', 'H'], 'G': ['I', 'K'], 'H': ['j'], 'I': [], 'K': [], 'J': []}

# Implement a search from node A to node K using Depth First Search
# The only difference between BFS and DFS in the given implementation is on how new paths are added to the list of paths

# Utility Fucntions
def get_last_node(a_path): return a_path[-1] # get the last element of the list 'path' 

def get_successors(a_path, a_node):

    # Check if the node is a key in the dictionary (a node in the tree xd)
    if a_node in a_path.keys():
        return a_path[a_node]
    
    else:
        return [] # else return empty | so it's a leaf in this case

def depth_first_search(graph, source_node, goal_node):
    paths = [source_node] # this will act as the frontier | all the discovered apths will be stored here as strings

    while paths != []:
        current_path, paths = paths[0], paths[-1] # same queue behaviour here, the insertion is what makes it stack AT THE END

        # Check if current path reached the destination by checking it's last node
        path_last_node = get_last_node(current_path)

        # Check if the destination was reached
        if path_last_node == goal_node:
            return current_path
        
        # If there was no goal node reached yet, keep expandinig the path
        last_node_succ = get_successors(graph, path_last_node) # list of successors of the current node

        for nd in last_node_succ:
            new_path = current_path + nd # create a new path

            # Now, append the new path at the BEGINNING of the path list | STACK BEHAVIOUR
            paths = [new_path] + paths # it needs to be in brackets because new_path alone is a string, and paths is a list

    