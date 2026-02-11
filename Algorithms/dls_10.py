# Prep powrkshop week 13

# Assume you are given the simple integer array [1, 3, 2], and suppose your task is to sort the array
# (ascending or discending order does not matter).

# Assume you want to use a depth-limited search algorithms, what would be a limit guaranteed to
# find a solution?

# Utility Functions
def is_sorted(a_state):
    SORTED_OPTIONS = [(1, 2, 3), (3, 2, 1)] # assending or dessending
    if a_state in SORTED_OPTIONS:
        return True # case where is sorted in one of the ways
    else:
        return False

def get_state_successors(a_state):
    numTuple = a_state
    numList = list(numTuple) # convert it to list to create the successors
    successors = []
    for i in range(0, len(numList) - 1):
        tmp_numList = numList.copy() # create a copy of the list  to avoid original mutation
        tmp_numList[i], tmp_numList[i+1] = tmp_numList[i+1], tmp_numList[i] # this creates variants by swapping adjacent values
        
        successors.append(tuple(tmp_numList))

    return successors # return a list containing multiple tuples of sorting combinations
            

def dls(source_state, limit):
    source_state = tuple(source_state)
    frontier = [(source_state, 0)]  # (state, depth)
    visited = set()

    while frontier != []:
        curr_state, depth = frontier.pop(0)

        if curr_state in visited:
            continue
        visited.add(curr_state)

        if is_sorted(curr_state):
            return (curr_state, depth)

        if depth == limit:
            continue

        for succ in get_state_successors(curr_state):
            if succ in visited:
                continue
            frontier = [(succ, depth + 1)] + frontier  # stack behavior

    return f"No sorted state found for {source_state} with limit {limit}"


test01 = dls([1, 3, 2], 1)
print(test01)