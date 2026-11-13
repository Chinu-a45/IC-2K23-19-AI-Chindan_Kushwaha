# Mini Project — Explainable Student Placement Decision Support

## Problem statement
Demonstrate a small, interpretable classifier that predicts a synthetic
placement label from CGPA, IQ and communication score.

## Objectives
- Train a Decision Tree classifier.
- Evaluate predictions with standard classification metrics.
- Explain the model with a tree diagram and permutation feature importance.

## Dataset and methodology
The project uses `datasets/placement.csv`, a synthetic teaching dataset.
A stratified train/test split is used. A depth-limited Decision Tree is trained
and evaluated. Permutation importance estimates how test accuracy changes when
each feature is shuffled.

## Run
`python mini_project/explainable_placement.py`

## Outputs
- `outputs/confusion_matrix.png`
- `outputs/feature_importance.png`
- `outputs/decision_tree.png`
- `models/explainable_placement.joblib`

## Limitations
The dataset is small and synthetic. This project is not suitable for real
admissions, hiring or placement decisions. Feature importance is model- and
dataset-dependent and does not establish causality.
