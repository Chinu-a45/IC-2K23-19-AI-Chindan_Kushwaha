from heapq import heappush, heappop

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):
    total = 0
    for i, value in enumerate(state):
        if value:
            goal_i = value - 1
            total += abs(i // 3 - goal_i // 3) + abs(i % 3 - goal_i % 3)
    return total

def solvable(state):
    values = [x for x in state if x]
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i+1, len(values)))
    return inversions % 2 == 0

def solve(start):
    if len(start) != 9 or set(start) != set(range(9)):
        raise ValueError("Puzzle must contain each integer 0 through 8 exactly once")
    if not solvable(start):
        return None
    heap, parent, best = [], {start: None}, {start: 0}
    heappush(heap, (manhattan(start), 0, start))
    while heap:
        _, cost, state = heappop(heap)
        if cost != best[state]: continue
        if state == GOAL:
            path = []
            while state is not None:
                path.append(state); state = parent[state]
            return list(reversed(path))
        zero = state.index(0)
        for nxt_pos in (zero-3, zero+3, zero-1, zero+1):
            if not 0 <= nxt_pos < 9: continue
            if abs(nxt_pos % 3 - zero % 3) + abs(nxt_pos // 3 - zero // 3) != 1: continue
            nxt = list(state); nxt[zero], nxt[nxt_pos] = nxt[nxt_pos], nxt[zero]
            nxt = tuple(nxt); new_cost = cost + 1
            if new_cost < best.get(nxt, float("inf")):
                best[nxt] = new_cost; parent[nxt] = state
                heappush(heap, (new_cost + manhattan(nxt), new_cost, nxt))
    return None

def main():
    start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    path = solve(start)
    print("A* 8-puzzle solution:")
    for state in path or []:
        print(state[:3]); print(state[3:6]); print(state[6:]); print()
    print("Moves:", len(path)-1 if path else "No solution")

if __name__ == "__main__":
    main()
