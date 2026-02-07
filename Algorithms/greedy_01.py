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

def get_next_state(a_state):
    vac_pos, room_state = a_state # assign the variable vals using list unpacking

    # as the orginal state hould be unmutable, we conver it to tuple
    room_state = tuple(room_state)


# in this problem, instead of nodes we have states of the rooms, such as [1, 0, 1, 0] or [1, 0, 0, 0], etc...
def greedy_search(source_state, goal_state):
    # the frontier should be a list of vales like these -> [5, [1, 0, 1, 0]], so [heuristic, [state]]
    frontier = [(h1(source_state), source_state)] # the structure of the tuple whould be (heuristic, path)

    while frontier != []:
        # sort the frontier to have the cheapest cost firs (based on heuristics)
        frontier.sort(key=lambda x: x[0]) # sort by the value index 0 of the tuple, so the heuristic val
        curr_heur, curr_state = frontier.pop(0) # pop the left-most value, and assign it to current state using tuple unpacking

        # chekc if the goal state was reached
        # curr_state is gonna be something like [3, [1, 0, 0, 1]] where the first value is the current possition of the vacuum
        if curr_state[1] == goal_state:
            return (curr_heur, curr_state)

        # else, get the next state to keep exploring
        next_state = get

