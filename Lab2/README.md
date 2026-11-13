# Lab 2 — Heuristic Search Algorithms

**Aim:** Implement and compare generate-and-test, BFS, DFS, Hill Climbing,
Greedy Best-First Search and A*. Also solve a maze and 8-puzzle.

**Algorithm:** BFS uses a FIFO queue; DFS uses a stack; Hill Climbing chooses
the best immediate heuristic neighbor; Greedy Best-First orders by h(n); A*
orders by f(n)=g(n)+h(n). Maze uses BFS; 8-puzzle uses A* with Manhattan distance.

**Run:** `python Lab2/search_algorithms.py`, `python Lab2/maze_solver.py`,
`python Lab2/eight_puzzle.py`.

**Results:** Scripts print paths, costs, explored nodes or move counts.

**Performance analysis:** `search_algorithms.py` reports expanded nodes and
execution time. BFS is shortest only for equal edge costs. A* is optimal when
the heuristic is admissible and the implementation's cost assumptions hold.
Greedy and Hill Climbing are not generally optimal or complete.

**Learning outcomes:** Queue/stack search, heuristic functions, path costs,
admissibility, local optima and state-space search.
