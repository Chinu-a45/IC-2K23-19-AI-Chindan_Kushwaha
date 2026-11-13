from collections import deque
from time import perf_counter

def solve(cap_a=4, cap_b=3, target=2):
    if target < 0 or target > max(cap_a, cap_b):
        raise ValueError("Target must be between zero and the larger jug capacity")
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}
    explored = 0
    while queue:
        (a, b), path = queue.popleft()
        explored += 1
        if a == target or b == target:
            return path, explored
        pour_ab = min(a, cap_b - b)
        pour_ba = min(b, cap_a - a)
        successors = [
            (cap_a, b), (a, cap_b), (0, b), (a, 0),
            (a - pour_ab, b + pour_ab),
            (a + pour_ba, b - pour_ba),
        ]
        for state in successors:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None, explored

def main():
    start = perf_counter()
    path, explored = solve()
    print("Water Jug solution (4L, 3L; target 2L):")
    for i, state in enumerate(path or []):
        print(f"{i}: {state}")
    print("Moves:", len(path) - 1 if path else "No solution")
    print("Explored states:", explored)
    print(f"Execution time: {perf_counter() - start:.6f}s")

if __name__ == "__main__":
    main()
