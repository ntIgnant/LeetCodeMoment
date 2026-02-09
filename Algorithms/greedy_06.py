# Vacuum problem with greedy search
# possible initial state -> [1, 0, 1, 0] where 1=dirty room, and 0=clean room
# the initial state is a tuple with two values (vaccum position, rooms)
# To get the heuristic value, h1(goal_state) = 0 !IMPORTANT

# the graph needs to be logic-built, no physical grpah given

def h1(a_state):
    vacPos, rooms = a_state
    heur = 0 # initial value for the heurisitc
    for r in rooms:
        # if the room is dirty, then add cost of 2 to the heuristic
        if r == 1:
            heur += 1

    return heur

def is_goal_state(a_state):
    vacPost, rooms = a_state # (1, (1, 0, 0, 1)) e.g
    if sum(rooms) == 0:
        return True
    return False

def get_state_successors(a_state):
    vacPos, rooms = a_state # unpack the values
    len_rooms = len(rooms)
    successors = [] # all the successor tuples are gonna be appended here

    # Logic for vacuum movement to the left
    if vacPos > 0:
        successors.append((vacPos - 1, rooms))
    
    # Logic for vacuum movement to the right
    if vacPos < len_rooms - 1:
        successors.append((vacPos + 1, rooms))

    # Logic for cleanning depending on vacuum possition | (1, 0, 1, 0) example where 1 = dirty and 0 = clean
    if rooms[vacPos] == 1:
        # create a copy of the tuple rooms as a list | to avoid oritignal tuple mutation for the successors
        new_rooms = list(rooms)
        new_rooms[vacPos] = 0 # 'celan' the specific room
        successors.append((vacPos, tuple(new_rooms))) # append the value as tuple, for set hashing

    return successors # return the list of successors


def greedy_search(source_state):
    # format the values (convert rooms from list to tuple for set hashing)
    vacPos, rooms = source_state
    source_state = (vacPos, tuple(rooms))

    frontier = [(h1(source_state), source_state)]
    visited = set() # visited as set to avoid cycles and duplicants

    while frontier != []:
        # sort the frontier based on the heuristic
        frontier.sort(key=lambda x: x[0])
        curr_heur, curr_state = frontier.pop(0) # unpack the values at index 0

        # check if the goal state was reached
        if is_goal_state(curr_state):
            return (curr_heur, curr_state)

        # else, add the current state to visited to keep track of it and avoid repetitions
        if curr_state in visited:
            continue
        visited.add(curr_state)

        # get the state successors
        state_successors = get_state_successors(curr_state)

        # add the successors to the frontier
        for succ in state_successors:
            if succ in visited:
                continue
            frontier = [(h1(succ), succ)] + frontier

    return 'no path found bruh'


myTest01 = greedy_search((0, [0, 1, 0, 1]))
print(myTest01)