import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identity_function(x):
    return x

def init_network():
    network={}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([[0.1, 0.2, 0.3]])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([[0.1, 0.2]])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([[0.1, 0.2]])
    return network
def forward(network, x):
    # layer 1
    W1=network['W1']
    b1=network['b1']
    a1=np.dot(x,W1)+b1
    z1=sigmoid(a1)
    # Layer 2
    W2=network['W2']
    b2=network['b2']
    a2=np.dot(z1,W2)+b2
    z2=sigmoid(a2)
    # Layer 3
    W3=network['W3']
    b3=network['b3']
    a3=np.dot(z2,W3)+b3
    y=identity_function(a3)
    return y

network = init_network()
x=np.array([1.0,0.5])
y=forward(network,x)
print(y) #[0.31682708 0.69627909]
