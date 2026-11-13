# Lab 7 — Explainable AI, Adversarial AI and Advanced Applications

**Aim:** Demonstrate PCA/SVD, CNN image classification, Grad-CAM visualization
and FGSM adversarial perturbations.

**Algorithm:** A small CNN is trained on scikit-learn's built-in handwritten
digits dataset. Grad-CAM weights convolutional activations by class gradients.
FGSM adds epsilon times the sign of the input gradient. PCA projects standardized
features to two dimensions; SVD decomposes the feature matrix.

**Run:** `python Lab7/vision_experiments.py` and `python Lab7/pca_svd.py`.

**Results:** The vision experiment prints training loss, clean test accuracy,
FGSM batch accuracy, PCA variance and SVD singular values. It saves the CNN and
Grad-CAM/FGSM/PCA images. Iris PCA is saved separately.

**Performance analysis:** Compare clean and adversarial accuracy at epsilon
0.12. This is a small demonstration on handwritten digits, not a benchmark of
real-world image robustness. Grad-CAM is a qualitative explanation, not proof
of causal feature use.

**Learning outcomes:** Dimensionality reduction, CNN training, gradients,
model interpretability and adversarial evaluation.
