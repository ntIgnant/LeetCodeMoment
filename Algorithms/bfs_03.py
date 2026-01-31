my_graph = {'a': ['b', 'c', 'd'], 'b': ['e'], 'c':['e'], 'd':['e'], 'e':['f'], 'f':[]}

# Implement a bfs search from the node a -> f

# Utility fucntion to get the successors of a node
def get_successors(graph, node):
    return graph[node]

def bfs(graph, source_node, goal_node):

    exp_nodes = set() # nodes that were visited
    frontier = [source_node] # initialization of frontier with the source node 'root'
    parent = {source_node: None} # used to recreate the path at the end (child, parent) exact one value each

    while frontier:
        tmp_node = frontier.pop(0) # pop left-most value (queue for bfs)
        exp_nodes.add(tmp_node) # add current node to the explored nodes

        if tmp_node == goal_node:
            # Recreate the path to the goal node
            path = []
            iter_node = goal_node # node that will work as an iterator in the parent dictionary
            
            while iter_node != None:
                path.append(iter_node) # store the current node in the path list
                iter_node = parent[iter_node]

            path.reverse() # reverse the path | f->e->c->a --->> a->c->e->f
            return path
        
        node_successors = get_successors(graph, tmp_node)

        for nd in node_successors:
            if nd not in exp_nodes and nd not in parent:
                exp_nodes.add(nd)
                parent[nd] = tmp_node # so as the structure here is (child, parent) | this will be (nd, tmp_node)
                frontier.append(nd) # append the node to explore the path later
    
    return False # case where no path was found


test_path = bfs(my_graph, 'a', 'f')
test_path2 = bfs(my_graph, 'd', 'f')
test_path3 = bfs(my_graph, 'a', 's')

print(test_path)
print(test_path2)
print(test_path3)