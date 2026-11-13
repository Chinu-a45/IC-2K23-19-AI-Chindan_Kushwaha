from collections import deque

MAZE = [
    "S...#....",
    "##.#.##..",
    "...#...#.",
    ".###.#...",
    ".....#..G",
]

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    if any(len(row) != cols for row in maze):
        raise ValueError("Maze rows must have equal length")
    starts = [(r, c) for r in range(rows) for c in range(cols) if maze[r][c] == "S"]
    goals = {(r, c) for r in range(rows) for c in range(cols) if maze[r][c] == "G"}
    if len(starts) != 1 or not goals:
        raise ValueError("Maze must contain exactly one S and at least one G")
    start = starts[0]
    q, parent = deque([start]), {start: None}
    while q:
        cell = q.popleft()
        if cell in goals:
            path = []
            while cell is not None:
                path.append(cell); cell = parent[cell]
            return list(reversed(path))
        r, c = cell
        for nxt in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            nr, nc = nxt
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#" and nxt not in parent:
                parent[nxt] = cell; q.append(nxt)
    return None

def main():
    path = solve_maze(MAZE)
    print("Maze path:", path)
    print("Path length:", len(path)-1 if path else "No path")

if __name__ == "__main__":
    main()
