from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def main():
    output = Path(__file__).resolve().parent / "outputs"
    output.mkdir(exist_ok=True)
    data = load_iris()
    X = StandardScaler().fit_transform(data.data)
    pca = PCA(n_components=2)
    Z = pca.fit_transform(X)
    u, s, vt = np.linalg.svd(X, full_matrices=False)
    print("PCA variance ratio:", pca.explained_variance_ratio_)
    print("SVD singular values:", s)
    print("Rank-2 reconstruction error:", np.linalg.norm(X-u[:,:2]@np.diag(s[:2])@vt[:2]))
    for label, name in enumerate(data.target_names):
        points = Z[data.target == label]
        plt.scatter(points[:,0], points[:,1], label=name)
    plt.xlabel("PC1"); plt.ylabel("PC2"); plt.legend()
    plt.title("Iris PCA"); plt.tight_layout()
    plt.savefig(output / "iris_pca.png", dpi=140); plt.close()

if __name__ == "__main__":
    main()
