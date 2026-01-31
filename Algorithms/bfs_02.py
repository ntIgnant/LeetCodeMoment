# graph representation
my_graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}


# utility function to get the successors of the current node
def get_successors(graph, node):
    return graph[node]

def bfs(graph, source_node, goal_node):

    # First create where the values are going to get store
    exp_paths = set()
    frontier = [source_node] # the frontier is initialized with the source node (initial node)
    parent = {source_node: None} # parent dictionary to get the path once the goal node is reached | 'root' (CHILD, PARENT)

    while frontier:
        tmp_node = frontier.pop(0) # pop the left-most value (bc bfs is queue based) | assuming that the index -1 is the tail of the list
        exp_paths.add(tmp_node) # add the current node to the explored paths

        # get the patth if goal node is reached
        if tmp_node == goal_node:
            # now build the path to the found goal node
            path = []
            iter_node = goal_node # this variable is gonna be used as an iterative goal in the dictionary of the paths

            while iter_node != None:
                path.append(iter_node)
                iter_node = parent[iter_node] # the new node is the parent of the iter node (current node)

            # Once the iter_node reached none, meaning reached the root, reverse the path to get the real path
            path.reverse()
            return path


        tmp_node_successors = get_successors(graph, tmp_node)

        for nd in tmp_node_successors:
            if nd not in exp_paths and nd not in parent:
                exp_paths.add(nd)
                parent[nd] = tmp_node # record who discovered the new tmp node
                frontier.append(nd)

    return False # case where there was no path found

test_path = bfs(my_graph, 'A', 'E')
print(test_path)