deep_graph = {
    'A': ['B', 'X'],
    'B': ['C'],
    'C': ['D', 'Y'],
    'D': ['E'],
    'E': ['F'],
    'F': ['G'],
    'G': ['H'],
    'H': ['I', 'Z'],
    'I': ['J'],
    'J': ['K'],
    'K': ['L'],
    'L': ['M'],
    'M': [],
    'X': [],
    'Y': [],
    'Z': []
}


# Implement Depth Limited Search (DLS) searching algorithm to find a path from node A to node
# DLS or Depth Limited search has also queue as underlying data struct | similar to BFS but with progressive eveling

# Utility Functions
def get_last_node(a_path): return a_path[-1] # return the last element of the path | in this case the last char in the str 

def get_successors(a_graph, a_node):
    # check if the node is one of the keys in the dictionary graph
    if a_node in a_graph.keys():
        return a_graph[a_node] # if yes, return the values of the requested key of the dict 'graph'
    else:
        return [] # else return an empty list, meaning it's a leaf

def depth_limited_search(graph, source_node, goal_node, max_depth):
    paths = [source_node] # the frontier starts the same as BFS and DFS | here is where the explored (not visited) paths are gonna be stored

    while paths != []:
        current_path, paths = paths[0], paths[1:] # assign the current path to visit (index 0), and update the 'to explore' paths with 1:0 list slising

        # get the last node of the current path to check if it's the goal node
        path_last_node = get_last_node(current_path)

        # check if the last node is the goal node
        if path_last_node == goal_node:
            return current_path # if yes, return the path where the node was found
        
        # else keep exploring paths, so increase the level of depth
        current_depth = len(current_path) - 1 # depth of a path = number of edges = len(path) - 1

        # check fi the maximum depth was reached
        if current_depth == max_depth:
            continue # if the limit was reached, don't keep expaning the path

        # increase de depth by exploring the next level
        last_node_succ = get_successors(graph, path_last_node)

        for nd in last_node_succ:
            # Quick verification to avoid cyclic paths (repetition of nodes in paths)
            if nd in current_path:
                continue
            new_path = current_path + nd # create a new explored path (not visited yet)
            paths = paths + [new_path] # append the new path at the end to have a QUEUE BEHAVIOR because Depth limited search is BFS based

    return f'No path found from {source_node} to {goal_node}'
    

print('dls (limit 3):', depth_limited_search(deep_graph, 'A', 'F', 3))
print('dls (limit 5):', depth_limited_search(deep_graph, 'A', 'F', 5))

#OoOOOOooooooooOOOOOOoo