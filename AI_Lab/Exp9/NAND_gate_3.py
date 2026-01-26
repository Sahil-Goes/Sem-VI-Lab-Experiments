# NAND Gate - Neural Network (3-input)
import numpy as np

def activation(f):
    if f < 3.5:
        return 1
    else:
        return 0

def neuron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def NANDgate(x):
    w = np.array([1, 1, 1])
    b = 0.5
    return neuron(x, w, b)

example1 = np.array([0, 0, 0])
example2 = np.array([0, 0, 1])
example3 = np.array([0, 1, 0])
example4 = np.array([0, 1, 1])
example5 = np.array([1, 0, 0])
example6 = np.array([1, 0, 1])
example7 = np.array([1, 1, 0])
example8 = np.array([1, 1, 1])

print("NAND(0,0,0):", NANDgate(example1))
print("NAND(0,0,1):", NANDgate(example2))
print("NAND(0,1,0):", NANDgate(example3))
print("NAND(0,1,1):", NANDgate(example4))
print("NAND(1,0,0):", NANDgate(example5))
print("NAND(1,0,1):", NANDgate(example6))
print("NAND(1,1,0):", NANDgate(example7))
print("NAND(1,1,1):", NANDgate(example8))
