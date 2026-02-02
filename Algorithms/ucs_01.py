# Implementation of Uniform Cost Search Algorithm (UCS)
# Finds the path with the cheapest cost from Source node to Goal node (Cheapest from the ROOT)
# Uniform-Cost-Search has a priority QUEUE as underlying DataStructure

# In Uniform Cost Search (UCS) each 'node' is stored as a tuple, wich contains the comulative cost from root, and the path
# e.g ('abde', cost)
# NORMALLY in the implementation of UCS, the tuples are structured as path, cost in that specific order, but it will depend on the graph

# weighted graph witth (cost, path) format
ucs_graph = {
    "a": [(1, "b"), (5, "c")],
    "b": [(1, "d")],
    "d": [(10, "f")],
    "c": [(1, "f")],
    "f": []
}


# Utility Functions
def get_last_node(a_path): return a_path[-1]

def get_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []

def ucs(graph, source_node, goal_node):
    frontier = [(0, source_node)]  # (cost, path)

    while frontier:
        frontier.sort(key=lambda x: x[0])     # sort by cost
        curr_cost, curr_path = frontier.pop(0)

        last = curr_path[-1]
        if last == goal_node:
            return curr_path, curr_cost

        for cos, pa in graph.get(last, []):   # (step_cost, successor)
            if pa in curr_path:
                continue
            new_path = curr_path + pa
            new_cost = curr_cost + cos
            frontier.append((new_cost, new_path))

    return None


print("Try 1 a->f:", ucs(ucs_graph, "a", "f"))  # expected ('acf', 6)
print("Try 2 a->d:", ucs(ucs_graph, "a", "d"))  # expected ('abd', 2)
print("Try 3 a->a:", ucs(ucs_graph, "a", "a"))  # expected ('a', 0)
print("Try 4 b->f:", ucs(ucs_graph, "b", "f"))  # expected ('bdf', 11)
