from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "outputs"

def main():
    OUT.mkdir(exist_ok=True)
    df = pd.read_csv(ROOT / "datasets" / "placement.csv")
    print("First five rows:\n", df.head())
    print("\nShape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isna().sum())
    print("\nSummary:\n", df.describe(include="all"))
    df = df.drop_duplicates().copy()
    for col in df.select_dtypes(include="number"):
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(exclude="number"):
        df[col] = df[col].fillna(df[col].mode().iloc[0])
    for col in df.select_dtypes(include="object"):
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))
    df["cgpa_band"] = pd.cut(df["cgpa"], bins=[0, 6.5, 7.5, 10],
                             labels=["low", "medium", "high"]).astype(str)
    df = pd.get_dummies(df, columns=["cgpa_band"], dtype=int)
    X, y = df.drop(columns="placed"), df["placed"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    print("Train:", X_train.shape, "Test:", X_test.shape)
    df.hist(figsize=(9, 6))
    plt.tight_layout(); plt.savefig(OUT / "feature_histograms.png", dpi=140); plt.close()
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(8, 6))
    image = ax.imshow(corr, cmap="coolwarm", aspect="auto", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(corr.columns)), corr.columns)
    fig.colorbar(image, ax=ax, label="Correlation")
    fig.tight_layout(); fig.savefig(OUT / "correlation_heatmap.png", dpi=140); plt.close()
    print("Saved EDA graphs to", OUT)

if __name__ == "__main__":
    main()
