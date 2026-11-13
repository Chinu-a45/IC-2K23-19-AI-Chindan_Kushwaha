from pathlib import Path
import time
import torch
from torch import nn

def tensor_autograd():
    x = torch.tensor([2.0, 3.0], requires_grad=True)
    loss = (x ** 2).sum()
    loss.backward()
    print("Tensor:", x.detach().tolist(), "Gradient:", x.grad.tolist())

def train_regression():
    torch.manual_seed(42)
    x = torch.linspace(0, 10, 120).reshape(-1, 1)
    y = 3.0 * x + 5.0 + torch.randn_like(x) * 1.2
    model = nn.Linear(1, 1)
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    initial = criterion(model(x), y).item()
    start = time.perf_counter()
    for _ in range(800):
        prediction = model(x)
        loss = criterion(prediction, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    elapsed = time.perf_counter() - start
    final = criterion(model(x), y).item()
    print(f"Initial MSE: {initial:.4f}; final MSE: {final:.4f}")
    print(f"Learned weight={model.weight.item():.3f}, bias={model.bias.item():.3f}")
    print(f"Training time: {elapsed:.6f}s")
    return model

def neural_network():
    model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 2))
    x = torch.randn(5, 4)
    print("Neural-network output shape:", tuple(model(x).shape))

def main():
    torch.set_num_threads(1)
    tensor_autograd()
    model = train_regression()
    neural_network()
    target = Path(__file__).resolve().parents[1] / "models" / "linear_regression.pt"
    target.parent.mkdir(exist_ok=True)
    torch.save(model.state_dict(), target)
    print("Saved:", target)

if __name__ == "__main__":
    main()
