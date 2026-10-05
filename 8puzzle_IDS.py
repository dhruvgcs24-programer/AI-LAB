
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def get_successors(state):
    """Generate all possible moves from the current state."""

    successors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            successors.append((tuple(new_state), move))

    return successors


def depth_limited_search(state, goal, limit, path, moves):
    """Depth Limited Search used by IDS."""

    if state == goal:
        return moves

    if limit == 0:
        return None

    for next_state, move in get_successors(state):

        if next_state not in path:

            path.add(next_state)

            result = depth_limited_search(
                next_state,
                goal,
                limit - 1,
                path,
                moves + [move]
            )

            if result is not None:
                return result

            path.remove(next_state)

    return None


def IDS(start, goal):
    """Iterative Deepening Search."""

    depth = 0

    while True:
        print("Searching at depth:", depth)

        path = {start}

        result = depth_limited_search(
            start,
            goal,
            depth,
            path,
            []
        )

        if result is not None:
            return result

        depth += 1


def print_puzzle(state):
    """Print the puzzle in 3x3 format."""

    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()



start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

print("Initial State:")
print_puzzle(start)

print("Goal State:")
print_puzzle(goal)

solution = IDS(start, goal)

print("Solution:")
print(solution)

print("Number of moves:", len(solution))
