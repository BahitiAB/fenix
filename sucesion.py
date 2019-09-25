# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:58:22 2019

@author: Computer
"""
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1,10)

xn = 1/n

plt.plot(n, xn, 'o', label= "xn = 1/n")