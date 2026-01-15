# NAND Gate - Neural Network
import numpy as np

def activation(f):
    if f >= 2.5:
        return 0
    else:
        return 1

def neuron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def NANDgate(x):
    w = np.array([1, 1])
    b = 0.5
    return neuron(x, w, b)

example1 = np.array([0, 0])
example2 = np.array([0, 1])
example3 = np.array([1, 0])
example4 = np.array([1, 1])

print("NAND(0,0):", NANDgate(example1))
print("NAND(0,1):", NANDgate(example2))
print("NAND(1,0):", NANDgate(example3))
print("NAND(1,1):", NANDgate(example4))
