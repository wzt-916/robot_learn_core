# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def read_data(addr):
    data = np.loadtxt(addr, delimiter=',')

    n = data.shape[0]
    
    ###### You may modify this section to change the model
    X = np.concatenate([np.ones([n, 1]), data[:,0:6]], axis=1)
    ###### You may modify this section to change the model
    
    Y = None
    if "train" in addr:
        Y = np.expand_dims(data[:, 6], axis=1)
    
    return (X,Y,n)

def cost_gradient(W, X, Y, n):
    y_predict = 1 / (np.exp(-np.dot(X,W) )+ 1)
    G = np.dot(X.T,(y_predict - Y))/n
    j = -np.dot(Y.T,np.log(y_predict))-np.dot((1-Y).T,np.log(1-y_predict))
    return (j, G)

def train(W, X, Y, lr, n, iterations):
    ###### You may modify this section to do 10-fold validation
    n = int(0.1*n)
    for j in range(0,1):
        J = np.zeros([iterations, 1])
        E_trn = np.zeros([iterations, 1])
        E_val = np.zeros([iterations, 1])
        X_trn = np.vstack((X[:n*j],X[n*j+n:]))
        Y_trn = np.vstack((Y[:n*j],Y[n*j+n:]))
        X_val = X[n*j:n*j+n]
        Y_val = Y[n*j:n*j+n]
        
        for i in range(iterations):
            (J[i], G) = cost_gradient(W, X_trn, Y_trn, n)
            W = W - lr*G
            E_trn[i] = error(W, X_trn, Y_trn)
            E_val[i] = error(W, X_val, Y_val)
        print(E_val[-1])
        ###### You may modify this section to do 10-fold validation
    
    return (W,J,E_trn,E_val)

def error(W, X, Y):
    Y_hat = 1 / (1 + np.exp(-X@W))
    Y_hat[Y_hat<0.5] = 0
    Y_hat[Y_hat>0.5] = 1
    
    return (1-np.mean(np.equal(Y_hat, Y)))

def predict(W):
    (X, _, _) = read_data("test_data.csv")
    
    Y_hat = 1 / (1 + np.exp(-X@W))
    Y_hat[Y_hat<0.5] = 0
    Y_hat[Y_hat>0.5] = 1
    
    idx = np.expand_dims(np.arange(1,201), axis=1)
    np.savetxt("predict.csv", np.concatenate([idx, Y_hat], axis=1), header = "Index,ID", comments='', delimiter=',')

iterations = 1000
lr = 0.001

(X, Y, n) = read_data("train.csv")
W = np.random.random([X.shape[1], 1])

(W,J,E_trn,E_val) = train(W, X, Y, lr, n, iterations)

###### You may modify this section to do 10-fold validation
plt.figure()
plt.plot(range(iterations), J)
plt.figure()
plt.ylim(0,1)
plt.plot(range(iterations), E_trn, "b")
plt.plot(range(iterations), E_val, "r")
###### You may modify this section to do 10-fold validation

predict(W)
