given_graph = {
    "A": [("B", 2), ("C", 5)],
    "B": [("A", 2), ("C", 1), ("D", 2)],
    "C": [("A", 5), ("B", 1), ("E", 3)],
    "D": [("B", 2), ("E", 1), ("F", 4)],
    "E": [("C", 3), ("D", 1), ("G", 2)],
    "F": [("D", 4), ("G", 1)],
    "G": [("E", 2), ("F", 1)],
}


# Implement a Uniform cost search algorithm (UCS) to find the cheapest path from node A to node G

# Utility Functions
def get_last_node(a_path): return a_path[-1]

def get_successors(a_node, a_graph):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []


def ucs(graph, source_node, goal_node):
    frontier = [(source_node, 0)] # so, for this specific frontier, the format will be a tupple with the format (node, cost)

    while frontier != []:
        # first, sort the frontier in assending order based on the cost
        frontier.sort(key=lambda x: x[1]) # here, the lamnda will be mapped to the item 1 in the tupple, so the cost, and then will be sorted based on it
        # now, get the values cost and node using tupple unpacking
        curr_path, curr_cost = frontier.pop(0) # pop out the first (index 0) of the frontier, and unpac the values for variable assignation

        # check if goal_node was reached
        path_last_node = get_last_node(curr_path)

        if path_last_node == goal_node:
            return curr_path, curr_cost

        # else, get the successors and keep discovering paths
        last_node_succ = get_successors(path_last_node, graph)

        for nd, cos in last_node_succ:
            #cicle avoidance check
            if nd in curr_path:
                continue

            new_path = curr_path + nd
            new_cost = curr_cost + cos

            frontier = [(new_path, new_cost)] + frontier # append the frontier at index 0 to have STACK BEHAVIOR

    return f"No path found from {source_node} to {goal_node}"

test01 = ucs(given_graph, "A", "G")
test02 = ucs(given_graph, "A", "C")
test03 = ucs(given_graph, "A", "D")
print(test01)
print(test02)
print(test03)