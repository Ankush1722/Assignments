from collections import deque

# Define the initial and final states
initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
final_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]

# Function to check if two states are equal
def is_equal(state1, state2):
    for i in range(3):
        for j in range(3):
            if state1[i][j] != state2[i][j]:
                return False
    return True

# Function to generate the possible next states from the current state
def generate_next_states(state):
    next_states = []
    zero_pos = None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_pos = (i, j)
                break
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Possible moves: right, left, down, up
    for move in moves:
        new_state = [row[:] for row in state] # Create a copy of the current state
        new_row = zero_pos[0] + move[0]
        new_col = zero_pos[1] + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state[zero_pos[0]][zero_pos[1]] = new_state[new_row][new_col]
            new_state[new_row] [new_col] = 0
            next_states.append(new_state)

    return next_states

# Breadth-first search algorithm to find the optimal solution
def bfs(initial_state, final_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(map(tuple, current_state)))

        if is_equal(current_state, final_state):
            return path

        next_states = generate_next_states(current_state)
        for next_state in next_states:
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [next_state]))
    return None

# Solve the 8-puzzle problem
solution = bfs(initial_state, final_state)

# Print the solution
if solution is None:
    print("No solution found.")
else:
    print("Solution:")
    for step, state in enumerate(solution):
        print(f"step {step + 1}:")
        for row in state:   
            print (row)
        print()



