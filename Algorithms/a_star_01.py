import heapq as hq

# Exercise: 1D Robot + Batteries

# You have a robot on a 1D line of 4 cells: 0,1,2,3.
# State = (pos, batteries)
# batteries is a length-4 tuple/list of 0/1

# 1 means there is a battery in that cell
# 0 means empty

# Actions:
# Left (cost 1) — if at 0, you stay at 0
# Right (cost 1) — if at 3, you stay at 3
# PickUp (cost 2) — removes a battery at pos if there is one; otherwise does nothing

# Goal: all batteries picked up → batteries all 0
# Robot can be anywhere.

# Utility Functions
def h1(a_state):
    robPos, batts = a_state # unpack the values
    curr_heur = 0 # initialize heuristic variable

    for b in batts:
        # if there is a battery...
        if b == 1:
            curr_heur += 2 # cost of pickup

    return curr_heur

def is_goal_state(a_state):
    robPos, batts = a_state

    # Return True if all the batteries are 0, otherwise return False
    if sum(batts) == 0:
        return True
    return False

def get_state_successors(a_state):
    robPos, batts = a_state
    len_batts = len(batts) # length of the tupe of batteries
    successors = [] # the successors are gonna be appended here

    # logic for left movement of the robot | +1 to the cost of movement
    if robPos > 0:

        successors.append((1, (robPos - 1, batts))) # append the tuple (new state) by deceasing the index of the robot possition by one

    # logic for right movement | +1 to the cost for movement
    if robPos < len_batts - 1:
        successors.append((1, (robPos + 1, batts))) # increase the index of the possition of the robot by one

    # Logic for battery 'pick-up' | +2 to the cost for battery pick-up
    if batts[robPos] == 1:
        # create a copy of the tuple batts, to avoid mutation to the original value (for the next successors)
        new_batts = list(batts)
        new_batts[robPos] = 0 # cahnge the value ot 0 "battery pickup"
        successors.append((2, (robPos, tuple(new_batts)))) # append the robPos and new batteries to the successors (newBatts as TUPLE)
    
    return successors

def a_star(source_state):
    #format the values (list->tuple)
    robPos, batts = source_state
    source_state = (robPos, tuple(batts))

    visited = set() # set to keep track of the visited states to avoi cyles (duplicated states)
    frontier = []
    steps = 0 # conter to count how many steps it took till the goal_state

    # Initialize the frontier with cost 0, so (heur, cost, state)
    hq.heappush(frontier, (h1(source_state), 0, source_state)) # Heap push just accepts two args (source_heap, value)

    while frontier != []:
        steps += 1 # add 1 step to the counter of steps

        curr_heur, curr_cost, curr_state = hq.heappop(frontier) # pop the fist (index 0) value of the heap (heap = priority queue)

        # check if the goal state was reached
        if is_goal_state(curr_state):
            print(f"Goal State reached after {steps} steps")
            return (curr_heur, curr_cost, curr_state)

        # check if the current state is in visited, if it isn't add it to the set
        if curr_state in visited:
            continue
        visited.add(curr_state)

        # else, keep discovering new paths
        succs = get_state_successors(curr_state) # so this should return (operation cost, (robPos, batts))

        for opCost, succStates in succs:
            # sanity check to avoid cyles
            if succStates in visited:
                continue
            newCost = curr_cost + opCost # create a new cost to append to the frontier heap
            newHeur = curr_heur + h1(succStates) # create a new heuristic value to append to the frontier heap
            hq.heappush(frontier, (newHeur, newCost, succStates))

    print("No goal state reached :(")
    return None # case where no goal state was found

test01 = a_star((1, [1, 0, 0, 1]))
print(test01)