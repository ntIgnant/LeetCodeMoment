import glob_graph # I'll get the graph from here

# Okay so implement an Iterative deepening search (IDS) to get the path from node 'A' to node 'G'

# Utility Functions

def get_last_node(a_path): return a_path[-1] # return the last node of a given path

def get_node_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return [] # case wher the node is a leaf (no successors)

def dls(graph, source_node, goal_node, limit):
    frontier = [source_node]

    while frontier != []:
        curr_path, frontier = frontier[0], frontier[1:] # split the variable values using list slicing

        # chek if the destinantion was reached by comparing the last node of curr path with goal node
        path_last_node = get_last_node(curr_path)

        if path_last_node == goal_node:
            return curr_path # case where the goal path is reahed

        # to continue exploring, verify if the limit wasn't reached
        curr_depth = len(curr_path) - 1
        if curr_depth >= limit:
            continue
        
        # continue discovering paths, so get the successors
        last_node_succ = get_node_successors(graph, path_last_node)

        for nd, cost in last_node_succ:
            # sanity check to avoid cycles
            if nd in curr_path:
                continue
            
            new_path = curr_path + nd # create a new path as string arrangement
            frontier = [new_path] + frontier # append it to the fronter in index 0 (to keep stack behavior)

    return None # return none to the IDS function in case no path was found with the given limit

# Iterative deepening search
def ids(graph, source_node, goal_node, max_depth):
    for lim in range(max_depth + 1):
        tmp_result = dls(graph, source_node, goal_node, lim)
        if tmp_result != None:
            return (tmp_result, lim)
    
    return f"No Path found from node {source_node} to node {goal_node} with limit of {max_depth}"

test01 = ids(glob_graph.given_graph, 'A', 'G', 2)
print(test01)

test02 = ids(glob_graph.given_graph, 'A', 'G', 5)
print(test02)