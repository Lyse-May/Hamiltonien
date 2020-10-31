# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:30:54 2020

@author: Capucine
"""
import numpy as np
from matplotlib import pyplot as plt

"""
Lab 1 : 
    
An investor has a fund. It has 1 million euros at time zero. It pays 5% interest per year for T=50
years. The investor cannot withdraw the invested money. But, (s)he consumes a proportion (at)
of the interest at time t and reinvests the rest. What should the investor do to maximize the
consumption before T?

"""



"Question 1) Implement the bang-bang controller described in class using the programming language Python"

r = 0.05
T = 50

a = np.ones(T,None,'F')
X = np.ones(T,None,'F')


for i in range (0,T):
    X[i] += r*X[i]*(1-a)