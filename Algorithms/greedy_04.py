# Vacuum problem with greedy search
# possible initial state -> [1, 0, 1, 0] where 1=dirty room, and 0=clean room
# the initial state is a tuple with two values (vaccum position, rooms)
# To get the heuristic value, h1(goal_state) = 0 !IMPORTANT

# the graph needs to be logic-built, no physical grpah given

# Utility Functions
def h1(a_state):
    # so for inution, each dirty room in the rooms has a cost of 2 to clean, so the bigger that value is, the further is to the goal state
    _, rooms = a_state
    heur_val = 0 # initialization of heuristic
    for r in rooms:
        # if room is diry, then count +1 to the heuristic | room with val 1 = dirty room
        if r == 1:
            heur_val += 2 # cost of cleaning a room = 2

    return heur_val

def is_goal_state(a_state):
    vPos, rooms = a_state
    if sum(rooms) == 0:
        return True # this should work, assuming that the goal state is (0, 0, 0, 0)
    return False # case where the rooms are (1, 0, 0, 1) or something like that

def get_state_successors(a_state):
    vacPos, rooms = a_state
    len_rooms = len(rooms) # for boundaries
    succsessors = [] # the succsessors found are gonna be stored here

    # Logic of vacuum movement to the LEFT
    if vacPos > 0:
        # append the new modified version, with the new vacuum possition
        succsessors.append((vacPos - 1, rooms)) # decrease the number to move to the left (as index val)
    
    # Logic for vacuum movement to the RIGHT
    if vacPos< len_rooms - 1:
        # append the new modified verison, with the new vacuum possition
        succsessors.append((vacPos + 1, rooms))

    # Logic for the 'Cleaninig room' action of the vacuum
    if rooms[vacPos] == 1:
        # if the possition of the vacuum in the rooms is 1 (which means dirty, then cleang it, so change to 0)

        new_rooms = list(rooms) # create a 'copy' of rooms to not to mutate the original object
        new_rooms[vacPos] = 0
        succsessors.append((vacPos, tuple(new_rooms)))

    return succsessors # return the list of new fonud states


def greedy_search(source_state):
    # format the values to be hashable for the set (convert list->tuple if there is any)
    vacPos, rooms = source_state
    source_state = (vacPos, tuple(rooms)) # literally just transform the list into a tuple
    frontier = [(h1(source_state), source_state)] # each tuple inside the frontier will be (heuristic val, (vacPos, [rooms]))
    visited = set() # set to store the visited states and avoid repetition (cycles)

    while frontier != []:
        # sort the frontier by priority based on heuristics
        frontier.sort(key=lambda x: x[0]) # sort by the mapped value of frontier at index 0, so HEURISTICS
        curr_heur, curr_state = frontier.pop(0)

        # check if goal state was reached
        if is_goal_state(curr_state):
            return (curr_heur, curr_state)

        # else, check if the current state is in visited, if it's not, then add it to avoid cyles
        if curr_state in visited:
            continue
        visited.add(curr_state) # add the state to the visited to keep track | NOTE: visited is a set

        # get the successor states for upcoming exploration
        curr_state_succ = get_state_successors(curr_state)

        for succ in curr_state_succ:
            # sanity check to avoid cycles
            if succ in visited:
                continue
            # append the new states to 'explore'
            frontier = [(h1(succ), succ)] + frontier # this is STACK behavior,but it doesn't really matter because of the PRIORITY QUEUE based on the heuristics

    return 'Bruh no path found :('


test01 = greedy_search((1, [1, 0, 0, 0]))
print(test01)
