from heapq import heappush, heappop

# Goal state
GOAL = (0,1,2,
        3,4,5,
        6,7,8)

# Misplaced Tiles heuristic
def misplaced_tiles(state):
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != GOAL[i])

# Find neighboring states
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            # Swap blank (0) with adjacent tile
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors

# A* search algorithm
def astar(start):
    # Priority queue: (f, g, state, path)
    pq = []
    heappush(pq, (misplaced_tiles(start), 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state == GOAL:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                h = misplaced_tiles(neighbor)
                new_f = new_g + h

                heappush(
                    pq, (new_f, new_g, neighbor, path + [neighbor])
                )

    return None

# Print puzzle state
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()

# Main program
start = (5, 4, 0, 6, 1, 8, 7, 3, 2)

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input! Enter numbers 0 to 8 exactly once.")
else:
    solution = astar(start)

    if solution:
        print("Manhattan method")
        print("Solution found!")
        print("Number of moves:", len(solution) - 1)

        for step, state in enumerate(solution):
            print("Step", step)
            print_state(state)
    else:
        print("No solution exists.")