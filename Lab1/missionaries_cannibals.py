from collections import deque

def valid(state):
    ml, cl, boat = state
    mr, cr = 3 - ml, 3 - cl
    if not (0 <= ml <= 3 and 0 <= cl <= 3 and boat in (0, 1)):
        return False
    return (ml == 0 or ml >= cl) and (mr == 0 or mr >= cr)

def solve():
    start, goal = (3, 3, 0), (0, 0, 1)
    passenger_options = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        ml, cl, boat = state
        direction = -1 if boat == 0 else 1
        for dm, dc in passenger_options:
            nxt = (ml + direction * dm, cl + direction * dc, 1 - boat)
            if valid(nxt) and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None

def main():
    path = solve()
    if path is None:
        print("No solution")
        return
    for i, (ml, cl, boat) in enumerate(path):
        print(f"{i}: left M={ml}, C={cl}; boat={'right' if boat else 'left'}")
    print("Crossings:", len(path) - 1)

if __name__ == "__main__":
    main()
