# Tryout of Breath First Search uninformed search algorithm

# Example of a graph (unweighted for bfs)

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': [],
    'E': []
}

def get_sucessors(graph, node):
    return graph[node]

def bfs(graph, source_node, goal_node):

    exp_paths = set() # explored paths | this is a set to AVOID duplicants
    frontier = [source_node] # discovered new paths (to be expanded)
    parent = {source_node: None} # dictionary to store the paths as parent and child

    while frontier:
        tmp_node = frontier.pop(0) # the leftmost value because has Queue as Underlying data Struct
        

        # Reconstruct the path from dictionary and retur it (need to revise this shit)
        if tmp_node == goal_node:
            path = [] # to reconstruct the path
            node = goal_node
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path

        # This is just for verification that the current node was 'transfered' to the explored paths | prevents duplicants (but is a set so xd)
        if tmp_node in exp_paths:
            continue

        exp_paths.add(tmp_node) # add the current node to the explored paths set

        # Verify if the current node is the goal_node
        if tmp_node == goal_node:
            return True
        
        tmp_node_successors = get_sucessors(graph, tmp_node) # get the successors of the current node (expanded node)

        for nd in tmp_node_successors:
            if nd not in exp_paths:
                frontier.append(nd)

    return False