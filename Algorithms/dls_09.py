import glob_graph # I'll get the graph from here

# given_graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('D', 2), ('E', 5)],
#     'C': [('F', 1)],
#     'D': [],
#     'E': [('G', 1)],
#     'F': [('G', 3)],
#     'G': []
# }

# Use Depth limited seach algorithm (DSL) to get the path from node "A" to node "G"

# Utility Functions

def get_last_node(a_path): return a_path[-1] # return the last value of the path paaaaaaaa

def get_node_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node] # return the values of the key 'given node'
    else:
        return [] # case 'node leaf'

def dls(graph, source_node, goal_node, limit):
    frontier = [source_node] # in the initial case, frontier is gonna be 'A'

    while frontier != []:
        curr_path, frontier = frontier[0], frontier[1:] # use list slicing to assign different values to variables

        # check if the goal_node was reahed (the last node of the current path)
        path_last_node = get_last_node(curr_path)
        if path_last_node == goal_node:
            return curr_path # case where the goal node is reached

        # else, continue disovering paths, so first verify if the limit wast reached yet
        curr_depth = len(curr_path) - 1
        if curr_depth == limit:
            continue # stop with the exploration

        # else, get the successors (continue discovering paths)
        last_node_succ = get_node_successors(graph, path_last_node)
        # so here, each value inside last_node_succ is gonna be a tuple composed out of two values
        # (node char, cost)
        # for dls, we just ignore the cost

        for nd, cost in last_node_succ:
            # sanity check to avoid cycles
            if nd in curr_path:
                continue
            new_path = curr_path + nd # create a new path to append to the frontier
            frontier = [new_path] + frontier # append the new path to the frontier in index 0 to have STACK behavior

    return f"No path found from node {source_node} to node {goal_node} with limit {limit}"

test01 = dls(glob_graph.given_graph, 'A', 'G', 1)
test02 = dls(glob_graph.given_graph, 'A', 'G', 4)

print(test01)
print(test02)