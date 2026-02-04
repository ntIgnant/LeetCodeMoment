# weighted graph witth (cost, path) format
ucs_graph = {
    "a": [(1, "b"), (5, "c")],
    "b": [(1, "d")],
    "d": [(10, "f")],
    "c": [(1, "f")],
    "f": []
}

# Unse Uniform Cost Search (UCS) to find the cheapest path from node a to node f

# Utility Functions
def get_last_node(a_path): return a_path[-1]

def get_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []

def ucs(graph, source_node, goal_node):
    frontier = [(0, source_node)] # the structure for the frontier path will be (cost, path)

    while frontier != []:
        # IMPORTANT! | PRIORITY QUEUE BEHAVIOR
        # Sort the frontier such that it has priority queue behaviour with the COST
        frontier.sort(key=lambda x: x[0]) # sort based on the index 0 of the tuple, so the cost
        curr_cost, curr_path = frontier.pop(0) # this pops out the first (index 0) tupple of the frontier, and then the values (cost, path) gets unpacked into specific vriables

        # check if goal node was reached
        path_last_node = get_last_node(curr_path)

        if path_last_node == goal_node:
            return (curr_cost, curr_path) # (cost, path)
        
        # else, keep discovering new paths
        last_node_succ = get_successors(graph, path_last_node)

        for cos, pa in last_node_succ:
            # avoid cycles
            if pa in curr_path:
                continue
            new_cost = curr_cost + cos
            new_path = curr_path + pa

            frontier = [(new_cost, new_path)] + frontier

    return f"No path found from {source_node} to {goal_node}"

test01 = ucs(ucs_graph, 'a', 'f')
print(test01)