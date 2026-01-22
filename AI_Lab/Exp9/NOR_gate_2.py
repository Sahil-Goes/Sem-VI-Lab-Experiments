# NOR Gate - Neural Network
import numpy as np

def activation(f):
    if f >= 1.5:
        return 0
    else:
        return 1

def neuron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def NORgate(x):
    w = np.array([1, 1])
    b = 0.5
    return neuron(x, w, b)

example1 = np.array([0, 0])
example2 = np.array([0, 1])
example3 = np.array([1, 0])
example4 = np.array([1, 1])

print("NOR(0,0):", NORgate(example1))
print("NOR(0,1):", NORgate(example2))
print("NOR(1,0):", NORgate(example3))
print("NOR(1,1):", NORgate(example4))
