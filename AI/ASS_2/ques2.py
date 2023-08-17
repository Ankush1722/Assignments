from collections import deque

# Define the capacitites of the jugs
jug_4_capacity = 4
jug_3_capacity = 3

# Function to check if the desired amount is reached
def is_desired_amount(amount):
    return amount == 2

# Function to generate the possible next states
def generate_next_states(state):
    next_states = []

    # Fill the 4-litre jug
    if(state[0]) < jug_4_capacity:
        next_states.append((jug_4_capacity, state[1]))

    # Fill the 3-litre jug
    if state[1] < jug_3_capacity:
        next_states.append((state[0], jug_3_capacity))

    # Empty the 4-litre jug
    if state[0] > 0:
        next_states.append((0, state[1]))

    # Empty the 3-litre jug
    if state[1] > 0:
        next_states.append((state[0], 0))

    # Pour water from the 3-litre jug to the 4-litre jug
    if state[0] > 0 and state[1] < jug_3_capacity:
        amount_to_pour = min(state[0], jug_3_capacity - state[1])
        next_states.append((state[0] - amount_to_pour, state[1] + amount_to_pour))

    # Pour water from the 3-litre jug to the 4-litre jug
    if state[0] < jug_4_capacity and state[1] > 0:
        amount_to_pour = min(jug_4_capacity - state[0], state[1])
        next_states.append((state[0] + amount_to_pour, state[1] - amount_to_pour))

    return next_states

# Breadth-first search algorithm to find the solution
def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)

        if is_desired_amount(current_state[0]):
            return path
        
        next_states = generate_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# Solve the jug problem
initial_state = (0,0)  # Initial state: both jugs are empty
solution = bfs(initial_state)

# Print the solution
if solution is None:
    print("No solution found.")
else:
    print("Solution.")
    for step, state in enumerate(solution):
        print(f"Step {step+1}: {state[0]}L, {state[1]}L")


