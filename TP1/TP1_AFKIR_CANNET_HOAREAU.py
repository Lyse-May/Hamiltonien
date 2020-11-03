#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:46:31 2020

@author: HOAREAU.LyseMay
"""
import numpy as np
from matplotlib import pyplot as plt

"""
Lab 1 : 
    
An investor has a fund. It has 1 million euros at time zero. It pays 5% interest per year for T=50
years. The investor cannot withdraw the invested money. But, (s)he consumes a proportion (at)
of the interest at time t and reinvests the rest. What should the investor do to maximize the
consumption before T ?

"""
# Definition of variables

r = 0.05
T = 50

X = np.zeros((T,1))
X[0] = 1000000

A = np.arange(0,1,1/(T-1))

W = np.zeros((T,1))
rho = np.zeros((T,1))
rho[-1] = 1 
time = np.array([i for i in range(0,T)])


"Question 1) Implement the bang-bang controller described in class using the programming language Python"

# Plant equation    
    
def plant(A): 
    for i in range (1,T):
        X[i] = X[i-1] + r*X[i-1]*(1-A[i-1])
    return X

# Definition of rho, a, X and W by Bellman method
    
def actions():
    for i in range (T,0,-1):
        
        if r >= 1/rho[i-1]:
            rho[i-2]=(1+r) * rho[i-1]
            A[i-2] = 0
        if r < 1/rho[i-1]:
            rho[i-2] = 1 + rho[i-1]
            A[i-2] = 1
        rho[-1] = 1 
    return rho,A

def Bellman(X,rho):        
    
    for i in range (0,T):
        W[i] = r * X[i] * rho[i]
    return W

rho,A = actions()
A[-1] = 1 
X = plant(A)
W = Bellman(X,rho)  


# Display of results

Y1 = (1 + rho)
Y2 = (1 + r )* rho


plt.plot(rho,Y1,label = 'Y1')
plt.plot(rho,Y2,label = 'Y2')
plt.ylabel("y")
plt.xlabel("rho")
plt.legend()
plt.xlim(10,40)
plt.ylim(10,40)
plt.show()


"Question 2) Compute the corresponding total consumption and find the sequence of optimal actions."

def consumption(A):
    X_cons = np.zeros((T,1))
    S=0
    
    for i in range (1,T+1):
        X_cons[i-1] = r*X[i-1]*A[i-1]
        S += X_cons[i-1]
    return X_cons,S

X_cons,S = consumption(A)
print("Total Consumption : ",S)


"Question 3) Plot the consumption as a function of time."

plt.plot(time,X_cons)
plt.ylabel("Consommation")
plt.xlabel("Time")
plt.show()



"Question 4) Plot the action sequence as a function of time."

plt.plot(time,A)
plt.ylabel("Action")
plt.xlabel("Time")
plt.show()


"Question 5) Choose a couple of other strategies (controllers) to compare their respective total consumption to that obtained using the bang-bang approach."


