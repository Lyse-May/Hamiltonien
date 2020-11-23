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

T = 50

"Bof"

for s in range (T,0,-1):
    p = 0.8
    q = 1-p
    if (D*p+1)*(q**parking_map(0.8,100)[s]) >= 1:
        break
        
        
    