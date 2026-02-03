# Workshop week 13 | implementation of searching algorithms

# Sort the array [1, 3, 2] in assending or dessending order
# Which would be a limit tht guarantees DLS to find the solution?

built_graph = {"132": "312",
               "312": "321",
               "321": "231",
               "231": "213",
               "213": "123",
               "123": []}


# Use depth limited search to find the sorted path and | wich level will guaranty a solution for DLS? = depth 6

# Utility functions
def get_successor(a_node, a_graph):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []


def dls(graph, source_node, goal_node, limit):
    frontier = [source_node]
    visited = []

    while frontier != []:
        curr_path, frontier = frontier[0], frontier[1:]
        visited.append(curr_path) # this list will just be to have the current depth metric | with its length

        # check if goal node was reached

        # in this case I compare directly the path with the goal node because those are strings, so the whole path is the node
        if curr_path == goal_node:
            return curr_path, limit
        
        # else keep exploring, verify if the depth was reached, and if it did, stop the exploration
        currr_depth = len(visited) # list all the visited nodes

        # if the depth limit was reached, stop exploring forward
        if currr_depth == limit:
            continue

        # else, get the current node succesor and keep exploring
        path_succ = get_successor(built_graph, currr_depth) # this is actually the succesor of the 'node', as this graph is linear actually

        # this is a sanity check to avoid cycle
        if path_succ in visited:
            continue
        new_paht = path_succ # just one node because this specific graphis linear, normally I would need to append it to the current path
        frontier = [new_paht] + frontier # append the new path to the index 0 to have STACK BEHAVIOUR as it is depth based

    return f'No path found from {source_node} to {goal_node} with depth {limit}'


for lim in range(1, 7):
    case01 = dls(built_graph, '132', '123', lim)
    print(case01)


