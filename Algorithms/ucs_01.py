# Implementation of Uniform Cost Search Algorithm (UCS)
# Finds the path with the cheapest cost from Source node to Goal node (Cheapest from the ROOT)
# Uniform-Cost-Search has a priority QUEUE as underlying DataStructure

# In Uniform Cost Search (UCS) each 'node' is stored as a tuple, wich contains the comulative cost from root, and the path
# e.g ('abde', cost)
# NORMALLY in the implementation of UCS, the tuples are structured as path, cost in that specific order, but it will depend on the graph




# Utility Functions
def get_last_node(a_path): return a_path[-1]

def get_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []

def ucs(graph, source_node, goal_node):
    frontier = [(0, source_node)] # So the fontier will store tuples, wich will contain (cost from root, path)

    while frontier != []:
        # sort the frontier values so that the cheaper cost appear first (having PRIORITY QUEUE BEHAVIOR)
        frontier.sort(key=lambda x: x[0]) #? kida get that its mapping the tuple to srot the cost?
        curr_cost, curr_path = frontier.pop(0) # so this pops the first tuple in the frontier, adn unpacks the values in cost and path (values of the tuple separated)

        # Get last node to verify if the goal node was reached 
        path_last_node = get_last_node(curr_path)

        # If the goal node was reached, return two values (path, cost from root to destination)
        if path_last_node == goal_node:
            return curr_path, curr_cost
        
        # else, keep discovering paths with their costs
        last_node_succ = get_successors(graph, path_last_node)

        for pa, cos in last_node_succ:
            if pa in curr_path:
                continue

            # Crate the values for the new tuple (cost, path)
            new_path = curr_path + pa
            new_cost = curr_cost + cos

            frontier.append((new_path, new_cost)) # append the new tuple (path, cost) to the frontier (for future visiting)

    return None