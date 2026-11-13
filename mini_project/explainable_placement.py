from pathlib import Path
import joblib
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.inspection import permutation_importance

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "outputs"

def main():
    OUT.mkdir(exist_ok=True)
    (ROOT / "models").mkdir(exist_ok=True)
    df = pd.read_csv(ROOT / "datasets" / "placement.csv")
    X, y = df.drop(columns="placed"), df["placed"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    model = DecisionTreeClassifier(max_depth=3, class_weight="balanced",
                                    random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Explainable Placement Decision Support — demonstration only")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
    print(classification_report(y_test, predictions, zero_division=0))
    ConfusionMatrixDisplay.from_predictions(y_test, predictions)
    plt.tight_layout(); plt.savefig(OUT / "confusion_matrix.png", dpi=140); plt.close()
    importance = permutation_importance(model, X_test, y_test,
                                        n_repeats=20, random_state=42)
    order = importance.importances_mean.argsort()
    plt.figure(figsize=(7, 4))
    plt.barh(X.columns[order], importance.importances_mean[order])
    plt.xlabel("Mean accuracy decrease"); plt.title("Permutation feature importance")
    plt.tight_layout(); plt.savefig(OUT / "feature_importance.png", dpi=140); plt.close()
    plt.figure(figsize=(10, 6))
    plot_tree(model, feature_names=list(X.columns),
              class_names=["Not placed", "Placed"], filled=True, rounded=True)
    plt.tight_layout(); plt.savefig(OUT / "decision_tree.png", dpi=140); plt.close()
    joblib.dump(model, ROOT / "models" / "explainable_placement.joblib")
    print("Saved metrics visualizations and model.")

if __name__ == "__main__":
    main()
