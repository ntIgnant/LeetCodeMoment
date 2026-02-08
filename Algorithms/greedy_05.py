# Vacuum problem with greedy search
# possible initial state -> [1, 0, 1, 0] where 1=dirty room, and 0=clean room
# the initial state is a tuple with two values (vaccum position, rooms)
# To get the heuristic value, h1(goal_state) = 0 !IMPORTANT

# the graph needs to be logic-built, no physical grpah given

# Utility Functions
def h1(a_state):
    vacPos, rooms = a_state
    heurisitc_val = 0 # initialize th heurisitc value

    for r in rooms:
        if r == 1:
            heurisitc_val += 2 # add up cost of 2, if there is a dirty room
    
    return heurisitc_val

def is_goal_reached(a_state):
    vacPos, rooms = a_state
    if sum(rooms) == 0:
        return True # assuming that the goal state is that all the rooms are cleaned, so all the values as 0
    return False

def get_state_successors(a_state):
    vacPos, rooms = a_state # unpack the values
    len_rooms = len(rooms)
    successors = [] # list where the successor tupples are gonna be stored

    # logic when the vacuum moves to the left
    if vacPos > 0:
        successors.append((vacPos - 1, rooms))

    # logic when the vauum moves to the right
    if vacPos < len_rooms - 1:
        successors.append((vacPos + 1, rooms)) # increase the index of the vauum by one

    # logic for the vacuum to cleaaaaaaaaaan
    if rooms[vacPos] == 1:
        # Create a copy of the rooms, for not to mutate the original rooms fo the future successors
        new_rooms = list(rooms)
        new_rooms[vacPos] = 0 # this is the 'cleaning' action
        successors.append((vacPos, tuple(new_rooms))) # append the vacuum position and new rooms as tuple
    
    return successors


def greedy_search(source_state):
    # format the vlues of the given state a stuples, to be hashable for the set() visited
    vacPos, rooms = source_state
    source_state = (vacPos, tuple(rooms))
    frontier = [(h1(source_state), source_state)] # frontier will store (heuristic, state) | where state = (vacuum possition, (rooms))
    visited = set() # store the visited states here | set to avoid duplicatns, so cycles

    while frontier != []:
        # sort the frontier by mapping at the heuristic value (index 0 of the frontier)
        frontier.sort(key=lambda x: x[0]) # map, per each item of the frontier, the index 0 of THAT item
        # unpack the values
        curr_heur, curr_state = frontier.pop(0)

        # check if the goal state was reached
        if is_goal_reached(curr_state):
            return (curr_heur, curr_state) # return the heurisitc value and sthe state

        # if there is no goal state reached, add the state to the set to keep track, then continue exporing
        if curr_state in visited:
            continue
        visited.add(curr_state) # add the state to avoid cycles

        # keep discovering new states (to be explored in the future)
        curr_state_succ = get_state_successors(curr_state)

        for succ in curr_state_succ:
            if succ in visited:
                continue
            frontier = [(h1(succ), succ)] + frontier # append the successor to the index 0 of the frontier (this is kinda useless bc of priority queue behaviour based on the heurisit)

    return 'Bruh no path found'


test01 = greedy_search((1, [1, 0, 0, 0]))
print(test01)