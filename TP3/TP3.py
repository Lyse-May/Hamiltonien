#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:06:04 2020

@author: HOAREAU.LyseMay
"""

import numpy as np
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt 

"""
QUESTION 1
"""

data = pd.read_csv("bank_of_america.csv")
data['Date']=[datetime.strptime(x, '%m/%d/%Y') for x in data['Date'].str.slice(0,11)]
data = data.drop(['Open', 'High','Low','Volume','Adj Close'], axis=1)
data=data.to_numpy()

"""
QUESTION 2
"""

NB_train = int(len(data)*0.75)

date_train = data[0:NB_train,0]
close_train = data[0:NB_train,1]

date_test = data[NB_train:len(data),0]
close_test = data[NB_train:len(data),1]

plt.plot(date_train,close_train, 'b')
plt.plot(date_test,close_test, 'r')
plt.show()

"""
QUESTION 3
"""
n = len(date_train)

def policy(S): #POLICY DE MERDE TROUVER MIEUX
    A = np.zeros((n,1))
    for i in range(0,n):
        if S[i] > np.mean(S):
            A[i] = -1 #sell
        if S[i] < np.mean(S):
            A[i] = 1 #buy
        if S[i] == np.mean(S):
            A[i] = 0 #hold
    return A

A = policy(close_train)
NB_share = 30
Cash = 5000

def reward(A,S,i):
    R = np.zeros((n,1))
    for j in range(0,n):
        if A[j] == -1:
            R[j]= -S[j] * NB_share
        if A[i] == 1:
            R[j]= S[j] * NB_share    
        if A[j] == 0:
            R[j]= 0
    return R[i]


R = [reward(A,close_train,i) for i in range(0,n)]

def ptfs(R,i):
    ptf = np.zeros((n,1))
    ptf[0] = Cash
    if i == 0: 
        ptf[0] = Cash
    else:
        for j in range(0,n-1):
            ptf[j+1] = ptf[j] + R[j]
    return ptf[i]

    
ptf = [ptfs(R,i) for i in range(0,n)]

alpha = 0.4
gamma = 0.9

def Q_learnigDEMERDE(S,A):
    Q = np.zeros((n,1))
    Q_prec = Q
    for itera in range(10):        
        for i in range(0,n):
            
            break




















        