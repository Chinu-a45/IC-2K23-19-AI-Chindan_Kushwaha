# Lab 6 — Deep Learning Fundamentals using PyTorch

**Aim:** Practice tensors, automatic differentiation, linear regression, neural
network layers, loss functions, optimizers and a training loop.

**Algorithm:** Generate deterministic synthetic linear data; initialize a
linear layer; repeatedly calculate MSE, backpropagate gradients and update
parameters using SGD; evaluate final loss and demonstrate a small neural network.

**Run:** `python Lab6/pytorch_fundamentals.py`.

**Results:** Prints gradients, initial/final loss, learned parameters, execution
time and neural-network output shape. Saves `models/linear_regression.pt`.

**Performance analysis:** Compare initial and final MSE and training time.
Training data are synthetic; results demonstrate convergence, not a real
forecasting task.

**Learning outcomes:** Tensor operations, autograd, model parameters,
backpropagation, optimizers and evaluation.
