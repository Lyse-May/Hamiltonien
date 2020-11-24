#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:20:19 2020

@author: HOAREAU.LyseMay
"""
import numpy as np
import matplotlib.pyplot as plt

"""
Questio 1
"""

state = [0,1] 
# 1 place libre
# 0 place occupée

def parking_space(proba,Nb_position): #proba : proba de place libre
    return (np.random.choice(state, Nb_position, p = [1-proba,proba]),proba)

#Park1 = parking_space(0.1,10)
#Park2 = parking_space(0.2,15)
#Park3 = parking_space(0.3,20)
#
#print(Park1)
#print(Park2)
#print(Park3)


"""
Question 2
"""

def parking_strategy(park,D):
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
            

#Strategy1 = parking_strategy(Park1,100)
#Strategy2 = parking_strategy(Park2,100)
#Strategy3 = parking_strategy(Park3,1000)
#
#print(Strategy1)
#print(Strategy2)
#print(Strategy3)
            
"""
Question 3
"""

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
    plt.show()
    return count
    
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
    #plt.plot(position,position)
    plt.show()
    return count

variation_Nb_position(500,0.5,100)