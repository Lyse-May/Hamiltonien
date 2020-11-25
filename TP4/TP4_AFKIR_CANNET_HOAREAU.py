#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:20:19 2020

@author: HOAREAU.LyseMay
"""
import numpy as np
import matplotlib.pyplot as plt

"""
Question 1
"""

state = [0,1] 
# 1 free place
# 0 occupied space, we continue

def parking_space(proba,Nb_position): # as a parameter the probability of having a free space and the number of spaces in the car park
    return (np.random.choice(state, Nb_position, p = [1-proba,proba]),proba)

# We generate several maps with different parking-space distributions

Park1 = parking_space(0.1,10)
Park2 = parking_space(0.2,15)
Park3 = parking_space(0.3,20)
Park4 = parking_space(0.8,20)

print("Park1 with p = 0.1 and 10 parking spaces",Park1)
print("\nPark2 with p = 0.2 and 15 parking spaces",Park2)
print("\nPark3 with p = 0.3 and 20 parking spaces",Park3)
print("\nPark4 with p = 0.8 and 20 parking spaces",Park4)

"""
Question 2
"""

def parking_strategy(park,D): # with D the cost of passing your destination without par
    Nb_position = len(park[0])
    p = park[1]
    q = 1-p
    park = park[0]
    park_car = park
    for s in range(Nb_position,1,-1):
        stop_condition = (D*p + 1) * q**s        
        if (stop_condition >= 1) & park[s-1] == 1:
            #print(s,stop_condition)
            park_car[s-1] = 2
            return park_car,s-1
            

Strategy1 = parking_strategy(Park1,100)
Strategy2 = parking_strategy(Park2,100)
Strategy3 = parking_strategy(Park3,1000)
Strategy4 = parking_strategy(Park4,1000)

# We implement the strategy for the different parkings
if Strategy1 != None:
    print("\nStrategy n°1 with Park1",Strategy1[0])
else:
    print("La stratégie n'a pas fonctionné pour Park1")
if Strategy2 != None:
    print("Strategy n°2 with Park2",Strategy2[0])
else:
    print("La stratégie n'a pas fonctionné pour Park2")
if Strategy3 != None:
    print("Strategy n°3 with Park3",Strategy3[0])
else:
    print("La stratégie n'a pas fonctionné pour Park3")
if Strategy4 != None:
    print("Strategy n°4 with Park4",Strategy4[0])
else:
    print("La stratégie n'a pas fonctionné pour Park4")
            
"""
Question 3
"""
# We define three functions to vary the cost D, the probability p and the number of position

def variation_D(p,Nb_position,D_max):
    park = parking_space(p,Nb_position)
    count = np.zeros((D_max,1))
    D = np.linspace(0,D_max-1,D_max)
    #print(park)
    for d in range(0,D_max):
        Strat = parking_strategy(park,d)
        #print(Strat)
        if Strat != None:
            ind_car = Strat[1]
            Strat = Strat[0]
            for i in range(ind_car,Nb_position):
                if Strat[i] == 1:
                    count[d] += 1
    plt.plot(D,count)
    plt.xlabel("D")
    plt.ylabel("Count")
    plt.title("Variation of D")
    plt.show()
    return count # "count" represents the number of free spaces remaining, i.e. when the car has parked (stop condition).

    
variation_D(0.1,50,500)

def variation_p(Nb_position,Nb_proba,D):
    proba = np.linspace(0,1,Nb_proba)
    count = np.zeros((Nb_proba,1))
    for p in range(0,Nb_proba):
        park = parking_space(proba[p],Nb_position)
        Strat = parking_strategy(park,D)
        #print(Strat)
        if Strat != None:
            ind_car = Strat[1]
            Strat = Strat[0]
            for i in range(ind_car,Nb_position):
                if Strat[i] == 1:
                    count[p] += 1
    plt.plot(proba,count)
    plt.xlabel("Probability p")
    plt.ylabel("Count")
    plt.title("Variation of p")
    plt.show()
    return count

variation_p(50,500,100)

def variation_Nb_position(Nb_position_max,p,D):
    count = np.zeros((Nb_position_max,1))
    position = np.linspace(0,Nb_position_max-1,Nb_position_max)
    for pos in range(0,Nb_position_max):
        park = parking_space(p,pos)
        Strat = parking_strategy(park,D)
        #print(Strat)
        if Strat != None:
            ind_car = Strat[1]
            Strat = Strat[0]
            for i in range(ind_car,pos):
                if Strat[i] == 1:
                    count[pos] += 1
    plt.plot(position,count)
    plt.xlabel("Number of position")
    plt.ylabel("Count")
    plt.title("Variation of the number of position")
    plt.show()
    return count

variation_Nb_position(500,0.5,100)