# -*- coding: utf-8 -*-
from __future__ import division
import pandas as pa
import numpy as np
from DateProcess import InDate
import matplotlib.pyplot as plt
# X is a m*Dimension matrix
# Y is a m*1 matrix
# theta is a Dimension*1 matrix

def CostFunction(X, y, theta):
    m = y.shape[0] #训练集数量

    tmp =(2*m)*( np.dot(X,theta)- y )**2
    J = 1/(2*m)*np.sum(( np.dot(X,theta)- y )**2)
    return J

def GradientDescent(X,y,theta,alpha,num_iters):

    J_history = np.zeros((num_iters, 1))
    for i in range(num_iters):
        Z = np.transpose(X)
        t = np.dot(np.transpose(X), (np.dot(X, theta) - y))
        theta = theta -alpha*np.dot(np.transpose(X),(np.dot(X,theta)-y))
        J_history[i, 0] = CostFunction(X, y, theta)

    plt.figure()
    plt.plot(J_history)
    plt.show()
    plt.figure()
    plt.plot(X,y)
    plt.plot(X,np.dot(X, theta),'red')
    plt.show()
    return theta

def Normalization(X, y):
    meanX = np.mean(X, 0)
    meanY = np.mean(y, 0)
    stdX = np.std(X)
    stdY = np.std(y)

    for i in range(X.shape[0]):
        X[i, :] = (X[i, :]-meanX)/stdX
    y = (y - meanY)/stdY

    return [X, y]



d = Normalization(X=InDate.load_date(path='X.json'), y=InDate.load_date(path='Y.json'))
print GradientDescent(X=d[0], y=d[1], theta=InDate.load_date(path='theta.json'), alpha=0.1, num_iters=100)

