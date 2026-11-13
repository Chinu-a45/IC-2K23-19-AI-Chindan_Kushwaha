from collections import deque
import heapq
from time import perf_counter

GRAPH = {
    "A": {"B": 1, "C": 4}, "B": {"A": 1, "D": 2, "E": 5},
    "C": {"A": 4, "F": 3}, "D": {"B": 2, "G": 5},
    "E": {"B": 5, "G": 1}, "F": {"C": 3, "G": 2}, "G": {}
}
H = {"A": 7, "B": 6, "C": 4, "D": 4, "E": 1, "F": 2, "G": 0}

def path_from(parent, goal):
    result = [goal]
    while result[-1] in parent:
        result.append(parent[result[-1]])
    return list(reversed(result))

def bfs(graph, start, goal):
    q, seen, parent = deque([start]), {start}, {}
    expanded = 0
    while q:
        node = q.popleft()
        expanded += 1
        if node == goal:
            return path_from(parent, goal), expanded
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt); parent[nxt] = node; q.append(nxt)
    return None, expanded

def dfs(graph, start, goal):
    stack, seen, parent, expanded = [start], set(), {}, 0
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node); expanded += 1
        if node == goal:
            return path_from(parent, goal), expanded
        for nxt in reversed(list(graph[node])):
            if nxt not in seen and nxt not in parent:
                parent[nxt] = node
                stack.append(nxt)
    return None, expanded

def hill_climbing(graph, heuristic, start, goal):
    current, path, expanded = start, [start], 0
    while current != goal:
        expanded += 1
        options = [n for n in graph[current] if n not in path]
        if not options:
            return None, expanded
        nxt = min(options, key=lambda n: heuristic[n])
        if heuristic[nxt] >= heuristic[current]:
            return None, expanded
        path.append(nxt); current = nxt
    return path, expanded

def greedy_best_first(graph, heuristic, start, goal):
    heap, parent, seen, expanded = [(heuristic[start], start)], {}, set(), 0
    while heap:
        _, node = heapq.heappop(heap)
        if node in seen: continue
        seen.add(node); expanded += 1
        if node == goal: return path_from(parent, goal), expanded
        for nxt in graph[node]:
            if nxt not in seen and nxt not in parent:
                parent[nxt] = node
                heapq.heappush(heap, (heuristic[nxt], nxt))
    return None, expanded

def a_star(graph, heuristic, start, goal):
    heap, parent, best, expanded = [(heuristic[start], 0, start)], {}, {start: 0}, 0
    while heap:
        _, cost, node = heapq.heappop(heap)
        if cost != best.get(node): continue
        expanded += 1
        if node == goal: return path_from(parent, goal), cost, expanded
        for nxt, weight in graph[node].items():
            candidate = cost + weight
            if candidate < best.get(nxt, float("inf")):
                best[nxt] = candidate; parent[nxt] = node
                heapq.heappush(heap, (candidate + heuristic[nxt], candidate, nxt))
    return None, float("inf"), expanded

def generate_and_test(candidates, goal_test):
    for candidate in candidates:
        if goal_test(candidate):
            return candidate
    return None

def main():
    cases = [
        ("BFS", lambda: bfs(GRAPH, "A", "G")),
        ("DFS", lambda: dfs(GRAPH, "A", "G")),
        ("Hill Climbing", lambda: hill_climbing(GRAPH, H, "A", "G")),
        ("Greedy Best-First", lambda: greedy_best_first(GRAPH, H, "A", "G")),
    ]
    for name, run in cases:
        t = perf_counter(); path, expanded = run()
        print(f"{name}: path={path}, expanded={expanded}, time={perf_counter()-t:.6f}s")
    t = perf_counter(); path, cost, expanded = a_star(GRAPH, H, "A", "G")
    print(f"A*: path={path}, cost={cost}, expanded={expanded}, time={perf_counter()-t:.6f}s")
    print("Generate and test (first even square > 20):",
          generate_and_test(range(21, 100), lambda n: n % 2 == 0 and int(n**0.5)**2 == n))

if __name__ == "__main__":
    main()
