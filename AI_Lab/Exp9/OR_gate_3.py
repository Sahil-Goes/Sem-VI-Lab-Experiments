# OR Gate - Neural Network (3-input)
import numpy as np

def activation(f):
    if f < 1.5:
        return 0
    else:
        return 1

def neuron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def ORgate(x):
    w = np.array([1, 1, 1])  # weights
    b = 0.5                  # bias
    return neuron(x, w, b)

# Examples
example1 = np.array([0, 0, 0])
example2 = np.array([0, 0, 1])
example3 = np.array([0, 1, 0])
example4 = np.array([0, 1, 1])
example5 = np.array([1, 0, 0])
example6 = np.array([1, 0, 1])
example7 = np.array([1, 1, 0])
example8 = np.array([1, 1, 1])

print("OR(0,0,0):", ORgate(example1))
print("OR(0,0,1):", ORgate(example2))
print("OR(0,1,0):", ORgate(example3))
print("OR(0,1,1):", ORgate(example4))
print("OR(1,0,0):", ORgate(example5))
print("OR(1,0,1):", ORgate(example6))
print("OR(1,1,0):", ORgate(example7))
print("OR(1,1,1):", ORgate(example8))
