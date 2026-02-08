# Vacuum problem with greedy search
# possible initial state -> [1, 0, 1, 0] where 1=dirty room, and 0=clean room
# the initial state is a tuple with two values (vaccum position, rooms)
# To get the heuristic value, h1(goal_state) = 0 !IMPORTANT

# the graph needs to be logic-built, no physical grpah given

# Utility Functions
def h1(a_state):
    vacPos, rooms = a_state
    heur_val = 0

    # iterate over all the rooms, each room is either 1 (dirty), or 0 (clean)
    for r in rooms:
        if r == 1:
            heur_val += 2 # cost of cleaninig is of 2

    return heur_val

def is_goal(a_state):
    # this is the goal state
    _, rooms = a_state
    if rooms == (0, 0, 0, 0):
        return True
    return False

def get_state_successors(a_state):
    # so the basic logic here is to move the vacuum t adjacent rooms
    vacPos, rooms = a_state
    lenRooms = len(rooms)
    successors = [] # list of found 'new' states

    # Logic for vacuum movement - LEFT
    if vacPos > 0:
        successors.append((vacPos - 1, rooms)) # decrease the index of the vacuum possition by 1

    # Logic for vacuum movement - RIGHT
    if vacPos < lenRooms - 1:
        successors.append((vacPos + 1, rooms)) # increase the index of the vacuum possition by 1

    # Logic for the cleaning (depending on vacuum possition)
    if rooms[vacPos] == 1:
        new_rooms = list(rooms) # create a 'copy' as a list of rooms to create a new variant
        new_rooms[vacPos] = 0 # do the 'celaninig' by assigning 0 to the index

        successors.append((vacPos, tuple(new_rooms))) # add the new variant to the successors

    return successors
    

def greedy_search(source_state):
    vacPos, rooms = source_state
    source_state = (vacPos, tuple(rooms)) # convert the list for the rooms as a tuple t have it as hashable object for the set
    frontier = [(h1(source_state), source_state)]
    visited = set() # set of visited states to avoid cycles

    while frontier != []:
        # heuristic = (e.g 5)
        # srouce_state = (vacPos, [rooms]) where rooms is e.g [1, 0, 0, 1]

        # sort the frontier based on the heuristic values (priority queue heuristic vals)
        frontier.sort(key=lambda x: x[0])

        curr_heur, curr_state = frontier.pop(0)

        # check if the goal state was reached
        if is_goal(curr_state):
            return (curr_heur, curr_state)
        # else, add the current state to the visited set to keep track
        if curr_state in visited:
            continue
        visited.add(curr_state)

        # else, get the next states to keep exploring
        curr_state_succ = get_state_successors(curr_state)

        for succ in curr_state_succ:
            # sanity check to avoid cyles
            if succ in visited:
                continue

            frontier = [(h1(succ), succ)] + frontier # append the heuristic result + succesor state to the frontier as a tuple
            # keep the stack based behavior (even though it's a riority queue so does't really matter ngl)

    return "No path found Mud :("

test01 = greedy_search((1, [1, 0, 1, 0]))
print(test01)