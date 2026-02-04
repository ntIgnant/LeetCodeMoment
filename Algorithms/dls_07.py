# Workshop week 13 - exercise 2
# Having the int array [1, 2, 3, 4], find the subset of the array such that the sum is equal to 6.
# Use depth limited search to find the path, and also, which would be the depth level to guarantee a solution?

GOAL_NODES = [(1, 2, 3), (2, 4)] # goal states
SOURCE_NODE  = () # is this a good source node?

# utility functions
def get_last_node(a_path): return a_path[-1]

def get_succerosrs(a_graph, a_node):
    candidates = [1, 2, 3, 4] # all the possible values for a comination
    listed_node = list(a_node) # convert the node into a list (easier manipulation)
    successors = []

    last_val_in_tuple = a_node[-1] if a_node else 0 # handle the case where the tuple is empty 

    for i in candidates:
        new_node = listed_node.copy() # create a copy of th ecurrent node to create a succesor one
        
        # check for duplicated value and sum of values <= 6
        # avoid scenario like (2, 1), as it should be sequenctial
        if i <= last_val_in_tuple:
            continue

        # cehck for the bounderies | the sum should be 6 or less, no more
        if sum(new_node) + i > 6:
            continue

        
        # append the list to the succerossr, but as a tuple!
        new_node.append(i)
        successors.append(tuple(new_node)) # tupplpe appending

    return successors # return the found succerors


def dls(graph, source_node, goal_nodes, limit):
    paths = [[source_node]]

    while paths != []:
        current_path, paths = paths[0], paths[1:]

        # verify if the goal node was reached
        path_last_node = get_last_node(current_path)

        # verify if the last node is not in the list of goal nodes
        if path_last_node in goal_nodes:
            return current_path

        # else coninue exploring, so check if the depth limit was not reached
        curr_depth = len(current_path) - 1
        
        # if the depth limit was reached, then stop rxploring forward
        if curr_depth == limit:
            continue

        # else, get the succesors and keep discovering new paths
        last_node_succ = get_succerosrs(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            # else, create a new path for further exploration
            new_path = current_path + [nd] # list concatenation with the current path and the found tuple
            paths = [new_path] + paths # append the new path at the index 0 of the paths | STACK BEHAVIOR

    return f'No path found from {source_node} within depth {limit}'


print(f"Depth 1: {dls(None, SOURCE_NODE, GOAL_NODES, 1)}")

print(f"Depth 3: {dls(None, SOURCE_NODE, GOAL_NODES, 3)}")

# Depth 8: Guaranteed to find solution?
print(f"Depth 8: {dls(None, SOURCE_NODE, GOAL_NODES, 8)}")
