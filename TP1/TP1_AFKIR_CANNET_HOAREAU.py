#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:46:31 2020

@author: HOAREAU.LyseMay
"""
import numpy as np
from matplotlib import pyplot as plt
np.seterr(divide='ignore')

"""
Group : AFKIR Sofia - CANNET Capucine - HOAREAU Lyse-May

Lab 1 : 
    
An investor has a fund. It has 1 million euros at time zero. It pays 5% interest per year for T=50
years. The investor cannot withdraw the invested money. But, (s)he consumes a proportion (at)
of the interest at time t and reinvests the rest. What should the investor do to maximize the
consumption before T ?

"""
# Definition of variables

r = 0.05
T = 50

X = np.zeros((T,1))
X[0] = 1000000

A = np.zeros((T,1))

W = np.zeros((T,1))
rho = np.zeros((T,1))
time = np.array([i for i in range(0,T)])


"Question 1) Implement the bang-bang controller described in class using the programming language Python"

print("Question 1")

# Plant equation    
    
def plant(A): 
    for i in range (1,T):
        X[i] = X[i-1] + r*X[i-1]*(1-A[i-1])
    return X

# Definition of rho, a, X and W by Bellman method
    
def rhos():
    for i in range (T,0,-1):
        
        if r >= 1/rho[i-1]:
            rho[i-2]=(1+r) * rho[i-1]
        if r < 1/rho[i-1]:
            rho[i-2] = 1 + rho[i-1]
        rho[-1] = 1 
    return rho

def actions():
    for i in range (T,0,-1):
        
        if r >= 1/rho[i-1]:
            A[i-2] = 0
        if r < 1/rho[i-1]:
            A[i-2] = 1

    return A

def Bellman(X,rho):        
    
    for i in range (0,T):
        W[i] = r * X[i] * rho[i]
    return W

rho = rhos()
A = actions()
A[-1] = 1 
X = plant(A)
W = Bellman(X,rho)  


# Display of results

Y1 = (1 + rho)
Y2 = (1 + r )* rho


plt.plot(rho,Y1,label = 'Y1')
plt.plot(rho,Y2,label = 'Y2')
plt.ylabel("y")
plt.xlabel("rho")
plt.legend()
plt.xlim(10,40)
plt.ylim(10,40)
plt.show()


"Question 2) Compute the corresponding total consumption and find the sequence of optimal actions."

print("Question 2\n")    
    
def consumption(A,X):
    X_cons = np.zeros((T,1))
    S=0
    
    for i in range (1,T+1):
        X_cons[i-1] = r*X[i-1]*A[i-1]
        S += X_cons[i-1]
    return X_cons,S

X_cons,S = consumption(A,X)
print("Total Consumption : ",S)

print("The sequence of optimal actions : ")
for i in range(0,T):
    print("A at T =",i, "is", A[i])
print("\n") 


"Question 3) Plot the consumption as a function of time."

print("Question 3")    
    
plt.plot(time,X_cons)
plt.ylabel("Consumption")
plt.xlabel("Time")
plt.show()

#To identify when savings stop and when consumption begins
for i in range(26,32):
    print("The consumption at T =",i, "is", X_cons[i])
print("\n") 


"Question 4) Plot the action sequence as a function of time."

print("Question 4")    
    
plt.plot(time,A)
plt.ylabel("Action")
plt.xlabel("Time")
plt.show()


"Question 5) Choose a couple of other strategies (controllers) to compare their respective total consumption to that obtained using the bang-bang approach."
    
print("Question 5")    
    
"A increasing"
A1 = np.arange(0,1,1/(T-1))
A1[-1] = 1 
X_cons1,S1 = consumption(A1,plant(A1))

"ONLY 1"# total consumption
A2 = np.ones((T,1))
X_cons2,S2 = consumption(A2,plant(A2))

"ONLY 0"#saving
A3 = np.zeros((T,1))
A3[-1] = 1 
X_cons3,S3 = consumption(A3,plant(A3))

"A alternating between 0 and 1"
A4 = np.zeros((T,1))
for i in range(0,T):
    if i%2 == 1:
        A4[i] = 1
A4[-1] = 1 
X_cons4,S4 = consumption(A4,plant(A4))


plt.plot(time,A1, label = "A increasing")
plt.plot(time,A2, label = "Total consumption")
plt.plot(time,A3, label = "Savings")
plt.plot(time,A4, label = "A alternating")

plt.ylabel("Action")
plt.xlabel("Time")
plt.legend()
plt.title("Representation of Action with different values")
plt.show()

plt.plot(time,X_cons1, label = "with A increasing")
plt.plot(time,X_cons2, label = "with only A = 1")
plt.plot(time,X_cons3, label = "with only A = 0")
plt.plot(time,X_cons4, label = "with A alternating")

plt.ylabel("Consumption")
plt.xlabel("Time")
plt.legend()
plt.title("Representation of the Consumption with different values of A")
plt.show()

print("Total Consumption with A increasing : ",S1)
print("Total Consumption with only 1 : ",S2)
print("Total Consumption with only 0 : ",S3)
print("Total Consumption with A alternating : ",S4)
