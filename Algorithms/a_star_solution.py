# library for a heapqueue, which is an implementation of a priority queue
import heapq as hq

# an example of a state
# the first element indicates the room where the vacuum cleaner is
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



# first heuristic returning the number of dirty rooms
def h1(state):
    count = 0
    for r in state[1]:
        if r:
            count += 1
    return count


# assumption for the following three functions: there is at least one dirty room
# the assumption follows from the implementation of h2
def get_first_left(state):
    for i in range(len(state[1])):
        if state[1][i]:
            return i

def get_first_right(state):
    for i in range(len(state[1])-1,-1,-1):
        if state[1][i]:
            return i

def max_distance(state):
    left = get_first_left(state)
    right = get_first_right(state)
    
    return max(abs(right - state[0]), abs(state[0]-left))
    

# second heuristic, it uses the three functions above
def h2(state):
    dirty_rooms = h1(state)
    if dirty_rooms == 0:
        return dirty_rooms
    
    furtherst_room = max_distance(state)
    return dirty_rooms + furtherst_room


# implementation of A*
def a_star(state, heuristic):
    frontier = []
    steps = 0 # varable to count the steps needed to find a solution

    # pushing the first state on the queue
    # the first element represents the overall estimated cost (i.e., cost of the path so far + heuristic last state)
    # the second element is a triple where
    #  - the first element is the heuristic value of the last state on the path
    #  - the second element is the cost of the path
    #  - the third element is the path itself
    hq.heappush(frontier, (heuristic(state), (heuristic(state), 0, [state])))
    
    while frontier != []:
        steps += 1

        # get the most promising path from the queue
        overall, (h_value, path_cost, path) = hq.heappop(frontier)

        # check if we reached the goal state by checking the heuristic value
        if h_value == 0:
            print("Solution found after", steps, "steps")
            return (path_cost, path)

        # get all possible successors to expand the current path
        successors = get_successors(get_last_state(path), heuristic)

        # create all possible extensions of the current path and push them on the queue
        for action_cost, new_h_value, next_state in successors:
            new_path = path[:] + [next_state]
            new_path_cost = path_cost + action_cost
            overall_cost = new_path_cost + new_h_value
            hq.heappush(frontier, (overall_cost, (new_h_value, new_path_cost, new_path)))
    
