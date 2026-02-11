# library for a heapqueue, which is an implementation of a priority queue
import heapq as hq

# an example of a state
# the first element states the room where the vacuum cleaner is
# the second element represents the rooms where True means there is dirt and False means the room is clean
a_state = (0, [True,True,False,True])


# simple function to create a copy of the rooms array given a state
def copy_rooms(state):
    return state[1][:]

# simple function to create a state given the vaccum position and rooms
def create_state(vacuum_position, rooms):
    return (vacuum_position, rooms)

# the following three functions perform the three actions
# each function returns a triple where
#  - the first element is the cost of the action
#  - the second element is the heuristic value assigned to the state reached after performing the action
#  - the third value is the state reached after performing the action

# function performing the move left action, it takes a state and a heuristic function as input
def move_left(state, heuristic):
    if state[0] == 0:
        return (1, heuristic(state), state)
    new_state = create_state(state[0]-1, copy_rooms(state))
    return (1, heuristic(new_state), new_state)
    
# function performing the move right action, it takes a state and a heuristic function as input
def move_right(state, heuristic):
    last_room = len(state[1])-1
    if state[0] == last_room:
        return (1, heuristic(state), state)
    new_state = create_state(state[0]+1, copy_rooms(state))
    return (1, heuristic(new_state), new_state)
    
# function performing the vacuuming action, it takes a state and a heuristic function as input
def vacuum(state, heuristic):
    if state[1][state[0]]: # check if the room is dirty
        rooms = copy_rooms(state)
        rooms[state[0]] = False
        new_state = create_state(state[0], rooms)
        return (2, heuristic(new_state), new_state)
    return (2, heuristic(state), state)

# function to obtain all possible successors (i.e., the result of performing all actions)
# It takes a state and a heuristic function as input
def get_successors(state, heuristic):
    return [move_left(state, heuristic), move_right(state, heuristic), vacuum(state, heuristic)]


# the usual function to return the last state of a path    
def get_last_state(path):
    return path[-1]


# uncomment and implement the following functions

# your first heuristic function
def h1(state):
    vacPos, rooms = state
    heur_val = 0
    for r in rooms:
        if r == True:
            heur_val += 2 # each dirty room to clean has a cost of 2

    return heur_val

# your second heuristic function
# def h2(state):
#
# the A* algorithm
def a_star(state, heuristic):
    vacPos, rooms = state
    state = vacPos, tuple(rooms) # convert list to tuple
    frontier = []
    hq.heappush(frontier, (0, h1(state), state)) # the second value is the cost (steps)
    visited = set()
    steps = 0 # just to count cow many steps it took till the goal

    while frontier != []:
        steps += 1
        curr_cost, curr_heur, curr_state = hq.heappop(frontier) # unpack the first values in the heap frontier

        # check if the goal state was reached
        if curr_state[1] == (False, False, False, False):
            print(f"Goal state reached after {steps} steps")
            return ((curr_co, curr_heur, curr_state))

        # else, keep exploring new paths
        if curr_state in visited:
            continue
        visited.add(curr_state)

        # get successors states to explore later
        path_succs = get_successors(curr_state, curr_heur)
        # this gives me a list of tuples, where each tuple is a successor

        for tup in path_succs:
            for cos, heur, st in tup:
                if st in visited:
                    continue

                new_cost = curr_cost + cos
                new_heur = h1(st)