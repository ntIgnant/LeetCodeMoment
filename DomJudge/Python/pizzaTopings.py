# So this problem involves traversre a graph of pizza toppings and mark (color) the 'forbiden' topic combinations
# Breath Fist Traversal Function to traverse the graph of toppings

def get_succesors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node] # return the values of the key (children of requested parent node in the graph)
    else:
        return [] # otherwise return empty list, meaning it's a leaf


# this breadth first traversal will also have a marking system to flag different path scenarios 'color'
def breath_first_traversal(graph, source_node, color):
    paths = [source_node] # initialization of the frontier with source node

    while paths != []:
        current_path, paths = paths[0], paths[1:] # take the current path and 'update' the pathhs to be without path index 0 | queue behhaviour

        # where should come the verification for goal node in case it's breadth first search

        # keep descovering paths (traversing), so get the succesors of the node
        last_node_succ = get_succesors(graph, current_path)

        for nd in last_node_succ:
            if color[nd] == 



num_cases = int(input) # Get the number of cases

for _ in range(num_cases):
    first_line = list(input) # get the first line containing n and m
    num_toppings, num_forbiden_pairs = int(first_line[0]), int(first_line[1]) # n and m

    for 

