import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    y = np.sum(w*x) + b
    return 1 if y > 0 else 0

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    y = np.sum(w*x) + b
    return 1 if y > 0 else 0

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    y = np.sum(w*x) + b
    return 1 if y > 0 else 0

def XOR(x1, x2): 
    return AND(NAND(x1, x2), OR(x1, x2))

if __name__ == '__main__':
    print("---AND GATE---")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        out = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(out))
    print("---NAND GATE---")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        out = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(out))
    print("---OR GATE---")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        out = OR(xs[0], xs[1])
        print(str(xs) + " -> " + str(out))
    print("---XOR GATE---")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        out = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(out))
