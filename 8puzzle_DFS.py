def get_neighbours(state):
    neighbours=[]
    zero=state.index(0)
    row=zero//3
    col=zero%3

    moves=[(-1,0),(1,0),(0,-1),(0,1)]

    for dr,dc in moves:
        nr=row+dr
        nc=col+dc
        if 0<=nr<3 and 0<=nc<3:
            new_zero=nr*3+nc
            new_state=list(state)
            new_state[zero],new_state[new_zero]=new_state[new_zero],new_state[zero]
            neighbours.append(tuple(new_state))

    return neighbours

def dfs(start,goal):
    stack=[(start,[start])]
    visited=set()
    while stack:
        state,path=stack.pop()
        if state==goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for next_state in get_neighbours(state):
            if next_state not in visited:
                stack.append((next_state,path+[next_state]))

    return None

def print_solution(path):
    if path is None:
        print("No solution found")
        return

    print("Number of moves:", len(path) - 1)

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

path = dfs(start, goal)
print("DFS Solution:")
print_solution(path)

