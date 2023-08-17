import heapq
# Define search tree
search_tree = {
    'A': {'B': 1, 'C': 1},
    'B': {'G': 1, 'H': 1},
    'C': {},
    'D': {'E': 1, 'F': 1},
    'E': {},
    'F': {},
    'G': {},
    'H': {}
}

# Define the heuristic costs
heuristic_costs = {
    'A': 0,
    'B': 5,
    'C': 12,
    'D': 10,
    'E': 4,
    'F': 4,
    'G': 0,
    'H': 7
}

# Define the AO* search algorithm
def ao_star_search(start, goal):
    # Define a priority queue to store the nodes
    priority_queue = []
    heapq.heappush(priority_queue, (0, start)) # Priority is determined by the estimated total cost
    g_cost = {start: 0} # Keep track of the cost to reach each node
    parent = {start: None} # Keep track of the parent node

    while priority_queue:
        # Pop the node with the lowest priority from the queue
        _, current_node = heapq.heappop(priority_queue)

        # Check if the current node is the goal
        if current_node == goal:
            return construct_path(parent, current_node)
        
        # Explore the neighbors of the current node
        for neighbor in search_tree[current_node]:
            # Calculate the estimated total cost for the neighbor
            total_cost = g_cost[current_node] + search_tree[current_node][neighbor] + heuristic_costs[neighbor]

            # Update the cost and parent if the neighbor has not been visited or has a lower cost
            if neighbor not in g_cost or total_cost < g_cost[neighbor]:
                g_cost[neighbor] = g_cost[current_node] + search_tree[current_node][neighbor]
                heapq.heappush(priority_queue, (total_cost, neighbor))
                parent[neighbor] = current_node

                # Print intermediate state
                print("Intermediate state:")
                path = construct_path(parent, neighbor)
                print('->'.join(path))
                print()
    # No pathe found
    return None

# Helper function to construct the path from the start to thte goal
def construct_path(parent, goal):
    path = [goal]
    current = goal
    while current != None:
        current = parent[current]
        if current is not None:
            path.append(current)
    path.reverse()
    return path

# Define the start and goal nodes
start_node = 'A'
goal_node = 'G'

# Run the AO* search algorithm
path = ao_star_search(start_node, goal_node)

# Print the result
if path is not None:
    print("Final path found:")
    print('->'.join(path))
else:
    print("No path found.")
