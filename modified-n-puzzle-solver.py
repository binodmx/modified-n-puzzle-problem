import sys

# define file names
start_conf_file_name = sys.argv[1]
goal_conf_file_name = sys.argv[2]
output_file_name = "Output.txt"

# read from input files 
start_configuration = []
goal_configuration = []

fo = open(start_conf_file_name, "r")
lines = fo.readlines()
for line in lines:
    start_configuration.append(line.strip().split())
fo.close()

fo = open(goal_conf_file_name, "r")
lines = fo.readlines()
for line in lines:
    goal_configuration.append(line.strip().split())
fo.close()

size = len(start_configuration)

# return hamming distance (number of misplaced tiles)
def hamming_distance(configuration):
    total = 0
    for row in range(size):
        for col in range(size):
            if goal_configuration[row][col] != configuration[row][col]:
                total += 1
    return total
    
# return manhattan distance
def manhattan_distance(tile, r, c):
    if tile == '-':
        return 0
    for row in range(size):
        for col in range(size):
            if goal_configuration[row][col] == tile:
                return abs(row - r) + abs(col - c)

# return total manhattan distance
def total_manhattan_distance(configuration):
    total_manhattan_distance = 0
    for r in range(size):
        for c in range(size):
            total_manhattan_distance += manhattan_distance(configuration[r][c], r, c)
    return total_manhattan_distance

# heuristic value --> return total manhattan distance or hamming distance
def h(n):
    return total_manhattan_distance(n)
    #return hamming_distance(n)

class State:
    def __init__(self, configuration, parent, g):
        self.configuration = configuration
        self.parent = parent
        self.g = g
        self.h = h(configuration)        

    def f(self):
        return self.g + self.h

OPEN = [State(start_configuration, None, 0)]
CLOSED = []

# return the state in OPEN which has the minimum f value
def get_initial_state():
    min_state = OPEN[0]
    min_f = OPEN[0].f()
    for state in OPEN[1:]:
        if state.f() < min_f:
            min_state = state
            min_f = state.f()
    return min_state

# return the state in OPEN which has the same configuration given in parameter
def get_open_state(state):
    for open_state in OPEN:
        if open_state.configuration == state.configuration:
            return open_state
        
# return possible next states
def next_states(current_state):
    blank_tile1 = None
    blank_tile2 = None
    states = []
    
    for row in range(size):
        for col in range(size):
            if current_state.configuration[row][col] == '-':
                if blank_tile1 == None:
                    blank_tile1 = (row, col)
                else:
                    blank_tile2 = (row, col)
    
    if blank_tile1[0] - 1 >= 0 and current_state.configuration[blank_tile1[0]-1][blank_tile1[1]] != '-':
        temp_conf = [x[:] for x in current_state.configuration]
        temp_conf[blank_tile1[0]][blank_tile1[1]], temp_conf[blank_tile1[0]-1][blank_tile1[1]] = temp_conf[blank_tile1[0]-1][blank_tile1[1]], temp_conf[blank_tile1[0]][blank_tile1[1]]
        states.append(State(temp_conf, current_state, current_state.g + 1))
    if blank_tile1[0] + 1 <= (size-1) and current_state.configuration[blank_tile1[0]+1][blank_tile1[1]] != '-':
        temp_conf = [x[:] for x in current_state.configuration]
        temp_conf[blank_tile1[0]][blank_tile1[1]], temp_conf[blank_tile1[0]+1][blank_tile1[1]] = temp_conf[blank_tile1[0]+1][blank_tile1[1]], temp_conf[blank_tile1[0]][blank_tile1[1]]
        states.append(State(temp_conf, current_state, current_state.g + 1))
    if blank_tile1[1] - 1 >= 0 and current_state.configuration[blank_tile1[0]][blank_tile1[1]-1] != '-':
        temp_conf = [x[:] for x in current_state.configuration]
        temp_conf[blank_tile1[0]][blank_tile1[1]], temp_conf[blank_tile1[0]][blank_tile1[1]-1] = temp_conf[blank_tile1[0]][blank_tile1[1]-1], temp_conf[blank_tile1[0]][blank_tile1[1]]
        states.append(State(temp_conf, current_state, current_state.g + 1))
    if blank_tile1[1] + 1 <= (size-1) and current_state.configuration[blank_tile1[0]][blank_tile1[1]+1] != '-':
        temp_conf = [x[:] for x in current_state.configuration]
        temp_conf[blank_tile1[0]][blank_tile1[1]], temp_conf[blank_tile1[0]][blank_tile1[1]+1] = temp_conf[blank_tile1[0]][blank_tile1[1]+1], temp_conf[blank_tile1[0]][blank_tile1[1]]
        states.append(State(temp_conf, current_state, current_state.g + 1))

    if blank_tile2[0] - 1 >= 0 and current_state.configuration[blank_tile2[0]-1][blank_tile2[1]] != '-':
        temp_conf = [x[:] for x in current_state.configuration]
        temp_conf[blank_tile2[0]][blank_tile2[1]], temp_conf[blank_tile2[0]-1][blank_tile2[1]] = temp_conf[blank_tile2[0]-1][blank_tile2[1]], temp_conf[blank_tile2[0]][blank_tile2[1]]
        states.append(State(temp_conf, current_state, current_state.g + 1))
    if blank_tile2[0] + 1 <= (size-1) and current_state.configuration[blank_tile2[0]+1][blank_tile2[1]] != '-':
        temp_conf = [x[:] for x in current_state.configuration]
        temp_conf[blank_tile2[0]][blank_tile2[1]], temp_conf[blank_tile2[0]+1][blank_tile2[1]] = temp_conf[blank_tile2[0]+1][blank_tile2[1]], temp_conf[blank_tile2[0]][blank_tile2[1]]
        states.append(State(temp_conf, current_state, current_state.g + 1))
    if blank_tile2[1] - 1 >= 0 and current_state.configuration[blank_tile2[0]][blank_tile2[1]-1] != '-':
        temp_conf = [x[:] for x in current_state.configuration]
        temp_conf[blank_tile2[0]][blank_tile2[1]], temp_conf[blank_tile2[0]][blank_tile2[1]-1] = temp_conf[blank_tile2[0]][blank_tile2[1]-1], temp_conf[blank_tile2[0]][blank_tile2[1]]
        states.append(State(temp_conf, current_state, current_state.g + 1))
    if blank_tile2[1] + 1 <= (size-1) and current_state.configuration[blank_tile2[0]][blank_tile2[1]+1] != '-':
        temp_conf = [x[:] for x in current_state.configuration]
        temp_conf[blank_tile2[0]][blank_tile2[1]], temp_conf[blank_tile2[0]][blank_tile2[1]+1] = temp_conf[blank_tile2[0]][blank_tile2[1]+1], temp_conf[blank_tile2[0]][blank_tile2[1]]
        states.append(State(temp_conf, current_state, current_state.g + 1))
        
    return states

# get move between two given states
def get_move(from_state, to_state):
    move = "("
    for row in range(size):
        for col in range(size):
            if from_state.configuration[row][col] != to_state.configuration[row][col] and from_state.configuration[row][col] != '-':
                move += from_state.configuration[row][col]+","
                if row-1 >= 0 and from_state.configuration[row][col] == to_state.configuration[row-1][col]:
                    move += "up)"
                if row+1 <= (size-1) and from_state.configuration[row][col] == to_state.configuration[row+1][col]:
                    move += "down)"
                if col-1 >= 0 and from_state.configuration[row][col] == to_state.configuration[row][col-1]:
                    move += "left)"
                if col+1 <= (size-1) and from_state.configuration[row][col] == to_state.configuration[row][col+1]:
                    move += "right)"
                break       
    return move

# return the total path
def reconstruct_path(current_state):
    total_path = []
    while current_state.parent != None:
        total_path.append(get_move(current_state.parent, current_state))
        current_state = current_state.parent
    total_path.reverse()
    return total_path

# check whether given state is in OPEN
def is_in_OPEN(state):
    for open_state in OPEN:
        if open_state.configuration == state.configuration:
            return True
    return False

# check whether given state is in CLOSED 
def is_in_CLOSED(state):
    for closed_state in CLOSED:
        if closed_state.configuration == state.configuration:
            return True
    return False

# A* search
def A():                
    while len(OPEN) > 0:
        current_state = get_initial_state()
        if current_state.configuration == goal_configuration:
            return reconstruct_path(current_state)
        OPEN.remove(current_state)
        CLOSED.append(current_state)
        for next_state in next_states(current_state):
            if is_in_CLOSED(next_state):
                continue
            if not(is_in_OPEN(next_state)):
                OPEN.append(next_state)
            else:
                open_state = get_open_state(next_state)
                if next_state.g < open_state.g:
                    open_state.g = next_state.g
                    open_state.parent = next_state.parent

# write to output file
fo = open(output_file_name, "w")
PATH = A()
fo.write(", ".join(PATH))
fo.close()

