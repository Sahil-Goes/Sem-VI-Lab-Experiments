# AND Gate - Neural Network
import numpy as np

# Activation function (Step Function)
def activation(f):
    if f < 0.5:   # threshold = 0.5 for AND gate
        return 0
    else:
        return 1

# Neuron model
def neuron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

# AND Gate using a single neuron
def ANDgate(x):
    w = np.array([1, 1])  # weights
    b = -1.5              # bias to implement AND logic
    return neuron(x, w, b)

# Test Inputs
example1 = np.array([0, 0])
example2 = np.array([0, 1])
example3 = np.array([1, 0])
example4 = np.array([1, 1])

print("AND(0,0):", ANDgate(example1))
print("AND(0,1):", ANDgate(example2))
print("AND(1,0):", ANDgate(example3))
print("AND(1,1):", ANDgate(example4))
