import random
# Define the initial and final states
initial_state=[[2,0,3], [1,8,4], [7,6,5]]
final_state=[[1,2,3], [8,0,4], [7,6,5]]

# Calculate the number of misplaced tiles heuristic function
def misplaced_tiles(state):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != final_state[i][j]:
                count += 1
    return count

# Generate random neighbors by swapping two files
def generate_neighbors(state):
    neighbors = []
    zero_row, zero_col = find_zero(state)

    # Generate neighbors by swapping with the left tile
    if zero_col > 0:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row][zero_col-1] = new_state[zero_row][zero_col-1], new_state[zero_row][zero_col]
        neighbors.append(new_state)

    # Generate neighbors by swapping with right tile
    if zero_col < len(state[0])-1:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row][zero_col+1] = new_state[zero_row][zero_col+1], new_state[zero_row][zero_col]
        neighbors.append(new_state)

    # Generate neighbors by swapping with above tile
    if zero_col > 0:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row-1][zero_col] = new_state[zero_row-1][zero_col], new_state[zero_row][zero_col]
        neighbors.append(new_state)

    # Generate neighbors by swapping with below tile
    if zero_col < len(state)-1:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row+1][zero_col] = new_state[zero_row+1][zero_col], new_state[zero_row][zero_col]
        neighbors.append(new_state)
    
    return neighbors

# Find the position of the zero (blank) tile
def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j
            
# Implement the Hill Climbing Algorithm
def hill_climbing(initial_state):
    current_state = initial_state
    while True:
        current_heuristic = misplaced_tiles(current_state)

        # Check if the current state is the goal state
        if current_heuristic == 0:
            return current_state
        neighbors = generate_neighbors(current_state)
        best_neighbor = None
        best_neighbor_heuristic = current_heuristic

        # Find the neighbor with the lowest heuristic value
        for neighbor in neighbors:
            neighbor_heuristic = misplaced_tiles(neighbor)
            if neighbor_heuristic < best_neighbor_heuristic:
                best_neighbor = neighbor
                best_neighbor_heuristic = neighbor_heuristic

        # If no better neighbor is found, return the current state
        if best_neighbor is None or best_neighbor_heuristic >= current_heuristic:
            return current_state
                
        # Move to the best neighbor and the continue the search
        current_state = best_neighbor

# Print the initial state
print("Initial State:")
for row in initial_state:
    print(row)
print() # ad a blank line

# Run the Hill Climbing Algorithm
result = hill_climbing(initial_state)

# Print the final state
print("Final state")
for row in result:
    print(row)


