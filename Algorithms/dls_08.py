import glob_graph # so I'll get the graph from here

# Each nod is ("char", cost)

# Find the path from node "A" to node "G" using Depth Limited search

# Utility Functions
def get_last_node(a_path): return a_path[-1] # retunt the last element of the path

def get_path_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node] # return the values of the key a_node
    else:
        return [] # else return empty list (case where the node is a leaf)

def dls(graph, source_node, goal_node, limit):
    # Create a frontier
    frontier = [source_node] # where source node = "A"

    while frontier != []:
        curr_path = frontier.pop(0) # pop first value of the frontier (index 0 placement)

        # check if the current path (last node) matches the goal node
        path_last_node = get_last_node(curr_path)
        
        if path_last_node == goal_node:
            return curr_path # retunt the path
        
        # else, continue epxloring paths, so verify if the limit wasn't reached and if the path_last node not in visited
        curr_depth = len(curr_path) - 1 # calculate the current depth

        if curr_depth == limit:
            continue # if the current depth has reached the limit (max depth), then stop

        # else, keep exporing the paths
        last_node_succ = get_path_successors(graph, path_last_node)

        for nd, cos in last_node_succ:
            # sanity check to avoid cycles
            if nd in frontier:
                continue
            new_path = curr_path + nd
            frontier = [new_path] + frontier # append the new path at index 0 to stick to STACK behavior bc DFS based

    return f'No path found from node {source_node} to node {goal_node} with limit {limit}'

test01 = dls(glob_graph.given_graph, 'A', 'G', 2)
print(test01)

test02 = dls(glob_graph.given_graph, 'A', 'G', 4)
print(test02)