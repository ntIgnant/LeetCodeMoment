ucs_graph_final = {
    "a": [(2, "b"), (4, "c"), (1, "d")],
    "b": [(7, "g"), (2, "e")],
    "c": [(1, "e"), (5, "f")],
    "d": [(2, "c"), (8, "g")],
    "e": [(2, "g")],
    "f": [(1, "g")],
    "g": []
}


# Implement a Uniform cost Search algorithm (UCS) to find the cheapes path from root 'a' to node 'g'

# Utillity functions
def get_last_node(a_path): return a_path[-1]

def get_succesors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []


def ucs(graph, source_node, goal_node):
    frontier = [(0, source_node)]

    while frontier != []:
        # First sort the frontier with cost rpitority to have priority queue behaviour (for cost)
        frontier.sort(key=lambda x: x[0]) # bc of cost is 0 index in the tuple brah
        curr_cost, curr_path = frontier.pop(0) # we pop the zero index tuple (the first inthe priority queue)

        # chec if the goal node was reached
        path_last_node = get_last_node(curr_path)

        if path_last_node == goal_node:
            return curr_cost, curr_path # return both values with the same format as the graph (cost, path)
        
        # else, keep exploring more possible paths to find goal node

        last_node_succ = get_succesors(graph, path_last_node) # this will return me a tuple with the 'children' of the current last node (cost, path)

        for cos, pa, in last_node_succ:
            if pa in curr_path:
                continue
            new_cost = curr_cost + cos
            new_path = curr_path + pa

            # now, create a tuple and append it to the frontier | this to have a QUEUE behaviour, that will after be transformed into priority queue
            frontier.append((new_cost, new_path)) # append as a tupple

    return None # case where no path was found


print("Test 1 a->g:", ucs(ucs_graph_final, "a", "g"))
print("Test 2 a->e:", ucs(ucs_graph_final, "a", "e"))
print("Test 3 d->g:", ucs(ucs_graph_final, "d", "g"))
print("Test 4 c->g:", ucs(ucs_graph_final, "c", "g"))
