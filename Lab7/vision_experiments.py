from pathlib import Path
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "outputs"
MODEL_DIR = ROOT / "models"

class SmallCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 8, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(), nn.Linear(8 * 4 * 4, 32), nn.ReLU(), nn.Linear(32, 10)
        )
    def forward(self, x):
        return self.classifier(self.features(x))

class GradCAM:
    def __init__(self, model, target_layer):
        self.model = model
        self.activations = None
        self.gradients = None
        self.fwd = target_layer.register_forward_hook(self._forward_hook)
        self.bwd = None
    def _forward_hook(self, module, inputs, output):
        self.activations = output
        output.register_hook(lambda gradient: setattr(self, "gradients", gradient))
    def generate(self, image, class_index=None):
        self.model.zero_grad(set_to_none=True)
        scores = self.model(image)
        if class_index is None:
            class_index = int(scores.argmax(1).item())
        scores[:, class_index].sum().backward()
        weights = self.gradients.mean(dim=(2, 3), keepdim=True)
        cam = torch.relu((weights * self.activations).sum(dim=1, keepdim=True))
        cam = torch.nn.functional.interpolate(cam, size=image.shape[-2:],
              mode="bilinear", align_corners=False).squeeze()
        cam = cam - cam.min()
        return (cam / cam.max().clamp_min(1e-8)).detach().cpu().numpy()
    def close(self):
        self.fwd.remove()
        if self.bwd is not None:
            self.bwd.remove()

def fgsm(model, images, labels, epsilon=0.12):
    images = images.detach().clone().requires_grad_(True)
    model.zero_grad(set_to_none=True)
    loss = nn.CrossEntropyLoss()(model(images), labels)
    loss.backward()
    adversarial = torch.clamp(images + epsilon * images.grad.sign(), 0, 1)
    return adversarial.detach()

def accuracy(model, loader):
    correct = total = 0
    model.eval()
    with torch.no_grad():
        for x, y in loader:
            correct += (model(x).argmax(1) == y).sum().item()
            total += y.numel()
    return correct / total

def main():
    torch.set_num_threads(1)
    OUT.mkdir(exist_ok=True); MODEL_DIR.mkdir(exist_ok=True)
    torch.manual_seed(7)
    digits = load_digits()
    images = torch.tensor(digits.images / 16.0, dtype=torch.float32).unsqueeze(1)
    labels = torch.tensor(digits.target, dtype=torch.long)
    generator = torch.Generator().manual_seed(7)
    train_size = int(0.8 * len(images))
    train_data, test_data = torch.utils.data.random_split(
        TensorDataset(images, labels), [train_size, len(images)-train_size],
        generator=generator)
    train_loader = DataLoader(train_data, batch_size=64, shuffle=True,
                              generator=torch.Generator().manual_seed(7))
    test_loader = DataLoader(test_data, batch_size=128, shuffle=False)

    model = SmallCNN()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.003)
    criterion = nn.CrossEntropyLoss()
    started = time.perf_counter()
    for epoch in range(8):
        model.train()
        running = 0.0
        for x, y in train_loader:
            optimizer.zero_grad()
            loss = criterion(model(x), y)
            loss.backward()
            optimizer.step()
            running += loss.item() * y.size(0)
        print(f"Epoch {epoch+1}/8 - loss: {running/len(train_data):.4f}")
    elapsed = time.perf_counter() - started
    clean_acc = accuracy(model, test_loader)

    x_batch, y_batch = next(iter(test_loader))
    adv_batch = fgsm(model, x_batch, y_batch, epsilon=0.12)
    with torch.no_grad():
        adv_acc = (model(adv_batch).argmax(1) == y_batch).float().mean().item()

    cam_engine = GradCAM(model, model.features[0])
    cam = cam_engine.generate(x_batch[:1])
    cam_engine.close()

    # PCA and SVD on standardized tabular digit features
    flattened = digits.data
    scaled = StandardScaler().fit_transform(flattened)
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(scaled)
    u, singular, vt = np.linalg.svd(scaled, full_matrices=False)
    print("PCA explained variance:", pca.explained_variance_ratio_.round(4))
    print("SVD first singular values:", singular[:5].round(3))
    print(f"Clean test accuracy: {clean_acc:.4f}")
    print(f"FGSM batch accuracy (epsilon=0.12): {adv_acc:.4f}")
    print(f"Training time: {elapsed:.3f}s")

    fig, axes = plt.subplots(1, 3, figsize=(10, 3))
    axes[0].imshow(x_batch[0, 0], cmap="gray"); axes[0].set_title("Input")
    axes[1].imshow(cam, cmap="jet"); axes[1].set_title("Grad-CAM")
    axes[2].imshow(adv_batch[0, 0], cmap="gray"); axes[2].set_title("FGSM")
    for ax in axes: ax.axis("off")
    fig.tight_layout(); fig.savefig(OUT / "gradcam_fgsm_examples.png", dpi=150); plt.close(fig)

    plt.figure(figsize=(6, 4))
    scatter = plt.scatter(reduced[:, 0], reduced[:, 1], c=digits.target, s=8, cmap="tab10")
    plt.xlabel("PC1"); plt.ylabel("PC2"); plt.title("PCA of handwritten digits")
    plt.colorbar(scatter, label="Digit class")
    plt.tight_layout(); plt.savefig(OUT / "pca_digits.png", dpi=150); plt.close()
    torch.save(model.state_dict(), MODEL_DIR / "digit_cnn.pt")
    print("Saved CNN and Lab 7 visualizations.")

if __name__ == "__main__":
    main()
