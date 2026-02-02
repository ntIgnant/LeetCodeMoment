import bfs_07

test_grph = {
    "a": ["c", "b"],
    "b": ["d"],
    "d": ["e"],
    "e": ["f"],
    "c": ["f"],
    "f": []
}



# Implement a Depth-Fist-Search (DFS) algorithm to search a path from a to g


# Utility functions
def get_last_node(a_path): return a_path[-1]

def get_successors(a_graph, a_node):
    if a_node in a_graph.keys():
        return a_graph[a_node]
    else:
        return []

def dfs(graph, source_node, goal_node):
    paths = [source_node]

    while paths != []:
        current_path, paths = paths[0], paths[1:]

        # get the last node of the current path
        path_last_node = get_last_node(current_path)

        if path_last_node == goal_node:
            return current_path
        
        # else, keep exploring new possible paths
        last_node_succ = get_successors(graph, path_last_node)

        for nd in last_node_succ:
            if nd in current_path:
                continue
            new_path = current_path + nd

            # now, append the new path to the index 0 of the list of paths, to have STACK BEHAVIOUR
            paths = [new_path] + paths

    return f'No path found from {source_node} to {goal_node}'

# Comparision with breath-first search
test01 = bfs_07.bfs(test_grph, 'a', 'f')

test02 = dfs(test_grph, 'a', 'f')

print(f'BFS result: {test01}')
print(f'DFS result: {test02}')