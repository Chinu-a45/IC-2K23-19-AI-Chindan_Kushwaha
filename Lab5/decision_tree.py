from pathlib import Path
import time
import joblib
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "outputs"

def main():
    OUT.mkdir(exist_ok=True)
    (ROOT / "models").mkdir(exist_ok=True)
    df = pd.read_csv(ROOT / "datasets" / "placement.csv")
    X, y = df.drop(columns="placed"), df["placed"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    started = time.perf_counter()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    elapsed = time.perf_counter() - started
    print(f"Accuracy: {accuracy_score(y_test, pred):.4f}")
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    print("Classification report:\n",
          classification_report(y_test, pred, zero_division=0))
    print(f"Fit and prediction time: {elapsed:.6f}s")
    ConfusionMatrixDisplay.from_predictions(y_test, pred)
    plt.tight_layout(); plt.savefig(OUT / "confusion_matrix.png", dpi=140); plt.close()
    plt.figure(figsize=(12, 7))
    plot_tree(model, feature_names=list(X.columns),
              class_names=["Not placed", "Placed"], filled=True, rounded=True)
    plt.tight_layout(); plt.savefig(OUT / "decision_tree.png", dpi=140); plt.close()
    joblib.dump(model, ROOT / "models" / "decision_tree.joblib")
    print("Saved model and visualizations.")

if __name__ == "__main__":
    main()
