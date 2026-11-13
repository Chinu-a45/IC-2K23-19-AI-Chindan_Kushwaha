from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    "Lab1/production_system.py",
    "Lab1/water_jug.py",
    "Lab1/missionaries_cannibals.py",
    "Lab1/vacuum_cleaner.py",
    "Lab2/search_algorithms.py",
    "Lab2/maze_solver.py",
    "Lab2/eight_puzzle.py",
    "Lab3/data_preprocessing.py",
    "Lab4/knowledge_representation.py",
    "Lab5/decision_tree.py",
    "Lab6/pytorch_fundamentals.py",
    "Lab7/pca_svd.py",
    "Lab7/vision_experiments.py",
    "mini_project/explainable_placement.py",
    "generate_reports.py",
]

def main():
    for relative in SCRIPTS:
        print(f"\n{'='*18} {relative} {'='*18}", flush=True)
        subprocess.run([sys.executable, str(ROOT / relative)], cwd=ROOT, check=True)
    print("\nAll experiment scripts completed successfully.")

if __name__ == "__main__":
    main()
