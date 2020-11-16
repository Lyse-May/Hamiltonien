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


data = pd.read_csv("https://raw.githubusercontent.com/Lyse-May/Hamiltonien/main/TP3/bank_of_america.csv")
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

#def policy(S): #POLICY DE MERDE TROUVER MIEUX
#    A = np.zeros((n,1))
#    for i in range(0,n):
#        if S[i] > np.mean(S):
#            A[i] = -1 #sell
#        if S[i] < np.mean(S):
#            A[i] = 1 #buy
#        if S[i] == np.mean(S):
#            A[i] = 0 #hold
#    return A
#
#A = policy(close_train)
NB_share = 30
Cash = 5000

#def reward(A,S,i):
#    R = np.zeros((n,1))
#    for j in range(0,n):
#        if A[j] == -1:
#            R[j]= -S[j] * NB_share
#        if A[i] == 1:
#            R[j]= S[j] * NB_share    
#        if A[j] == 0:
#            R[j]= 0 # on ne doit pas mettre une récompense négative ici (ex - 0,02) ?
#    return R[i]

def reward(init,A,S,i,Nb):
    R = 0
    ptf = np.zeros((n,1))
    ptf[0] = Cash
    if i == 0: 
        ptf[0] = Cash
    else:
        if (A == -1) & (Nb >= 30): #vendre
            R = S[i] * NB_share
            Nb -= 30
            
        if (A == 1) & (init >= (S[i] * NB_share)) : #achète
            R = -S[i] * NB_share  
            Nb += 30
            
        if A == 0:
            R = 0 # on ne doit pas mettre une récompense négative ici (ex - 0,02) ?
        ptf[i] = init + R
    return ptf[i],Nb,R

#R = [reward(A,close_train,i) for i in range(0,n)]
#
#def ptfs(R,i):
#    ptf = np.zeros((n,1))
#    ptf[0] = Cash
#    if i == 0: 
#        ptf[0] = Cash
#    else:
#        for j in range(0,n-1):
#            ptf[j+1] = ptf[j] + R[j]
#    return ptf[i]
#
#    
#ptf = [ptfs(R,i) for i in range(0,n)]

alpha = 0.03
gamma = 0.8

def maxi(init,S,i,Nb):
    A = np.zeros((3,1))
    for j in range(-1,2,1):
        A[j] = reward(init,j,S,i,Nb)[0]
    index = np.where(A == max(A))
    a = index[0][0] - 1 
    return a

def Q_learning(S):
    Q = np.zeros((n,1))
    res,Nb,_ = reward(0,1,S,0,0)
    for t in range(1,n):
        
        for itera in range(0,10):
            
            a = maxi(res,S,t-1,Nb)
            at = np.random.choice([-1,0,1])
            Q[t-1],_,R = reward(res,at,S,t-1,Nb)
            Q[t-1] = (1 - alpha) * Q[t-1] + alpha * (R + gamma * reward(Q[t-1],a,S,t,Nb)[0])
        
        res,Nb,_ = reward(Q[t-1],a,S,t-1,Nb) 
    
    return Q

Q = Q_learning(close_train)

plt.plot(date_train,Q)

#def Q_learningDEMERDE(S,A):
#    Q = np.zeros((n,1))
#    Q_prec = Q
#    for itera in range(10): 
#        epsilon = 1
#        s = S[0]
#        for i in range(0,n):
#            s_curr = S[i]
#            nb  = np.random.random_integers(0,1)
#            if (nb< epsilon):
#                next_action = int(np.random.choice(A,1))
#                
#            else : 
#                next_action = np.argmax(Q[s_curr,next_action]) #on sait ce qu'il faut mettre à la place de next_action ici
#            s_next = S[i+1]
#            Q[i+1] = (1-alpha)*Q[i]+alpha*(R[i+1]+gamma*max(Q[i]))
#            alpha == 0.99 * alpha
#            epsilon == 0.99 * epsilon
#            
#            if (s_next == S[n-1]):
#                break
#    return Q_learningDEMERDE
#
#
#policy_star = np.argmax(Q_learningDEMERDE(close_train,A))


"ALORS ON A TENTE DE FAIRE L ALGO DU DEUXIEME LIEN p17 ---> HELP"

"""

https://amunategui.github.io/reinforcement-learning/index.html

http://emmanuel.adam.free.fr/site/IMG/pdf/iacollective_apprentissage.pdf p.17

https://cdancette.fr/2017/08/18/reinforcement-learning-part1/

J'ai cherché sur ces sites pour essayer de m'inspirer pour le Q-learning 
mais ya des trucs que je comprends pas trop. Le deuxième lien donne un algorithme

"""


















        