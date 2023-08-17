from queue import PriorityQueue

# Function to calculate the nusber of misplaced tiles
def heuristic_misplaced_tiles(current_state, goal_state):
    misplaced_tiles = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if current_state[i][j] != goal_state[i][j]:
                misplaced_tiles += 1
    return misplaced_tiles

# Function to check if the current state is the goal state
def is_goal_state(current_state, goal_state):
    return current_state == goal_state

# Function to generate all possible successor node
def generate_successor_nodes(current_state):
    successor_nodes = []
    empty_tile_index = None
    # Find the index of the empty tile (0)
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if current_state[i][j] == 0:
                empty_tile_index = (i, j)
                break

    # Check possible moves: up, down, left, right
    possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for move in possible_moves:
        new_index = (empty_tile_index[0] + move[0], empty_tile_index[1] + move[1])
        if 0 <= new_index[0] < len(current_state) and 0 <= new_index[1] < len(current_state[0]):
            new_state = [row[:] for row in current_state]
            new_state[empty_tile_index[0]][empty_tile_index[1]] = new_state[new_index[0]][new_index[1]]
            new_state[new_index[0]][new_index[1]] = 0
            successor_nodes.append(new_state)
    return successor_nodes

# Best-First Search Algorithm
def best_first_search(initial_state, goal_state):
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic_misplaced_tiles(initial_state, goal_state), initial_state))
    visited = set(tuple(map(tuple, initial_state)))  # Keep track of visited nodes
    while not priority_queue.empty():
        current_node = priority_queue.get()[1]
        if is_goal_state(current_node, goal_state):
            return current_node
        successors = generate_successor_nodes(current_node)

        for successor in successors:
            successor_tuple = tuple(map(tuple, successor))
            if successor_tuple not in visited: 
                visited.add(successor_tuple)
                priority_queue.put((heuristic_misplaced_tiles(successor, goal_state), successor))
    return None  # No solution found
# Example usage
initial_state = [[2, 0, 3],
                 [1, 8, 4],
                 [7, 6, 5]]

goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

print("Initial State:")

for row in initial_state:
    print(row)
print()

solution = best_first_search(initial_state, goal_state)

if solution is None:
    print("No solution found.")
else:
    print("Final State:")
    for row in solution:
        print (row)

        