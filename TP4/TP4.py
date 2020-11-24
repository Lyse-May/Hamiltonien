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

#We generate several maps with different parking-space distributions

print("Our parking with p = 0.8 and 50 parking spaces : " ,parking_map(0.8,50)) # as a parameter the probability of having a free space and the number of spaces in the car park
print("\nOur parking with p = 0.3 and 50 parking spaces :  " ,parking_map(0.3,50))
print("\nOur parking with p = 0.9 and 100 parking spaces : " ,parking_map(0.9,100)) # as a parameter the probability of having a free space and the number of spaces in the car park


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
            arret == 0.1
        
    return M,K
        
        
    