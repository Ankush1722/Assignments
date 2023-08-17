import copy
import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.prev_node = None
        self.cost = float('inf')

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost
    
    def get_neighbors(self):
        return self.neighbors.keys()
    
    def get_cost(self, neighbor):
        return self.neighbors[neighbor]
    
def construct_path(node):
    path=[]
    while node:
        path.append(node.name)
        node = node.prev_node
    path.reverse()
    return path

def UCS(start_node, goal_node):
    start_node.cost=0
    heap = [(start_node.cost, start_node)]
    visited = set()
    
    while heap:
        current_cost, current_node = heapq.heappop(heap)
        visited.add(current_node)

        if current_node == goal_node:
            return construct_path(current_node)
        for neighbor in current_node.get_neighbors():
            cost = current_node.get_cost(neighbor)
            if neighbor not in visited:
                total_cost = current_cost + cost
                if total_cost < neighbor.cost:
                    neighbor.cost = total_cost
                    neighbor.prev_node = current_node
                    heapq.heappush(heap, (total_cost, neighbor))
    return None

# Create nodes for each city
S = Node('S')
A = Node('A')
B = Node('B')
C = Node('C')
G = Node('G')

# Add neighbors and their costs
S.add_neighbor(A,1)
S.add_neighbor(B,5)
S.add_neighbor(C,15)
A.add_neighbor(S,1)
A.add_neighbor(G,10)
B.add_neighbor(S,5)
B.add_neighbor(G,5)
G.add_neighbor(A,10)
G.add_neighbor(B,5)
G.add_neighbor(C,5)
C.add_neighbor(S,15)
C.add_neighbor(G,5)

# Run UCS
solution = UCS(S, G)
# Print the optimal path with arrows
print('Optimal Path:')
for i, city in enumerate(solution):
    if i<len(solution) - 1:
        print(city, "->", end=" ")
    else:
        print(city)