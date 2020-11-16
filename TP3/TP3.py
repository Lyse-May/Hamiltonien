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
            R[j]= 0 # on ne doit pas mettre une récompense négative ici (ex - 0,02) ?
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

def Q_learningDEMERDE(S,A):
    Q = np.zeros((n,1))
    Q_prec = Q
    for itera in range(10): 
        epsilon = 1
        s = S[0]
        for i in range(0,n):
            s_curr = S[i]
            nb  = np.random.random_integers(0,1)
            if (nb< epsilon):
                next_action = int(np.random.choice(A,1))
                
            else : 
                next_action = np.argmax(Q[s_curr,next_action]) #on sait ce qu'il faut mettre à la place de next_action ici
            s_next = S[i+1]
            Q[i+1] = (1-alpha)*Q[i]+alpha*(R[i+1]+gamma*max(Q[i]))
            alpha == 0.99 * alpha
            epsilon == 0.99 * epsilon
            
            if (s_next == S[n-1]):
                break
    return Q_learningDEMERDE


policy_star = np.argmax(Q_learningDEMERDE(close_train,A))


"ALORS ON A TENTE DE FAIRE L ALGO DU DEUXIEME LIEN p17 ---> HELP"

"""

https://amunategui.github.io/reinforcement-learning/index.html

http://emmanuel.adam.free.fr/site/IMG/pdf/iacollective_apprentissage.pdf p.17

https://cdancette.fr/2017/08/18/reinforcement-learning-part1/

J'ai cherché sur ces sites pour essayer de m'inspirer pour le Q-learning 
mais ya des trucs que je comprends pas trop. Le deuxième lien donne un algorithme

"""


















        