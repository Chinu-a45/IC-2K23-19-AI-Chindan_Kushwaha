# Lab 5 — Decision Tree Classifier and Model Evaluation

**Aim:** Create a feature matrix, train a Decision Tree, predict placement class
and evaluate classification performance.

**Algorithm:** Load synthetic placement data; split into training and test sets;
fit a depth-limited Decision Tree; predict test labels; calculate accuracy,
confusion matrix, precision, recall and F1-score; visualize and serialize model.

**Run:** `python Lab5/decision_tree.py`.

**Results:** Prints metrics and creates confusion-matrix/tree images in `outputs/`.
The trained estimator is saved in `models/decision_tree.joblib`.

**Performance analysis:** Metrics are computed on a held-out test split. The
small synthetic dataset makes these values illustrative only; they must not be
interpreted as real placement prediction performance.

**Learning outcomes:** Supervised learning, feature matrix creation,
classification, evaluation metrics and model visualization.
