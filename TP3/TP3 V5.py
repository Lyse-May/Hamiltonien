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

NB_train = int(len(data)*0.75) #0.75 est le pourcentage de train dans data

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
Nb_init = 0 #Nb share à l'état initial
Nb_share = 30 #Nb share par transaction
Cash_init = 5000 

def state(p,Nb,Cash): #Nb coorespond aux nombre d'action à l'état t
    pas = 10
    Price = []
    for i in range(1,pas):
        Price.append(p[0:i:1])
    for i in range(pas,n+1):
        Price.append(p[i-pas:i:1])
    S = [Price,Nb,Cash]
    return S

def reward(S,a,t):
    R = 0
    Cash = S[2]
    Nb = S[1]
    S = S[0]
    if (a == 1) & (Nb >= 30): #avoir le nombre d'action suffisant
        if (S[t][-1] >= (np.mean(S[t]) * 0.99)): #vendre 
            R = S[t][-1] * Nb_share
            Cash+= R
            Nb -= Nb_share
        else:
            R = 0
            Nb = Nb
            Cash = Cash
    if (a == 2): 
        if (Cash >= S[t][-1] * Nb_share):
            if (S[t][-1] <= (np.mean(S[t]) * 1.01)): #achat
                R = -S[t][-1] * Nb_share
                Cash+= R
                Nb += Nb_share
            else:
                R = 0
                Nb = Nb
                Cash = Cash
            
    if (a == 0):
        R = 0
        Nb = Nb
        Cash = Cash
        
    if (Nb == 0):
        R = S[t][-1] * Nb_share
        Cash+= R
        Nb -= Nb_share
        
    return R,Nb,Cash

def portfolio(ptf_prec,S,a,t):
    R,Nb,Cash = reward(S,a,t)
    ptf = ptf_prec
    if t == 0:
        ptf = Cash_init 
    else:
        ptf += Cash
    return ptf

"""
QUESTION 4
"""

alpha = 0.3
gamma = 0.9

def maxi(cash_prec,S,t):
    A = np.zeros((3,1))
    Nb = S[1]
    if Nb == 0:
        a = 2
        A[a] = portfolio(cash_prec,S,a,t)
    else:
        for j in range(0,3):
            A[j] = portfolio(cash_prec,S,j,t)
        index = np.where(A == np.max(A))
        a = index[0][0] 
    return A[a],a

def Q_learning(data):
    Q = np.zeros((n-1,3))
    Nb_prec,Cash_prec = Nb_init,Cash_init
    Cashs = [Cash_prec]
    for t in range(1,n):
        S = state(data,Nb_prec,Cash_prec)
        for a in range(0,3):
            
            R,Nb,Cash = reward(S,a,t-1)
            Qmax = maxi(Cash,S,t)
            
            for itera in range(0,10):
                Q[t-1,a] = (1 - alpha) * Q[t-1,a] + alpha * (R + gamma * Qmax[0])                
            
        R,Nb_new,Cash_new = reward(state(data,Nb,Cash),Qmax[1],t)
        Nb_prec,Cash_prec = Nb_new,Cash_new
        Cashs.append(Cash_new)
        
    return Q,Cashs

Q,Cash = Q_learning(close_train)

plt.plot(date_train[:-1],Q[:,0], label = 'A = 0')
plt.plot(date_train[:-1],Q[:,1], label = 'A = 1')
plt.plot(date_train[:-1],Q[:,2], label = 'A = 2')
plt.legend()
plt.show()

plt.plot(date_train,Cash, label = 'Cash') 
plt.legend()
plt.show()

action_opti = np.zeros((len(Q),1))
for i in range(0,len(Q)):
    action_opti[i] = np.argmax(Q[i])
    
plt.plot(date_train[:-1],action_opti)
plt.legend()
plt.show()    


    
    
    
    
    
    
    
    
    
