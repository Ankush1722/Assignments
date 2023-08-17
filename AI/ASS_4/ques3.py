import heapq
# Define the initial and final states
initial_state = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
final_state = [[1, 3, 4], [8, 0, 4], [7, 6, 5]]

# Define the heuristic function: number of correctly placed tiles
def correctly_placed_tiles(state):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[1])):
            if state[i][j] == final_state[i][j]:
                count += 1
    return count

def astar_search(initial_state):
    # Define a priority queue to store the states
    priority_queue = []
    heapq.heappush(priority_queue, (0, initial_state)) # Priority is determined by the sum of heuristic and cost
    cost = {tuple(map(tuple, initial_state)): 0} # Keep track of the cost to reach each state
    parent = {tuple(map(tuple, initial_state)): None} # Keep track of the parent state
    
    while priority_queue:
        # Pop the state with the lowest priority from the queue
        _, current_state = heapq.heappop(priority_queue)
        
        # Check if the current state is the goal state
        if current_state == final_state:
            return current_state
        
        # Generate all possible neighbors
        zero_row, zero_col = find_zero(current_state)
        neighbors = generate_neighbors (current_state, zero_row, zero_col)
        
        for neighbor in neighbors:
            neighbor_cost = cost[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, neighbor)) not in cost or neighbor_cost < cost[tuple(map(tuple, neighbor))]:
                cost[tuple(map(tuple,neighbor))] = neighbor_cost
                priority = neighbor_cost + correctly_placed_tiles(neighbor)
                heapq.heappush(priority_queue, (priority, neighbor))
                parent[tuple(map(tuple, neighbor))] = current_state
    # No solution found
    return None

# Generate possible neighbors by swapping the zero (blank) tile with adjacent tiles
def generate_neighbors(state, zero_row, zero_col):
    neighbors = []

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
    if zero_row > 0:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row-1][zero_col] = new_state[zero_row-1][zero_col], new_state[zero_row][zero_col]
        neighbors.append(new_state)

    # Generate neighbors by swapping with below tile
    if zero_row < len(state)-1:
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
            
# Print the initial state
print("Initial State:")
for row in initial_state:
    print(row)
print()

# Run the A* search algorithm
result= astar_search(initial_state)

# Print the result
if result is not None:
    print("Final State:")
    for row in result:
        print(row)
else:
    print("Pattern not found.")

