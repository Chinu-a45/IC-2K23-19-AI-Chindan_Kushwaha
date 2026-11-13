# Chindan Kushwaha — Artificial Intelligence Lab Portfolio

This repository implements the seven laboratory units in the IC-703 C
Artificial Intelligence syllabus. All experiment implementations are Python
source files. The repository also includes sample data, generated outputs,
trained model artifacts, reports, diagrams, and automated tests.

## Environment
- Python 3.10+
- NumPy, Pandas, Matplotlib, scikit-learn, PyTorch, Pillow, ReportLab

## Install and run
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python run_all.py
python -m unittest discover -s tests -v
```

PyTorch CPU is supported. If the PyTorch wheel selected by pip is not compatible
with the machine, install the appropriate build from the official PyTorch
installation selector, then run `pip install -r requirements.txt` again.

## Experiments
| Unit | Contents |
|---|---|
| Lab1 | Production system, Water Jug, Missionaries and Cannibals, Vacuum Cleaner |
| Lab2 | Generate-and-test, BFS, DFS, Hill Climbing, Greedy Best-First, A*, Maze, 8-puzzle |
| Lab3 | NumPy, Pandas, EDA, missing values, encoding, feature engineering, visualization |
| Lab4 | Predicates, rule-based reasoning, semantic network, frames, conceptual dependency, inference |
| Lab5 | Decision Tree, placement prediction, metrics, confusion matrix, model visualization |
| Lab6 | PyTorch tensors, autograd, linear regression, neural network, training and evaluation |
| Lab7 | PCA, SVD, CNN image classification, Grad-CAM, FGSM and robustness evaluation |

## Mini-project
`mini_project/` contains a reproducible Explainable AI dashboard experiment
using a Decision Tree on the included synthetic student-placement dataset.
It generates predictions, feature importance, a confusion matrix and a report.
The dataset is synthetic and is for academic demonstration only.

## Generated artifacts
Run `python run_all.py` to regenerate outputs, models and the two PDF reports.
Generated files are committed in this repository so the initial submission has
actual artifacts, not empty folders.

## Git
The repository is organized for incremental commits. `GIT_WORKFLOW.md` contains
the suggested branch, commit and tag commands. The current repository directory
name is `Chindan-Kushwaha-AI-Lab`; no roll number was supplied, so none has been
invented.
