import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from Lab1.water_jug import solve as solve_jug
from Lab1.missionaries_cannibals import solve as solve_crossing, valid
from Lab1.vacuum_cleaner import vacuum_cleaner
from Lab2.search_algorithms import bfs, a_star, GRAPH, H
from Lab2.maze_solver import solve_maze, MAZE
from Lab2.eight_puzzle import solve as solve_puzzle, GOAL
from Lab4.knowledge_representation import forward_chain

class TestAILabs(unittest.TestCase):
    def test_water_jug_reaches_target(self):
        path, explored = solve_jug()
        self.assertIsNotNone(path)
        self.assertTrue(any(2 in state for state in path))
        self.assertGreater(explored, 0)

    def test_missionaries_cannibals(self):
        path = solve_crossing()
        self.assertEqual(path[0], (3, 3, 0))
        self.assertEqual(path[-1], (0, 0, 1))
        self.assertTrue(all(valid(state) for state in path))

    def test_vacuum(self):
        final_state, _ = vacuum_cleaner({"A": "Dirty", "B": "Dirty"})
        self.assertEqual(set(final_state.values()), {"Clean"})

    def test_search(self):
        path, _ = bfs(GRAPH, "A", "G")
        self.assertEqual(path[0], "A")
        self.assertEqual(path[-1], "G")
        path, cost, _ = a_star(GRAPH, H, "A", "G")
        self.assertEqual(path[-1], "G")
        self.assertEqual(cost, 7)

    def test_maze(self):
        path = solve_maze(MAZE)
        self.assertIsNotNone(path)
        self.assertEqual(MAZE[path[0][0]][path[0][1]], "S")
        self.assertEqual(MAZE[path[-1][0]][path[-1][1]], "G")

    def test_eight_puzzle(self):
        path = solve_puzzle((1, 2, 3, 4, 0, 6, 7, 5, 8))
        self.assertEqual(path[-1], GOAL)

    def test_forward_chaining(self):
        facts = forward_chain({("a",), ("b",)}, [([("a",), ("b",)], ("c",))])
        self.assertIn(("c",), facts)

if __name__ == "__main__":
    unittest.main()
