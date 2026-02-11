import glob_graph # I'll get the graph from here
import heapq as hq

# Grpah structure:
# given_graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('D', 2), ('E', 5)],
#     'C': [('F', 1)],
#     'D': [],
#     'E': [('G', 1)],
#     'F': [('G', 3)],
#     'G': []
# }

# Utility Functions

def get_last_node(a_path): return a_path[-1]

def get_node_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return [] # case where the last node is a leaf (dead end)

def ucs(graph, source_node, goal_node):
    # create the frontier having the cost at first possition, for th heapq to interpreat it
    frontier = [] # (cost, path)
    hq.heappush(frontier, (0, source_node)) # push values of the tuples to the heap | NOTE: have the cost first, for the heap to prioritize it
    visited = set()

    while frontier != []:
        # pop te values cost and path from the heapyfied frontier
        curr_cost, curr_path = hq.heappop(frontier) # fist in priority queue (based on cost)

        # check if the goal was reached based on the last node of the current path
        path_last_node = get_last_node(curr_path)
        if path_last_node == goal_node:
            return (curr_path, curr_cost) # return the path and the cost
        
        # else keep disvoering new paths
        if path_last_node in visited:
            continue
        visited.add(path_last_node) # add the current path to the set visited, to avoid cycles

        # get successors
        last_node_succ = get_node_successors(graph, path_last_node)

        for nd, cost in last_node_succ:
            # avoid cycles in the current path
            if nd in curr_path:
                continue

            new_cost = curr_cost + cost # new cost
            new_path = curr_path + nd # new path

            hq.heappush(frontier, (new_cost, new_path)) # push tuple to the heap (with cost first to have the priority based on it)

    return f"No node found from node {source_node} to node {goal_node}"


test01 = ucs(glob_graph.given_graph, 'A', 'G')
print(test01)