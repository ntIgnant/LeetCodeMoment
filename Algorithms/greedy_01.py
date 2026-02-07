# Vacuum problem with heuristics (informed search) and Greedy search algorithm
# Important Info:
# The 'cleanning' of the room has a cost of 2
# The adjacent movement has a cost of 1
# Example initial state: [1, 0, 1, 0] | here each 0 is 'clean room', and 1 means 'dirty room'
# Also, the graph should be build logically, there is no physical given graph...

# IMPORTANT:
# for heuristics, we build a 'path to nearest soution' based on given information,
# so when the goal state is reached, the heuristic = 0 ALWAYS

# For the input state, there should exist two things (current index of vacuum, [state of rooms])

# Utility Functions

def h1(a_state):
    # so the intuiton here is that each '1' in the state of [1, 0 , 1, 0] has a cost of 2, while the clean room has a cost of 0
    total_heuristic = 0 # initial value for the heuristic
    for room in a_state:
        if room == 1:
            total_heuristic += 2 # add up '2' if the room is dirty
    
    return total_heuristic

def get_state_succsessors(a_state):
    vac_pos, room_state = a_state # assign the variable vals using list unpacking

    # as the orginal state hould be unmutable, we conver it to tuple
    room_state = tuple(room_state)
    len_rooms = len(room_state)

    successors = [] # there is weher all the succsessors are gonna be stored
    # each element of the successors will be a tuple with this structure:
    # ((vacuum pos, room state), "MOVE DIRECTION", cost of move)

    # Scenario where the vacuum needs to move to the left
    if vac_pos > 0:
        successors.append(((vac_pos - 1, room_state), "LEFT", 1))

    # Scenario where the vacuum needs to move to the right
    if vac_pos < n -1:
        successors.append(((vac_pos + 1, room_state), "RIGHT", 1))


    # Scenario where the room needs to be vacuumed
    if room_state[vac_pos] == 1:
        # Create a copy of the room state (the original cannot be modified)
        new_room_state = list(room_state)
        new_room_state[vac_pos] = 0 # perform vacuum action | 0 = clean room
        successors.append(((vac_pos, tuple(new_room_state)), "VACUUM", 2))

    return successors



# in this problem, instead of nodes we have states of the rooms, such as [1, 0, 1, 0] or [1, 0, 0, 0], etc...
def greedy_search(source_state, goal_state):
    # the frontier should be a list of vales like these -> [5, [1, 0, 1, 0]], so [heuristic, [state]]
    frontier = [(h1(source_state), source_state, [], 0)] # the structure of the tuple whould be (heuristic, path)
    visited = set() # the visited states are gonna be here in form of set to avoid duplicants

    while frontier != []:
        # sort the frontier to have the cheapest cost firs (based on heuristics)
        frontier.sort(key=lambda x: x[0]) # sort by the value index 0 of the tuple, so the heuristic val
        curr_heur, curr_state, action, operation_cost = frontier.pop(0) # pop the left-most value, and assign it to current state using tuple unpacking

        # chekc if the goal state was reached
        # curr_state is gonna be something like [3, [1, 0, 0, 1]] where the first value is the current possition of the vacuum
        if curr_state == goal_state:
            return (curr_heur, curr_state, action, operation_cost)

        # else, get the next state to keep exploring
        curr_state_succ_tuple = get_state_succsessors(curr_state)

        curr_state_succ = curr_state_succ_tuple[0] # this will get a tuple with (vacuum pos, (state))

        for state, act, opCost in curr_state_succ:
            if state in visited:
                continue
            frontier.append(h1(state), state, act, opCost)