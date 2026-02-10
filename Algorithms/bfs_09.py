import glob_graph # I'll just get the graph from here

# Implement a BFS (bread first search) algorithm to find a the shortes path by number of nodes
# path from node 'A' to node 'G'

# Utility Functions
def get_last_node(a_path): return a_path[-1] # return the last character of the path (last node)

def get_path_successors(a_node, a_graph):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    return [] # return empty list if the path has no successors (leaf case)

def bfs(graph, source_node, goal_node):
    frontier = [source_node] # append the initial node to the frontier | each node = (char, cost)
    visited = set() # set to avoid cyles

    while frontier != []:
        curr_path = frontier.pop(0) # pop the fist value (index 0) as the current path reference

        # get the last node of the path, to verify if destination was reached (goal_node)
        path_last_node = get_last_node(curr_path)

        # verify ig goal_node was reached
        if path_last_node == goal_node:
            print("Goal node reached!")
            return (curr_path)

        # else, keep discovering paths
        last_node_succ = get_path_successors(path_last_node, graph)

        for char, cost in last_node_succ:
            newPath = curr_path + char # this is probably wrong ngl
            # add the path to the frontier (INPORTANT: Make it so it has QUEUE behavior bc BFS)
            frontier = frontier + [newPath]

    return f"Couldn't Get from node {source_node} to node {goal_node}"

test01 = bfs(glob_graph.given_graph, 'A', 'G')
print(test01)