# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:49:22 2020

@author: Capucine
"""

import numpy as np

"Question 1"

X =[0,1]


def parking_map(proba,nb_place):
    parking = np.random.choice(X,nb_place,p = [1-proba,proba])
    return(parking)



print("Our parking : " ,parking_map(0.8,100)) # en paramètre le probabilité d'avoir une place libre et le nombre de place dans le parking

"Question 2"

D = 0.9

T = 100

"Bof, c'est pas terminé"

def parking_stategy (D,p,parking,n):
    K = np.zeros(n)
    M = np.zeros(n)
    q = 1-p
    K[0] = q*D
    arret = 0
    while arret == 0:
        s = n-1
        M[n-1] = s
        K[s] = s - q/p + (D + 1/p)*(q**(s+1))
        
        if (D*p+1)*q**s >=1 :
            break
        
    return M,K
        
        
    