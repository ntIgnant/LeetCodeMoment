# Uniform Cost Search algorithm grph, with (cost, node) format
ucs_graph_2 = {
    "a": [(2, "b"), (1, "c")],
    "b": [(2, "d"), (5, "e")],
    "c": [(2, "d")],
    "d": [(3, "f")],
    "e": [(1, "f")],
    "f": []
}

#Implement a Uniform Cost Search (UCS) algorithm to find the cheapest path from node a to node f

# Utility Functions
def get_last_node(a_path): return a_path[-1]

def get_succesors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []

def ucs(graph, source_node, goal_node):
    frontier = [(0, source_node)] # so the frontier will store a path, wich will be a tuple composed like (total cost, path) | total cost refears to the cost from source to the last explored node

    while frontier != []:
        frontier.sort(key=lambda x: x[0]) # so this sorts the frontier to have the cheapest cost first | priority QUEUE BEHAVIOR
        curr_cost, curr_path = frontier.pop(0) # pop the first (index 0) tuple of the frontier, and unpack its values

        # Get the last node of the currennt path to check if the goal node was reached
        path_last_node = get_last_node(curr_path)

        # check if the goal node was reached        
        if path_last_node == goal_node:
            return curr_cost, curr_path # if it was reached, then return the cost and the path | same format (cost, path)
        
        # else keep expaning
        last_node_succ = get_succesors(graph, path_last_node) # so this will return the succesor nodes, wich its cost to go there

        for cos, pa in last_node_succ:
            # sanity Check to avoid cycles
            if pa in curr_path:
                continue
            new_cost = curr_cost + cos
            new_path = curr_path + pa

            # now, create a tuple with those values and append it (AT THE END) to the frontier | QUEUE BEHAVIOR
            frontier.append((new_cost, new_path))

    return None

print("a -> f :", ucs(ucs_graph_2, "a", "f"))
print("a -> d :", ucs(ucs_graph_2, "a", "d"))
print("b -> f :", ucs(ucs_graph_2, "b", "f"))
print("c -> f :", ucs(ucs_graph_2, "c", "f"))

