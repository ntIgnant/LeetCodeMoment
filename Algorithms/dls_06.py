# workshop prep week 13
# the goal is to sort the num array [1, 3, 2] in assending or dessiending order by using searching algorithms
# use dls | depth limited search | to find the path and also wich depth level would guarantee a solution?

START_NODE = (1, 3, 2)
GOAL_NODES = [(1, 2, 3), (3, 2, 1)] # possible goal nodes, both are valid


# utility functions
def get_last_node(a_path): return a_path[-1] # this will get the last tupe of the current path

def get_successors(a_graph, a_node):
    # here, the gaph is ignored because the swap is more logical than structural
    listed_node = list(a_node) # conver the node into a list for modification
    successors = []

    # so this will iterate 3 times (range(3-1) times, so 0, 1, 2) | so the length of the value sin the tuple
    for i in range(len(listed_node) - 1):
        new_list = listed_node.copy()

        # perform adjacent swap
        new_list[i], new_list[i+1] = new_list[i+1], new_list[i] # this swaps the valeus of adjacent values in the list (next indices)
        #print(new_list)
        successors.append(tuple(new_list)) # append the new list as a tupple

    return successors # return all the found succesors | NOTE: Those are represented back as tuples, not lists

def dls(graph, source_node, goal_nodes, limit):
    paths = [[source_node]] # now, the paths is a list of lists (list of tuples)

    while paths != []:
        current_path, paths = paths[0], paths[1:] # set variables for the current path (current tuple) and update the paths from index 1 tuple to so on

        # check if the last node is in the list of goal nodes (goal_nodes = list of two tuples assending and dessending sorted)
        path_last_node = get_last_node(current_path)

        # check if the node is in the list of tuples goal_nodes
        if path_last_node in goal_nodes:
            return current_path
        
        # if there was no match in goal ndoes, keep expaning so verify if the deptth limit was not reached
        curr_depth = len(current_path) - 1
        # if the limit was reached, stop expaning
        if curr_depth == limit:
            continue
        
        # else, get the succesors to create new nodes to explore
        last_node_succ = get_successors(graph, path_last_node) # this should return me a list of tupples, wich are the succesor nodes

        for nd in last_node_succ:
            # sanity check to avoid cyles
            if nd in current_path:
                continue
            new_path = current_path + [nd] # list concatenation
            paths = [new_path] + paths # add to the front to have STACK behavior
    
    return f'No path found from {source_node} within depth {limit}'

print(f"Depth 1: {dls(None, START_NODE, GOAL_NODES, 1)}")

# Depth 3: Guaranteed to find solution
print(f"Depth 3: {dls(None, START_NODE, GOAL_NODES, 3)}")