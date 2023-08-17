import copy

class TSP():
    def __init__ (self, map, startCity):
        TSP.map = map
        self.startCity = startCity
        self.currentCity = startCity
        self.visitedList = []
        self.visitedList.append(self.currentCity)
        self.cost = 0
        self.prevState = None

    def isGoalReached(self):
        if len(self.visitedList) == len(TSP.map[0]) + 1:
            return True
        else:
            return False

    def __gt__(self, other):
        return self.cost > other.cost
    
    def move(self, city):
        if TSP.map[self.currentCity][city] != 0 and city not in self.visitedList:
            self.prevState = copy.deepcopy(self)
            self.cost = self.cost + TSP.map[ self.currentCity][city]
            self.currentCity = city
            self.visitedList.append(self.currentCity)
            return True
        elif len(self.visitedList) == len(TSP.map[0]) and TSP.map[self.currentCity][city] != 0: 
            self.prevState = copy.deepcopy(self)
            self.cost = self.cost + TSP.map[self.currentCity][city]
            self.currentCity = city
            self.visitedList.append(self.currentCity)
            return True
        else:
            return False
        
    def possibleNextStates(Self):
        stateList = []

        for i in range(0, len(TSP.map[0])):
            stateCopy = copy.deepcopy(Self)
            if stateCopy.move(i):
                stateList.append(stateCopy)
        return stateList
    
def constructGoalPath(goalState):
    path = []
    while goalState:
        path.append(goalState.currentCity)
        goalState = goalState.prevState
    path.reverse()
    return path

open = []
closed = []

def UCS(startState):
    open.append(startState)
    while open:
        thisState = open.pop(0)
        closed.append(thisState)
        if thisState.isGoalReached():
            return constructGoalPath(thisState)
        nextStates = thisState.possibleNextStates()
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                open.append(eachState)
                open.sort()
            elif eachState in open:
                index = open.index(eachState)
                if eachState < open[index]:
                    open.append(eachState)
                    open.sort()
            elif eachState in closed:
                index = closed.index(eachState)
                if eachState < closed[index]:
                    closed.append(eachState)
                    closed.sort()

# Get the number of cities from the user
num_cities = int(input("Enter the number of cities: "))

# Get the distance between cities from the user
map = []
for i in range(num_cities):
    row = []
    for j  in range(num_cities):
        if i == j:
            row.append(0)
        else:
            dist = float(input(f"Enter the distance between city {i+1} and city {j+1}: "))
            row.append(dist)
    map.append(row)
startCity = int(input("Enter the starting city (1 to N): ")) - 1
problem = TSP(map, startCity)
solution = UCS(problem)

# Print the optimal path
print("Optimal Path:")
for city in solution:
    print(f"City {city+1}")


    

