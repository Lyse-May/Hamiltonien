#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:46:31 2020

@author: HOAREAU.LyseMay
"""
import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt

"""
Lab 1 : 
    
An investor has a fund. It has 1 million euros at time zero. It pays 5% interest per year for T=50
years. The investor cannot withdraw the invested money. But, (s)he consumes a proportion (at)
of the interest at time t and reinvests the rest. What should the investor do to maximize the
consumption before T ?

"""

r = 0.05
T = 50

X = np.zeros((T,1))
X[0] = 1000000

A = np.arange(0,1,1/(T-1))

W = np.zeros((T,1))
rho = np.zeros((T,1))
time = np.array([i for i in range(0,T)])


"Question 1) Implement the bang-bang controller described in class using the programming language Python"

def plant():
    for i in range (1,T):
        X[i] = X[i-1] + r*X[i-1]*(1-A[i-1])
    return X

def optimize(A):
    S=0
    X = plant()
    for i in range(0,T):
        S+= r* X[i]* A[i]
    return -S

bounds = [(0,1) for i in range(0,T)]
result = minimize(optimize,A,method='SLSQP',bounds=bounds)

A_plant = result.x
A_plant[-1] = 1
X_plant = plant()

def Bellman():
    for i in range (T,0,-1):
        
        if r >= 1/rho[i-1]:
            rho[i-2]=(1+r) * rho[i-1]
            
        if r < 1/rho[i-1]:
            rho[i-2] = 1 + rho[i-1]
        rho[-1] = 1    
    for i in range (0,T):
        W[i] = r * X[i] * rho[i]
    return rho, W



"Question 2) Compute the corresponding total consumption and find the sequence of optimal actions."

def consumption(A):
    X_cons = np.zeros((T,1))
    S=0
    for i in range (1,T+1):
        X_cons[i-1] = r*X_plant[i-1]*A[i-1]
        S += X_cons[i-1]
    return X_cons,S

def optimize2(A):
    S = consumption(A)[1]
    return -S

result2= minimize(optimize2,A,method='SLSQP',bounds=bounds)

A_cons = result.x
A_cons[-1] = 1
X_cons = consumption(A)[0]



"Question 3) Plot the consumption as a function of time."

plt.plot(time,X_cons)
plt.show()



"Question 4) Plot the action sequence as a function of time."

plt.plot(time,A_cons)
plt.show()



"Question 5) Choose a couple of other strategies (controllers) to compare their respective total consumption to that obtained using the bang-bang approach."



    
