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

#plt.plot(date_train,close_train, 'b')
#plt.plot(date_test,close_test, 'r')