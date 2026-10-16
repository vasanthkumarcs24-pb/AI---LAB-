
from heapq import heappush, heappop

# Goal state
GOAL = (0,1,2,
        3,4,5,
        6,7,8)

# Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            # Current position
            row, col = divmod(i, 3)

            # Goal position
            goal_row, goal_col = divmod(tile - 1, 3)

            # Manhattan distance
            distance += abs(row - goal_row) + abs(col - goal_col)

    return distance


# Generate neighboring states
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

            # Swap blank with adjacent tile
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* search algorithm
def astar(start):
    pq = []
    heappush(pq, (manhattan_distance(start), 0, start))

    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, state = heappop(pq)

        # Goal test
        if state == GOAL:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        # Ignore outdated queue entries
        if g != cost[state]:
            continue

        for neighbor in get_neighbors(state):
            new_g = g + 1

            if neighbor not in cost or new_g < cost[neighbor]:
                cost[neighbor] = new_g
                parent[neighbor] = state

                h = manhattan_distance(neighbor)
                heappush(pq, (new_g + h, new_g, neighbor))

    return None


# Display puzzle
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
        print("Solution found!")
        print("Number of moves:", len(solution) - 1)

        for step, state in enumerate(solution):
            print("Step", step)
            print_state(state)
    else:
        print("No solution exists.")
