# Vacuum problem with greedy search
# possible initial state -> [1, 0, 1, 0] where 1=dirty room, and 0=clean room
# the initial state is a tuple with two values (vaccum position, rooms)
# To get the heuristic value, h1(goal_state) = 0 !IMPORTANT

# the grpah needs to be logic-built, no physical grpah given

# Utility Functions
def h1(state):
    vac_pos, rooms = state  # rooms is a tuple of 0/1
    # vacuuming cost is 2 per dirty room (your heuristic definition)
    return 2 * sum(rooms)


def get_successor_state(state):
    vac_pos, rooms = state
    room_len = len(rooms)
    successors = []

    # move left
    if vac_pos > 0:
        successors.append((vac_pos - 1, rooms))

    # move right
    if vac_pos < room_len - 1:
        successors.append((vac_pos + 1, rooms))

    # vacuum (only changes state if current room is dirty)
    if rooms[vac_pos] == 1:
        new_rooms = list(rooms)
        new_rooms[vac_pos] = 0
        successors.append((vac_pos, tuple(new_rooms)))

    return successors


def greedy_search(source_state, goal_state):
    # frontier stores (heuristic, state)
    frontier = [(h1(source_state), source_state)]
    visited = set()

    while frontier:
        # priority queue behavior by heuristic (same pattern as your UCS sorting by cost)
        frontier.sort(key=lambda x: x[0])
        curr_h, curr_state = frontier.pop(0)

        if curr_state == goal_state:
            return (curr_h, curr_state)

        if curr_state in visited:
            continue
        visited.add(curr_state)

        for succ in get_successor_state(curr_state):
            if succ in visited:
                continue
            frontier = [(h1(succ), succ)] + frontier

    return "No path found"


start = (1, (1, 0, 1, 0))      # vacuum at index 1
goal  = (0, (0, 0, 0, 0))      # or any (pos, all_clean) depending on your goal definition
print(greedy_search(start, goal))

