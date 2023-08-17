class State:
    def __init__(self, blocks):
        self.blocks = blocks
        self.parent = None

    def __str__(self):
        return str(self.blocks)
    
def dls_search(initial_state, goal_state, depth_limit):
    return dls_recursive(initial_state, goal_state, depth_limit)

def dls_recursive(state, goal_state, depth_limit):
    if state.blocks == goal_state.blocks:
        return state, True
    
    if depth_limit == 0:
        return None, False
    
    for next_state in get_next_states(state):
        result, complete = dls_recursive(next_state, goal_state, depth_limit - 1)
        if complete:
            return result, True
        
    return None, False

def get_next_states(state):
    next_states = []

    for i in range (len(state.blocks)):
        for j in range (len(state.blocks)):
            if i != j and state.blocks[i] and (not state.blocks[j] or state.blocks[i][-1] < state.blocks[j][-1]):
                new_blocks = [block[:] for block in state.blocks]
                new_blocks[j].append(new_blocks[i].pop())
                next_states.append(State(new_blocks))
    return next_states

def print_state_horizontal(state):
    for block in state.blocks:
        print(" ".join(block))
    print()

def print_state_vertical(state):
    max_height = max(len(block) for block in state.blocks)
    for height in range(max_height - 1, -1, -1):
        for block in state.blocks:
            if height < len(block):
                print(block[height])
            else:
                print(" ")
        print()

def main():
    # Define the initial state and goal state 
    initial_blocks = [['B'], ['A', 'C'], []]
    goal_blocks = [['C'], ['B'], ['A']]

    # Create state objects
    initial_state = State(initial_blocks)
    goal_state = State(goal_blocks)

    # Print the initial state vertically
    print("Initial state:")
    print_state_horizontal(initial_state)
    print()

    # Perform DFS search
    final_state, complete = dls_search(initial_state, goal_state, depth_limit=1)

    if complete:
        # Retrive the path from the initial to final state
        path = []
        current_state = final_state
        while current_state:
            path.append(current_state)
            current_state = current_state.parent
        # Print the path and final in reverse order vertically
        print("Path from initial state to goal state:")
        for state in reversed(path):
            print_state_horizontal(state)
            print()
        print("Final state:")
        print_state_vertical(final_state)
        print("Search is complete at depth 1.")
    else:
        print("Search is incomplete at depth 1.")

if __name__ == "__main__":
    main()

