# Workshop 12 | task breath first search
given_graph = {'a':['b', 'c', 'd'],
               'b':['e'],
               'c':['e'],
               'd':['e'],
               'e':['f'],
               'f':[]}

# Now, Implement bfs to get from node a to node f

# utility fuctions
def get_last_node(a_path): return a_path[-1]

def get_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []


def bfs(graph, source_node, goal_node):
    frontier = [source_node]

    while frontier != []:
        current_path, frontier = frontier[0], frontier[1:]

        # check if the goal node was reached
        path_last_node = get_last_node(current_path)

        # compare it with the goal node
        if path_last_node == goal_node:
            return current_path
        
        #else, keep discovering new paths

        last_node_succ = get_successors(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            new_path = current_path + nd
            frontier = frontier + [new_path] # append the new path at the end of the frontier | to have a QUEUE BEHAVIOUR

    return f"no path found from {source_node} to {goal_node}"


# depth first search (just change STACK BEHAVIOUR) compared to bfs
def dfs(graph, source_node, goal_node):
    frontier = [source_node]

    while frontier != []:
        current_path, frontier = frontier[0], frontier[1:]

        # check if the goal node was reached
        path_last_node = get_last_node(current_path)

        # compare it with the goal node
        if path_last_node == goal_node:
            return current_path
        
        #else, keep discovering new paths

        last_node_succ = get_successors(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            new_path = current_path + nd
            frontier = [new_path] + frontier # append the new path at the index 0 to hvee STACK BEHAVIOUR for the dfs

    return f"no path found from {source_node} to {goal_node}"


test_bfs = bfs(given_graph, 'a', 'f')
print(test_bfs)

test_dfs = dfs(given_graph, 'a', 'f')
print(test_dfs)