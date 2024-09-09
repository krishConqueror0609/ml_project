from collections import deque

def water_jug_bfs(x, y, target):
    def get_neighbors(state):
        x, y = state
        neighbors = [
            (x, 0), # Empty jug X
            (0, y), # Empty jug Y
            (x, y - min(y, x + y)), # Pour from Y to X
            (x - min(x, x + y), y), # Pour from X to Y
            (x - min(x, x - (x - min(x, x + y))), y + min(x, x - (x - min(x, x + y)))), # Fill jug X
            (x + min(y, y - (y - min(x, x + y))), y - min(y, y - (y - min(x, x + y)))) # Fill jug Y
        ]
        return neighbors

    visited = set()
    queue = deque([(0, 0, [])]) # (jug1, jug2, path)

    while queue:
        jug1, jug2, path = queue.popleft()
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]
        for neighbor in get_neighbors((jug1, jug2)):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor[0], neighbor[1], path + [(jug1, jug2)]))

    return None

# Input values
x = int(input("Enter the capacity of the first jug: "))
y = int(input("Enter the capacity of the second jug: "))
target = int(input("Enter the target amount of water: "))

# Check if the target is achievable
if target > max(x, y):
    print("Target amount is not achievable with the given jug capacities.")
else:
    result = water_jug_bfs(x, y, target)
    if result:
        print("Steps to measure the target amount of water:")
        for step in result:
            print(f"Jug1: {step[0]}, Jug2: {step[1]}")
    else:
        print("No solution found.")
