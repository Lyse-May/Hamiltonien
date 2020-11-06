#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:07:55 2020

@author: HOAREAU.LyseMay
"""

import numpy as np
from matplotlib import pyplot as plt

T = 50
W = np.zeros((T,1))
W_T = 0.998
W[-1] = W_T
P = np.zeros((T,1))
P_real = 30000
time = np.array([i for i in range(0,T)])

"Question 1"

def wealth():
    for i in range (T-1,0,-1):
        W[i-1] = ((1 + W[i]) / 2.)**2
    return W

def price(W):
    for i in range(1,T):
        P[i-1] = (W[i] + 1)/2
    P[-1] = W[-1]
    return P

W = wealth()
P = price(W)

#W = wealth()*P_real
#P = price(W)*P_real

"Question 2"

plt.plot(time,W, label = "W")
plt.title("W ")
plt.show()
plt.plot(time,P, label = "P")
plt.title("P")
plt.show()

"Question 3"

def wealth_by_price(P):
    W = P**2 
    #j'ai isolé C(t-s+1) dans l'eq de P(t_s) et l'ai remplacé dans l'eq de C(t-s)
    return W

"P constant = 0.8"

P1 = np.array([0.8 for i in range(0,T)])
W1 = wealth_by_price(P1)


#P1 = np.array([0.8 for i in range(0,T)])*P_real
#W1 = wealth_by_price(P1)*P_real

plt.plot(time,P1, label = "P = 0.8")
plt.title("P = 0.8")
plt.show()
plt.plot(time,W1, label = "W pour P = 0.8")
plt.title("W pour P = 0.8")
plt.show()

"P croissant"

P2 = np.arange(0,1,1/(T-1))
W2 = wealth_by_price(P2)

#P2 = np.arange(0,1,1/(T-1))*P_real
#W2 = wealth_by_price(P2)*P_real

plt.plot(time,P2, label = "P = croissant")
plt.title("P = croissant")
plt.show()
plt.plot(time,W2, label = "W pour P = croissant")
plt.title("W pour P = croissant")
plt.show()

"P décroissant"

P3 = np.arange(1,0,-(1/(T)))
W3 = wealth_by_price(P3)

#P3 = np.arange(1,0,-(1/(T)))*P_real
#W3 = wealth_by_price(P3)*P_real

plt.plot(time,P3, label = "P = décroissant")
plt.title("P = décroissant")
plt.show()
plt.plot(time,W3, label = "W pour P = décroissant")
plt.title("W pour P = décroissant")
plt.show()