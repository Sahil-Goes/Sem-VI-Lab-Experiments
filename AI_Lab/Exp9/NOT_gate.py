# NOT Gate - Neural Network
import numpy as np

def activation(f):
    if f >= 0:
        return 1
    else:
        return 0

def neuron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def NOTgate(x):
    w = np.array([-1])
    b = 0.5
    return neuron(x, w, b)

example1 = np.array([0])
example2 = np.array([1])

print("NOT(0):", NOTgate(example1))
print("NOT(1):", NOTgate(example2))
