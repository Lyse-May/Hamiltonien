#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:54:16 2020

@author: HOAREAU.LyseMay
"""

import numpy as np
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt 

"""
QUESTION 1
"""

data = pd.read_csv("https://raw.githubusercontent.com/Lyse-May/Hamiltonien/main/TP3/bank_of_america.csv")
data['Date']=[datetime.strptime(x, '%m/%d/%Y') for x in data['Date'].str.slice(0,11)]
data = data.drop(['Open', 'High','Low','Volume','Adj Close'], axis=1)
data = data.to_numpy()

"""
QUESTION 2
"""

NB_train = int(len(data)*0.75)

#date_train = data['Date'][0:NB_train]
#close_train = data['Close'][0:NB_train]
#
#date_test = data['Date'][NB_train:]
#close_test = data['Close'][NB_train:]

date_train = data[0:NB_train,0]
close_train = data[0:NB_train,1]

date_test = data[NB_train:len(data),0]
close_test = data[NB_train:len(data),1]

#plt.plot(date_train,close_train, 'b')
#plt.plot(date_test,close_test, 'r')
#plt.show()

"""
QUESTION 3
"""

n = len(date_train)
Nb_init = 0
Nb_share = 30
Cash_init = 5000

def state(p,Nb,Cash):
    pas = 10
    Price = []
    for i in range(1,pas):
        Price.append(p[0:i:1])
    for i in range(pas,n+1):
        Price.append(p[i-pas:i:1])
    S = [Price,Nb,Cash]
    return S

#S = state(close_train,Nb,Cash_init) 
#print(S) 

def reward(S,a,t):
    R = 0
    Cash = S[2]
    Nb = S[1]
    S = S[0]
    if (S[t][-1] >= (np.mean(S[t]) * 0.99)):
        if (a == 1) & (Nb >= 30): #vendre
            R = S[t][-1] * Nb_share
            Cash+= R
            Nb -= Nb_share
    if (S[t][-1] <= (np.mean(S[t]) * 1.01)):
        if (a == 2) & (Cash >= S[t][-1]*Nb_share): #achat
            R = -S[t][-1] * Nb_share
            Cash+= R
            Nb += Nb_share
    return R,Nb,Cash

#R = reward(S,1,0)
#print(R)

def portfolio(ptf_prec,S,a,t):
    R,Nb,Cash = reward(S,a,t)
    ptf = ptf_prec
    if t == 0:
        ptf = Cash_init 
    else:
        ptf += Cash
    return ptf

alpha = 0.3
gamma = 0.1


"""
QUESTION 4
"""

def maxi(cash_prec,S,t):
    A = np.zeros((3,1))
    for j in range(0,3):
        A[j] = portfolio(cash_prec,S,j,t)
    index = np.where(A == np.max(A))
    a = index[0][0] 
    return A[a],a

def Q_learning(data):
    Q = np.zeros((n,3))
    S = state(data,Nb_init,Cash_init)
    for t in range(0,n-1):
        for a in range(0,3):
            R,Nb,Cash = reward(S,a,t)
            Qmax = maxi(Cash,S,t+1)
            for itera in range(0,20):
                Q[t,a] = (1 - alpha) * Q[t,a] + alpha * (R + gamma * Qmax[0])                
        R,Nb,Cash = reward(S,Qmax[1],t)
    return Q

Q = Q_learning(close_train)
PI = np.argmax(Q)
print(Q)
print(PI)


#def Q_learning(S):
#    Q = np.zeros((n,1))
#    res,Nb,_ = reward(0,1,S,0,0)
#    for t in range(1,n):
#        
#        for itera in range(0,10):
#            
#            a = maxi(res,S,t-1,Nb)
#            at = np.random.choice([-1,0,1])
#            Q[t-1],_,R = reward(res,at,S,t-1,Nb)
#            Q[t-1] = (1 - alpha) * Q[t-1] + alpha * (R + gamma * reward(Q[t-1],a,S,t,Nb)[0])
#        
#        res,Nb,_ = reward(Q[t-1],a,S,t-1,Nb) 
#    
#    return Q



    
   